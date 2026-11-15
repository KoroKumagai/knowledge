#!/usr/bin/env python3
"""Offline schema/provenance audit for the 128 unresolved AWS catalog entries.

"未確認" is never turned into unavailable. Stale evidence is WARNING-only.
A service endpoint/SSM listing cannot automatically establish GA or sign-up.
"""
from __future__ import annotations
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path
import argparse
import json
import sys

ROOT=Path(__file__).resolve().parents[1]
AWS=ROOT/"cloud/aws"
SCHEMA=AWS/"availability-decisions.json"
OUTPUT=AWS/"availability-decisions.md"
DIM=("phase","tokyo","osaka","new_customers","support_plan","commitment","sales_channel")
ALLOWED={
    "確認済み","公式記載なし","対象外（ツール）","対象外（グローバル）",
    "対象外（物理端末）","対象外（終了済み）","未確認"
}
NONE="未確認"

def files():
    return (
        json.loads(SCHEMA.read_text(encoding="utf-8")),
        json.loads((AWS/"open-items-classification.json").read_text(encoding="utf-8")),
        json.loads((AWS/"availability-evidence.json").read_text(encoding="utf-8")),
        json.loads((AWS/"products-source.json").read_text(encoding="utf-8"))
    )

def audit(as_of=None):
    state,cls,evidence,products=files()
    now=date.fromisoformat(as_of) if as_of else date.today()
    if state["schema_version"]!=1 or state["max_age_days"]!=180:
        raise ValueError("Unexpected verification schema version/expiry rule")
    rows=state["records"]
    byid={p["id"]:p["name"] for p in products["products"]}
    expected={("product",x["id"]):byid[x["id"]] for x in cls["product_cards"]}
    expected.update({("reference",x["name"]):x["name"] for x in cls["reference_entries"]})
    if len(expected)!=128 or len(rows)!=128:
        raise ValueError("Audit must cover exactly 33 Product IDs + 95 Reference names")
    kinds={("product",x["id"]):x["kind"] for x in cls["product_cards"]}
    kinds.update({("reference",x["name"]):x["kind"] for x in cls["reference_entries"]})
    checks={("product",x["id"]):x for x in cls["product_cards"]}
    checks.update({("reference",x["name"]):x for x in cls["reference_entries"]})
    keyset=set()
    count=Counter()
    stale=[]
    evidence_keys={(x["type"],x["key"]) for x in evidence["records"]}
    evidence_bykey={(x["type"],x["key"]):x for x in evidence["records"]}
    confirmed=[]
    for item in rows:
        key=(item.get("type"),item.get("key"))
        if key in keyset or key not in expected or item.get("name")!=expected[key]:
            raise ValueError("Duplicate/missing/renamed audit row "+str(key))
        keyset.add(key)
        statuses=item.get("status") or {}
        if set(statuses)!=set(DIM) or not set(statuses.values()).issubset(ALLOWED):
            raise ValueError("Invalid audit status dimensions: "+str(key))
        for dim,val in statuses.items():
            count[(dim,val)]+=1
        if any(v!="未確認" for v in statuses.values()):
            if not item.get("verified_on") or not item.get("sources") or not item.get("scope"):
                raise ValueError("Audited decision needs verification date, official source and scope "+str(key))
            checked=date.fromisoformat(item["verified_on"])
            age=(now-checked).days
            if age < 0:
                raise ValueError("Verification date in future for "+str(key))
            if age > state["max_age_days"]:
                stale.append((item["name"],age))
            if not all(u.startswith(("https://aws.amazon.com/","https://docs.aws.amazon.com/"))
                       for u in item["sources"]):
                raise ValueError("Audit decision needs AWS official URLs "+str(key))
        elif item.get("verified_on") and item.get("sources"):
            # An old open inquiry remains allowed, but is not called complete.
            pass
        if any(v in ("確認済み","公式記載なし") for v in statuses.values()):
            if key not in evidence_keys:
                raise ValueError("Source-backed decision must have an evidence record: "+str(key))
            fact=evidence_bykey[key]
            if not fact.get("verified_on") or not fact.get("sources") or not fact.get("scope"):
                raise ValueError("Evidence needs date/official URLs/scope "+str(key))
            if any(v=="公式記載なし" for v in statuses.values()) and not item.get("scope"):
                raise ValueError("Not-found status requires scope "+str(key))
            confirmed.append(item["name"])
        if any(v=="対象外（ツール）" for v in statuses.values()) and kinds[key]!="ツール・SDK・配布物":
            raise ValueError("Tool exclusion is not a tool: "+str(key))
        if any(v=="対象外（物理端末）" for v in statuses.values()) and kinds[key]!="端末・アプライアンス":
            raise ValueError("Physical-device exclusion without device category: "+str(key))
        if any(v=="対象外（終了済み）" for v in statuses.values()):
            # Statuses of terminated services are grounded by the official
            # lifecycle snapshot; check that an official shutdown exists.
            name=item["name"]
            original=(AWS/"products.md").read_text(encoding="utf-8") if key[0]=="product" else (AWS/"catalog.md").read_text(encoding="utf-8")
            lines=original.splitlines()
            official=[line for line in lines if
                     ("| "+name+" |" in line if key[0]=="reference"
                      else line.startswith("| "+name+" |") and (" | "+key[1]+" |" in line))]
            if not any("Full Shutdown" in line for line in official):
                raise ValueError("Retired exclusion without full shutdown source: "+name)
        if statuses["phase"]=="確認済み":
            confirmed.append(item["name"])
    if keyset!=set(expected):
        raise ValueError("Missing audit IDs: "+repr(sorted(set(expected)-keyset)))
    for f in evidence["records"]:
        verified=date.fromisoformat(f["verified_on"])
        if verified>now:
            raise ValueError("Evidence date is in future: "+str(f["key"]))
        if (now-verified).days>state["max_age_days"] and not any(
              x[0]==f["key"] for x in stale):
            stale.append((f["key"],(now-verified).days))
    return state,count,stale,confirmed

