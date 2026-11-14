#!/usr/bin/env python3
"""Rebuild a source-scoped AWS General Reference service inventory.

Data sources are official AWS General Reference pages for service endpoints,
Maintenance, Sunset, and Full Shutdown. This is NOT a list of every marketed
product or every feature, and a service with an endpoint is NOT necessarily GA.
"""
from __future__ import annotations

from datetime import datetime, timezone, date
from pathlib import Path
from urllib.parse import urljoin
from urllib.request import Request, urlopen
import argparse
import json
import re
import sys

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://docs.aws.amazon.com/general/latest/gr/"
SOURCES = {
    "endpoints": BASE + "aws-service-information.html",
    "maintenance": BASE + "maintenance_services.html",
    "sunset": BASE + "sunset_services.html",
    "shutdown": BASE + "full_shutdown_services.html",
}
LIFECYCLE_LABELS = {
    "maintenance": "Maintenance（新規利用制限あり）",
    "sunset": "Sunset（終了日を確認）",
    "shutdown": "Full Shutdown（終了済）",
}
# Exact overrides ONLY, after manual inspection. Not fuzzy matches.
INDEX_TO_LIFECYCLE = {"App Mesh": "AWS App Mesh",
                      "DevOps Guru": "Amazon DevOps Guru",
                      "Forecast": "Amazon Forecast",
                      "Lookout for Equipment": "Amazon Lookout for Equipment",
                      "Managed Blockchain": "Amazon Managed Blockchain",
                      "Migration Hub": "AWS Migration Hub",
                      "App Runner": "AWS App Runner",
                      "Audit Manager": "AWS Audit Manager",
                      "Cloud Directory": "Amazon Cloud Directory",
                      "CloudSearch": "Amazon CloudSearch",
                      "CodeGuru Reviewer": "Amazon CodeGuru Reviewer",
                      "AWS IoT Greengrass V1": "AWS IoT Greengrass V1",
                      "FinSpace": "Amazon FinSpace",
                      "Amazon Pinpoint": "Amazon Pinpoint",
                      "AWS Proton": "AWS Proton",
                      "AWS WAF Classic": "AWS WAF Classic",
                      "AWS Panorama": "AWS Panorama"}
CURATED_MAP = {
    "AWS Organizations": "Organizations",
    "AWS Control Tower": "AWS Control Tower",
    "AWS Service Catalog": "AWS Service Catalog endpoints and quotas",
    "AWS Resource Access Manager (RAM)": "AWS RAM",
    "AWS Audit Manager": "Audit Manager",
    "AWS Well-Architected Tool": "AWS Well-Architected",
    "Amazon Route 53 Application Recovery Controller": "ARC",
    "AWS Resilience Hub": "Resilience Hub",
    "AWS AppSync": "AWS AppSync",
    "Amazon EventBridge Pipes": "EventBridge Pipes",
    "Amazon Simple Email Service (SES)": "Amazon SES",
    "AWS End User Messaging": "AWS End User Messaging",
    "Amazon Braket": "Braket",
    "AWS Ground Station": "AWS Ground Station",
    "AWS IoT Greengrass": "AWS IoT Greengrass V2",
    "AWS Deadline Cloud": "AWS Deadline Cloud",
    "AWS HealthImaging": "HealthImaging",
    "AWS Clean Rooms": "AWS Clean Rooms",
    # AWS Artifact, Amazon Connect, AWS Quick, Amazon Nova are deliberately
    # not forced onto unrelated endpoints.
}

def get(url: str, fixture: Path | None, label: str) -> BeautifulSoup:
    if fixture is not None:
        raw = (fixture / (label + ".html")).read_bytes()
    else:
        request = Request(url, headers={"User-Agent": "Mozilla/5.0 knowledge-audit/1.0",
                                        "Accept-Language": "en-US,en;q=0.8"})
        with urlopen(request, timeout=45) as response:
            raw = response.read()
    if len(raw) < 5000:
        raise RuntimeError(f"{label}: incomplete official source ({len(raw)} bytes)")
    return BeautifulSoup(raw, "html.parser")

