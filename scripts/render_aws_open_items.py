#!/usr/bin/env python3
"""Render/check the 33+95 unresolved AWS inventory; do not infer GA from a listing."""
from collections import Counter
from pathlib import Path
import argparse, json, re, sys

BASE=Path(__file__).resolve().parents[1]/"cloud/aws"
OUT=BASE/"open-items.md"
UNKNOWN="未確認"

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

def phase(s):
    if s.startswith("[Full Shutdown（"):return "Full Shutdown（公式台帳）"
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
    facts={}
    for item in evidence["records"]:
        key=(item["type"],item["key"])
        if key in facts or item["type"]!="reference" or item["key"] not in ref_names:
            raise ValueError("Bad evidence identifier: "+str(key))
        if not item.get("sources") or not all(
                u.startswith(("https://docs.aws.amazon.com/","https://aws.amazon.com/"))
                for u in item["sources"]):
            raise ValueError("Official source links required for verified claims")
        if any(not item.get(field) for field in ("ga","tokyo","osaka","contract")):
            raise ValueError("Each verified fact must specify all verification dimensions")
        facts[key]=item
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
          "| 公式Productsカード | 暫定分類 | 既存ライフサイクル | GA・提供状態 | 東京 | 大阪 | 契約条件 | 根拠 |",
          "|---|---|---|---|---|---|---|---|"]
    for row in products:
        card=byid[row["id"]]
        own=original.get(row["id"])
        if not own:raise ValueError("Missing original Product card: "+row["id"])
        out.append("| "+" | ".join([
            esc(card["name"])+" (ID: "+row["id"]+")",
            esc(row["kind"]),own[3],phase(own[3]),UNKNOWN,UNKNOWN,UNKNOWN,
            "[AWS Products]("+card["url"]+")"])+" |")
    out+=["","## General Reference側の未対応95項目","",
          "| 公式General Reference | 暫定分類 | ライフサイクルの掲載 | GA・提供状態 | 東京 | 大阪 | 契約条件 | 根拠 |",
          "|---|---|---|---|---|---|---|---|"]
    for row in reference:
        name=row["name"]
        if name not in refs:raise ValueError("Reference link absent: "+name)
        url,state=refs[name]
        fact=facts.get(("reference",name))
        ga= fact["ga"] if fact else phase(state)
        tokyo= fact["tokyo"] if fact else UNKNOWN
        osaka= fact["osaka"] if fact else UNKNOWN
        contract= fact["contract"] if fact else UNKNOWN
        links=("[公式参照]("+url+")" +
               (" "+" / ".join("[根拠"+str(i)+"]("+u+")"
                   for i,u in enumerate(fact["sources"],1)) if fact else ""))
        out.append("| "+" | ".join([
            esc(name),esc(row["kind"]),state,esc(ga),esc(tokyo),
            esc(osaka),esc(contract),links])+" |")
    out+=["","## 個別の公式確認例","",
          "| 名称 | 確認範囲・留意点 | 公式出典 |",
          "|---|---|---|"]
    for item in evidence["records"]:
        links=" / ".join("[AWS "+str(i)+"]("+u+")"
                       for i,u in enumerate(item["sources"],1))
        out.append("| "+esc(item["key"])+" | "+esc(item["notes"])+" | "+links+" |")
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