def esc(x):
    return str(x).replace("|",r"\|").replace("\n"," ")

def render(state,count,stale):
    dimensions=list(DIM)
    names={
        "phase":"提供段階","tokyo":"東京","osaka":"大阪",
        "new_customers":"新規顧客受付","support_plan":"サポートプラン",
        "commitment":"事前契約","sales_channel":"購入経路"
    }
    rows=state["records"]
    out=[
        "# AWS未対応128項目：適用可否・根拠付き判定の進捗","",
        "**基準日:** "+state["review_date"]+" / **再検証期限:** 180日超でWARN（CIは失敗させない）","",
        "> **確認済み = サービスのGAとは限りません。** 受付停止・契約制限の事実が確認できた場合も含みます。",
        "> **未確認 ≠ 利用不可**、**公式記載なし ≠ 提供なし**。対象外はツール／地域概念のないサービス／物理端末／終了済みに限り、理由とAWS公式出典を記録します。",
        "> AWS SSM公開パラメータはエンドポイント/リージョン候補の補助情報であり、GA、新規顧客受付、契約可能性の直接の証拠にはしません。","",
        "公式根拠の全文と確認範囲は [availability-evidence.json](availability-evidence.json)、"
        "128件の個別判定・適用理由は [availability-decisions.json](availability-decisions.json)。","",
        "## 次元別判定（128行×7次元）","",
        "| 次元 | 確認済み | 公式記載なし | 対象外 | 未確認 |",
        "|---|---:|---:|---:|---:|"]
    for d in dimensions:
        n=lambda s:count[(d,s)]
        na=sum(v for (dim,status),v in count.items() if dim==d and status.startswith("対象外"))
        vals=(n("確認済み"),n("公式記載なし"),na,n("未確認"))
        if sum(vals)!=128:
            raise ValueError("Dimensions do not total 128: "+d)
        out.append("| "+names[d]+" | "+" | ".join(map(str,vals))+" |")
    out+=["","## 第1段：優先6項目（現時点での根拠状況）","",
          "| 項目 | 提供段階 | 東京 / 大阪 | 新規顧客受付 | 公式根拠 |",
          "|---|---|---|---|---|"]
    for name in ("VPC Lattice","Firehose","AWS Private CA","Kinesis Data Streams",
                 "Amazon ML","Amazon SimpleDB"):
        xs=[x for x in rows if x["type"]=="reference" and x["name"]==name]
        if len(xs)!=1:
            raise ValueError("Stage1 service not found: "+name)
        v=xs[0]
        links=" / ".join("[AWS "+str(j)+"]("+url+")" for j,url in enumerate(v["sources"],1))
        out.append("| "+esc(name)+" | "+v["status"]["phase"]+" | "+
                   v["status"]["tokyo"]+" / "+v["status"]["osaka"]+" | "+
                   v["status"]["new_customers"]+" | "+links+" |")
    out+=["","## 実施上の制限と次段階","",
          "- SSMの読取専用OIDCロールは未接続。実際のSSMパラメータ取得結果が無い段階では、リージョンをSSMにより確定しません。",
          "- 第2段＝独立サービス候補、第3段＝親子機能・専門API、第4段＝ツール・グローバル・終了済みの適用可否判定。",
          "- 「対象外（ツール）」や「対象外（終了済み）」でもサポート・移行義務の調査が必要な場合があります。",
          "- 金額・最低利用期間は転載せず [availability-evidence.json](availability-evidence.json) の公式料金URLを使用します。",
          ""]
    if stale:
        out+=["## 再確認が必要（180日超）",""]
        out.extend("- "+esc(name)+"（"+str(days)+"日前に検証）" for name,days in stale)
        out.append("")
    else:
        out+=["**再確認期限切れ:** なし（判定済みの根拠のみを対象とした判定）",""]
    return "\n".join(out).rstrip()+"\n"

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--check",action="store_true")
    ap.add_argument("--write",action="store_true")
    ap.add_argument("--as-of",type=str,default=None)
    args=ap.parse_args()
    state,count,stale,confirmed=audit(args.as_of)
    expected=render(state,count,stale if not args.as_of else [])
    for name,age in stale:
        print(f"WARN: AWS evidence {name} verified {age} days ago; recheck after 180d")
    if args.write:
        OUTPUT.write_text(expected,encoding="utf-8")
    if args.check:
        if not OUTPUT.is_file() or OUTPUT.read_text(encoding="utf-8")!=expected:
            raise SystemExit("ERROR: availability-decisions.md stale; regenerate")
    print("OK: 128 tracked; 7 dimensional statuses; "+
          str(sum(count[("phase",s)] for s in ("確認済み","公式記載なし")))+
          " phase dimensions source-backed; 180-day warning rule; "+
          str(len(stale))+" stale evidence items")

if __name__=="__main__":
    main()
