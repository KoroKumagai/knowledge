# AWS未対応128項目：適用可否・根拠付き判定の進捗

**基準日:** 2026-11-15 / **再検証期限:** 180日超でWARN（CIは失敗させない）

> **確認済み = サービスのGAとは限りません。** 受付停止・契約制限の事実が確認できた場合も含みます。
> **未確認 ≠ 利用不可**、**公式記載なし ≠ 提供なし**。対象外はツール／地域概念のないサービス／物理端末／終了済みに限り、理由とAWS公式出典を記録します。
> AWS SSM公開パラメータはエンドポイント/リージョン候補の補助情報であり、GA、新規顧客受付、契約可能性の直接の証拠にはしません。

公式根拠の全文と確認範囲は [availability-evidence.json](availability-evidence.json)、128件の個別判定・適用理由は [availability-decisions.json](availability-decisions.json)。

## 次元別判定（128行×7次元）

| 次元 | 確認済み | 公式記載なし | 対象外 | 未確認 |
|---|---:|---:|---:|---:|
| 提供段階 | 7 | 6 | 19 | 96 |
| 東京 | 3 | 0 | 23 | 102 |
| 大阪 | 2 | 0 | 23 | 103 |
| 新規顧客受付 | 4 | 0 | 19 | 105 |
| サポートプラン | 1 | 0 | 19 | 108 |
| 事前契約 | 4 | 0 | 19 | 105 |
| 購入経路 | 1 | 0 | 19 | 108 |

## 第1段：優先6項目（現時点での根拠状況）

| 項目 | 提供段階 | 東京 / 大阪 | 新規顧客受付 | 公式根拠 |
|---|---|---|---|---|
| VPC Lattice | 確認済み | 確認済み / 確認済み | 未確認 | [AWS 1](https://aws.amazon.com/about-aws/whats-new/2023/03/general-availability-amazon-vpc-lattice/) / [AWS 2](https://aws.amazon.com/vpc/lattice/faqs/) / [AWS 3](https://aws.amazon.com/vpc/lattice/pricing/) |
| Firehose | 公式記載なし | 未確認 / 未確認 | 未確認 | [AWS 1](https://aws.amazon.com/about-aws/whats-new/2024/02/amazon-data-firehose-formerly-kinesis-data-firehose/) / [AWS 2](https://docs.aws.amazon.com/general/latest/gr/fh.html) / [AWS 3](https://aws.amazon.com/firehose/pricing/) |
| AWS Private CA | 公式記載なし | 未確認 / 未確認 | 未確認 | [AWS 1](https://docs.aws.amazon.com/privateca/latest/userguide/) / [AWS 2](https://docs.aws.amazon.com/privateca/latest/userguide/vpc-endpoints.html) / [AWS 3](https://aws.amazon.com/private-ca/pricing/) |
| Kinesis Data Streams | 公式記載なし | 未確認 / 未確認 | 未確認 | [AWS 1](https://docs.aws.amazon.com/general/latest/gr/ak.html) / [AWS 2](https://docs.aws.amazon.com/streams/latest/dev/vpc.html) / [AWS 3](https://aws.amazon.com/kinesis/data-streams/pricing/) |
| Amazon ML | 公式記載なし | 未確認 / 未確認 | 確認済み | [AWS 1](https://docs.aws.amazon.com/machine-learning/latest/dg/what-is-amazon-machine-learning.html) |
| Amazon SimpleDB | 公式記載なし | 未確認 / 未確認 | 未確認 | [AWS 1](https://aws.amazon.com/simpledb/faqs/) / [AWS 2](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/Endpoints.html) / [AWS 3](https://aws.amazon.com/simpledb/pricing/) |

## 実施上の制限と次段階

- SSMの読取専用OIDCロールは未接続。実際のSSMパラメータ取得結果が無い段階では、リージョンをSSMにより確定しません。
- 第2段＝独立サービス候補、第3段＝親子機能・専門API、第4段＝ツール・グローバル・終了済みの適用可否判定。
- 「対象外（ツール）」や「対象外（終了済み）」でもサポート・移行義務の調査が必要な場合があります。
- 金額・最低利用期間は転載せず [availability-evidence.json](availability-evidence.json) の公式料金URLを使用します。

**再確認期限切れ:** なし（判定済みの根拠のみを対象とした判定）
