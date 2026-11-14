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
KNOWN = {
 "agent-memory": ("private beta", "/agent-memory/"),
 "artifacts": ("open beta", "/changelog/product/artifacts/"),
 "k2": ("public beta", "/k2/platform/pricing/"),
 "email-service": ("sending: public beta", "/email-service/"),
 "workers-vpc": ("beta", "/workers-vpc/get-started/"),
 "basin": ("GA (2026-10-01)", "/changelog/post/2026-10-01-basin-ga/"),
 "basin-pipelines": ("GA (2026-10-01)", "/changelog/post/2026-10-01-basin-ga/"),
 "basin-catalog": ("GA (2026-10-01)", "/changelog/post/2026-10-01-basin-ga/"),
 "basin-sql": ("GA (2026-10-01)", "/changelog/post/2026-10-01-basin-ga/"),
 "wallets": ("name reservation only", "/wallets/"),
}
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
                source="https://github.com/cloudflare/cloudflare-docs/blob/"+commit+"/"+path)
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
    now=datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")
    visible=sum(bool(x["url"]) and not x["hidden"] for x in all_entries)
    hidden=sum(x["hidden"] for x in all_entries)
    groups=sorted({x["group"] for x in all_entries},key=str.casefold)
    lines=[
      "# Cloudflare公式Docsディレクトリ全件スナップショット","",
      "**取得日 (UTC):** "+now+"  ",
      "**固定ソース:** [cloudflare-docs "+commit[:12]+"](https://github.com/cloudflare/cloudflare-docs/commit/"+commit+")  ",
      "**対象:** src/content/directory/*.yaml の全件（"+str(len(all_entries))+"件）","",
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
        lines += ["### "+group+"（"+str(len(items))+"件）","","| 名前 | Docs索引 | 提供段階 | 公式Docs | メタデータ |","|---|---|---|---|---|"]
        for x in items:
            known=KNOWN.get(x["slug"])
            stage=("["+known[0]+"]("+DOCS+known[1]+")") if known else "未個別確認"
            visibility="非表示" if x["hidden"] else "公開" if x["url"] else "URLなし"
            doc="[公式]("+x["url"]+")" if x["url"] else "—"
            lines.append("| "+" | ".join([esc(x["name"]),visibility,stage,doc,"["+x["slug"]+".yaml]("+x["source"]+")"])+" |")
        lines.append("")
    lines += [
     "## 使い分け","",
     "- [個別サービス一覧](services.md) は他社と単純比較しにくいものを厳選した編集済み一覧です。",
     "- [横断比較](../service-comparison.md) は2社以上で比較するものです。",
     "- この全件スナップショットは公式Docs索引を追跡するものであり、両方のリストと重複します。","",
     "## 2026年の変更例","",
     "- [Basinは2026-10-01にGA](https://developers.cloudflare.com/changelog/post/2026-10-01-basin-ga/)。旧Data Platform、Pipelines、R2 Data Catalog、R2 SQLの改称に注意。",
     "- [Agent Memoryはprivate beta](https://developers.cloudflare.com/agent-memory/)。",
     "- [K2はpublic beta](https://developers.cloudflare.com/k2/platform/pricing/)。",
     "- [Email Service送信はpublic beta](https://developers.cloudflare.com/email-service/)。",
     "- [Artifactsはopen beta](https://developers.cloudflare.com/changelog/product/artifacts/)。",
     "- [Workers VPCはbeta](https://developers.cloudflare.com/workers-vpc/get-started/)。",
     "- [Cloudflare Walletsはハンドル予約のみ](https://developers.cloudflare.com/wallets/)。","",
     "## 再生成","",
     "リポジトリルートで python scripts/refresh_cloudflare_directory.py を実行。Cloudflare公式GitHub productionのコミットを固定し、YAMLを全件取得します。失敗時はファイルを上書きしません。","",
     "**残課題:** 正式なProductsページとの全件照合、独立製品とDocs機能の分類、GA/リージョン/契約条件の全製品確認。",""
    ]
    out=ROOT/"cloud/cloudflare/catalog.md"
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text("\n".join(lines),encoding="utf-8")
    print("OK",len(all_entries),"source entries,",visible,"visible,",hidden,"hidden; wrote",out)

if __name__=="__main__":
    main()
