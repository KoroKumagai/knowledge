#!/usr/bin/env python3
"""Record AWS official Products service cards, then diff General Reference.

Official source: AWS Products webpage directory API with service tag.
An AWS marketing product, a billed service, and an endpoint/quota entry are
different units. Matches are identifiers only, never proof of GA or parity.
"""
from collections import defaultdict, Counter
from datetime import datetime, timezone
from html import unescape
from pathlib import Path
from urllib.parse import urlencode, urljoin, urlsplit
from urllib.request import Request, urlopen
import json
import re

ROOT = Path(__file__).resolve().parent.parent
DIR = ROOT / "cloud/aws"
API = "https://aws.amazon.com/api/dirs/items/search"
PAGE = "https://aws.amazon.com/products/"
PARAMS = {
    "item.directoryId": "products-cards-interactive-aws-products-ams",
    "item.locale": "en_US",
    "tags.id": "GLOBAL#local-tags-aws-products-type#service",
    "sort_by": "item.additionalFields.title", "sort_order": "asc", "size": "500"
}

def get_products():
    api_url = API + "?" + urlencode(PARAMS)
    req = Request(api_url, headers={"User-Agent": "Mozilla/5.0",
                                    "Accept": "application/json"})
    with urlopen(req, timeout=60) as response:
        data = json.load(response)
    entries = data.get("items", [])
    meta = data.get("metadata", {})
    total = meta.get("totalHits")
    if not isinstance(total, int) or not 170 <= total <= 450:
        raise ValueError("Unexpected official Products count: " + repr(meta))
    if len(entries) != total or meta.get("count") != total:
        raise ValueError("Partial AWS Products response: " + repr(meta))
    products = []
    for entry in entries:
        item = entry.get("item") or {}
        fields = item.get("additionalFields") or {}
        tags = entry.get("tags") or []
        if not any(t.get("id") == PARAMS["tags.id"] for t in tags):
            raise ValueError("Missing service category tag on " + repr(item.get("name")))
        name = unescape(re.sub(r"<[^>]*>", "", fields.get("title", ""))).strip()
        identifier = item.get("name", "")
        if not name or not identifier:
            raise ValueError("Empty title or ID in official response")
        try:
            categories = json.loads(fields.get("badge") or "{}").get("value") or []
        except (ValueError, TypeError):
            categories = []
        category = categories[0] if categories else "Uncategorized"
        url = urljoin(PAGE, fields.get("ctaLink") or "")
        docs_url = urljoin(PAGE, fields["secondaryCTALink"]) if fields.get("secondaryCTALink") else ""
        if urlsplit(url).scheme != "https" or not urlsplit(url).netloc:
            raise ValueError("Unsafe official catalog product link: " + url)
        products.append({
            "id": identifier, "name": name, "category": category,
            "url": url, "docs_url": docs_url,
            "description": unescape(re.sub(r"<[^>]*>", " ", fields.get("body",""))).strip(),
            "updated": item.get("dateUpdated","")
        })
    if len({p["id"] for p in products}) != total:
        raise ValueError("Duplicate official marketing card IDs")
    duplicated={name:n for name,n in Counter(p["name"] for p in products).items() if n>1}
    if duplicated:
        print("WARN: distinct official product cards share display names: "+repr(duplicated))
    return api_url, total, sorted(products, key=lambda p:(p["name"].casefold(),p["id"]))

def get_general_reference():
    result=[]
    for line in (DIR/"catalog.md").read_text(encoding="utf-8").splitlines():
        if not re.match(r"^\| \d+ \|", line):
            continue
        cols=[x.strip() for x in line.strip("|").split("|")]
        if len(cols)!=4:
            raise ValueError("Invalid reference line: "+line)
        link=re.search(r"\[公式\]\((https://docs\.aws\.amazon\.com/[^)]+)\)",cols[2])
        if not link:
            raise ValueError("No source URL for "+cols[1])
        result.append({"name":cols[1],"url":link.group(1),"lifecycle":cols[3]})
    if len(result)<240 or len(set(x["name"] for x in result))!=len(result):
        raise ValueError("Incomplete General Reference or duplicate name")
    return result

def esc(x):
    return str(x).replace("|",r"\|").replace("\n"," ").strip()

