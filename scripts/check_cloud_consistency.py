#!/usr/bin/env python3
"""Validate the manually curated cloud comparison and provider-specific inventories.

Run: python scripts/check_cloud_consistency.py
No third-party dependencies. Does not attempt to validate a full official catalog.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent / "cloud"
PROVIDERS = {"aws": (2, "AWS"), "azure": (3, "Azure"),
             "google": (4, "Google Cloud"), "oracle": (5, "OCI"),
             "cloudflare": (6, "Cloudflare")}
ALIASES = {
    "Amazon Bedrock AgentCore": "Bedrock AgentCore",
    "AWS Application Migration Service (MGN)": "AWS Application Migration Service",
    "Azure Dev Box": "Dev Box",
    "Microsoft Defender for Cloud": "Defender for Cloud",
    "Google Cloud Deploy": "Cloud Deploy",
    "Foundry Agent Service": "Microsoft Foundry Agent Service",
    "Pages": "Cloudflare Pages",
    "Queues": "Cloudflare Queues",
    "Workflows": "Cloudflare Workflows",
}

errors = []

def check(condition, message):
    if not condition:
        errors.append(message)

def section(text, heading):
    match = re.search(r"^## " + re.escape(heading) + r"\s*$", text, re.M)
    if not match:
        errors.append("Missing section: " + heading)
        return ""
    tail = text[match.end():]
    stop = re.search(r"^## ", tail, re.M)
    return tail[:stop.start()] if stop else tail

def bullets(text):
    return [x[2:].strip().strip("*") for x in text.splitlines() if x.startswith("- ") and x != "- なし"]

def service_terms(cell):
    """Match full service entries separated by ' / '; never match partial names.

    e.g. Workers must not match Workers AI, Microsoft Entra ID must not
    match Microsoft Entra External ID. ALIASES bridge display-name differences.
    """
    return {part.strip() for part in re.split(r"\s+/\s+", cell) if part.strip()}

def product_rows(text):
    return [(pieces[0], pieces[1]) for line in text.splitlines()
            if line.startswith("| ") and not line.startswith("| サービス |")
            for pieces in [list(map(str.strip, line.strip("|").split("|")))]
            if len(pieces) == 2]

comparison = (ROOT / "service-comparison.md").read_text(encoding="utf-8")
readme = (ROOT / "README.md").read_text(encoding="utf-8")
start = comparison.index("| 領域 |")
stop = comparison.index("\n## サービスの廃止・改称・変更履歴", start)
raw_rows = [line for line in comparison[start:stop].splitlines()
            if line.startswith("| ") and not line.startswith("| 領域 |")]
rows = [list(map(str.strip, line.strip("|").split("|"))) for line in raw_rows]
check(all(len(row) == 8 for row in rows), "Cross-provider rows must have 8 columns")
check(all(sum(cell != "対象外" for cell in row[2:7]) >= 2 for row in rows if len(row) == 8),
      "Every cross-provider row must have at least two providers")
check(all("要確認" not in "|".join(row) for row in rows), "Unresolved '要確認' in table")
check(all("—" not in "|".join(row[2:7]) for row in rows), "Use '対象外' for unsupported cells")

match = re.search(r"## 比較可能な機能の横断表（(\d+)項目）", comparison)
check(bool(match) and int(match.group(1)) == len(rows), "Cross-provider count mismatch")
check(f"比較可能な{len(rows)}項目" in readme, "README cross-provider count mismatch")

# Within the comparison table, each area must be a contiguous block.
seen = set()
previous = None
for row in rows:
    if len(row) != 8:
        continue
    area = row[0]
    if area != previous:
        check(area not in seen, f"Repeated disjoint area: {area}")
        seen.add(area)
        previous = area

for slug, (column, label) in PROVIDERS.items():
    text = (ROOT / slug / "services.md").read_text(encoding="utf-8")
    primary = text.split("## 横断比較へ移動した項目")[0]
    main_names = [name for name, _ in product_rows(primary)]
    moved = bullets(section(text, "横断比較へ移動した項目"))
    excluded = bullets(section(text, "機能・旧名のため除外・統合した項目"))
    excluded_names = [entry.split("**", 2)[1] for entry in excluded if entry.startswith("**")]

    count_match = re.search(r"\| " + re.escape(label) +
        r" \| \[個別一覧\]\(" + re.escape(slug) +
        r"/services\.md\) \| 採録候補(\d+)件 \|", readme)
    check(bool(count_match) and int(count_match.group(1)) == len(main_names),
          f"{slug}: README count mismatch ({len(main_names)} rows)")
    check(len(main_names) == len(set(main_names)), f"{slug}: duplicate primary product names")
    check(len(moved) == len(set(moved)), f"{slug}: duplicate moved product names")
    check(not (set(moved) & set(excluded_names)), f"{slug}: moved and excluded overlap")
    for name in moved:
        check(name not in main_names, f"{slug}: moved item remains in primary list: {name}")
        target = ALIASES.get(name, name)
        check(any(len(row) == 8 and target in service_terms(row[column]) for row in rows),
              f"{slug}: no cross-provider destination for: {name} (lookup: {target})")
    for name in excluded_names:
        check(name not in main_names, f"{slug}: excluded entry still in primary list: {name}")

    for name in main_names:
        check(not any(len(row) == 8 and name in service_terms(row[column]) for row in rows),
              f"{slug}: product exists in both primary list and comparison: {name}")

check("Workers" not in service_terms("Workers AI"), "Whole-name matching broken (Workers)")
check("Microsoft Entra ID" not in service_terms("Microsoft Entra External ID"),
      "Whole-name matching broken (Entra ID)")
check("Workers" in service_terms("Agents SDK / Workers"),
      "Slash-separated comparison matching broken")
check("## レビュー反映（2026-11-14）" not in readme, "PR-only notes in README")
check("同じ役割の5社製品" not in readme, "Obsolete 5-company comparison wording")

if errors:
    for err in errors:
        print("ERROR:", err, file=sys.stderr)
    sys.exit(1)
print(f"OK: {len(rows)} comparison rows; 5 provider inventories and move/exclusion histories consistent")
