# AWS：個別サービス一覧

> **対象:** 5社横断で同一機能として単純比較しにくいサービス・独自製品・独特の統合体系。これは独自性のある**候補一覧**であり、各社全製品の網羅・GAを保証するものではありません。

参照: [公式サービスディレクトリ](https://aws.amazon.com/products/)（2026-11-14時点の参照）

AWS固有の設計モデル、AWSが強みを持つ統合サービスや他社と1対1対応しないサービスを収録。

**区分の注意:** 比較表と重複する製品は原則として掲載せず、製品に固有の機能や利用上の制限を重点的に記載します。 このリストに載る製品でも、部分的な競合・他社での複合構成はあり得ます。製品の存否と採用可否は個別に確認してください。

## アカウント・統制

| サービス | 各社固有の設計上の特徴・用途 |
|---|---|
| AWS Organizations | 組織単位のアカウント統制 |
| AWS Control Tower | マルチアカウントの統制とランディングゾーン |
| AWS Service Catalog | 承認済み製品の提供 |
| AWS Resource Access Manager (RAM) | AWSリソースの共有 |
| AWS Config | 構成履歴とルール評価 |
| AWS Audit Manager | 監査証跡の収集 |
| AWS Artifact | コンプライアンス文書 |
| AWS Well-Architected Tool | 構成評価 |

## アーキテクチャ・可用性

| サービス | 各社固有の設計上の特徴・用途 |
|---|---|
| Amazon Route 53 Application Recovery Controller | マルチAZ・リージョンの復旧制御 |
| AWS Resilience Hub | 耐障害性評価 |
| AWS Elastic Disaster Recovery | 災害復旧 |

## アプリケーション・統合

| サービス | 各社固有の設計上の特徴・用途 |
|---|---|
| AWS AppSync | GraphQLなどのAPI |
| Amazon EventBridge Pipes | イベントソースとターゲットの接続 |
| Amazon Simple Email Service (SES) | メール送受信 |
| AWS End User Messaging | 顧客向けメッセージング |

## 専用分野

| サービス | 各社固有の設計上の特徴・用途 |
|---|---|
| Amazon Braket | 量子コンピューティング |
| AWS Ground Station | 衛星地上局 |
| AWS IoT Greengrass | IoTエッジランタイム |
| Amazon Connect | コンタクトセンター |
| AWS Deadline Cloud | レンダリングファーム |
| AWS HealthImaging | 医療画像 |
| AWS Clean Rooms | データクリーンルーム |
| Amazon Quick Suite | 業務データの分析とAI支援。Q Businessの移行候補（対応機能の検証が必要） |
| Amazon Nova | AWSのモデルファミリー |

## 横断比較へ移動した項目

- AWS Fault Injection Service
- AWS Application Migration Service (MGN)
- Amazon Bedrock AgentCore
- AWS Step Functions Distributed Map
- AWS IoT TwinMaker
- Amazon GameLift Servers

同目的のサービスは[横断比較](../service-comparison.md)に集約。単独製品ではなくサービス内の機能は一覧から除外しました。
