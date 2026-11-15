# AWS未対応項目：一次分類と提供条件の検証台帳

**基準日:** 2026-11-15 / [Products原票](products-source.json) / [General Reference](catalog.md) / [公式ライフサイクル](lifecycle.md)

> **33カード＋95参照項目の一次分類まで完了。すべてのGA・リージョン・契約条件を検証したわけではありません。**
> 一次分類は公式見出しや製品説明からの暫定判断です。独立課金サービス数・GA・契約可能性を確定しません。
> 東京（ap-northeast-1）と大阪（ap-northeast-3）を優先確認。未確認は不提供と同じ意味ではありません。
> APIエンドポイント掲載はGA・契約可能性を保証しません。ライフサイクルはサービス本体と個別機能を区別します。

**一覧:** Products 33カード（カードIDで区別）/ General Reference 95項目。 **公式根拠付き個別確認:** 5件（すべての列が確定したという意味ではありません）。

## 調査方法と今後のデータソース

- GA：公式GA発表またはライフサイクルの一次資料による。目録への掲載だけではGAとはしない。
- リージョン：公式の製品提供状況とAPIエンドポイントを分ける。APIがあることは新規契約可を意味しない。
- 契約条件：新規受付・販売方式・課金単位・サポートプランを個別に確認する。
- [AWS Capabilities by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/)を優先調査先とする。
- AWSが公開する[リージョンデータのS3アクセス方法](https://aws.amazon.com/blogs/storage/building-automated-aws-regional-availability-checks-with-amazon-s3/)はAWS認証・IAM権限を必要とする。無認証で全件取得できたとは主張しない。

## 暫定分類の内訳

| 暫定分類 | 件数 |
|---|---:|
| AIモデル・モデル構築/操作機能 | 3 |
| サブ機能・専門API候補 | 53 |
| ツール・SDK・配布物 | 8 |
| ポータル・移行支援サービス | 2 |
| 共通管理・基盤API候補 | 13 |
| 提供終了の旧製品 | 8 |
| 業務アプリ・専門マネージドサービス候補 | 7 |
| 独立サービス・専門サービス候補 | 29 |
| 端末・アプライアンス | 3 |
| 終了予定・提供制限の製品 | 2 |

## Products側の未対応33カード

| 公式Productsカード | 暫定分類 | 既存ライフサイクル | GA・提供状態 | 東京 | 大阪 | 契約条件 | 根拠 |
|---|---|---|---|---|---|---|---|
| Amazon Connect Decisions (ID: amazon-connect-decisions) | 業務アプリ・専門マネージドサービス候補 | 本体の該当記載なし（GA未確認） | 未確認 | 未確認 | 未確認 | 未確認 | [AWS Products](https://aws.amazon.com/products/connect/decisions/) |
| Amazon Connect Talent (ID: amazon-connect-talent) | 業務アプリ・専門マネージドサービス候補 | 本体の該当記載なし（GA未確認） | 未確認 | 未確認 | 未確認 | 未確認 | [AWS Products](https://aws.amazon.com/products/connect/talent/) |
| Amazon Corretto (ID: amazon-corretto) | ツール・SDK・配布物 | 本体の該当記載なし（GA未確認） | 未確認 | 未確認 | 未確認 | 未確認 | [AWS Products](https://aws.amazon.com/corretto/?did=ap_card&trk=ap_card) |
| Amazon Dash Cart (ID: amazon-dash-cart) | 端末・アプライアンス | 本体の該当記載なし（GA未確認） | 未確認 | 未確認 | 未確認 | 未確認 | [AWS Products](https://aws.amazon.com/dash-cart/?did=ap_card&trk=ap_card) |
| Amazon Elastic Transcoder (ID: amazon-elastic-transcoder) | 提供終了の旧製品 | [Full Shutdown（終了済み）](lifecycle.md)（2025-11-13） | Full Shutdown（公式台帳） | 未確認 | 未確認 | 未確認 | [AWS Products](https://aws.amazon.com/elastictranscoder/?did=ap_card&trk=ap_card) |
| Amazon Lookout for Metrics (ID: amazon-lookout-for-metrics) | 提供終了の旧製品 | [Full Shutdown（終了済み）](lifecycle.md)（2025-10-10） | Full Shutdown（公式台帳） | 未確認 | 未確認 | 未確認 | [AWS Products](https://aws.amazon.com/lookout-for-metrics/?did=ap_card&trk=ap_card) |
| Amazon Lookout for Vision (ID: amazon-lookout-for-vision) | 提供終了の旧製品 | [Full Shutdown（終了済み）](lifecycle.md)（2025-10-31） | Full Shutdown（公式台帳） | 未確認 | 未確認 | 未確認 | [AWS Products](https://aws.amazon.com/lookout-for-vision/?did=ap_card&trk=ap_card) |
| Amazon Nimble Studio (ID: amazon-nimble-studio) | 提供終了の旧製品 | [Full Shutdown（終了済み）](lifecycle.md)（2024-06-30） | Full Shutdown（公式台帳） | 未確認 | 未確認 | 未確認 | [AWS Products](https://aws.amazon.com/nimble-studio/?did=ap_card&trk=ap_card) |
| Amazon Nova (ID: amazon-nova) | AIモデル・モデル構築/操作機能 | 本体の該当記載なし（GA未確認） | 未確認 | 未確認 | 未確認 | 未確認 | [AWS Products](https://aws.amazon.com/nova/?hp=fa&trk=c6553eb9-60f2-436a-b294-162bda8a1ebb) |
| Amazon Quantum Ledger Database (QLDB) (ID: amazon-quantum-ledger-database-qldb) | 提供終了の旧製品 | [Full Shutdown（終了済み）](lifecycle.md)（2025-07-31） | Full Shutdown（公式台帳） | 未確認 | 未確認 | 未確認 | [AWS Products](https://aws.amazon.com/qldb/?did=ap_card&trk=ap_card) |
| Amazon WorkSpaces Thin Client (ID: amazon-workspaces-thin-client) | 終了予定・提供制限の製品 | [Sunset（終了予定）](lifecycle.md)（2027-03-31） | Sunset（公式台帳） | 未確認 | 未確認 | 未確認 | [AWS Products](https://aws.amazon.com/workspaces/thin-client/?did=ap_card&trk=ap_card) |
| AWS App2Container (ID: aws-app2container) | ツール・SDK・配布物 | 本体の該当記載なし（GA未確認） | 未確認 | 未確認 | 未確認 | 未確認 | [AWS Products](https://aws.amazon.com/app2container/?did=ap_card&trk=ap_card) |
| AWS Artifact (ID: aws-artifact) | ポータル・移行支援サービス | 本体の該当記載なし（GA未確認） | 未確認 | 未確認 | 未確認 | 未確認 | [AWS Products](https://aws.amazon.com/artifact/?did=ap_card&trk=ap_card) |
| AWS Command Line Interface (CLI) (ID: aws-command-line-interface) | ツール・SDK・配布物 | 本体の該当記載なし（GA未確認） | 未確認 | 未確認 | 未確認 | 未確認 | [AWS Products](https://aws.amazon.com/cli/?did=ap_card&trk=ap_card) |
| AWS Copilot (ID: aws-copilot) | ツール・SDK・配布物 | 本体の該当記載なし（GA未確認） | 未確認 | 未確認 | 未確認 | 未確認 | [AWS Products](https://aws.amazon.com/containers/copilot/?did=ap_card&trk=ap_card) |
| AWS Deep Learning Containers (ID: aws-deep-learning-containers) | ツール・SDK・配布物 | 本体の該当記載なし（GA未確認） | 未確認 | 未確認 | 未確認 | 未確認 | [AWS Products](https://aws.amazon.com/machine-learning/containers/?did=ap_card&trk=ap_card) |
| AWS DeepComposer (ID: aws-deepcomposer) | 提供終了の旧製品 | [Full Shutdown（終了済み）](lifecycle.md)（2025-09-17） | Full Shutdown（公式台帳） | 未確認 | 未確認 | 未確認 | [AWS Products](https://aws.amazon.com/deepcomposer/?did=ap_card&trk=ap_card) |
| AWS DeepLens (ID: aws-deeplens) | 提供終了の旧製品 | [Full Shutdown（終了済み）](lifecycle.md)（2024-01-31） | Full Shutdown（公式台帳） | 未確認 | 未確認 | 未確認 | [AWS Products](https://aws.amazon.com/deeplens/?did=ap_card&trk=ap_card) |
| AWS DevOps Agent (ID: aws-devops-agent-(preview)) | 業務アプリ・専門マネージドサービス候補 | 本体の該当記載なし（GA未確認） | 未確認 | 未確認 | 未確認 | 未確認 | [AWS Products](https://aws.amazon.com/devops-agent/) |
| AWS DevOps Agent (ID: aws-devops-agent-preview) | 業務アプリ・専門マネージドサービス候補 | 本体の該当記載なし（GA未確認） | 未確認 | 未確認 | 未確認 | 未確認 | [AWS Products](https://aws.amazon.com/devops-agent/) |
| AWS Distro for OpenTelemetry (ID: aws-distro-open-telemetry) | ツール・SDK・配布物 | 本体の該当記載なし（GA未確認） | 未確認 | 未確認 | 未確認 | 未確認 | [AWS Products](https://aws.amazon.com/otel/?did=ap_card&trk=ap_card) |
| AWS Elemental Appliances & Software (ID: aws-elemental-appliances-software) | 端末・アプライアンス | 本体の該当記載なし（GA未確認） | 未確認 | 未確認 | 未確認 | 未確認 | [AWS Products](https://aws.amazon.com/elemental-appliances-software/?did=ap_card&trk=ap_card) |
| AWS Elemental MediaStore (ID: aws-elemental-mediastore) | 提供終了の旧製品 | [Full Shutdown（終了済み）](lifecycle.md)（2025-11-12） | Full Shutdown（公式台帳） | 未確認 | 未確認 | 未確認 | [AWS Products](https://aws.amazon.com/mediastore/?did=ap_card&trk=ap_card) |
| AWS IoT Button (ID: aws-iot-button) | 端末・アプライアンス | [関連サービスが終了済み：AWS IoT 1-Click](lifecycle.md)（2025-01-29終了）。製品本体の提供状態とは区別 | 未確認 | 未確認 | 未確認 | 未確認 | [AWS Products](https://aws.amazon.com/iotbutton/?did=ap_card&trk=ap_card) |
| AWS RTB Fabric (ID: aws-rtb-fabric) | 業務アプリ・専門マネージドサービス候補 | 本体の該当記載なし（GA未確認） | 未確認 | 未確認 | 未確認 | 未確認 | [AWS Products](https://aws.amazon.com/rtb-fabric/) |
| AWS Security Agent (ID: aws-security-agent-) | 業務アプリ・専門マネージドサービス候補 | 本体の該当記載なし（GA未確認） | 未確認 | 未確認 | 未確認 | 未確認 | [AWS Products](https://aws.amazon.com/security-agent/) |
| AWS Service Management Connector (ID: aws-service-management-connector) | 終了予定・提供制限の製品 | [Sunset（終了予定）](lifecycle.md)（2027-03-31） | Sunset（公式台帳） | 未確認 | 未確認 | 未確認 | [AWS Products](https://aws.amazon.com/service-management-connector/?did=ap_card&trk=ap_card) |
| AWS Supply Chain (ID: aws-supply-chain) | 業務アプリ・専門マネージドサービス候補 | 本体の該当記載なし（GA未確認） | 未確認 | 未確認 | 未確認 | 未確認 | [AWS Products](https://aws.amazon.com/aws-supply-chain/?did=ap_card&trk=ap_card) |
| AWS Tools and SDKs (ID: aws-tools-and-sdks) | ツール・SDK・配布物 | 本体の該当記載なし（GA未確認） | 未確認 | 未確認 | 未確認 | 未確認 | [AWS Products](https://aws.amazon.com/getting-started/tools-sdks/?did=ap_card&trk=ap_card) |
| Kiro (ID: aws-kiro) | ツール・SDK・配布物 | 本体の該当記載なし（GA未確認） | 未確認 | 未確認 | 未確認 | 未確認 | [AWS Products](https://kiro.dev/) |
| Migration Evaluator (formerly TSO Logic) (ID: migration-evaluator-formerly-tso-logic) | ポータル・移行支援サービス | 本体の該当記載なし（GA未確認） | 未確認 | 未確認 | 未確認 | 未確認 | [AWS Products](https://aws.amazon.com/migration-evaluator/?did=ap_card&trk=ap_card) |
| Nova Act (ID: nova-act) | AIモデル・モデル構築/操作機能 | 本体の該当記載なし（GA未確認） | 未確認 | 未確認 | 未確認 | 未確認 | [AWS Products](https://aws.amazon.com/nova/act/) |
| Nova Forge (ID: nova-forge) | AIモデル・モデル構築/操作機能 | 本体の該当記載なし（GA未確認） | 未確認 | 未確認 | 未確認 | 未確認 | [AWS Products](https://aws.amazon.com/nova/forge/) |

## General Reference側の未対応95項目

| 公式General Reference | 暫定分類 | ライフサイクルの掲載 | GA・提供状態 | 東京 | 大阪 | 契約条件 | 根拠 |
|---|---|---|---|---|---|---|---|
| Account access management | 共通管理・基盤API候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/account-access.html) |
| Amazon AI Operations | 独立サービス・専門サービス候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/aiops_region.html) |
| AWS AppConfig | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/appconfig.html) |
| ARC | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/arc.html) |
| Application Auto Scaling | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/as-app.html) |
| Aurora DSQL | 独立サービス・専門サービス候補 | 該当記載なし（GA判定不可） | GA確認 | サービス利用可能（公式） | サービス利用可能（公式） | 従量課金・前払い費用なし（DPU／ストレージ） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/dsql.html) [根拠1](https://aws.amazon.com/about-aws/whats-new/2025/05/amazon-aurora-dsql-generally-available/) / [根拠2](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/) / [根拠3](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/billing-metering.html) |
| AWS MCP Server | 独立サービス・専門サービス候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/aws-mcp.html) |
| Billing and Cost Management | 共通管理・基盤API候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/billing.html) |
| AWS Billing Conductor | 共通管理・基盤API候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/billingconductor.html) |
| Amazon Chime SDK | 独立サービス・専門サービス候補 | [機能単位の掲載あり（Maintenance（新規利用制限あり） / Full Shutdown（終了済））](lifecycle.md)（本体のGA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/chime-sdk.html) |
| AWS Clean Rooms ML | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/clean-rooms-ml.html) |
| Cloud Control API | 共通管理・基盤API候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/cloudcontrolapi.html) |
| Cloud Directory | 独立サービス・専門サービス候補 | [Maintenance（新規利用制限あり）](https://docs.aws.amazon.com/general/latest/gr/maintenance_services.html) | Maintenance（公式台帳） | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/clouddirectory.html) |
| CloudShell | 共通管理・基盤API候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/cloudshell.html) |
| AWS Control Catalog | 共通管理・基盤API候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/controlcatalog.html) |
| CloudWatch Application Insights | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/applicationinsights.html) |
| CloudWatch Application Signals | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/cwApplicationSignals_region.html) |
| CloudWatch Events | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/cwe_region.html) |
| CloudWatch Internet Monitor | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/cwim_region.html) |
| CloudWatch Logs | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/cwl_region.html) |
| CloudWatch Network Synthetic Monitor | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/cwnm_region.html) |
| CloudWatch OAM | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/cloudwatchoam.html) |
| CloudWatch Observability Admin | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/cwobsadmin.html) |
| CloudWatch Omni | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/cwomni.html) |
| CloudWatch RUM | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/cw_rum_region.html) |
| CloudWatch Synthetics | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/cw-synthetics_region.html) |
| AWS CodeConnections | 共通管理・基盤API候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/codeconnections.html) |
| CodeGuru Profiler | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/codeguru-profiler.html) |
| CodeGuru Reviewer | サブ機能・専門API候補 | [Maintenance（新規利用制限あり）](https://docs.aws.amazon.com/general/latest/gr/maintenance_services.html) | Maintenance（公式台帳） | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/codeguru-reviewer.html) |
| CodeGuru Security | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/codeguru-security.html) |
| AWS CodeStar Connections | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/codestar_connections.html) |
| AWS CodeStar Notifications | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/codestar_notifications.html) |
| Amazon Comprehend Medical | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/comprehend-med_region.html) |
| Amazon Data Lifecycle Manager | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/dlm.html) |
| DevOps Guru | 独立サービス・専門サービス候補 | [Sunset（終了予定）](https://docs.aws.amazon.com/general/latest/gr/sunset_services.html) | Sunset（公式台帳） | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/devops-guru.html) |
| EC2 Image Builder | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/imagebuilder.html) |
| EC2 Instance Connect | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/ec2-instance-connect.html) |
| Amazon ECR Public | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/ecr-public.html) |
| Elemental Inference | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/elemental-inference.html) |
| AWS Entity Resolution | 独立サービス・専門サービス候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/entity-resolution.html) |
| EventBridge Pipes | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/ev_pipes.html) |
| EventBridge Scheduler | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/eventbridgescheduler.html) |
| EventBridge Schemas | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/eventbridgeschemas.html) |
| Amazon EVS | 独立サービス・専門サービス候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/evs.html) |
| Firehose | 独立サービス・専門サービス候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/fh.html) |
| Amazon GameLift Streams | 独立サービス・専門サービス候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/gameliftstreams.html) |
| Global Networks for Transit Gateways | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/network_manager.html) |
| DataBrew | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/gluedatabrew.html) |
| HealthImaging | 独立サービス・専門サービス候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/healthimaging.html) |
| IAM Access Analyzer | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/access-analyzer.html) |
| IAM Roles Anywhere | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/rolesanywhere.html) |
| Incident Manager | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/incident-manager.html) |
| AWS IoT Wireless | 独立サービス・専門サービス候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/iot-lorawan.html) |
| AWS IoT Greengrass V1 | サブ機能・専門API候補 | [Full Shutdown（終了済）](https://docs.aws.amazon.com/general/latest/gr/full_shutdown_services.html) | Full Shutdown（公式台帳） | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/greengrass.html) |
| AWS IoT Greengrass V2 | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/greengrassv2.html) |
| Kinesis Data Streams | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/ak.html) |
| Amazon ML | 独立サービス・専門サービス候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/machinelearning.html) |
| Managed Service for Apache Flink | 独立サービス・専門サービス候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/ka.html) |
| AWS Marketplace | 共通管理・基盤API候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/aws-marketplace.html) |
| Amazon MSK Connect | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/msk-connect.html) |
| Migration Hub Orchestrator | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/migrationhuborchestrator.html) |
| AWS Migration Hub Refactor Spaces | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/migrationhub-refactor-spaces.html) |
| Migration Hub Strategy Recommendations | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/migrationhubstrategy.html) |
| Network Security Manager | 独立サービス・専門サービス候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/network-security-manager.html) |
| Oracle Database@AWS | 独立サービス・専門サービス候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/odb-service.html) |
| AWS Payment Cryptography | 独立サービス・専門サービス候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/payment-cryptography.html) |
| AWS PCS | 独立サービス・専門サービス候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/pcs.html) |
| AWS Private CA | 独立サービス・専門サービス候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/pca.html) |
| Amazon Q Business | 独立サービス・専門サービス候補 | [Maintenance（新規利用制限あり）](https://docs.aws.amazon.com/general/latest/gr/maintenance_services.html) | Maintenance（新規顧客受付停止） | 未確認 | 未確認 | 新規顧客利用不可（2026-07-31から）。既存顧客へのサポート継続 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/amazonq.html) [根拠1](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html) / [根拠2](https://aws.amazon.com/about-aws/whats-new/2026/06/aws-service-availability/) |
| Amazon Q Developer | 独立サービス・専門サービス候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/amazonqdev.html) |
| Quick Setup | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/quick-setup.html) |
| Recycle Bin | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/rbin.html) |
| AWS re:Post Private | 独立サービス・専門サービス候補 | [Sunset（終了予定）](https://docs.aws.amazon.com/general/latest/gr/sunset_services.html) | Sunset（公式台帳） | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/repostprivate.html) |
| Resource Explorer | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/arex.html) |
| Resource Groups and Tagging | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/arg.html) |
| Security Hub CSPM | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/sechub.html) |
| AWS Security Incident Response | 独立サービス・専門サービス候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/securityir.html) |
| Service Quotas | 共通管理・基盤API候補 | 該当記載なし（GA判定不可） | 未確認 | APIエンドポイント掲載のみ | APIエンドポイント掲載のみ | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/servicequotas.html) [根拠1](https://docs.aws.amazon.com/general/latest/gr/servicequotas.html) |
| Shield Advanced | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/shield.html) |
| Amazon Glacier | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/s3glacier.html) |
| AWS Signer | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/signer.html) |
| AWS Sign-In | 共通管理・基盤API候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/signin-service.html) |
| Amazon SimpleDB | 独立サービス・専門サービス候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/sdb.html) |
| AWS STS | 共通管理・基盤API候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/sts.html) |
| Amazon SWF | 独立サービス・専門サービス候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/swf-service.html) |
| Support | 共通管理・基盤API候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | AWS Support API利用にはBusiness Support+／Enterprise Support／Unified Operations等の対象サポートプランが必要（例外条件あり） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/awssupport.html) [根拠1](https://docs.aws.amazon.com/awssupport/latest/APIReference/Welcome.html) / [根拠2](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_DescribeServices.html) |
| AWS Systems Manager for SAP | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/ssm-sap.html) |
| AWS TNB | 独立サービス・専門サービス候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/tnb.html) |
| Trusted Advisor API | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/trustedadvisor-pas.html) |
| AWS User Experience Customization | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/uxc.html) |
| VPC Lattice | 独立サービス・専門サービス候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/vpc-lattice-service.html) |
| AWS WAF Classic | 共通管理・基盤API候補 | [Full Shutdown（終了済）](https://docs.aws.amazon.com/general/latest/gr/full_shutdown_services.html) | Full Shutdown（2026-10-07） | 終了済み・リージョン判定対象外 | 終了済み・リージョン判定対象外 | 新規導入不可（Full Shutdown） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/waf-classic.html) [根拠1](https://docs.aws.amazon.com/general/latest/gr/full_shutdown_services.html) |
| Amazon WorkSpaces | 独立サービス・専門サービス候補 | [機能単位の掲載あり（Maintenance（新規利用制限あり） / Sunset（終了日を確認））](lifecycle.md)（本体のGA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/wsp.html) |
| Amazon WorkSpaces Instances | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | 未確認 | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/wsp-instances.html) |
| Amazon WorkSpaces Secure Browser | 独立サービス・専門サービス候補 | [Maintenance（新規利用制限あり）](https://docs.aws.amazon.com/general/latest/gr/maintenance_services.html) | Maintenance（公式台帳） | 未確認 | 未確認 | 未確認 | [公式参照](https://docs.aws.amazon.com/general/latest/gr/workspacesweb.html) |

## 個別の公式確認例

| 名称 | 確認範囲・留意点 | 公式出典 |
|---|---|---|
| Aurora DSQL | 2025-05-27 GAを公式発表。東京・大阪の利用可能リージョンを公式User Guideで確認。料金は使用量課金で、各地域の最新単価・アカウント権限は別途確認。 | [AWS 1](https://aws.amazon.com/about-aws/whats-new/2025/05/amazon-aurora-dsql-generally-available/) / [AWS 2](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/) / [AWS 3](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/billing-metering.html) |
| Amazon Q Business | 同一サービスの地域別既存顧客利用状況は未検証。Quickへの移行ガイダンスあり。 | [AWS 1](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html) / [AWS 2](https://aws.amazon.com/about-aws/whats-new/2026/06/aws-service-availability/) |
| Service Quotas | 東京・大阪に公式APIエンドポイントが列挙されている。ただし単独でGAや全機能の提供／契約可否を証明しない。 | [AWS 1](https://docs.aws.amazon.com/general/latest/gr/servicequotas.html) |
| Support | この条件はSupport APIの利用権限であり、AWS Support全般の契約要件とは同一視しない。 | [AWS 1](https://docs.aws.amazon.com/awssupport/latest/APIReference/Welcome.html) / [AWS 2](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_DescribeServices.html) |
| AWS WAF Classic | AWS公式のFull Shutdown台帳に掲載。最新AWS WAFとは異なる旧製品。 | [AWS 1](https://docs.aws.amazon.com/general/latest/gr/full_shutdown_services.html) |

## 次の検証

1. 128項目の一次分類について、公式ドキュメントを基に製品本体・機能・旧名称を追加で確定する。
2. 東京・大阪を優先に、AWS Capabilities by Regionと個別サービス文書で地域可用性を検証する。
3. 新規顧客受付、料金モデル、契約条件、サポートプランを個別に確認する。
4. 終了済み・Maintenance製品を新規採用可能と誤認しないよう再確認する。

再生成：python scripts/render_aws_open_items.py --write / 検証：同 --check。
分類原本：[open-items-classification.json](open-items-classification.json)。
確認根拠：[availability-evidence.json](availability-evidence.json)。
