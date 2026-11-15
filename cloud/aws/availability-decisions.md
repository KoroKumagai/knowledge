# AWS未対応128項目：適用可否・根拠付き判定の進捗

**基準日:** 2026-11-15 / **再検証期限:** 180日超でWARN（CIは失敗させない）

判定値の定義とSSMの扱いは [availability-policy.md](availability-policy.md) を正とします。
公式根拠の全文と確認範囲は [availability-evidence.json](availability-evidence.json)、128件の個別判定・適用理由は [availability-decisions.json](availability-decisions.json)。

## 次元別判定（128行×7次元）

| 次元 | 確認済み | 公式記載なし | 対象外 | 未確認 |
|---|---:|---:|---:|---:|
| 提供段階 | 10 | 3 | 19 | 96 |
| 東京 | 6 | 0 | 23 | 99 |
| 大阪 | 5 | 0 | 23 | 100 |
| 新規顧客受付 | 4 | 0 | 19 | 105 |
| サポートプラン | 1 | 0 | 19 | 108 |
| 事前契約 | 4 | 0 | 19 | 105 |
| 購入経路 | 1 | 0 | 19 | 108 |

> 対象外の内訳：提供段階・契約系はツール8件＋終了済み11件＝19件。東京・大阪はそれに物理端末4件を加えた23件です。


## 第1段：優先6項目（現時点での根拠状況）

| 項目 | 提供段階 | 東京 / 大阪 | 新規顧客受付 | 公式根拠 |
|---|---|---|---|---|
| VPC Lattice | 確認済み | 確認済み / 確認済み | 未確認 | [AWS 1](https://aws.amazon.com/about-aws/whats-new/2023/03/general-availability-amazon-vpc-lattice/) / [AWS 2](https://aws.amazon.com/vpc/lattice/faqs/) / [AWS 3](https://aws.amazon.com/vpc/lattice/pricing/) |
| Firehose | 確認済み | 確認済み / 確認済み | 未確認 | [AWS 1](https://aws.amazon.com/legal/service-level-agreements/) / [AWS 2](https://aws.amazon.com/about-aws/whats-new/2015/10/introducing-amazon-kinesis-firehose/) / [AWS 3](https://aws.amazon.com/about-aws/whats-new/2024/02/amazon-data-firehose-formerly-kinesis-data-firehose/) / [AWS 4](https://docs.aws.amazon.com/firehose/latest/dev/limits.html) / [AWS 5](https://aws.amazon.com/firehose/pricing/) |
| AWS Private CA | 確認済み | 確認済み / 確認済み | 未確認 | [AWS 1](https://aws.amazon.com/legal/service-level-agreements/) / [AWS 2](https://aws.amazon.com/blogs/aws/aws-certificate-manager-launches-private-certificate-authority/) / [AWS 3](https://aws.amazon.com/about-aws/whats-new/2025/07/aws-private-ca-issuing-100-million-certificates-ca/) / [AWS 4](https://docs.aws.amazon.com/privateca/latest/userguide/) / [AWS 5](https://aws.amazon.com/private-ca/pricing/) |
| Kinesis Data Streams | 確認済み | 確認済み / 確認済み | 未確認 | [AWS 1](https://aws.amazon.com/legal/service-level-agreements/) / [AWS 2](https://aws.amazon.com/about-aws/whats-new/2015/10/amazon-kinesis-extended-data-retention/) / [AWS 3](https://aws.amazon.com/about-aws/whats-new/2026/09/kinesis/service-managed-partition-keys/) / [AWS 4](https://docs.aws.amazon.com/streams/latest/dev/large-records.html) / [AWS 5](https://aws.amazon.com/kinesis/data-streams/pricing/) |
| Amazon ML | 公式記載なし | 未確認 / 未確認 | 確認済み | [AWS 1](https://docs.aws.amazon.com/machine-learning/latest/dg/what-is-amazon-machine-learning.html) |
| Amazon SimpleDB | 公式記載なし | 未確認 / 未確認 | 未確認 | [AWS 1](https://aws.amazon.com/simpledb/faqs/) / [AWS 2](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/Endpoints.html) / [AWS 3](https://aws.amazon.com/simpledb/pricing/) |

## 実施上の制限と次段階

- SSMの読取専用OIDCロールは未接続。実際のSSMパラメータ取得結果が無い段階では、リージョンをSSMにより確定しません。
- 第2段＝独立サービス候補、第3段＝親子機能・専門API、第4段＝ツール・グローバル・終了済みの適用可否判定。
- 「対象外（ツール）」や「対象外（終了済み）」でもサポート・移行義務の調査が必要な場合があります。
- 金額・最低利用期間は転載せず [availability-evidence.json](availability-evidence.json) の公式料金URLを使用します。

**再確認期限切れ:** なし（判定済みの根拠のみを対象とした判定）
