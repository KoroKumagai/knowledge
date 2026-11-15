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
        if not fields.get("ctaLink"):
            raise ValueError("AWS Products card has no product CTA: "+identifier)
        url = urljoin(PAGE, fields["ctaLink"])
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

def read_product_lifecycle():
    """Load WHOLE-service statuses; never propagate sub-feature retirements."""
    content=(DIR/"lifecycle.md").read_text(encoding="utf-8")
    stage=None
    byname=defaultdict(list)
    totals={}
    for line in content.splitlines():
        header=re.match(r"^## (Maintenance|Sunset|Full Shutdown).*?(\d+)件$",line)
        if header:
            stage={"Maintenance":"maintenance","Sunset":"sunset",
                   "Full Shutdown":"shutdown"}[header.group(1)]
            totals[stage]=int(header.group(2))
            continue
        if not stage or not line.startswith("| ") or line.startswith("| AWS公式掲載名"):
            continue
        cells=[v.strip() for v in line.strip("|").split("|")]
        if len(cells)!=4 or not cells[3].startswith("[公式](https://"):
            raise ValueError("Malformed official lifecycle entry: "+line)
        byname[cells[0]].append({"stage":stage,"end":cells[2],"source":cells[3]})
    if set(totals)!={"maintenance","sunset","shutdown"}:
        raise ValueError("Missing an official lifecycle category")
    for status,total in totals.items():
        actual=sum(v["stage"]==status for entries in byname.values() for v in entries)
        if actual!=total:
            raise ValueError("Lifecycle table section count mismatch: "+status)
    return byname

LIFECYCLE_LABELS={
    "maintenance":"Maintenance（新規利用に制限）",
    "sunset":"Sunset（終了予定）",
    "shutdown":"Full Shutdown（終了済み）"
}

def lifecycle_coverage_note(row):
    """A full-product or related-service status, independent of ref mapping."""
    stage=row["stage"]
    date=row["end"]
    if stage=="shutdown":
        return "Full Shutdown済み"+("（"+date+"）" if date!="—" else "")
    if stage=="sunset":
        return "Sunset"+("（"+date+"終了予定）" if date!="—" else "（終了予定）")
    return "Maintenance（新規利用に制限）"+(
        "（サポート終了日 "+date+"）" if date!="—" else "")

def related_product_date(row):
    if row["end"]=="—":
        return ""
    return "（"+row["end"]+("終了" if row["stage"]=="shutdown"
             else "終了予定" if row["stage"]=="sunset"
             else "サポート終了日")+"）"

def related_lifecycle(name,config,byname):
    """Return statuses of a related service, NOT the Product's own statuses."""
    relation=config.get("lifecycle_related",{}).get(name)
    if not relation:
        return []
    return sorted(byname[relation["service"]],key=lambda r:
                  {"shutdown":0,"sunset":1,"maintenance":2}[r["stage"]])

