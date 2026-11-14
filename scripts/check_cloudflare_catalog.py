#!/usr/bin/env python3
"""Validate Cloudflare's frozen official Docs and Products source inventories."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1] / "cloud"
catalog = (ROOT / "cloudflare/catalog.md").read_text(encoding="utf-8")
products = (ROOT / "cloudflare/products.md").read_text(encoding="utf-8")
index = (ROOT / "cloudflare/README.md").read_text(encoding="utf-8")
root_index = (ROOT / "README.md").read_text(encoding="utf-8")

errors = []
def check(ok, msg):
    if not ok:
        errors.append(msg)

# Every entry must identify its upstream YAML and immutable commit.
pattern = re.compile(r"\[([^]\n]+\.yaml)\]\(https://github\.com/cloudflare/cloudflare-docs/blob/([a-f0-9]{40})/src/content/directory/([^)\n]+\.yaml)\)")
source_rows = pattern.findall(catalog)
names = [filename for filename, _, path in source_rows]
commits = {commit for _, commit, _ in source_rows}
check(len(names) == len(set(names)), "Duplicated upstream YAML filenames")
check(all(filename == path.split("/")[-1] for filename, _, path in source_rows),
      "Filename differs from upstream source")
check(len(commits) == 1, "Multiple upstream commits; snapshot must be immutable")
visible_match = re.search(r"Docs公開目録相当: \*\*(\d+)件\*\*", catalog)
hidden_match = re.search(r"Docs非表示エントリ: \*\*(\d+)件\*\*", catalog)
check(bool(visible_match and hidden_match) and
      int(visible_match.group(1)) + int(hidden_match.group(1)) == len(source_rows),
      "Docs visibility groups must reconcile to the complete YAML count")
count = re.search(r"の全件（(\d+)件）", catalog)
check(bool(count) and int(count.group(1)) == len(source_rows),
      "Docs YAML entry count mismatch")
check(bool(count) and "公式Docs索引" + count.group(1) + "件" in root_index,
      "Global cloud README count differs from Docs catalog")

# Product marketing comparison must include every item it claims.
product_lines = [line for line in products.splitlines()
                 if line.startswith("| ") and not line.startswith("| 公式Products掲載名 |")]
product_lines = [line for line in product_lines if line.count("|") == 4 and
                 not line.startswith("|---")]
product_names = [line.split("|")[1].strip() for line in product_lines]
check(len(product_names) == len(set(product_names)), "Duplicate marketing product rows")
check(len(product_names) == 68, "Expected 68 marketing products in frozen snapshot")
check("Basin" in product_names and "K2" in product_names, "Missing current Basin / K2 marketing products")
check("公式Products68件" in root_index, "Global README marketing count mismatch")
check("195エントリ" in index and "68項目" in index, "Cloudflare README count mismatch")
check("網羅的検証は未完了" in index, "GA/region audit limitation must remain explicit")

# Visible/hidden are documentation flags and must never be conflated with GA.
check("Docs非表示エントリ:" in catalog, "Missing docs visibility tracking")
check("提供段階" in catalog, "Missing verified-only availability field")
check("GA、プラン、地域" in catalog, "Must flag unverified GA/plans/regions")
check("Cloudflare Data Platform" not in index, "Avoid unsupported old branding")

if errors:
    for error in errors:
        print("ERROR:", error, file=sys.stderr)
    sys.exit(1)
print(f"OK: Cloudflare {len(source_rows)} official Docs YAML entries / "
      f"{len(product_names)} marketing products, one pinned upstream commit")
