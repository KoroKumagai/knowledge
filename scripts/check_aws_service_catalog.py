#!/usr/bin/env python3
"""Verify the AWS official reference snapshot, lifecycle data and curated mapping.

The checks prove consistency WITHIN the frozen AWS General Reference scope,
not that every AWS product, API or SKU is represented.
"""
from collections import Counter
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
    "| # | 公式参照名 | エンドポイント・クォータ | 公式ライフサイクル掲載（完全一致・手動別名のみ） |",
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
check(all(("該当記載なし（GA判定不可）" in row[3]) or
          (row[3].startswith("[") and "docs.aws.amazon.com/" in row[3])
          for row in catalog_rows), "Lifecycle status must link its official source")
for note in ("商用製品一覧", "新規導入可能"):
    check(note in catalog, "Reference scope warning missing: "+note)

groups = {}
for key in ("maintenance", "sunset", "shutdown"):
    m = re.search(r"^## " + key + r"（(\d+)件）$", lifecycle, re.M)
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
    groups[key] = trows
check(set(groups) == {"maintenance", "sunset", "shutdown"},
      "Lifecycle three stages not fully represented")
check("サービスと機能" in lifecycle and "Full Shutdown" in lifecycle,
      "Lifecycle scope warnings missing")

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
        check("別のAWS公式製品資料で確認が必要" in result,
              "Unknown coverage classification: "+name)
check(f"個別一覧との照合:** " in coverage, "Coverage summary missing")
check(f"**{len(catalog_rows)}件**" in readme,
      "AWS README reference count mismatch")
check("公式カタログ網羅性の進捗" in root_readme and
      "[調査結果](aws/README.md)" in root_readme,
      "Global README lacks AWS progress")
check("AWS Quick" in services and "Amazon Quick Suite" not in services,
      "AWS Quick 2026 branding not updated")

if errors:
    for err in errors:
        print("ERROR:",err,file=sys.stderr)
    sys.exit(1)
print(f"OK: AWS General Reference {len(catalog_rows)} entries, "
      f"lifecycle { {k:len(v) for k,v in groups.items()} }, "
      f"curated {len(curated)} matched to coverage table")