def product_lifecycle(name,config,byname):
    alias=config.get("lifecycle_aliases",{}).get(name,name)
    rows=sorted(byname.get(alias,[]),key=lambda r:
                {"shutdown":0,"sunset":1,"maintenance":2}[r["stage"]])
    if not rows:
        # Related services are shown as dependencies, never as product aliases.
        related=config.get("lifecycle_related",{}).get(name)
        statuses=related_lifecycle(name,config,byname)
        if related and statuses:
            dependency=related["service"]
            terms=[]
            for row in statuses:
                if row["stage"]=="shutdown":
                    state="関連サービスが終了済み"
                else:
                    state="関連サービスの"+LIFECYCLE_LABELS[row["stage"]]
                terms.append("["+state+"："+dependency+"](lifecycle.md)"
                             +related_product_date(row))
            return " / ".join(terms)+"。製品本体の提供状態とは区別",[]
        return "本体の該当記載なし（GA未確認）",[]
    terms=[]
    for row in rows:
        term="["+LIFECYCLE_LABELS[row["stage"]]+"](lifecycle.md)"
        if row["end"]!="—":term+="（"+row["end"]+"）"
        terms.append(term)
    return " / ".join(terms),rows

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
    byname=read_product_lifecycle()
    whole_aliases=config.get("lifecycle_aliases",{})
    if not set(whole_aliases).issubset(prod_names) or not set(whole_aliases.values()).issubset(byname):
        raise ValueError("Invalid product-level lifecycle alias map")
    related_lifecycle_cfg=config.get("lifecycle_related",{})
    if (not set(related_lifecycle_cfg).issubset(prod_names)
        or set(related_lifecycle_cfg)&set(whole_aliases)
        or not all(isinstance(v,dict) and v.get("service") in byname
                   and v.get("reason") and v["service"]!=k
                   for k,v in related_lifecycle_cfg.items())):
        raise ValueError("Invalid separate lifecycle-related service mapping")
    note_names=config.get("alias_notes",{})
    if not set(note_names).issubset(set(aliases)):
        raise ValueError("Alias notes must refer to an exact alias")
    groups=defaultdict(list)
    for p in products: groups[p["category"]].append(p)
    lines=[
        "# AWS公式Productsの全サービス区分カード", "",
        "**取得日 (UTC):** "+day+"  ",
        "**AWS公式:** [Products]("+PAGE+") / [Productsページ内部の検索エンドポイント（非公開・仕様保証なし）]("+API+") / [取得データ](products-source.json)", "",
        "**API totalHits:** "+str(len(products))+"件 / **収録:** "+str(len(products))+"件", "",
        "> この件数は公式Productsページのserviceタグを持つカード数。独立課金サービス数やGA数とは限りません。",
        "> 廃止済み製品の掲載もあります。列の表示は[公式ライフサイクル台帳](lifecycle.md)のサービス本体名との完全一致・手動別名による照合であり、機能単位の終了を本体の終了とみなしません。検索エンドポイントは非公開・仕様保証がなく、件数が一致しなければ更新を停止します。", "",
        "公式の Amazon DocumentDB (with MongoDB compatability) は綴り誤りを含む掲載名をそのまま記録（原文ママ）。", "",
        "[269項目との差分](products-coverage.md) / [手動対応定義](products-mapping.json)", ""
    ]
    for category in sorted(groups,key=str.casefold):
        subset=sorted(groups[category],key=lambda x:x["name"].casefold())
        lines+=["## "+esc(category)+"（"+str(len(subset))+"件）","",
                "| 公式Products名 | 製品ページ | Docs（掲載分） | ライフサイクル（本体） | ディレクトリID |",
                "|---|---|---|---|---|"]
        for p in subset:
            lifecycle_state,_=product_lifecycle(p["name"],config,byname)
            lines.append("| "+esc(p["name"])+" | [公式]("+p["url"]+") | "+
              ("[Docs]("+p["docs_url"]+")" if p["docs_url"] else "—")+
              " | "+lifecycle_state+" | "+esc(p["id"])+" |")
        lines.append("")
    coverage=[
        "# AWS ProductsとGeneral Referenceの差分照合","",
        "**取得日 (UTC):** "+day+" / **Products:** "+str(len(products))+
        "件 / **General Reference:** "+str(len(references))+"件","",
        "この表は**掲載名・掲載粒度の差分**です。目録外を製品不存在と解釈しません。",
        "**分類:** 同名＝名称一致（サービス同等・GAの証明ではない）、確認済み別名＝明示的な名称の対応、関連・別粒度＝関連はあるが非同等、目録外・未対応＝対応先未確定。",
        "理由欄は例外事項のみ記載します。原本のカードIDは[全件一覧](products.md)と[取得データ](products-source.json)で確認できます。",
        "同名の別カードはその行だけIDを併記します。",""]
    display_rows=[]
    matched=set()
    classes=Counter()
    repeated=Counter(p["name"] for p in products)
    for p in products:
        name=p["name"]
        if name in aliases:
            key=aliases[name];kind="確認済み別名";note=config.get("alias_notes",{}).get(name,"")
            matched.add(key)
        elif name in byref:
            key=name;kind="同名";note=""
            matched.add(key)
        elif name in related:
            key=related[name]["reference"];kind="関連・別粒度（非同等）"
            note=related[name]["reason"]
        else:
            key=None;kind="目録外・未対応";note=""
        # Reference matching and lifecycle are orthogonal. Surface all three
        # lifecycle stages for every Product, regardless of match class.
        _,own_statuses=product_lifecycle(name,config,byname)
        for status in own_statuses:
            suffix=lifecycle_coverage_note(status)
            note=(note+"。"+suffix) if note else suffix
        dependency=related_lifecycle(name,config,byname)
        if dependency:
            related_name=related_lifecycle_cfg[name]["service"]
            parts=[lifecycle_coverage_note(row) for row in dependency]
            suffix=(related_name+"（関連サービス）は"+" / ".join(parts)
                    +"。製品本体の提供状態とは区別")
            note=(note+"。"+suffix) if note else suffix
        classes[kind]+=1
        link="["+esc(name)+"]("+p["url"]+")"
        if repeated[name]>1:
            link+="（ID: "+esc(p["id"])+"）"
        display_rows.append("| "+link+" | "+kind+" | "+
            ("["+esc(key)+"]("+byref[key]["url"]+")" if key else "—")+
            " | "+(esc(note) if note else "—")+" |")
    coverage+=["## 照合サマリー","",
        "- 同名: "+str(classes["同名"])+"件",
        "- 確認済み別名: "+str(classes["確認済み別名"])+"件",
        "- 関連・別粒度（非同等）: "+str(classes["関連・別粒度（非同等）"])+"件",
        "- 目録外・未対応: "+str(classes["目録外・未対応"])+"件",
        "- General Referenceで対応したユニーク項目: "+str(len(matched))+"件",
        "- General Reference側の未対応: "+str(len(references)-len(matched))+"件",
        "", "## Products側の全件照合", "",
        "| Products掲載名 | 分類 | General Reference名 | 例外・補足 |",
        "|---|---|---|---|",
        *display_rows,
        "", "## General Reference側の未対応項目","",
        "未対応にはAPI・内部機能・旧名称・マーケティングに掲載されない製品も含まれます。",
        "","| General Reference名 | 公式出典 | ライフサイクル |",
        "|---|---|---|"]
    for item in references:
        if item["name"] not in matched:
            coverage.append("| "+esc(item["name"])+" | [公式]("+item["url"]+") | "+
                            item["lifecycle"]+" |")
    coverage+=["","**注意:** どちらのリストにもないことを理由に製品不在とは判断しない。",
               "区分変更は手動でproducts-mapping.jsonに根拠付きで記録する。",""]
    shutdown_cards=sum(
        any(row["stage"]=="shutdown" for row in product_lifecycle(p["name"],config,byname)[1])
        for p in products)
    status_index=lines.index("[269項目との差分](products-coverage.md) / [手動対応定義](products-mapping.json)")
    lines.insert(status_index,"**公式Full Shutdown台帳でサービス本体の終了を確認: "+str(shutdown_cards)+"カード**")
    lines.insert(status_index+1,"")
    return "\n".join(lines).rstrip()+"\n","\n".join(coverage).rstrip()+"\n",classes,len(matched)

