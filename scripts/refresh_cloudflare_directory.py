#!/usr/bin/env python3
"""Snapshot ALL YAML entries in Cloudflare's official docs directory, not all GA products."""
import concurrent.futures
import datetime
import json
import os
from pathlib import Path
import re
from urllib.parse import quote, urljoin
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parent.parent
API = "https://api.github.com/repos/cloudflare/cloudflare-docs"
DOCS = "https://developers.cloudflare.com"
STATUS_FILE = ROOT / "cloud/cloudflare/catalog-status.json"
PRODUCT_FILE = ROOT / "cloud/cloudflare/products.md"
CATALOG_FILE = ROOT / "cloud/cloudflare/catalog.md"

def read_curated():
    data = json.loads(STATUS_FILE.read_text(encoding="utf-8"))
    if not data.get("verified_on") or not isinstance(data.get("statuses"), dict):
        raise RuntimeError("Missing curated status metadata")
    return data

def fetch(url, api=False):
    headers={"User-Agent":"knowledge-cloudflare-audit/1.0"}
    if api:
        headers["Accept"]="application/vnd.github+json"
        if os.getenv("GITHUB_TOKEN"):
            headers["Authorization"]="Bearer "+os.environ["GITHUB_TOKEN"]
    with urlopen(Request(url, headers=headers), timeout=45) as response:
        return response.read()

def field(raw, key):
    match=re.search("^"+re.escape(key)+r":\s*(.*)$",raw,re.M)
    value=match.group(1).strip() if match else ""
    if len(value)>1 and value[0] in "'\"" and value[-1]==value[0]:
        value=value[1:-1]
    return value

def get_one(meta, commit):
    path=meta["path"]
    raw=fetch("https://raw.githubusercontent.com/cloudflare/cloudflare-docs/"+commit+"/"+quote(path)).decode("utf-8-sig")
    slug=meta["name"].removesuffix(".yaml")
    relative=field(raw,"  url")
    return dict(slug=slug,name=field(raw,"name") or field(raw,"  title") or slug,
                group=field(raw,"  group") or "未分類",
                hidden=bool(re.search(r"^  show:\s*false\s*$",raw,re.M)),
                url=urljoin(DOCS+"/", relative) if relative else "",
                source_filename=meta["name"])
def esc(s):
    return s.replace("|",r"\|").replace("\n"," ").replace("\r"," ")

