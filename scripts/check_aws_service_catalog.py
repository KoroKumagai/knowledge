#!/usr/bin/env python3
"""Verify the AWS official reference snapshot, lifecycle data and curated mapping.

The checks prove consistency WITHIN the frozen AWS General Reference scope,
not that every AWS product, API or SKU is represented.
"""
from collections import Counter
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1] / "cloud"
AWS = ROOT / "aws"
catalog = (AWS / "catalog.md").read_text(encoding="utf-8")
lifecycle = (AWS / "lifecycle.md").read_text(encoding="utf-8")
coverage = (AWS / "coverage.md").read_text(encoding="utf-8")
readme = (AWS / "README.md").read_text(encoding="utf-8")
services = (AWS / "services.md").read_text(encoding="utf-8")
root_readme = (ROOT / "README.md").read_text(encoding="utf-8")
mapping = json.loads((AWS / "lifecycle-mapping.json").read_text(encoding="utf-8"))
unmatched_doc = (AWS / "lifecycle-unmatched.md").read_text(encoding="utf-8")
errors = []

def check(ok, message):
    if not ok:
        errors.append(message)

def cells(line):
    return [x.strip() for x in re.split(r"(?<!\\)\|", line.strip())[1:-1]]

def table(text, header, sep, cols):
    lines = text.splitlines()
    indices = [i for i, line in enumerate(lines) if line == header]
    check(len(indices) == 1, "Expected one table: " + header)
    if len(indices) != 1:
        return []
    i = indices[0]
    check(i + 1 < len(lines) and lines[i+1] == sep, "Invalid table separator")
    data = []
    for line in lines[i+2:]:
        if not line.startswith("| "):
            break
        entries = cells(line)
        check(len(entries) == cols, "Bad table row width: "+line[:90])
        data.append(entries)
    return data

catalog_rows = table(catalog,
    "| # | 公式参照名 | エンドポイント・クォータ | 公式ライフサイクル掲載（本体と機能を区別） |",
    "|---:|---|---|---|", 4)
official = [row[1] for row in catalog_rows]
check(len(official) >= 220, "Unreasonably small AWS General Reference snapshot")
check(len(set(official)) == len(official), "Duplicate General Reference names")
check(all(row[0] == str(i) for i, row in enumerate(catalog_rows, 1)),
      "Catalog row sequence has gaps")
check({"Amazon EC2", "Amazon S3", "Lambda", "Amazon RDS", "IAM"}.issubset(set(official)),
      "Missing essential reference entries")
n = re.search(r"\*\*収録数:\*\* \*\*(\d+)件\*\*", catalog)
check(bool(n) and int(n.group(1)) == len(catalog_rows),
      "Catalog stated total does not equal rows")
check(all(row[2].startswith("[公式](https://docs.aws.amazon.com/") for row in catalog_rows),
      "Catalog entries must link to AWS official reference")
check(all(
    ("該当記載なし（GA判定不可）" in row[3])
    or ("機能単位の掲載あり" in row[3] and
        "](lifecycle.md)" in row[3] and "本体のGA判定不可" in row[3])
    or (row[3].startswith("[") and "docs.aws.amazon.com/" in row[3])
    for row in catalog_rows), "Lifecycle status must link to its official source")
for feature_name in ("SageMaker AI", "CloudTrail", "AWS Glue",
                     "AWS Service Catalog endpoints and quotas",
                     "Amazon SNS", "Systems Manager", "Amazon RDS",
                     "AWS Direct Connect", "Amazon Chime SDK"):
    feature_match = [row for row in catalog_rows if row[1] == feature_name]
    check(len(feature_match) == 1 and "機能単位の掲載あり" in feature_match[0][3],
          "Missing parent-service feature lifecycle warning: " + feature_name)
check(any(row[1] == "Amazon Glacier" and "Maintenance" in row[3]
          for row in catalog_rows),
      "Legacy Amazon Glacier must display Maintenance in General Reference")