def generate(products, references, config, day):
    aliases=config.get("aliases",{})
    related=config.get("related_not_equivalent",{})
    prod_names={p["name"] for p in products}
    byref={r["name"]:r for r in references}
    if not set(aliases).issubset(prod_names) or not set(aliases.values()).issubset(byref):
        raise ValueError("Invalid manually reviewed exact aliases")
    if not set(related).issubset(prod_names) or set(aliases)&set(related):
        raise ValueError("Invalid related-but-different mapping")
    if not all(isinstance(r,dict) and r.get("reference") in byref and r.get("reason") for r in related.values()):
        raise ValueError("Related mapping needs a real reference and a reason")
    groups=defaultdict(list)
    for p in products: groups[p["category"]].append(p)
    lines=[
        "# AWS公式Productsの全サービス区分カード", "",
        "**取得日 (UTC):** "+day+"  ",
        "**AWS公式:** [Products]("+PAGE+") / [公式検索API]("+API+") / [取得データ](products-source.json)", "",
        "**API totalHits:** "+str(len(products))+"件 / **収録:** "+str(len(products))+"件", "",
        "> この件数は公式Productsページのserviceタグを持つカード数。独立課金サービス数やGA数とは限りません。",
        "> 廃止済み製品が表示される場合もあります。提供可能性はライフサイクル台帳で個別確認してください。AWS公式APIが案内する外部ドメインの公式製品サイトもあります。", "",
        "[269項目との差分](products-coverage.md) / [手動対応定義](products-mapping.json)", ""
    ]
    for category in sorted(groups,key=str.casefold):
        subset=sorted(groups[category],key=lambda x:x["name"].casefold())
        lines+=["## "+esc(category)+"（"+str(len(subset))+"件）","",
                "| 公式Products名 | 製品ページ | Docs（掲載分） | ディレクトリID |",
                "|---|---|---|---|"]
        for p in subset:
            lines.append("| "+esc(p["name"])+" | [公式]("+p["url"]+") | "+
              ("[Docs]("+p["docs_url"]+")" if p["docs_url"] else "—")+
              " | "+esc(p["id"])+" |")
        lines.append("")
    coverage=[
        "# AWS ProductsとGeneral Referenceの差分照合","",
        "**取得日 (UTC):** "+day+" / **Products:** "+str(len(products))+
        "件 / **General Reference:** "+str(len(references))+"件","",
        "この表は**掲載名・掲載粒度の差分**です。目録外を製品不存在と解釈しません。",
        "別名対応は明示的に検証したものだけ。関連・別粒度は同一サービスと数えません。",
        "",
        "| Products掲載名 | 分類 | General Reference名 | 判定理由 |",
        "|---|---|---|---|"]
    matched=set()
    classes=Counter()
    for p in products:
        name=p["name"]
        if name in aliases:
            key=aliases[name];kind="確認済み別名";note="対応名を手動確認。機能範囲・GAは別途検証"
            matched.add(key)
        elif name in byref:
            key=name;kind="同名";note="名称一致。製品とエンドポイントは同じ粒度とは限らない"
            matched.add(key)
        elif name in related:
            key=related[name]["reference"];kind="関連・別粒度（非同等）"
            note=related[name]["reason"]
        else:
            key=None;kind="目録外・未対応";note="General Referenceの該当項目は未確定"
        classes[kind]+=1
        coverage.append("| ["+esc(name)+"]("+p["url"]+") ("+esc(p["id"])+") | "+kind+" | "+
            ("["+esc(key)+"]("+byref[key]["url"]+")" if key else "—")+
            " | "+esc(note)+" |")
    coverage+=["","## 照合サマリー","",
        "- 同名: "+str(classes["同名"])+"件",
        "- 確認済み別名: "+str(classes["確認済み別名"])+"件",
        "- 関連・別粒度（非同等）: "+str(classes["関連・別粒度（非同等）"])+"件",
        "- 目録外・未対応: "+str(classes["目録外・未対応"])+"件",
        "- General Referenceで対応したユニーク項目: "+str(len(matched))+"件",
        "- General Reference側の未対応: "+str(len(references)-len(matched))+"件",
        "","## General Reference側の未対応項目","",
        "未対応にはAPI・内部機能・旧名称・マーケティングに掲載されない製品も含まれます。",
        "","| General Reference名 | 公式出典 | ライフサイクル |",
        "|---|---|---|"]
    for item in references:
        if item["name"] not in matched:
            coverage.append("| "+esc(item["name"])+" | [公式]("+item["url"]+") | "+
                            item["lifecycle"]+" |")
    coverage+=["","**注意:** どちらのリストにもないことを理由に製品不在とは判断しない。",
               "区分変更は手動でproducts-mapping.jsonに根拠付きで記録する。",""]
    return "\n".join(lines).rstrip()+"\n","\n".join(coverage).rstrip()+"\n",classes,len(matched)

def main():
    api,total,products=get_products()
    refs=get_general_reference()
    config=json.loads((DIR/"products-mapping.json").read_text(encoding="utf-8"))
    day=datetime.now(timezone.utc).strftime("%Y-%m-%d")
    products_md,coverage_md,classes,matched=generate(products,refs,config,day)
    dups={name:n for name,n in Counter(p["name"] for p in products).items() if n>1}
    if dups:
        additions=["", "## 同一表示名の別カード（公式原票のまま保持）", "",
                   "表示名が同じでもカードIDが異なるため集計から除外しません。"]
        for title in sorted(dups):
            ids=[p["id"] for p in products if p["name"]==title]
            additions.append("- "+title+": "+", ".join(ids))
        products_md += "\n".join(additions)+"\n"
        coverage_md += "\n".join(additions)+"\n"
    snapshot={"retrieved_utc":day,"source_page":PAGE,"api_url":api,
              "source_total_hits":total,"products":products}
    (DIR/"products-source.json").write_text(
        json.dumps(snapshot,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    (DIR/"products.md").write_text(products_md,encoding="utf-8")
    (DIR/"products-coverage.md").write_text(coverage_md,encoding="utf-8")
    print(json.dumps({"products":total,"generalReference":len(refs),
                      "categories":len({p["category"] for p in products}),
                      "classifications":classes,"matched":matched},ensure_ascii=False))

if __name__=="__main__":
    main()