def main():
    commit=json.loads(fetch(API+"/commits/production",api=True))["sha"]
    listing=json.loads(fetch(API+"/contents/src/content/directory?ref="+commit,api=True))
    source=[x for x in listing if x.get("type")=="file" and x["name"].endswith(".yaml")]
    if len(source)<150 or len({x["name"] for x in source})!=len(source):
        raise RuntimeError("Official YAML listing is unexpectedly small or duplicated")
    with concurrent.futures.ThreadPoolExecutor(max_workers=12) as pool:
        all_entries=list(pool.map(lambda x:get_one(x,commit),source))
    if len(all_entries)!=len(source) or len({x["slug"] for x in all_entries})!=len(source):
        raise RuntimeError("Incomplete YAML retrieval")
    curated=read_curated()
    statuses=curated["statuses"]
    unknown=set(statuses)-{x["slug"] for x in all_entries}
    if unknown:
        raise RuntimeError("Curated status refers to removed directory YAML: "+str(sorted(unknown)))
    # Both documents share one source revision. Product/YAML mapping remains
    # curated: fail rather than silently accept removed source entries.
    old_products=PRODUCT_FILE.read_text(encoding="utf-8")
    pin=re.search(r"\*\*Docs照合元コミット:\*\* `([a-f0-9]{40})`",old_products)
    if not pin:
        raise RuntimeError("products.md must include a pinned Docs source commit")
    referenced=set(re.findall(r"`([a-z0-9.-]+\.yaml)` \| (?:同名|改称|表記ゆれ|機能・製品群) \|",old_products))
    if len(referenced)<50:
        raise RuntimeError("Cannot parse enough referenced Products YAML entries")
    missing=referenced-{x["source_filename"] for x in all_entries}
    if missing:
        raise RuntimeError("products.md references removed upstream YAML: "+str(sorted(missing)))
    updated_products=old_products.replace(pin.group(1),commit,1)
    count=len(all_entries)
    visible=sum(bool(x["url"]) and not x["hidden"] for x in all_entries)
    hidden=sum(x["hidden"] for x in all_entries)
    cf_readme_path=ROOT/"cloud/cloudflare/README.md"
    root_readme_path=ROOT/"cloud/README.md"
    cf_readme=cf_readme_path.read_text(encoding="utf-8")
    root_readme=root_readme_path.read_text(encoding="utf-8")

    def substitute(pattern, new, text, description):
        result, matches=re.subn(pattern, new, text)
        if not matches:
            raise RuntimeError("Cannot update documented count: "+description)
        return result

    updated_products=substitute(r"の\d+エントリのどれに対応",
        "の"+str(count)+"エントリのどれに対応",updated_products,"products Docs count")
    cf_readme=substitute(
        r"\*\*\d+エントリ\*\*全件。公開\d+、非表示\d+",
        "**"+str(count)+"エントリ**全件。公開"+str(visible)+"、非表示"+str(hidden),
        cf_readme,"Cloudflare README summary")
    cf_readme=substitute(r"\d+件を漏れなく一覧化",
        str(count)+"件を漏れなく一覧化",cf_readme,"Cloudflare README total")
    root_readme=substitute(r"公式Docs索引\d+件","公式Docs索引"+str(count)+"件",
        root_readme,"global README Docs inventory")
    root_readme=substitute(r"公式目録については\d+件",
        "公式目録については"+str(count)+"件",root_readme,"global README audit note")
    now=datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")
    visible=sum(bool(x["url"]) and not x["hidden"] for x in all_entries)
    hidden=sum(x["hidden"] for x in all_entries)
    groups=sorted({x["group"] for x in all_entries},key=str.casefold)
    lines=[
      "# Cloudflare公式Docsディレクトリ全件スナップショット","",
      "**取得日 (UTC):** "+now+"  ",
      "**固定ソース:** [cloudflare-docs "+commit[:12]+"](https://github.com/cloudflare/cloudflare-docs/commit/"+commit+")  ",
      "**対象:** src/content/directory/*.yaml の全件（"+str(len(all_entries))+"件）  ",
      "**ソースYAMLの位置:** `https://github.com/cloudflare/cloudflare-docs/blob/"+commit+"/src/content/directory/<filename>`（一覧にはファイル名のみ掲載。コミットは上記リンクで固定）","",
      "- Docs公開目録相当: **"+str(visible)+"件**（URLあり、show:false指定なし）",
      "- Docs非表示エントリ: **"+str(hidden)+"件**",
      "- URL未指定エントリ: **"+str(sum(not x["url"] for x in all_entries))+"件**","",
      "> 注意：YAMLエントリは製品、機能、管理操作、プラットフォーム、文書集、旧製品を含みます。全エントリがGAサービスという意味ではありません。",
      "> Docs公開/非表示は製品の提供/終了状況を表しません。GA、プラン、地域、価格・SLAの網羅的検証は未完了です。","",
      "[公式Docs directory](https://developers.cloudflare.com/directory/) / [公式Products](https://www.cloudflare.com/products/) / [YAML元ディレクトリ](https://github.com/cloudflare/cloudflare-docs/tree/"+commit+"/src/content/directory)","",
      "## 全件（グループ別）","",
      "ステータスは一次資料で確認できた代表例のみ記載しています。未確認はGAを意味しません。","",
    ]
    for group in groups:
        items=sorted([x for x in all_entries if x["group"]==group],key=lambda x:(x["name"].casefold(),x["slug"]))
        lines += ["### "+group+"（"+str(len(items))+"件）","","| 名前 | Docs索引 | 提供段階 | 公式Docs | ソースYAML |","|---|---|---|---|---|"]
        for x in items:
            known=statuses.get(x["slug"])
            stage=("["+known["status"]+"]("+known["source"]+")") if known else "未個別確認"
            visibility="非表示" if x["hidden"] else "公開" if x["url"] else "URLなし"
            doc="[公式]("+x["url"]+")" if x["url"] else "—"
            lines.append("| "+" | ".join([esc(x["name"]),visibility,stage,doc,"`"+x["source_filename"]+"`"])+" |")
        lines.append("")
    lines += [
     "## 使い分け","",
     "- [個別サービス一覧](services.md) は他社と単純比較しにくいものを厳選した編集済み一覧です。",
     "- [横断比較](../service-comparison.md) は2社以上で比較するものです。",
     "- この全件スナップショットは公式Docs索引を追跡するものであり、両方のリストと重複します。","",
     "## 提供状況・改称の確認履歴（手動管理データ）","",
     "この節は [`catalog-status.json`](catalog-status.json) から生成されます。**取得日と提供段階の検証日は異なる**ため、ソース一覧を再生成しても提供状況は自動で最新化されません。","",
     "## 再生成","",
     "リポジトリルートで python scripts/refresh_cloudflare_directory.py を実行。Cloudflare公式GitHub productionのコミットを固定し、YAMLを全件取得します。失敗時はファイルを上書きしません。","",
     "**残課題:** 公式Products側との別名対応の詳細確認、独立製品とDocs機能の分類、GA/リージョン/契約条件の全製品確認。",""
    ]
    # Place the verified changes immediately before the regeneration section.
    marker=lines.index("## 再生成")
    additions=["- "+event["date"]+" ["+event["product"]+"]("+event["source"]+"): "+event["summary"]
               for event in curated.get("change_notes",[])]
    lines[marker:marker]=additions+[""]
    # Complete all related documents only after upstream and mapping checks.
    CATALOG_FILE.write_text("\n".join(lines),encoding="utf-8")
    PRODUCT_FILE.write_text(updated_products,encoding="utf-8")
    cf_readme_path.write_text(cf_readme,encoding="utf-8")
    root_readme_path.write_text(root_readme,encoding="utf-8")
    print("OK",len(all_entries),"source entries,",visible,"visible,",hidden,"hidden; pinned source",commit)

if __name__=="__main__":
    main()
