# AWS：個別サービス一覧

> **対象:** 2社以上で比較できる共通機能とは区別して扱うサービス・独自製品・独特の統合体系。これは独自性のある**候補一覧**であり、各社全製品の網羅・GAを保証するものではありません。

参照: [公式サービスディレクトリ](https://aws.amazon.com/products/)（2026-11-14時点の参照）

[公式General Reference全件台帳](catalog.md)と[ライフサイクル](lifecycle.md)、[既存個別22件との照合](coverage.md)も参照。公式製品一覧の代替ではありません。

AWS固有の設計モデル、AWSが強みを持つ統合サービスや他社と1対1対応しないサービスを収録。

**区分の注意:** 比較表と重複する製品は原則として掲載しません。このリストに載る製品でも、部分的な競合・他社での複合構成はあり得ます。製品の存否と採用可否は個別に確認してください。

## アカウント・統制

| サービス | 用途 |
|---|---|
| AWS Organizations | 組織単位のアカウント統制 |
| AWS Control Tower | マルチアカウントの統制とランディングゾーン |
| AWS Service Catalog | 承認済み製品の提供 |
| AWS Resource Access Manager (RAM) | AWSリソースの共有 |
| AWS Audit Manager | 監査証跡の収集（公式Maintenance一覧に掲載。新規顧客には提供されない） |
| AWS Artifact | コンプライアンス文書 |
| AWS Well-Architected Tool | 構成評価 |

## アーキテクチャ・可用性

| サービス | 用途 |
|---|---|
| Amazon Route 53 Application Recovery Controller | マルチAZ・リージョンの復旧制御 |
| AWS Resilience Hub | 耐障害性評価 |

## アプリケーション・統合

| サービス | 用途 |
|---|---|
| AWS AppSync | GraphQLなどのAPI |
| Amazon EventBridge Pipes | イベントソースとターゲットの接続 |
| Amazon Simple Email Service (SES) | メール送受信 |
| AWS End User Messaging | 顧客向けメッセージング |

## 専用分野

| サービス | 用途 |
|---|---|
| Amazon Braket | 量子コンピューティング |
| AWS Ground Station | 衛星地上局 |
| AWS IoT Greengrass | IoTエッジランタイム |
| Amazon Connect | コンタクトセンター |
| AWS Deadline Cloud | レンダリングファーム |
| AWS HealthImaging | 医療画像 |
| AWS Clean Rooms | データクリーンルーム |
| AWS Quick | 業務データの分析とAI支援。旧Amazon Quick / Quick Suite。Q Businessからの移行は機能要件の確認が必要 |
| Amazon Nova | AWSのモデルファミリー |

## 横断比較へ移動した項目

- Amazon Bedrock AgentCore
- Amazon GameLift Servers
- AWS Application Migration Service (MGN)
- AWS Config
- AWS Elastic Disaster Recovery
- AWS Fault Injection Service
- AWS IoT TwinMaker

## 機能・旧名のため除外・統合した項目

- **AWS Step Functions Distributed Map** — Step Functionsの一機能であり独立サービスではない

[横断比較表](../service-comparison.md)の該当領域を参照してください。
