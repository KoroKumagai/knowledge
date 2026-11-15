#!/usr/bin/env python3
"""Read AWS-maintained SSM public infrastructure Region lists, read-only.

These Parameter Store lists are service/endpoints discovery hints, not proof of
General Availability, new-customer onboarding or feature-level availability.
Require real AWS OIDC credentials; no dry-run value is shown as real evidence.
"""
from datetime import datetime, timezone
import argparse
import json
from pathlib import Path
import re

BASE="/aws/service/global-infrastructure/services"
REGION_CODES={"ap-northeast-1":"Tokyo","ap-northeast-3":"Osaka"}
# Candidate IDs. Each must be discovered in the official top-level SSM
# service directory before querying. No missing ID means a service is absent.
CANDIDATES={
    "VPC Lattice":"vpc-lattice",
    "Firehose":"firehose",
    "AWS Private CA":"acm-pca",
    "Kinesis Data Streams":"kinesis",
    "Amazon ML":"machinelearning",
    "Amazon SimpleDB":"sdb",
}

def all_params(client,path):
    next_token=None
    result=[]
    while True:
        opts={"Path":path,"Recursive":False,"WithDecryption":False,"MaxResults":10}
        if next_token:
            opts["NextToken"]=next_token
        data=client.get_parameters_by_path(**opts)
        result.extend(data.get("Parameters",[]))
        next_token=data.get("NextToken")
        if not next_token:
            return result

def probe(client):
    directory=all_params(client,BASE)
    ids={item.get("Name","").removeprefix(BASE+"/") for item in directory
         if re.fullmatch(re.escape(BASE)+r"/[^/]+",item.get("Name",""))}
    result={"as_of_utc":datetime.now(timezone.utc).isoformat(),
            "source":"AWS Systems Manager public parameters", "read_region":"us-east-1",
            "source_path":BASE, "interpretation":"service-region directory only, not GA",
            "regions":REGION_CODES,"items":[]}
    for service,candidate in CANDIDATES.items():
        entry={"service":service,"ssm_id_candidate":candidate,
               "ssm_id_found":candidate in ids,"tokyo":"未確認",
               "osaka":"未確認","reason":""}
        if candidate not in ids:
            entry["reason"]="SSM識別子が公式サービス一覧に無い。提供なしという意味ではない"
        else:
            values=all_params(client,BASE+"/"+candidate+"/regions")
            available=set()
            for row in values:
                region=row.get("Value","")
                if re.fullmatch(r"[a-z]{2}(?:-gov)?-[a-z]+-\d+",region):
                    available.add(region)
            for code,label in REGION_CODES.items():
                entry[label.lower()]="SSMに地域値あり（GA未保証）" if code in available else "SSM地域値なし（不提供と断定不可）"
            entry["region_count"]=len(available)
            entry["region_values"]=sorted(available)
            entry["reason"]="公式公開パラメータ。サービス提供・新規契約には別途公式資料の確認が必要"
        result["items"].append(entry)
    return result

def selftest():
    class Fake:
        def get_parameters_by_path(self,**kw):
            p=kw["Path"]
            if p==BASE and not kw.get("NextToken"):
                return {"Parameters":[{"Name":BASE+"/kinesis"}],"NextToken":"second"}
            if p==BASE and kw.get("NextToken")=="second":
                return {"Parameters":[{"Name":BASE+"/firehose"}]}
            if p==BASE+"/kinesis/regions":
                return {"Parameters":[{"Value":"ap-northeast-1"},{"Value":"ap-northeast-3"}]}
            if p==BASE+"/firehose/regions":
                return {"Parameters":[{"Value":"ap-northeast-1"}]}
            raise AssertionError("Unexpected path "+p)
    out=probe(Fake())
    k=next(x for x in out["items"] if x["service"]=="Kinesis Data Streams")
    f=next(x for x in out["items"] if x["service"]=="Firehose")
    m=next(x for x in out["items"] if x["service"]=="Amazon ML")
    assert k["ssm_id_found"] and "地域値あり" in k["tokyo"] and "地域値あり" in k["osaka"]
    assert f["ssm_id_found"] and "地域値なし" in f["osaka"]
    assert not m["ssm_id_found"] and m["tokyo"]=="未確認"
    assert out["interpretation"]=="service-region directory only, not GA"
    print("OK: SSM public parameter discovery pagination, explicit IDs and unknown semantics")

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--self-test",action="store_true")
    ap.add_argument("--output",default="aws-ssm-region-probe.json")
    args=ap.parse_args()
    if args.self_test:
        selftest()
        return
    try:
        import boto3
    except ImportError as exc:
        raise SystemExit("Install boto3 or run --self-test") from exc
    client=boto3.client("ssm",region_name="us-east-1")
    result=probe(client)
    Path(args.output).write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print("SSM read-only region probe written",args.output,"(NOT GA verification)")

if __name__=="__main__":
    main()
