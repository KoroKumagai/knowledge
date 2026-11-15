#!/usr/bin/env python3
"""Render/check the 33+95 unresolved AWS inventory; do not infer GA from a listing."""
from collections import Counter
from pathlib import Path
import argparse, json, re, sys

BASE=Path(__file__).resolve().parents[1]/"cloud/aws"
OUT=BASE/"open-items.md"
UNKNOWN="未確認"
NOT_APPLICABLE="対象外（終了済み）"
RETIRED_KIND="提供終了の旧製品"

def load(name):
    return json.loads((BASE/name).read_text(encoding="utf-8"))

def cells(line):
    return [x.strip().replace(r"\|","|") for x in re.split(r"(?<!\\)\|",line.strip())[1:-1]]

def esc(x):
    return str(x).replace("|",r"\|").replace("\n"," ")

def source_rows():
    products={}
    for line in (BASE/"products.md").read_text(encoding="utf-8").splitlines():
        if not line.startswith("| "): continue
        c=cells(line)
        if len(c)==5 and c[4]!="ディレクトリID":
            products[c[4]]=c
    refs={}
    for line in (BASE/"catalog.md").read_text(encoding="utf-8").splitlines():
        if not re.match(r"^\| \d+ \|",line):continue
        c=cells(line)
        if len(c)!=4 or c[1] in refs:
            raise ValueError("Invalid reference: "+line[:150])
        hit=re.search(r"\[公式\]\((https://docs\.aws\.amazon\.com/[^)]+)\)",c[2])
        if not hit:raise ValueError("Reference source missing "+c[1])
        refs[c[1]]=(hit.group(1),c[3])
    return products,refs

def unmatched():
    coverage=(BASE/"products-coverage.md").read_text(encoding="utf-8")
    names=[]
    for line in coverage.splitlines():
        if "| 目録外・未対応 |" in line and line.startswith("| ["):
            hit=re.match(r"^\| \[([^\]]+)\]\(",line)
            if hit:names.append(hit.group(1))
    section="## General Reference側の未対応項目"
    if coverage.count(section)!=1:raise ValueError("Reference section missing")
    refs=[]
    for line in coverage.split(section)[1].splitlines():
        if not line.startswith("| ") or line.startswith("| General Reference"):continue
        c=cells(line)
        if len(c)==3:refs.append(c[0])
    if len(names)!=33 or len(refs)!=95 or len(set(refs))!=95:
        raise ValueError("Unexpected unresolved counts: "+str((len(names),len(refs))))
    return names,refs

def is_shutdown(s):
    return s.startswith("[Full Shutdown（")

def phase(s):
    if is_shutdown(s):return "Full Shutdown（公式台帳）"
    if s.startswith("[Sunset（"):return "Sunset（公式台帳）"
    if s.startswith("[Maintenance（"):return "Maintenance（公式台帳）"
    return UNKNOWN