def clean(text: str) -> str:
    return re.sub(r"\s+", " ", text.replace("\u00a0", " ")).strip()

def official_catalog(soup: BeautifulSoup):
    candidates = [h for h in soup.find_all(re.compile("^h[1-6]$"))
                  if clean(h.get_text(" ", strip=True)) == "Services"]
    if not candidates:
        raise RuntimeError("Cannot find Services heading in official index")
    heading = candidates[-1]
    ul = heading.find_next("ul")
    if not ul:
        raise RuntimeError("Cannot find Services list after heading")
    records = []
    for li in ul.find_all("li", recursive=False):
        anchor = li.find("a", href=True)
        if not anchor:
            continue
        name, url = clean(anchor.get_text(" ", strip=True)), urljoin(SOURCES["endpoints"], anchor["href"])
        if not name or not url.startswith("https://docs.aws.amazon.com/"):
            continue
        records.append((name, url))
    if not 220 <= len(records) <= 500:
        raise RuntimeError(f"Only {len(records)} endpoints; HTML structure likely changed")
    if len(set(x[0] for x in records)) != len(records):
        raise RuntimeError("Duplicate endpoint directory labels; manual review needed")
    required = {"Amazon EC2", "Amazon S3", "Lambda", "Amazon RDS", "IAM"}
    if not required.issubset({n for n, _ in records}):
        raise RuntimeError("Unexpected AWS directory names, missing " + str(required - {n for n, _ in records}))
    return records

def lifecycle(soup: BeautifulSoup, stage: str):
    tables = soup.find_all("table")
    selected = next((t for t in tables if
                     "Service" in clean(t.get_text(" ", strip=True))[:200] and
                     ("Date" in clean(t.get_text(" ", strip=True))[:250])), None)
    if selected is None:
        raise RuntimeError(f"{stage}: cannot find official lifecycle table")
    out = []
    for tr in selected.find_all("tr"):
        cols = tr.find_all("td")
        if not cols:
            continue
        vals = [clean(c.get_text(" ", strip=True)) for c in cols]
        if len(vals) < 2 or not vals[0]:
            continue
        # Maintenance (service, announcement, resources)
        # Sunset (service, announcement, end-of-support, resources)
        # Shutdown (service, end-of-support, resources)
        announced = vals[1] if stage in ("maintenance", "sunset") else ""
        ended = vals[2] if stage == "sunset" else (vals[1] if stage == "shutdown" else "")
        links = [urljoin(SOURCES[stage], a["href"]) for a in tr.find_all("a", href=True)]
        out.append({"name": vals[0], "stage": stage, "announcement": announced,
                    "end_of_support": ended, "resources": links[0] if links else SOURCES[stage]})
    if len(out) < {"maintenance": 30, "sunset": 12, "shutdown": 35}[stage]:
        raise RuntimeError(f"{stage}: suspiciously few rows: {len(out)}")
    if len(set(r["name"] for r in out)) != len(out):
        raise RuntimeError(stage + ": duplicated lifecycle rows")
    return out

def esc(s: str) -> str:
    return s.replace("|", r"\|").replace("\n", " ")

