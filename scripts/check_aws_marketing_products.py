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
# Render expectations with the snapshot day, as the generator does, so that a
# Sunset entry whose end date has passed is expected as "終了日経過".
snapshot_day=source["retrieved_utc"]
source_lifecycle=generator.read_product_lifecycle()
def expected_label(lifecycle_name, stage):
    rows=[r for r in source_lifecycle.get(lifecycle_name,[]) if r["stage"]==stage]
    check(len(rows)==1, "Official lifecycle row missing: "+lifecycle_name+" ("+stage+")")
    return generator.lifecycle_coverage_note(rows[0],snapshot_day) if rows else "<missing>"
thin_client_label=expected_label("Amazon WorkSpaces – Thin Client","sunset")
iot_1click_label=expected_label("AWS IoT 1-Click","shutdown")

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
check(params.get("sort_by")==["item.additionalFields.title"] and
      params.get("sort_order")==["asc"],
      "AWS Products internal search order changed; review snapshot before accepting")
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

# Independently verify each Markdown section is a 5-column GFM table with
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
    check(len(rows)>=2 and rows[0]=="| 公式Products名 | 製品ページ | Docs（掲載分） | ライフサイクル（本体） | ディレクトリID |" and
          rows[1]=="|---|---|---|---|---|", "Invalid product table heading/divider: "+group)
    actual=rows[2:] if len(rows)>=2 else []
    check(len(actual)==int(section.group(2)), "Group count mismatch: "+group)
    for line in actual:
        cols=[x.strip() for x in re.split(r"(?<!\\)\|",line.strip())[1:-1]]
        check(len(cols)==5,"Invalid product data row width: "+group)
        if len(cols)==5:
            found_ids.append(cols[4])
            check("](lifecycle.md)" in cols[3] or
                  cols[3]=="本体の該当記載なし（GA未確認）",
                  "Missing or unsupported lifecycle status: "+cols[0])
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

shutdown_products={
    "Amazon FinSpace","Amazon Chime","Amazon Pinpoint",
    "Amazon Lookout for Equipment","Amazon Lookout for Metrics",
    "Amazon Lookout for Vision","AWS DeepLens","AWS DeepComposer",
    "Amazon Nimble Studio","AWS Proton","AWS App Mesh",
    "Amazon Elastic Transcoder","AWS Elemental MediaStore",
    "Amazon Quantum Ledger Database (QLDB)"
}
for name in shutdown_products:
    lines=[line for line in product_md.splitlines() if line.startswith("| "+name+" |")]
    check(len(lines)==1 and re.search(
          r"\[Full Shutdown（(?:\d{4}-\d{2}-\d{2}終了|終了済み)）\]\(lifecycle.md\)", lines[0]),
          "Full Shutdown must be visible on official Product row: "+name)
check("**"+str(total)+"カード**" in overview and
      str(len({p["category"] for p in products}))+"カテゴリ" in overview,
      "AWS README official Products counts are stale")
check("service区分"+str(total)+"カード" in global_overview,
      "Root cloud README Products progress is stale")
check("General Reference側"+str(len(refs)-matched)+"項目" in overview,
      "AWS README unmatched unique reference count stale")
check("GA" in overview and "同一" in overview,
      "AWS README must not conflate Products, availability and endpoints")
check(mapping.get("aliases",{}).get("Amazon QuickSight")=="AWS Quick Sight",
      "AWS Quick Sight current brand alias missing")
check(mapping.get("related_not_equivalent",{}).get("AWS Quick",{}).get("reference")=="AWS Quick Sight",
      "AWS Quick must not be equated with its Quick Sight BI capability")
check(mapping.get("aliases",{}).get("AWS Personal Health Dashboard")=="AWS Health",
      "AWS Health Dashboard renamed service mapping missing")
check(mapping.get("lifecycle_aliases",{}).get("Amazon Quantum Ledger Database (QLDB)")
      =="Amazon Quantum Ledger Database (Amazon QLDB)",
      "QLDB shutdown alias missing")
check(mapping.get("lifecycle_aliases",{}).get("Amazon WorkSpaces Thin Client")
      =="Amazon WorkSpaces – Thin Client",
      "WorkSpaces Thin Client sunset name mapping missing")
related_button=mapping.get("lifecycle_related",{}).get("AWS IoT Button",{})
check(related_button.get("service")=="AWS IoT 1-Click" and related_button.get("reason"),
      "IoT Button must link to the retired IoT 1-Click DEPENDENCY, not alias")
check("AWS IoT Button" not in mapping.get("lifecycle_aliases",{}),
      "IoT Button may not inherit whole-product retirement through an alias")
