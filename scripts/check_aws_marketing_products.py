#!/usr/bin/env python3
"""Offline consistency check of AWS official marketing Products snapshot.

The original API fetch proves upstream completeness at refresh time; this
checker verifies the frozen response, hand-reviewed mappings, both rendered
tables and README. It does not claim general availability or contract status.
"""
from collections import Counter
from pathlib import Path
from urllib.parse import parse_qs, urlsplit
import json
import re
import sys

ROOT=Path(__file__).resolve().parents[1]
AWS=ROOT/"cloud/aws"
sys.path.insert(0,str(ROOT/"scripts"))
import refresh_aws_marketing_products as generator

errors=[]
def check(ok,msg):
    if not ok: errors.append(msg)

source=json.loads((AWS/"products-source.json").read_text(encoding="utf-8"))
mapping=json.loads((AWS/"products-mapping.json").read_text(encoding="utf-8"))
products=source.get("products",[])
product_md=(AWS/"products.md").read_text(encoding="utf-8")
coverage_md=(AWS/"products-coverage.md").read_text(encoding="utf-8")
overview=(AWS/"README.md").read_text(encoding="utf-8")
global_overview=(ROOT/"cloud/README.md").read_text(encoding="utf-8")
refs=generator.get_general_reference()
total=source.get("source_total_hits",0)

check(source.get("source_page")=="https://aws.amazon.com/products/",
      "Official marketing source page missing")
api=urlsplit(source.get("api_url",""))
params=parse_qs(api.query)
check(api.netloc=="aws.amazon.com" and
      api.path=="/api/dirs/items/search", "Nonofficial source API")
check(params.get("item.directoryId")==["products-cards-interactive-aws-products-ams"] and
      params.get("tags.id")==["GLOBAL#local-tags-aws-products-type#service"] and
      params.get("item.locale")==["en_US"],
      "Incorrect official Products service-tag filter")
check(params.get("size")==["500"], "Not fetching enough results for complete service-tag catalog")
check(isinstance(total,int) and total==len(products) and 170<=total<=450,
      "API totalHits differs from frozen product cards")
ids=[p.get("id") for p in products]
check(len(ids)==len(set(ids)), "Duplicate AWS Products directory card IDs")
names=[p.get("name") for p in products]
check(all(isinstance(x,str) and x for x in names),
      "Blank marketing Product name")
check(all(isinstance(p.get("category"),str) and p["category"] for p in products),
      "Missing marketing Product category")
check(all(p.get("url","").startswith("https://") for p in products),
      "Unsafe or missing product URL in official listing")
check(len(refs)>=250, "General Reference source unexpectedly small")

# Independently verify each Markdown section is a 4-column GFM table with
# header, separator and the exact number of marketing card IDs.
sections=list(re.finditer(r"^## (.+?)（(\d+)件）$",product_md,re.M))
check(len(sections)==len({p["category"] for p in products}),
      "Products Markdown category heading count mismatch")
found_ids=[]
for i,section in enumerate(sections):
    group=section.group(1)
    span=product_md[section.end():(sections[i+1].start() if i+1<len(sections)
                               else product_md.find("## 同一表示名の別カード",section.end())
                               if "## 同一表示名の別カード" in product_md[section.end():]
                               else len(product_md))]
    rows=[line for line in span.splitlines() if line.startswith("|")]
    check(len(rows)>=2 and rows[0]=="| 公式Products名 | 製品ページ | Docs（掲載分） | ディレクトリID |" and
          rows[1]=="|---|---|---|---|", "Invalid product table heading/divider: "+group)
    actual=rows[2:] if len(rows)>=2 else []
    check(len(actual)==int(section.group(2)), "Group count mismatch: "+group)
    for line in actual:
        cols=[x.strip() for x in re.split(r"(?<!\\)\|",line.strip())[1:-1]]
        check(len(cols)==4,"Invalid product data row width: "+group)
        if len(cols)==4: found_ids.append(cols[3])
check(set(found_ids)==set(ids) and len(found_ids)==len(ids),
      "Product Markdown dropped, duplicated or changed official card IDs")

try:
    expected_products, expected_coverage, classes, matched=generator.generate(
        products,refs,mapping,source.get("retrieved_utc",""))
    duplicate=Counter(names)
    duplicates={k:v for k,v in duplicate.items() if v>1}
    if duplicates:
        appendix=["","## 同一表示名の別カード（公式原票のまま保持）","",
                  "表示名が同じでもカードIDが異なるため集計から除外しません。"]
        for name in sorted(duplicates):
            appendix.append("- "+name+": "+", ".join(
                p["id"] for p in products if p["name"]==name))
        expected_products+="\n".join(appendix)+"\n"
        expected_coverage+="\n".join(appendix)+"\n"
    check(product_md==expected_products,
          "Official Products Markdown differs from frozen source; regenerate it")
    check(coverage_md==expected_coverage,
          "Marketing vs General Reference diff is stale; regenerate it")
    check(sum(classes.values())==total,"Marketing classification counts do not reconcile")
    check(matched<=len(refs),"General Reference matched more than its unique entries")
except Exception as exc:
    check(False,"Products mapping/rendering failed: "+repr(exc))

check("**"+str(total)+"カード**" in overview and
      str(len({p["category"] for p in products}))+"カテゴリ" in overview,
      "AWS README official Products counts are stale")
check("service区分"+str(total)+"カード" in global_overview,
      "Root cloud README Products progress is stale")
check("GA" in overview and "同一" in overview,
      "AWS README must not conflate Products, availability and endpoints")
check(mapping.get("aliases",{}).get("Amazon QuickSight")=="AWS Quick Sight",
      "AWS Quick Sight current brand alias missing")
check(mapping.get("related_not_equivalent",{}).get("AWS Quick",{}).get("reference")=="AWS Quick Sight",
      "AWS Quick must not be equated with its Quick Sight BI capability")
for display_name, repeat_count in duplicates.items():
    check(display_name in overview or display_name in product_md,
          "Duplicated marketing display name not documented: "+display_name)
    check(repeat_count>=2, "Duplicate count inconsistent")

if errors:
    for e in errors:
        print("ERROR:",e,file=sys.stderr)
    sys.exit(1)
print("OK: AWS Products "+str(total)+" cards; General Reference "+
      str(len(refs))+" endpoints; class counts "+str(dict(classes))+
      "; unique refs mapped "+str(matched)+"; source URLs and README consistent")