def date_state(row, today):
    stage = row["stage"]
    if stage != "sunset":
        return LIFECYCLE_LABELS[stage]
    try:
        expires = datetime.strptime(row["end_of_support"], "%B %d, %Y").date()
    except ValueError:
        return LIFECYCLE_LABELS[stage]
    if expires <= today:
        return "終了日経過（Sunset掲載・Full Shutdown未照合）"
    return "Sunset（終了予定）"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--fixture-dir", type=Path, help="HTML fixtures; only for local parser tests")
    args = parser.parse_args()
    today = datetime.now(timezone.utc).date()
    pages = {key: get(url, args.fixture_dir, key) for key, url in SOURCES.items()}
    services = official_catalog(pages["endpoints"])
    lists = {k: lifecycle(pages[k], k) for k in ("maintenance", "sunset", "shutdown")}
    lifecycle_rows = [r for value in lists.values() for r in value]
    for item in lifecycle_rows:
        item["state"] = date_state(item, today)
    # Preserve the complete lifecycle records including features not in the
    # endpoint directory (do not silently suppress or conflate them).
    stages = {key: {r["name"]: r for r in lst} for key, lst in lists.items()}
    def get_lifecycle(name):
        lookup = INDEX_TO_LIFECYCLE.get(name, name)
        for stage in ("shutdown", "sunset", "maintenance"):
            if lookup in stages[stage]:
                return stages[stage][lookup]
        return None

    ids = {name for name, _ in services}
    aws_services = (ROOT / "cloud/aws/services.md").read_text(encoding="utf-8")
    before_moves = aws_services.split("## 横断比較へ移動した項目")[0]
    curated = [clean(line.split("|")[1]) for line in before_moves.splitlines()
               if line.startswith("| ") and not line.startswith("| サービス |")]
    if len(curated) != len(set(curated)) or len(curated) < 20:
        raise RuntimeError("Curated AWS inventory is unexpectedly changed")
    for original, reference in CURATED_MAP.items():
        if original not in curated or reference not in ids:
            raise RuntimeError(f"Invalid curated manual mapping: {original} => {reference}")

    out = ROOT / "cloud/aws"
    out.mkdir(parents=True, exist_ok=True)
    catalog = [
        "# AWS General Reference：エンドポイント・クォータ掲載サービス全件", "",
        f"**取得日 (UTC):** {today}  ",
        f"**公式出典:** [Service endpoints and quotas]({SOURCES['endpoints']})  ",
        f"**収録数:** **{len(services)}件**（公式Services一覧の全リンク）", "",
        "> この表はAWS公式General Referenceに掲載された**エンドポイント・クォータ参照項目**の全件です。",
        "> 提供中の商用製品一覧、GA製品数、全SKU、すべてのAWS機能と同義ではありません。",
        "> 終了済みのサービスも出典に残るため、掲載されているだけで新規導入可能とは判断できません。", "",
        "[ライフサイクル台帳](lifecycle.md) / [既存独自一覧との突合](coverage.md) / [AWS公式Products](https://aws.amazon.com/products/)", "",
        "| # | 公式参照名 | エンドポイント・クォータ | 公式ライフサイクル掲載（完全一致・手動別名のみ） |",
        "|---:|---|---|---|"
    ]
    for i, (name, url) in enumerate(services, 1):
        row = get_lifecycle(name)
        if row:
            status = f"[{row['state']}]({SOURCES[row['stage']]})"
        else:
            status = "該当記載なし（GA判定不可）"
        catalog.append(f"| {i} | {esc(name)} | [公式]({url}) | {status} |")
    (out / "catalog.md").write_text("\n".join(catalog)+"\n",encoding="utf-8")

    changes = [
        "# AWS公式ライフサイクル全件", "",
        f"**取得日 (UTC):** {today}", "",
        "公式のMaintenance/Sunset/Full Shutdownページの各表を全件収録。",
        "**状態はライフサイクル表への掲載であり、製品と個別機能が混在**しています。",
        "終了日を過ぎていてもSunset表に残る場合は、Full Shutdownと推測せず公式の掲載分類を残します。", "",
        f"- [Maintenance]({SOURCES['maintenance']}): **{len(lists['maintenance'])}件**",
        f"- [Sunset]({SOURCES['sunset']}): **{len(lists['sunset'])}件**",
        f"- [Full Shutdown]({SOURCES['shutdown']}): **{len(lists['shutdown'])}件**",""]
    for stage in ("maintenance", "sunset", "shutdown"):
        changes += [f"## {stage}（{len(lists[stage])}件）", "",
                    "| AWS公式掲載名（サービス・機能） | 発表日 | サポート終了日 | 公式根拠 |",
                    "|---|---|---|---|"]
        for row in lists[stage]:
            changes.append(f"| {esc(row['name'])} | {esc(row['announcement']) or '—'} | "
                           f"{esc(row['end_of_support']) or '—'} | [公式]({row['resources']}) |")
        changes.append("")
    (out / "lifecycle.md").write_text("\n".join(changes)+"\n",encoding="utf-8")

    coverage = [
        "# AWS個別一覧と公式エンドポイント目録の対応", "",
        f"**取得日:** {today} / [公式目録](catalog.md) / [既存の個別サービス一覧](services.md) / [横断比較](../service-comparison.md)", "",
        "独自一覧の22件をAWS General Referenceの見出しと突合します。公式目録にないことは、",
        "**製品が存在しないことの証明ではありません**（AWS ArtifactやAWS Quickなど）。",
        "表記ゆれは根拠なしの部分一致を避け、手動確認した1対1の名前マップだけ使います。", "",
        "| 個別一覧の名称 | 公式General Reference参照名 | 突合 |",
        "|---|---|---|"]
    matched = set()
    for name in curated:
        reference = CURATED_MAP.get(name, name)
        present = reference in ids
        if present:
            matched.add(reference)
        coverage.append(f"| {esc(name)} | {esc(reference) if present else '対象カタログに記載なし'} | "
                        f"{'照合済み' if present else '別のAWS公式製品資料で確認が必要'} |")
    coverage += ["", f"**個別一覧との照合:** {len(matched)} / {len(curated)}件", "",
                 "## 独立サービスかどうか・横断比較への振り分けの残課題", "",
                 "公式エンドポイント目録の各項目は**API/機能群**を含みます。"
                 "このカタログの全件収録と、他社比較への分類完了は別の作業です。", "",
                 "上記の個別22件以外も[公式エンドポイントカタログ](catalog.md)で全件検索できます。"
                 "機械的な文字列一致で50項目の5社比較へ流し込むことはしません。", ""]
    coverage += [
        "## エンドポイント一覧にない既存AWS独自項目の一次資料", "",
        "| 名称 | AWS公式資料 | 目録での扱い |",
        "|---|---|---|",
        "| AWS Artifact | [公式FAQ](https://aws.amazon.com/artifact/faq/) | コンプライアンス資料取得ポータル。専用エンドポイント項目とは別 |",
        "| Amazon Connect | [Connect Customerの製品概要](https://docs.aws.amazon.com/connect/latest/adminguide/what-is-amazon-connect.html) | Amazon Connectは製品群。General ReferenceのConnect Customer等と同一視しない |",
        "| AWS Quick | [2026-11-09改称告知](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-quick-aws-quick/) | AWS Quick Sightは一部機能で、AWS Quick全体とは異なる |",
        "| Amazon Nova | [Amazon Nova公式](https://aws.amazon.com/nova/) | 基盤モデル・関連サービス群。単独のエンドポイントサービス名ではない |",
        "",
        "これら4件は存在しないという意味ではなく、**採録基準となるAWS General Referenceの外側にある**という意味です。", ""
    ]
    (out / "coverage.md").write_text("\n".join(coverage),encoding="utf-8")

    overview = [
        "# AWS公式サービス目録の監査", "", f"**取得日:** {today}", "",
        "Cloudflareで採用した「全件の公式目録」と「編集された独自・横断比較」を分ける方針をAWSにも適用。", "",
        "| ファイル | 役割 |", "|---|---|",
        f"| [catalog.md](catalog.md) | General Referenceの **{len(services)}件**（サービスエンドポイント/クォータ一覧）の全件採録 |",
        f"| [lifecycle.md](lifecycle.md) | Maintenance **{len(lists['maintenance'])}件**、Sunset **{len(lists['sunset'])}件**、Full Shutdown **{len(lists['shutdown'])}件** の公式表を全件採録 |",
        f"| [coverage.md](coverage.md) | 既存[個別一覧](services.md)22件と公式参照名の突合。移動済みの項目は[横断表](../service-comparison.md)で管理 |",
        "| [services.md](services.md) | AWS独自・個別扱いの人手で編集した一覧（全製品カタログとは別） |", "",
        "## スコープの境界", "",
        "- **全件の範囲はGeneral Reference「Service endpoints and quotas」ページのServices節です。**",
        "- 公式の[マーケティング用製品ページ](https://aws.amazon.com/products/)は検索と絞り込みで掲載内容が変わるため、そこにある全製品の収録を確認したものではありません。",
        "- 製品のサブ機能・API・マーケットプレイス商品・リージョン・SKUと、エンドポイント・クォータの掲載項目は同じ粒度ではありません。",
        "- AWSのライフサイクル表は**サービスと機能の両方**を含みます。終了日を過ぎたSunset掲載項目も、正式なFull Shutdown掲載がなければ推測で改分類しません。",
        "- 出典に掲載されていないサービスや、新しい製品名への移行があっても、そのサービスが存在しないとは判断できません。", "",
        "## 現行名称の注意（2026-11時点）", "",
        "- **AWS Quick** は2026-11-09に旧Amazon Quickから改称。AWS Quick SightはそのBI機能。既存QuickSight APIと概念上別のため、公式参照表の名称を強制的に置換しません。",
        "  [公式告知](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-quick-aws-quick/)",
        "- **Amazon Pinpoint** は2026-10-30にサポート終了。",
        "  [AWS公式](https://docs.aws.amazon.com/pinpoint/latest/userguide/migrate.html)",
        "- **AWS App Mesh / AWS Proton / AWS WAF Classic** は2026年にサポート終了した製品。公式目録に残っていても新規採用を推奨しません。",
        "  [AWS公式ライフサイクル](https://docs.aws.amazon.com/general/latest/gr/full_shutdown_services.html)", "",
        "## 更新手順", "",
        "- `python -m pip install beautifulsoup4` で依存ライブラリを導入。",
        "- `python scripts/refresh_aws_service_catalog.py` で4つのAWS公式参照ページを読み、4つのMarkdownを再生成。",
        "- `python scripts/check_aws_service_catalog.py` で件数・重複・ライフサイクル参照・22件対応表を検証。",
        "- GitHub Actions `Propose AWS official service catalog refresh` の手動実行では、生成後の2本の検証を通して**レビュー用PR**を作ります。mainには直接pushしません。",
        "- `GITHUB_TOKEN`で作られたPRでは通常のPRトリガーが起動しないため、生成Workflow内で事前に整合性を検証します。PR作成を許可するリポジトリ設定が必要です。",
        "- 公式ページのレイアウトが変わった場合は最低件数・必須サービス名の検査で失敗させます。", "",
        "## 次の段階", "",
        "- マーケティング用AWS Productsの全件を別ソースで取得し、サービスエンドポイント目録と差集合を作る。",
        "- 公式参照項目のうち独立サービス・機能・旧製品を区別し、横断表と個別一覧の分類漏れをなくす。",
        "- 主要サービスの地域、GA、価格、契約条件を別途確認する。",""]
    (out / "README.md").write_text("\n".join(overview)+"\n",encoding="utf-8")
    # Update the shared progress counter from the official snapshot rather
    # than allowing the next monthly refresh to leave an outdated README.
    global_path = ROOT / "cloud/README.md"
    original = global_path.read_text(encoding="utf-8")
    dynamic = (f"エンドポイント/クォータ参照{len(services)}項目、"
               f"Maintenance {len(lists['maintenance'])}件、"
               f"Sunset {len(lists['sunset'])}件、"
               f"Full Shutdown {len(lists['shutdown'])}件")
    updated, occurrences = re.subn(
        r"エンドポイント/クォータ参照\d+項目、Maintenance \d+件、"
        r"Sunset \d+件、Full Shutdown \d+件", dynamic, original)
    if occurrences != 1:
        raise RuntimeError("Cannot locate AWS audit counts in cloud/README.md")
    global_path.write_text(updated,encoding="utf-8")
    print(json.dumps({"reference": len(services),
                      "lifecycle": {key: len(value) for key, value in lists.items()},
                      "curated_matched": len(matched), "curated_total": len(curated)},
                     ensure_ascii=False))

if __name__ == "__main__":
    main()