check("機能だけがMaintenance" in catalog,
      "Catalog must distinguish parent service and feature lifecycle")
for note in ("商用製品一覧", "新規導入可能"):
    check(note in catalog, "Reference scope warning missing: "+note)

groups = {}
for key in ("maintenance", "sunset", "shutdown"):
    title = {"maintenance": "Maintenance（新規受付停止・継続提供）",
             "sunset": "Sunset（終了予定）",
             "shutdown": "Full Shutdown（終了済み）"}[key]
    m = re.search(r"^## " + re.escape(title) + r" — (\d+)件$", lifecycle, re.M)
    check(bool(m), "Missing lifecycle section: "+key)
    if not m:
        continue
    section = lifecycle[m.end():]
    section = section.split("\n## ", 1)[0]
    lines = section.splitlines()
    trows = [cells(line) for line in lines
             if line.startswith("| ") and not line.startswith("| AWS公式掲載名")]
    check(all(len(row) == 4 for row in trows),
          "Lifecycle section wrong number of columns: "+key)
    check(len(trows) == int(m.group(1)),
          "Lifecycle count doesn't match rows: "+key)
    check(len(set(row[0] for row in trows)) == len(trows),
          "Duplicate lifecycle entries: "+key)
    check(all(row[3].startswith("[公式](https://") for row in trows),
          "Missing lifecycle source URLs: "+key)
    check(all(re.fullmatch(r"\d{4}-\d{2}-\d{2}|—", field)
              for row in trows for field in row[1:3]),
          "Lifecycle dates must be ISO-8601 or dash: " + key)
    groups[key] = trows
check(set(groups) == {"maintenance", "sunset", "shutdown"},
      "Lifecycle three stages not fully represented")
check("製品と個別機能" in lifecycle and "Full Shutdown" in lifecycle and
      "発表日 ≠ 新規受付停止日" in lifecycle and "2026-04-30" in lifecycle,
      "Lifecycle scope warnings missing")

# The same manually reviewed mapping is consumed by the generator and checker.
# Every lifecycle row not attached to an endpoint is intentionally a WARN and
# remains inspectable in lifecycle-unmatched.md, not silently dropped.
check(mapping.get("version") == 1, "Unknown AWS lifecycle mapping format")
direct_aliases = mapping.get("direct_service_names", {})
check(direct_aliases.get("Amazon Glacier") == "Amazon S3 Glacier Direct",
      "Legacy Amazon Glacier vaults must map to official Direct maintenance entry")
prefix_aliases = mapping.get("feature_prefixes", {})
exact_aliases = mapping.get("feature_exact", {})
for group_name, values in (("direct", direct_aliases),
                           ("prefixes", prefix_aliases),
                           ("exact", exact_aliases)):
    check(isinstance(values, dict) and set(values).issubset(set(official)),
          "Lifecycle mapping contains unknown catalog entries in " + group_name)

source_entries = []
for stage in ("maintenance", "sunset", "shutdown"):
    source_entries.extend((stage, row[0], row[3]) for row in groups.get(stage, []))

def feature_of(parent, lifecycle_name):
    prefixes = [parent] + prefix_aliases.get(parent, [])
    return lifecycle_name in exact_aliases.get(parent, []) or any(
        lifecycle_name.startswith((prefix + " – ", prefix + " - "))
        for prefix in prefixes)

for parent, explicit in exact_aliases.items():
    for feature in explicit:
        check(any(name == feature for _, name, _ in source_entries),
              "Exact alias no longer present in lifecycle: " + parent + " -> " + feature)

linked = set()
for row in catalog_rows:
    parent = row[1]
    canonical = direct_aliases.get(parent, parent)
    direct = [entry for entry in source_entries if entry[1] == canonical]
    related = [entry for entry in source_entries if feature_of(parent, entry[1])]
    linked.update((entry[0], entry[1]) for entry in direct + related)
    if related and not direct:
        check("機能単位の掲載あり" in row[3],
              "Unlabeled feature lifecycle for: " + parent)