def render():
    taxonomy=load("open-items-classification.json")
    evidence=load("availability-evidence.json")
    cards=load("products-source.json")["products"]
    byid={x["id"]:x for x in cards}
    original,refs=source_rows()
    product_names,ref_names=unmatched()
    products=taxonomy["product_cards"]
    reference=taxonomy["reference_entries"]
    if len(products)!=33 or len(reference)!=95 or len({x["id"] for x in products})!=33:
        raise ValueError("Taxonomy must include 33 unique Product IDs and 95 references")
    if len({x["name"] for x in reference})!=95:
        raise ValueError("Taxonomy must include 95 unique references")
    if Counter(byid[x["id"]]["name"] for x in products)!=Counter(product_names):
        raise ValueError("Products taxonomy does not match exact unresolved cards")
    if set(x["name"] for x in reference)!=set(ref_names):
        raise ValueError("Reference taxonomy does not match unresolved entries")
    if any(not x["kind"] or not x.get("basis") for x in products+reference):
        raise ValueError("Incomplete provisional taxonomy classification")
    # Terminated services must be classified consistently in both official
    # source lists, irrespective of whether evidence records exist.
    for row in products:
        own=original.get(row["id"])
        if own is None:
            raise ValueError("Product card missing: "+row["id"])
        if is_shutdown(own[3]) and row["kind"]!=RETIRED_KIND:
            raise ValueError("Full Shutdown Product must be retired: "+row["id"])
    for row in reference:
        name=row["name"]
        if name not in refs:
            raise ValueError("General Reference not in catalog: "+name)
        if is_shutdown(refs[name][1]) and row["kind"]!=RETIRED_KIND:
            raise ValueError("Full Shutdown Reference must be retired: "+name)
    facts={}
    for item in evidence["records"]:
        key=(item["type"],item["key"])
        if key in facts:
            raise ValueError("Duplicate verification record: "+str(key))
        if item["type"]=="reference":
            valid=item["key"] in ref_names
        elif item["type"]=="product":
            valid=item["key"] in {r["id"] for r in products}
        else:
            valid=False
        if not valid:
            raise ValueError("Evidence key outside the unresolved 33+95 scope: "+str(key))
        if not item.get("sources") or not all(
                u.startswith(("https://docs.aws.amazon.com/","https://aws.amazon.com/"))
                for u in item["sources"]):
            raise ValueError("Official source links required for verified claims")
        if any(not item.get(field) for field in ("ga","tokyo","osaka","contract")):
            raise ValueError("Each verified fact must specify all verification dimensions")
        facts[key]=item
    # Regression checks for adoption-critical facts. Document discrepancies,
    # do not silently choose one conflicting official date.
    q=facts.get(("reference","Amazon Q Business"))
    glacier=facts.get(("reference","Amazon Glacier"))
    if (not q or not all(day in q["contract"]+q["notes"]
                         for day in ("2026-07-30","2026-07-31"))):
        raise ValueError("Amazon Q Business official cutoff discrepancy must remain visible")
    if (not glacier or "2025-12-15" not in glacier["contract"]
        or not any("aws.amazon.com/s3/glacier/pricing" in url
                   for url in glacier["sources"])):
        raise ValueError("Amazon Glacier vault new-customer freeze requires AWS pricing evidence")
    glacier_kind=next(x["kind"] for x in reference if x["name"]=="Amazon Glacier")
    if glacier_kind!="終了予定・提供制限の製品":
        raise ValueError("Legacy Amazon Glacier vaults must be classified as restricted")
    if phase(refs["Amazon Glacier"][1])!="Maintenance（公式台帳）":
        raise ValueError("Legacy Glacier General Reference must show Maintenance")
    kinesis_kind=next(x["kind"] for x in reference if x["name"]=="Kinesis Data Streams")
    if kinesis_kind!="独立サービス・専門サービス候補":
        raise ValueError("Kinesis Data Streams independent billable service classification regressed")
    counts=Counter(x["kind"] for x in products+reference)
    out=[
      "# AWS未対応項目：一次分類と提供条件の検証台帳","",
      "**基準日:** 2026-11-15 / [Products原票](products-source.json) / "
      "[General Reference](catalog.md) / [公式ライフサイクル](lifecycle.md)","",
      "> **33カード＋95参照項目の一次分類まで完了。すべてのGA・リージョン・契約条件を検証したわけではありません。**",
      "> 一次分類は公式見出しや製品説明からの暫定判断です。独立課金サービス数・GA・契約可能性を確定しません。",
      "> 東京（ap-northeast-1）と大阪（ap-northeast-3）を優先確認。未確認は不提供と同じ意味ではありません。",
      "> APIエンドポイント掲載はGA・契約可能性を保証しません。ライフサイクルはサービス本体と個別機能を区別します。","",
      "**一覧:** Products 33カード（カードIDで区別）/ General Reference 95項目。"
      " **公式根拠付き個別確認:** "+str(len(facts))+"件（すべての列が確定したという意味ではありません）。","",
      "## 調査方法と今後のデータソース","",
      "- GA：公式GA発表またはライフサイクルの一次資料による。目録への掲載だけではGAとはしない。",
      "- リージョン：公式の製品提供状況とAPIエンドポイントを分ける。APIがあることは新規契約可を意味しない。",
      "- 契約条件：新規受付・販売方式・課金単位・サポートプランを個別に確認する。",
      "- [AWS Capabilities by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/)を優先調査先とする。",
      "- AWSが公開する[リージョンデータのS3アクセス方法](https://aws.amazon.com/blogs/storage/building-automated-aws-regional-availability-checks-with-amazon-s3/)はAWS認証・IAM権限を必要とする。無認証で全件取得できたとは主張しない。","",
      "## 暫定分類の内訳","",
      "| 暫定分類 | 件数 |","|---|---:|"]
    for kind,count in sorted(counts.items()):
        out.append("| "+esc(kind)+" | "+str(count)+" |")
    out+=["","## Products側の未対応33カード","",
          "全33件を分類と公式ライフサイクルに絞って表示。終了済みの製品は後方にまとめています。",
          "GA・リージョン・契約条件は下段の検証済み記録だけに示します。","",
          "| 公式Productsカード | 暫定分類 | 公式ライフサイクル | 出典 |",
          "|---|---|---|---|"]
    for row in sorted(products, key=lambda x:
                      (is_shutdown(original[x["id"]][3]), x["kind"], byid[x["id"]]["name"], x["id"])):
        card=byid[row["id"]]
        own=original[row["id"]]
        out.append("| "+" | ".join([
            esc(card["name"])+" (ID: "+row["id"]+")",
            esc(row["kind"]),own[3],
            "[AWS Products]("+card["url"]+")"])+" |")
    out+=["","## General Reference側の未対応95項目","",
          "全95件は元の公式参照へのリンクと暫定分類を掲載。Full Shutdownは末尾にまとめています。","",
          "| 公式General Reference | 暫定分類 | 公式ライフサイクル | 出典 |",
          "|---|---|---|---|"]
    for row in sorted(reference, key=lambda x:
                      (is_shutdown(refs[x["name"]][1]), x["kind"], x["name"])):
        name=row["name"]
        url,state=refs[name]
        out.append("| "+" | ".join([
            esc(name),esc(row["kind"]),state,"[公式参照]("+url+")"])+" |")
    out+=["","## GA・リージョン・契約条件を個別確認した記録","",
          "ここに掲載するのは**根拠付きで個別確認した項目だけ**です。"
          "各列の「未確認」は不提供を意味しません。",
          "Full Shutdownの製品について、リージョン別の新規利用可否は「対象外（終了済み）」と表示します。","",
          "| 公式名称 | GA・提供段階 | 東京 | 大阪 | 契約条件 | 根拠の適用範囲 | AWS一次資料 |",
          "|---|---|---|---|---|---|---|"]
    for item in evidence["records"]:
        links=" / ".join("[AWS "+str(i)+"]("+u+")"
                       for i,u in enumerate(item["sources"],1))
        label=(byid[item["key"]]["name"] if item["type"]=="product"
               else item["key"])
        source_lifecycle=(original[item["key"]][3] if item["type"]=="product"
                          else refs[item["key"]][1])
        discontinued=is_shutdown(source_lifecycle) or item["ga"].startswith("Full Shutdown")
        tokyo=NOT_APPLICABLE if discontinued else item["tokyo"]
        osaka=NOT_APPLICABLE if discontinued else item["osaka"]
        out.append("| "+" | ".join([
            esc(label),esc(item["ga"]),esc(tokyo),esc(osaka),
            esc(item["contract"]),esc(item["notes"]),links])+" |")
    out+=["","## 次の検証","",
          "1. 128項目の一次分類について、公式ドキュメントを基に製品本体・機能・旧名称を追加で確定する。",
          "2. 東京・大阪を優先に、AWS Capabilities by Regionと個別サービス文書で地域可用性を検証する。",
          "3. 新規顧客受付、料金モデル、契約条件、サポートプランを個別に確認する。",
          "4. 終了済み・Maintenance製品を新規採用可能と誤認しないよう再確認する。","",
          "再生成：python scripts/render_aws_open_items.py --write / 検証：同 --check。",
          "分類原本：[open-items-classification.json](open-items-classification.json)。",
          "確認根拠：[availability-evidence.json](availability-evidence.json)。",""]
    return "\n".join(out).rstrip()+"\n"

def main():
    p=argparse.ArgumentParser()
    group=p.add_mutually_exclusive_group(required=True)
    group.add_argument("--write",action="store_true")
    group.add_argument("--check",action="store_true")
    args=p.parse_args()
    text=render()
    if args.check:
        if not OUT.exists() or OUT.read_text(encoding="utf-8")!=text:
            print("ERROR: open-items.md is stale or incomplete",file=sys.stderr)
            sys.exit(1)
        print("OK: all 33 unmatched Products and 95 reference items classified; evidence traceable")
    else:
        OUT.write_text(text,encoding="utf-8")
        print("WROTE",OUT,len(text))

if __name__=="__main__":
    main()
