# AWS個別一覧と公式エンドポイント目録の対応

**取得日:** 2026-11-14 / [公式目録](catalog.md) / [既存の個別サービス一覧](services.md) / [横断比較](../service-comparison.md)

独自一覧の22件をAWS General Referenceの見出しと突合します。公式目録にないことは、
**製品が存在しないことの証明ではありません**（AWS ArtifactやAWS Quickなど）。
表記ゆれは根拠なしの部分一致を避け、手動確認した1対1の名前マップだけ使います。

| 個別一覧の名称 | 公式General Reference参照名 | 突合 |
|---|---|---|
| AWS Organizations | Organizations | 照合済み |
| AWS Control Tower | AWS Control Tower | 照合済み |
| AWS Service Catalog | AWS Service Catalog endpoints and quotas | 照合済み |
| AWS Resource Access Manager (RAM) | AWS RAM | 照合済み |
| AWS Audit Manager | Audit Manager | 照合済み |
| AWS Artifact | 対象カタログに記載なし | 別のAWS公式製品資料で確認が必要 |
| AWS Well-Architected Tool | AWS Well-Architected | 照合済み |
| Amazon Route 53 Application Recovery Controller | ARC | 照合済み |
| AWS Resilience Hub | Resilience Hub | 照合済み |
| AWS AppSync | AWS AppSync | 照合済み |
| Amazon EventBridge Pipes | EventBridge Pipes | 照合済み |
| Amazon Simple Email Service (SES) | Amazon SES | 照合済み |
| AWS End User Messaging | AWS End User Messaging | 照合済み |
| Amazon Braket | Braket | 照合済み |
| AWS Ground Station | AWS Ground Station | 照合済み |
| AWS IoT Greengrass | AWS IoT Greengrass V2 | 照合済み |
| Amazon Connect | 対象カタログに記載なし | 別のAWS公式製品資料で確認が必要 |
| AWS Deadline Cloud | AWS Deadline Cloud | 照合済み |
| AWS HealthImaging | HealthImaging | 照合済み |
| AWS Clean Rooms | AWS Clean Rooms | 照合済み |
| AWS Quick | 対象カタログに記載なし | 別のAWS公式製品資料で確認が必要 |
| Amazon Nova | 対象カタログに記載なし | 別のAWS公式製品資料で確認が必要 |

**個別一覧との照合:** 18 / 22件

## 独立サービスかどうか・横断比較への振り分けの残課題

公式エンドポイント目録の各項目は**API/機能群**を含みます。このカタログの全件収録と、他社比較への分類完了は別の作業です。

上記の個別22件以外も[公式エンドポイントカタログ](catalog.md)で全件検索できます。機械的な文字列一致で50項目の5社比較へ流し込むことはしません。

## エンドポイント一覧にない既存AWS独自項目の一次資料

| 名称 | AWS公式資料 | 目録での扱い |
|---|---|---|
| AWS Artifact | [公式FAQ](https://aws.amazon.com/artifact/faq/) | コンプライアンス資料取得ポータル。専用エンドポイント項目とは別 |
| Amazon Connect | [Connect Customerの製品概要](https://docs.aws.amazon.com/connect/latest/adminguide/what-is-amazon-connect.html) | Amazon Connectは製品群。General ReferenceのConnect Customer等と同一視しない |
| AWS Quick | [2026-11-09改称告知](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-quick-aws-quick/) | AWS Quick Sightは一部機能で、AWS Quick全体とは異なる |
| Amazon Nova | [Amazon Nova公式](https://aws.amazon.com/nova/) | 基盤モデル・関連サービス群。単独のエンドポイントサービス名ではない |

これら4件は存在しないという意味ではなく、**採録基準となるAWS General Referenceの外側にある**という意味です。