for product_name,expected in (
    ("Amazon WorkSpaces Thin Client", "["+thin_client_label+"](lifecycle.md)"),
    ("AWS IoT Button", "[関連サービスの"+iot_1click_label+"：AWS IoT 1-Click](lifecycle.md)。製品本体の提供状態とは区別")
):
    candidates=[line for line in product_md.splitlines()
                if line.startswith("| "+product_name+" |")]
    check(len(candidates)==1 and expected in candidates[0],
          "Expected lifecycle status missing for "+product_name)
check("| [Amazon Quantum Ledger Database (QLDB)]" in coverage_md and
      "目録外・未対応 | — | Full Shutdown（2025-07-31終了） |" in coverage_md,
      "QLDB General Reference mismatch needs its shutdown annotation")
check("AWS IoT 1-Click（関連サービス）は"+iot_1click_label+"。"
      "製品本体の提供状態とは区別" in coverage_md,
      "Related service must be marked as distinct, using product-neutral wording")
check("ボタン本体" not in coverage_md and "ボタン本体" not in product_md,
      "Related service wording must remain reusable for non-button products")
# Regression: a related service can have any lifecycle stage, including a
# future mapping with multiple entries, without implying a parent shutdown.
synthetic={
    "Example Dependency": [
        {"stage":"maintenance","end":"—"},
        {"stage":"sunset","end":"2027-04-30"},
        {"stage":"shutdown","end":"2027-12-31"}
    ]
}
synthetic_config={"lifecycle_related":{
    "Example Product":{"service":"Example Dependency","reason":"Integration dependency"}
}}
synthetic_text, synthetic_own=generator.product_lifecycle(
    "Example Product",synthetic_config,synthetic)
check(not synthetic_own and all(x in synthetic_text for x in (
      "関連サービスのMaintenance", "関連サービスのSunset",
      "関連サービスのFull Shutdown", "製品本体の提供状態とは区別")),
      "Related service must support Maintenance, Sunset and Shutdown generically")
# All lifecycle stages must appear in coverage even if General Reference
# matches by exact name or a reviewed alias. No state implies GA.
counts=Counter()
for item in products:
    name=item["name"]
    _,direct_rows=generator.product_lifecycle(name,mapping,source_lifecycle,snapshot_day)
    if not direct_rows:
        continue
    candidates=[row for row in coverage_md.splitlines()
                if row.startswith("| ["+name+"](")]
    for status in direct_rows:
        counts[status["stage"]]+=1
        expected=generator.lifecycle_coverage_note(status,snapshot_day)
        check(len(candidates)==1 and expected in candidates[0],
              "Coverage omits "+status["stage"]+" for Product "+name)
check(counts["shutdown"]>=14 and counts["maintenance"]>=12 and counts["sunset"]>=5,
      "Unexpectedly few official lifecycle matches in marketing inventory")
check("この差分表でも**Maintenance・Sunset・Full Shutdown" in coverage_md,
      "Coverage needs lifecycle scope explanation")
for name,statement in (("AWS App Runner",expected_label("AWS App Runner","maintenance")),
                       ("Amazon WorkSpaces Thin Client",thin_client_label)):
    rows=[line for line in coverage_md.splitlines() if line.startswith("| ["+name+"](")]
    check(len(rows)==1 and statement in rows[0],
          "Coverage spot-check missing: "+name)

summary="**公式Full Shutdown台帳でサービス本体の終了を確認: 14カード**"
check(summary+"\n\n[269項目との差分]" in product_md,
      "Full Shutdown summary must be a separate Markdown paragraph")
for name,target in (("AWS Local Zones","Amazon EC2"),
                    ("AWS Inferentia","Amazon EC2"),
                    ("AWS PrivateLink","Amazon VPC"),
                    ("AWS Transit Gateway","Amazon VPC"),
                    ("AWS VPN","Amazon VPC"),
                    ("Amazon Q","Amazon Q Business")):
    check(mapping.get("related_not_equivalent",{}).get(name,{}).get("reference")==target,
          "Related-but-not-equivalent rule missing: "+name)
check("非公開" in product_md and "仕様保証なし" in product_md and
      "原文ママ" in product_md,
      "Internal endpoint warning or original AWS spelling note missing")
check("## 照合サマリー" in coverage_md and
      coverage_md.index("## 照合サマリー")<coverage_md.index("## Products側の全件照合"),
      "Coverage summary must come before detailed rows")
for name in ("AWS DevOps Agent","Amazon SageMaker AI"):
    check("（ID: " in coverage_md and
          any(name in row for row in coverage_md.splitlines() if "（ID: " in row),
          "Duplicate product cards must be distinguished by ID")
check("Broadcom提供" in coverage_md and "旧VMware Cloud on AWS" not in coverage_md,
      "VMware Cloud on AWS must not be presented as a discontinued product")
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
