# クラウドサービス整理

**基準日:** 2026-11-14（JST）  
**対象:** AWS / Azure / Google Cloud / Oracle Cloud Infrastructure / Cloudflare

## ディレクトリ

```text
cloud/
├── README.md
├── service-comparison.md   # 2社以上で用途を比較できるサービス
├── aws/
│   └── services.md          # AWS独自・個別扱い
├── azure/
│   └── services.md          # Azure独自・個別扱い
├── google/
│   └── services.md          # Google Cloud独自・個別扱い
├── oracle/
│   └── services.md          # OCI独自・個別扱い
├── cloudflare/
│   └── services.md          # Cloudflare独自・個別扱い
└── oracle-cloud.md          # OCIの運用メモ（既存ファイル・変更なし）
```

## 分類基準

1. **横断比較:** 2社以上で同目的のサービスが実在し、選定の対象になる場合のみ [service-comparison.md](service-comparison.md) へ載せる。機能の一部のみの類似や、構成上の代替は同一行に押し込まない。
2. **各社別:** その会社特有の製品体系、別物の実行モデル、機能を組み合わせて初めて類似するものは各社一覧へ分離する。**独自一覧への掲載は他社に類似製品が皆無という意味ではない**。
3. **重複排除:** 同じサービスの重複掲載は原則避ける。比較可能なサービスは横断表を優先し、独自技術・機能の説明が不可欠な場合は個別表から横断表を参照する。
4. **現行掲載と利用可否は別:** 廃止済み・終了予定・プレビュー・リージョン限定は採用前に必ず確認。
5. **全件網羅の基準:** 公式製品/サービスカタログで掲載される粒度。サービス内の個別機能（例: Distributed Map、BigQuery ML）、個別API、料金SKU、リージョン、Marketplace出品商品は別の対象。今回の個別一覧は全件網羅を**完了していない**ため、空白を「サービスなし」と解釈しない。

## 一覧

| 区分 | ファイル | 備考 |
|---|---|---|
| 5社横断 | [機能比較](service-comparison.md) | 比較可能な38項目 |
| AWS | [個別一覧](aws/services.md) | 採録候補24件 |
| Azure | [個別一覧](azure/services.md) | 採録候補20件 |
| Google Cloud | [個別一覧](google/services.md) | 採録候補16件 |
| OCI | [個別一覧](oracle/services.md) | 採録候補26件 |
| Cloudflare | [個別一覧](cloudflare/services.md) | 採録候補35件 |

## 全製品の確認元

- AWS: [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html) / [全製品](https://aws.amazon.com/products/)
- Azure: [製品ディレクトリ](https://azure.microsoft.com/en-us/products/)
- Google Cloud: [Products at a glance](https://docs.cloud.google.com/docs/product-list)
- Oracle Cloud: [OCI Documentation - Services](https://docs.oracle.com/en-us/iaas/Content/)
- Cloudflare: [Docs directory](https://developers.cloudflare.com/directory/)

## 更新時の手順

1. 5社の公式カタログに対して一覧を突合し、未収録品、改称品、廃止済み品、終了予定品を確認。
2. 同じ役割の5社製品として意味のある対応だけを横断表へ残す。対応先がない製品を「—」の列で水増しせず、各社ディレクトリに記録。
3. 「実行モデル」「ステートの扱い」「SQL・API互換性」「認証・権限」「リージョン・SLA」「価格」「IaC対応」を比較する。単純なサービス名の類似で結論を出さない。
4. 見直した日付と参照先を更新し、可能なら変更の根拠をコミットまたはPRに記載する。

> 全サービスカタログとの自動突合、完全なGA/終了ステータスの検証は別途必要。上記件数は今回の**採録件数**であり、各社の総サービス数ではない。

## 更新時の確認事項（TODO）

- 各社の公式カタログとの全件照合は未完了。網羅率を保証しない。
- 2026-11時点のプレビュー・リージョン・終了予定を製品単位で再確認する。
- 具体的な導入検討時は類似製品の機能範囲・契約条件の差を公式仕様で確認する。

## レビュー反映（2026-11-14）

- 2社以上で直接比較できるものを共通表へ。直接の対応先がないセルは「対象外」と記載。
- AWS Bedrock Agents Classic / Q Business のメンテナンス移行、CodeCommit再開を反映。
- 旧Cloudflare CallsをRealtimeへ統合、Agent Memoryのprivate betaを注記。
- 独自表から重複製品、他社との機能比較対象、製品内機能を整理。