unmatched = [entry for entry in source_entries
             if (entry[0], entry[1]) not in linked]
unmatched_lines = [line for line in unmatched_doc.splitlines()
                   if line.startswith("| ") and not line.startswith("| 公式ステータス |")]
unmatched_rows = [cells(line) for line in unmatched_lines]
check(all(len(row) == 3 for row in unmatched_rows),
      "Unmatched lifecycle report must have three Markdown columns")
stage_labels = {"maintenance": "Maintenance（新規利用制限あり）",
                "sunset": "Sunset（終了日を確認）",
                "shutdown": "Full Shutdown（終了済）"}
expected_unmatched = [
    [stage_labels[stage], name, source.replace("[公式]", "[AWS公式]")]
    for stage, name, source in unmatched]
check(unmatched_rows == expected_unmatched,
      "Unmatched lifecycle report differs from official records or aliases")
expected_summary = f"**未対応:** **{len(unmatched)} / {len(source_entries)}件**"
check(expected_summary in unmatched_doc, "Unmatched lifecycle count mismatch")
check(f"未対応 **{len(unmatched)} / {len(source_entries)}件**" in readme,
      "AWS README unresolved lifecycle count mismatch")
check("未対応は**製品が存在しない" in unmatched_doc,
      "Unmatched lifecycle items must not imply a product is unavailable")
if unmatched:
    print(f"WARN: {len(unmatched)} / {len(source_entries)} AWS lifecycle rows "
          "not linked to a General Reference service; review cloud/aws/lifecycle-unmatched.md")


curated = [cells(line)[0] for line in
           services.split("## 横断比較へ移動した項目")[0].splitlines()
           if line.startswith("| ") and not line.startswith("| サービス")]
mapped = table(coverage,
    "| 個別一覧の名称 | 公式General Reference参照名 | 突合 |",
    "|---|---|---|", 3)
check(len(curated) == len(mapped),
      "Every curated service must appear in coverage")
check(len(set(curated)) == len(curated),
      "Duplicate curated service name")
check([row[0] for row in mapped] == curated,
      "Coverage row order/names must match curated AWS services.md")
for name, reference, result in mapped:
    if result == "照合済み":
        check(reference in official, "Verified coverage ref absent from catalog: "+name)
    else:
        check("General Referenceの範囲外（公式資料で確認済み）" in result,
              "Unknown coverage classification: "+name)
check(f"個別一覧との照合:** " in coverage, "Coverage summary missing")
check(f"**{len(catalog_rows)}件**" in readme,
      "AWS README reference count mismatch")
check("公式カタログ網羅性の進捗" in root_readme and
      "[調査結果](aws/README.md)" in root_readme,
      "Global README lacks AWS progress")
comparison = (ROOT / "service-comparison.md").read_text(encoding="utf-8")
check("2026-04-30以降、新規顧客利用不可（2026-03-31発表）" in comparison and
      comparison.count("2026-04-30以降、新規顧客利用不可（2026-03-31発表）") == 2,
      "AWS App Runner effective date must appear correctly in both comparison rows")
check("Amazon Quick Suiteを移行候補" not in comparison and
      "AWS Quick（旧Amazon Quick / Quick Suite）" in comparison,
      "AWS Quick rebrand must be consistent across comparison and individual list")
check("SageMaker AIの一部機能" in comparison and
      "(aws/lifecycle.md)" in comparison,
      "MLOps row must point to feature lifecycle limitations")
check("Application Registry機能はMaintenance" in services,
      "Service Catalog subordinate feature maintenance warning missing")
check("AWS Quick" in services and "Amazon Quick Suite" not in services,
      "AWS Quick 2026 branding not updated")

if errors:
    for err in errors:
        print("ERROR:",err,file=sys.stderr)
    sys.exit(1)
print(f"OK: AWS General Reference {len(catalog_rows)} entries, "
      f"lifecycle { {k:len(v) for k,v in groups.items()} }, "
      f"curated {len(curated)} matched to coverage table")