def synchronize_documented_counts(total, categories, classes, matched, reference_total):
    """Keep human overview totals aligned with the official refreshed snapshot."""
    aws_path = DIR / "README.md"
    global_path = ROOT / "cloud/README.md"
    aws = aws_path.read_text(encoding="utf-8")
    general = global_path.read_text(encoding="utf-8")
    def change(text, pattern, replacement, label):
        updated, count = re.subn(pattern, replacement, text)
        if not count:
            raise ValueError("README count marker missing: " + label)
        return updated
    aws = change(aws, r"\*\*\d+カード\*\*", "**"+str(total)+"カード**", "AWS cards")
    aws = change(aws, r"\d+カテゴリ", str(categories)+"カテゴリ", "AWS categories")
    aws = change(aws, r"serviceタグ付きカード\d+件",
                 "serviceタグ付きカード"+str(total)+"件", "AWS service-tag scope")
    aws = change(aws, r"同名\d+件、確認済み別名\d+件、関連・別粒度\d+件、目録外・未対応\d+件",
                 "同名"+str(classes["同名"])+"件、確認済み別名"+
                 str(classes["確認済み別名"])+"件、関連・別粒度"+
                 str(classes["関連・別粒度（非同等）"])+"件、目録外・未対応"+
                 str(classes["目録外・未対応"])+"件", "AWS classifications")
    aws = change(aws, r"(?<=側の未対応は)\d+件",
                 str(reference_total-matched)+"件",
                 "AWS reference remainder")
    aws = change(aws, r"未対応\d+カード",
                 "未対応"+str(classes["目録外・未対応"])+"カード",
                 "AWS review queue")
    aws = change(aws, r"General Reference側\d+項目",
                 "General Reference側"+str(reference_total-matched)+"項目",
                 "AWS ref unmatched mentions")
    general = change(general, r"AWS公式Products \d+カード",
                     "AWS公式Products "+str(total)+"カード", "global tree")
    general = change(general, r"service区分\d+カード",
                     "service区分"+str(total)+"カード", "global progress")
    aws_path.write_text(aws,encoding="utf-8")
    global_path.write_text(general,encoding="utf-8")

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
    synchronize_documented_counts(total,len({p["category"] for p in products}),
                                   classes,matched,len(refs))
    print(json.dumps({"products":total,"generalReference":len(refs),
                      "categories":len({p["category"] for p in products}),
                      "classifications":classes,"matched":matched},ensure_ascii=False))

if __name__=="__main__":
    main()
