#!/usr/bin/env python3
"""Audit a frozen Cloudflare Docs YAML snapshot and curated Products mappings.

Every source filename must be present in the pinned catalog. This is NOT a
guarantee that the documentation index represents all available Cloudflare APIs,
SKUs or released services.
"""
from collections import Counter
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1] / "cloud"
CF = ROOT / "cloudflare"
catalog = (CF / "catalog.md").read_text(encoding="utf-8")
products = (CF / "products.md").read_text(encoding="utf-8")
services = (CF / "services.md").read_text(encoding="utf-8")
index = (CF / "README.md").read_text(encoding="utf-8")
root_index = (ROOT / "README.md").read_text(encoding="utf-8")
statuses = json.loads((CF / "catalog-status.json").read_text(encoding="utf-8"))

errors = []

def check(value, message):
    if not value:
        errors.append(message)

def pinned_commit(text, pattern, label):
    matches = re.findall(pattern, text)
    check(len(matches) == 1, "Exactly one " + label + " source SHA required")
    return matches[0] if len(matches) == 1 else None

catalog_pin = pinned_commit(
    catalog,
    r"\*\*固定ソース:\*\* \[cloudflare-docs [^\]]+\]\(https://github\.com/cloudflare/cloudflare-docs/commit/([a-f0-9]{40})\)",
    "catalog")
products_pin = pinned_commit(
    products,
    r"\*\*Docs照合元コミット:\*\* \x60([a-f0-9]{40})\x60",
    "products")
check(bool(catalog_pin and catalog_pin == products_pin),
      "Products and Docs must use the SAME pinned source commit")
if catalog_pin:
    check("blob/" + catalog_pin + "/src/content/directory/" in catalog,
          "Catalog must explain fixed YAML source path")

catalog_rows = [line for line in catalog.splitlines()
                if line.startswith("| ") and re.search(r"\x60[a-z0-9.-]+\.yaml\x60 \|$", line)]
catalog_files = []
catalog_display_names = set()
for line in catalog_rows:
    cells = [c.strip() for c in line.strip("|").split("|")]
    check(len(cells) == 5, "Docs row must have 5 columns: " + line[:100])
    if len(cells) != 5:
        continue
    name, visibility, stage, docs_url, filename = cells
    catalog_display_names.add(name)
    catalog_files.append(filename.strip(chr(96)))
    check(visibility in ("公開", "非表示", "URLなし"),
          "Unknown visibility value: " + visibility)
    check(stage == "未個別確認" or ("http" in stage and stage.startswith("[")),
          "Verified status must include a source URL: " + name)

check(len(catalog_files) == len(set(catalog_files)), "Duplicated Docs YAML filename")
docs_total = re.search(r"の全件（(\d+)件）", catalog)
check(bool(docs_total) and int(docs_total.group(1)) == len(catalog_files),
      "Catalog header must match the number of YAML rows")
visible = re.search(r"Docs公開目録相当: \*\*(\d+)件\*\*", catalog)
hidden = re.search(r"Docs非表示エントリ: \*\*(\d+)件\*\*", catalog)
if visible and hidden:
    count_vis = sum(" | 公開 | " in line for line in catalog_rows)
    count_hidden = sum(" | 非表示 | " in line for line in catalog_rows)
    check(int(visible.group(1)) == count_vis, "Docs visible count mismatch")
    check(int(hidden.group(1)) == count_hidden, "Docs hidden count mismatch")
    check(count_vis + count_hidden == len(catalog_rows),
          "Unexpected URL-less entries require separate coverage")
else:
    check(False, "Catalog missing visibility counts")

product_rows = [line for line in products.splitlines()
                if line.startswith("| ") and not line.startswith("| 公式Products掲載名 |")
                and line.count("|") == 5]
product_files = []
product_names = []
classes = Counter()
for line in product_rows:
    cells = [c.strip() for c in line.strip("|").split("|")]
    if len(cells) != 4:
        check(False, "Product row does not have 4 columns")
        continue
    name, linked_doc, classification, note = cells
    matches = re.findall(r"\x60([a-z0-9.-]+\.yaml)\x60", linked_doc)
    check(len(matches) == 1, "Product must identify one YAML source: " + name)
    if matches:
        product_files.extend(matches)
    product_names.append(name)
    classes[classification] += 1
    check(classification in {"同名", "改称", "表記ゆれ", "機能・製品群"},
          "Unknown Products comparison class: " + classification)
    check(linked_doc.startswith("[公式](https://developers.cloudflare.com/"),
          "Product Docs link missing: " + name)

check(len(product_names) == len(set(product_names)), "Duplicate Products display names")
check(len(product_names) == 68, "Expected 68 frozen Products entries")
check({"K2", "Basin"}.issubset(set(product_names)),
      "K2 and Basin must be present")
check(set(product_files).issubset(set(catalog_files)),
      "Products refers to upstream YAML absent from catalog: " +
      str(sorted(set(product_files) - set(catalog_files))))
check(classes == {"同名": 49, "改称": 1, "表記ゆれ": 5, "機能・製品群": 13},
      "Unexpected classification totals: " + str(classes))
check("Page Shield" in product_names and
      any(line.startswith("| Page Shield |") and "| 改称 |" in line for line in product_rows),
      "Page Shield must be classified as legacy naming")
check("195エントリ" in index and "68項目" in index,
      "Cloudflare README catalog counts stale")
check("公式Products68件" in root_index and "公式Docs索引195件" in root_index,
      "Global cloud README counts stale")
check("網羅的検証は未完了" in index and "GA、プラン、地域" in catalog,
      "Limitations about GA and regional availability must remain explicit")

# The standalone curated list uses different display names for some Docs entries.
# These mappings identify documentation coverage; not necessarily identical products.
DISPLAY_ALIASES = {
    "Cloudflare Access": "Access",
    "Cloudflare Gateway": "Gateway",
    "Cloudflare WARP": "WARP Client",
    "Cloudflare Realtime": "Realtime",
    "Email Routing": "Email Service",  # A feature, not an exact one-to-one product
    "Web Analytics": "Cloudflare Web Analytics",
    "Cloudflare Radar": "Radar",
    "Cloudflare Zaraz": "Zaraz",
}
primary = services.split("## 横断比較へ移動した項目")[0]
names = [line.split("|")[1].strip() for line in primary.splitlines()
         if line.startswith("| ") and not line.startswith("| サービス |")]
check(len(names) == 27, "Expected 27 provider-specific curated entries")
check(len(names) == len(set(names)), "Duplicate provider-specific service")
for name in names:
    target = DISPLAY_ALIASES.get(name, name)
    check(target in catalog_display_names,
          "Standalone Cloudflare entry missing from catalog: " + name +
          " (expected Docs: " + target + ")")

valid_statuses = statuses.get("statuses", {})
check(bool(statuses.get("verified_on")) and isinstance(valid_statuses, dict),
      "Curated status verification metadata missing")
check(all(slug + ".yaml" in catalog_files for slug in valid_statuses),
      "Status data references missing upstream YAML")
for slug, data in valid_statuses.items():
    check(bool(data.get("verified_on")) and data.get("source", "").startswith("https://"),
          "Status lacks a verification date or source URL: " + slug)

if errors:
    for error in errors:
        print("ERROR:", error, file=sys.stderr)
    sys.exit(1)
print(f"OK: Cloudflare {len(catalog_files)} Docs YAML entries, " +
      f"{len(product_names)} Products (single commit), " +
      f"{len(names)} curated services; classes: {dict(classes)}")
