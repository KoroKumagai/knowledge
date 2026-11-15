# AWS未対応項目：一次分類と提供条件の検証台帳

**基準日:** 2026-11-15 / [Products原票](products-source.json) / [General Reference](catalog.md) / [公式ライフサイクル](lifecycle.md)

> **33カード＋95参照項目の一次分類まで完了。すべてのGA・リージョン・契約条件を検証したわけではありません。**
> 一次分類は公式見出しや製品説明からの暫定判断です。独立課金サービス数・GA・契約可能性を確定しません。
> 東京（ap-northeast-1）と大阪（ap-northeast-3）を優先確認。未確認は不提供と同じ意味ではありません。
> APIエンドポイント掲載はGA・契約可能性を保証しません。ライフサイクルはサービス本体と個別機能を区別します。

**一覧:** Products 33カード（カードIDで区別）/ General Reference 95項目。 **公式根拠付き個別確認:** 15件（すべての列が確定したという意味ではありません）。

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
| サブ機能・専門API候補 | 50 |
| ツール・SDK・配布物 | 8 |
| ポータル・移行支援サービス | 2 |
| 共通管理・基盤API候補 | 12 |
| 提供終了の旧製品 | 10 |
| 業務アプリ・専門マネージドサービス候補 | 7 |
| 独立サービス・専門サービス候補 | 30 |
| 端末・アプライアンス | 3 |
| 終了予定・提供制限の製品 | 3 |

## Products側の未対応33カード

全33件を分類と公式ライフサイクルに絞って表示。終了済みの製品は後方にまとめています。
GA・リージョン・契約条件は下段の検証済み記録だけに示します。

| 公式Productsカード | 暫定分類 | 公式ライフサイクル | 出典 |
|---|---|---|---|
| Amazon Nova (ID: amazon-nova) | AIモデル・モデル構築/操作機能 | 本体の該当記載なし（GA未確認） | [AWS Products](https://aws.amazon.com/nova/?hp=fa&trk=c6553eb9-60f2-436a-b294-162bda8a1ebb) |
| Nova Act (ID: nova-act) | AIモデル・モデル構築/操作機能 | 本体の該当記載なし（GA未確認） | [AWS Products](https://aws.amazon.com/nova/act/) |
| Nova Forge (ID: nova-forge) | AIモデル・モデル構築/操作機能 | 本体の該当記載なし（GA未確認） | [AWS Products](https://aws.amazon.com/nova/forge/) |
| AWS App2Container (ID: aws-app2container) | ツール・SDK・配布物 | 本体の該当記載なし（GA未確認） | [AWS Products](https://aws.amazon.com/app2container/?did=ap_card&trk=ap_card) |
| AWS Command Line Interface (CLI) (ID: aws-command-line-interface) | ツール・SDK・配布物 | 本体の該当記載なし（GA未確認） | [AWS Products](https://aws.amazon.com/cli/?did=ap_card&trk=ap_card) |
| AWS Copilot (ID: aws-copilot) | ツール・SDK・配布物 | 本体の該当記載なし（GA未確認） | [AWS Products](https://aws.amazon.com/containers/copilot/?did=ap_card&trk=ap_card) |
| AWS Deep Learning Containers (ID: aws-deep-learning-containers) | ツール・SDK・配布物 | 本体の該当記載なし（GA未確認） | [AWS Products](https://aws.amazon.com/machine-learning/containers/?did=ap_card&trk=ap_card) |
| AWS Distro for OpenTelemetry (ID: aws-distro-open-telemetry) | ツール・SDK・配布物 | 本体の該当記載なし（GA未確認） | [AWS Products](https://aws.amazon.com/otel/?did=ap_card&trk=ap_card) |
| AWS Tools and SDKs (ID: aws-tools-and-sdks) | ツール・SDK・配布物 | 本体の該当記載なし（GA未確認） | [AWS Products](https://aws.amazon.com/getting-started/tools-sdks/?did=ap_card&trk=ap_card) |
| Amazon Corretto (ID: amazon-corretto) | ツール・SDK・配布物 | 本体の該当記載なし（GA未確認） | [AWS Products](https://aws.amazon.com/corretto/?did=ap_card&trk=ap_card) |
| Kiro (ID: aws-kiro) | ツール・SDK・配布物 | 本体の該当記載なし（GA未確認） | [AWS Products](https://kiro.dev/) |
| AWS Artifact (ID: aws-artifact) | ポータル・移行支援サービス | 本体の該当記載なし（GA未確認） | [AWS Products](https://aws.amazon.com/artifact/?did=ap_card&trk=ap_card) |
| Migration Evaluator (formerly TSO Logic) (ID: migration-evaluator-formerly-tso-logic) | ポータル・移行支援サービス | 本体の該当記載なし（GA未確認） | [AWS Products](https://aws.amazon.com/migration-evaluator/?did=ap_card&trk=ap_card) |
| AWS DevOps Agent (ID: aws-devops-agent-(preview)) | 業務アプリ・専門マネージドサービス候補 | 本体の該当記載なし（GA未確認） | [AWS Products](https://aws.amazon.com/devops-agent/) |
| AWS DevOps Agent (ID: aws-devops-agent-preview) | 業務アプリ・専門マネージドサービス候補 | 本体の該当記載なし（GA未確認） | [AWS Products](https://aws.amazon.com/devops-agent/) |
| AWS RTB Fabric (ID: aws-rtb-fabric) | 業務アプリ・専門マネージドサービス候補 | 本体の該当記載なし（GA未確認） | [AWS Products](https://aws.amazon.com/rtb-fabric/) |
| AWS Security Agent (ID: aws-security-agent-) | 業務アプリ・専門マネージドサービス候補 | 本体の該当記載なし（GA未確認） | [AWS Products](https://aws.amazon.com/security-agent/) |
| AWS Supply Chain (ID: aws-supply-chain) | 業務アプリ・専門マネージドサービス候補 | 本体の該当記載なし（GA未確認） | [AWS Products](https://aws.amazon.com/aws-supply-chain/?did=ap_card&trk=ap_card) |
| Amazon Connect Decisions (ID: amazon-connect-decisions) | 業務アプリ・専門マネージドサービス候補 | 本体の該当記載なし（GA未確認） | [AWS Products](https://aws.amazon.com/products/connect/decisions/) |
| Amazon Connect Talent (ID: amazon-connect-talent) | 業務アプリ・専門マネージドサービス候補 | 本体の該当記載なし（GA未確認） | [AWS Products](https://aws.amazon.com/products/connect/talent/) |
| AWS Elemental Appliances & Software (ID: aws-elemental-appliances-software) | 端末・アプライアンス | 本体の該当記載なし（GA未確認） | [AWS Products](https://aws.amazon.com/elemental-appliances-software/?did=ap_card&trk=ap_card) |
| AWS IoT Button (ID: aws-iot-button) | 端末・アプライアンス | [関連サービスが終了済み：AWS IoT 1-Click](lifecycle.md)（2025-01-29終了）。製品本体の提供状態とは区別 | [AWS Products](https://aws.amazon.com/iotbutton/?did=ap_card&trk=ap_card) |
| Amazon Dash Cart (ID: amazon-dash-cart) | 端末・アプライアンス | 本体の該当記載なし（GA未確認） | [AWS Products](https://aws.amazon.com/dash-cart/?did=ap_card&trk=ap_card) |
| AWS Service Management Connector (ID: aws-service-management-connector) | 終了予定・提供制限の製品 | [Sunset（終了予定）](lifecycle.md)（2027-03-31） | [AWS Products](https://aws.amazon.com/service-management-connector/?did=ap_card&trk=ap_card) |
| Amazon WorkSpaces Thin Client (ID: amazon-workspaces-thin-client) | 終了予定・提供制限の製品 | [Sunset（終了予定）](lifecycle.md)（2027-03-31） | [AWS Products](https://aws.amazon.com/workspaces/thin-client/?did=ap_card&trk=ap_card) |
| AWS DeepComposer (ID: aws-deepcomposer) | 提供終了の旧製品 | [Full Shutdown（終了済み）](lifecycle.md)（2025-09-17） | [AWS Products](https://aws.amazon.com/deepcomposer/?did=ap_card&trk=ap_card) |
| AWS DeepLens (ID: aws-deeplens) | 提供終了の旧製品 | [Full Shutdown（終了済み）](lifecycle.md)（2024-01-31） | [AWS Products](https://aws.amazon.com/deeplens/?did=ap_card&trk=ap_card) |
| AWS Elemental MediaStore (ID: aws-elemental-mediastore) | 提供終了の旧製品 | [Full Shutdown（終了済み）](lifecycle.md)（2025-11-12） | [AWS Products](https://aws.amazon.com/mediastore/?did=ap_card&trk=ap_card) |
| Amazon Elastic Transcoder (ID: amazon-elastic-transcoder) | 提供終了の旧製品 | [Full Shutdown（終了済み）](lifecycle.md)（2025-11-13） | [AWS Products](https://aws.amazon.com/elastictranscoder/?did=ap_card&trk=ap_card) |
| Amazon Lookout for Metrics (ID: amazon-lookout-for-metrics) | 提供終了の旧製品 | [Full Shutdown（終了済み）](lifecycle.md)（2025-10-10） | [AWS Products](https://aws.amazon.com/lookout-for-metrics/?did=ap_card&trk=ap_card) |
| Amazon Lookout for Vision (ID: amazon-lookout-for-vision) | 提供終了の旧製品 | [Full Shutdown（終了済み）](lifecycle.md)（2025-10-31） | [AWS Products](https://aws.amazon.com/lookout-for-vision/?did=ap_card&trk=ap_card) |
| Amazon Nimble Studio (ID: amazon-nimble-studio) | 提供終了の旧製品 | [Full Shutdown（終了済み）](lifecycle.md)（2024-06-30） | [AWS Products](https://aws.amazon.com/nimble-studio/?did=ap_card&trk=ap_card) |
| Amazon Quantum Ledger Database (QLDB) (ID: amazon-quantum-ledger-database-qldb) | 提供終了の旧製品 | [Full Shutdown（終了済み）](lifecycle.md)（2025-07-31） | [AWS Products](https://aws.amazon.com/qldb/?did=ap_card&trk=ap_card) |

## General Reference側の未対応95項目

全95件は元の公式参照へのリンクと暫定分類を掲載。Full Shutdownは末尾にまとめています。

| 公式General Reference | 暫定分類 | 公式ライフサイクル | 出典 |
|---|---|---|---|
| ARC | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/arc.html) |
| AWS AppConfig | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/appconfig.html) |
| AWS Clean Rooms ML | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/clean-rooms-ml.html) |
| AWS CodeStar Connections | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/codestar_connections.html) |
| AWS CodeStar Notifications | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/codestar_notifications.html) |
| AWS IoT Greengrass V2 | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/greengrassv2.html) |
| AWS Migration Hub Refactor Spaces | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/migrationhub-refactor-spaces.html) |
| AWS Signer | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/signer.html) |
| AWS Systems Manager for SAP | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/ssm-sap.html) |
| AWS User Experience Customization | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/uxc.html) |
| Amazon Comprehend Medical | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/comprehend-med_region.html) |
| Amazon Data Lifecycle Manager | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/dlm.html) |
| Amazon ECR Public | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/ecr-public.html) |
| Amazon MSK Connect | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/msk-connect.html) |
| Amazon WorkSpaces Instances | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/wsp-instances.html) |
| Application Auto Scaling | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/as-app.html) |
| CloudWatch Application Insights | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/applicationinsights.html) |
| CloudWatch Application Signals | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/cwApplicationSignals_region.html) |
| CloudWatch Events | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/cwe_region.html) |
| CloudWatch Internet Monitor | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/cwim_region.html) |
| CloudWatch Logs | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/cwl_region.html) |
| CloudWatch Network Synthetic Monitor | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/cwnm_region.html) |
| CloudWatch OAM | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/cloudwatchoam.html) |
| CloudWatch Observability Admin | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/cwobsadmin.html) |
| CloudWatch Omni | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/cwomni.html) |
| CloudWatch RUM | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/cw_rum_region.html) |
| CloudWatch Synthetics | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/cw-synthetics_region.html) |
| CodeGuru Profiler | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/codeguru-profiler.html) |
| CodeGuru Reviewer | サブ機能・専門API候補 | [Maintenance（新規利用制限あり）](https://docs.aws.amazon.com/general/latest/gr/maintenance_services.html) | [公式参照](https://docs.aws.amazon.com/general/latest/gr/codeguru-reviewer.html) |
| CodeGuru Security | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/codeguru-security.html) |
| DataBrew | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/gluedatabrew.html) |
| EC2 Image Builder | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/imagebuilder.html) |
| EC2 Instance Connect | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/ec2-instance-connect.html) |
| Elemental Inference | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/elemental-inference.html) |
| EventBridge Pipes | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/ev_pipes.html) |
| EventBridge Scheduler | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/eventbridgescheduler.html) |
| EventBridge Schemas | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/eventbridgeschemas.html) |
| Global Networks for Transit Gateways | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/network_manager.html) |
| IAM Access Analyzer | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/access-analyzer.html) |
| IAM Roles Anywhere | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/rolesanywhere.html) |
| Incident Manager | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/incident-manager.html) |
| Migration Hub Orchestrator | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/migrationhuborchestrator.html) |
| Migration Hub Strategy Recommendations | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/migrationhubstrategy.html) |
| Quick Setup | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/quick-setup.html) |
| Recycle Bin | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/rbin.html) |
| Resource Explorer | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/arex.html) |
| Resource Groups and Tagging | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/arg.html) |
| Security Hub CSPM | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/sechub.html) |
| Shield Advanced | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/shield.html) |
| Trusted Advisor API | サブ機能・専門API候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/trustedadvisor-pas.html) |
| AWS Billing Conductor | 共通管理・基盤API候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/billingconductor.html) |
| AWS CodeConnections | 共通管理・基盤API候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/codeconnections.html) |
| AWS Control Catalog | 共通管理・基盤API候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/controlcatalog.html) |
| AWS Marketplace | 共通管理・基盤API候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/aws-marketplace.html) |
| AWS STS | 共通管理・基盤API候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/sts.html) |
| AWS Sign-In | 共通管理・基盤API候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/signin-service.html) |
| Account access management | 共通管理・基盤API候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/account-access.html) |
| Billing and Cost Management | 共通管理・基盤API候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/billing.html) |
| Cloud Control API | 共通管理・基盤API候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/cloudcontrolapi.html) |
| CloudShell | 共通管理・基盤API候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/cloudshell.html) |
| Service Quotas | 共通管理・基盤API候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/servicequotas.html) |
| Support | 共通管理・基盤API候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/awssupport.html) |
| AWS Entity Resolution | 独立サービス・専門サービス候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/entity-resolution.html) |
| AWS IoT Wireless | 独立サービス・専門サービス候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/iot-lorawan.html) |
| AWS MCP Server | 独立サービス・専門サービス候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/aws-mcp.html) |
| AWS PCS | 独立サービス・専門サービス候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/pcs.html) |
| AWS Payment Cryptography | 独立サービス・専門サービス候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/payment-cryptography.html) |
| AWS Private CA | 独立サービス・専門サービス候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/pca.html) |
| AWS Security Incident Response | 独立サービス・専門サービス候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/securityir.html) |
| AWS TNB | 独立サービス・専門サービス候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/tnb.html) |
| AWS re:Post Private | 独立サービス・専門サービス候補 | [Sunset（終了予定）](https://docs.aws.amazon.com/general/latest/gr/sunset_services.html) | [公式参照](https://docs.aws.amazon.com/general/latest/gr/repostprivate.html) |
| Amazon AI Operations | 独立サービス・専門サービス候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/aiops_region.html) |
| Amazon Chime SDK | 独立サービス・専門サービス候補 | [機能単位の掲載あり（Maintenance（新規利用制限あり） / Full Shutdown（終了済））](lifecycle.md)（本体のGA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/chime-sdk.html) |
| Amazon EVS | 独立サービス・専門サービス候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/evs.html) |
| Amazon GameLift Streams | 独立サービス・専門サービス候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/gameliftstreams.html) |
| Amazon ML | 独立サービス・専門サービス候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/machinelearning.html) |
| Amazon Q Business | 独立サービス・専門サービス候補 | [Maintenance（新規利用制限あり）](https://docs.aws.amazon.com/general/latest/gr/maintenance_services.html) | [公式参照](https://docs.aws.amazon.com/general/latest/gr/amazonq.html) |
| Amazon Q Developer | 独立サービス・専門サービス候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/amazonqdev.html) |
| Amazon SWF | 独立サービス・専門サービス候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/swf-service.html) |
| Amazon SimpleDB | 独立サービス・専門サービス候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/sdb.html) |
| Amazon WorkSpaces | 独立サービス・専門サービス候補 | [機能単位の掲載あり（Maintenance（新規利用制限あり） / Sunset（終了日を確認））](lifecycle.md)（本体のGA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/wsp.html) |
| Amazon WorkSpaces Secure Browser | 独立サービス・専門サービス候補 | [Maintenance（新規利用制限あり）](https://docs.aws.amazon.com/general/latest/gr/maintenance_services.html) | [公式参照](https://docs.aws.amazon.com/general/latest/gr/workspacesweb.html) |
| Aurora DSQL | 独立サービス・専門サービス候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/dsql.html) |
| Cloud Directory | 独立サービス・専門サービス候補 | [Maintenance（新規利用制限あり）](https://docs.aws.amazon.com/general/latest/gr/maintenance_services.html) | [公式参照](https://docs.aws.amazon.com/general/latest/gr/clouddirectory.html) |
| DevOps Guru | 独立サービス・専門サービス候補 | [Sunset（終了予定）](https://docs.aws.amazon.com/general/latest/gr/sunset_services.html) | [公式参照](https://docs.aws.amazon.com/general/latest/gr/devops-guru.html) |
| Firehose | 独立サービス・専門サービス候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/fh.html) |
| HealthImaging | 独立サービス・専門サービス候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/healthimaging.html) |
| Kinesis Data Streams | 独立サービス・専門サービス候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/ak.html) |
| Managed Service for Apache Flink | 独立サービス・専門サービス候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/ka.html) |
| Network Security Manager | 独立サービス・専門サービス候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/network-security-manager.html) |
| Oracle Database@AWS | 独立サービス・専門サービス候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/odb-service.html) |
| VPC Lattice | 独立サービス・専門サービス候補 | 該当記載なし（GA判定不可） | [公式参照](https://docs.aws.amazon.com/general/latest/gr/vpc-lattice-service.html) |
| Amazon Glacier | 終了予定・提供制限の製品 | [Maintenance（新規利用制限あり）](https://docs.aws.amazon.com/general/latest/gr/maintenance_services.html) | [公式参照](https://docs.aws.amazon.com/general/latest/gr/s3glacier.html) |
| AWS IoT Greengrass V1 | 提供終了の旧製品 | [Full Shutdown（終了済）](https://docs.aws.amazon.com/general/latest/gr/full_shutdown_services.html) | [公式参照](https://docs.aws.amazon.com/general/latest/gr/greengrass.html) |
| AWS WAF Classic | 提供終了の旧製品 | [Full Shutdown（終了済）](https://docs.aws.amazon.com/general/latest/gr/full_shutdown_services.html) | [公式参照](https://docs.aws.amazon.com/general/latest/gr/waf-classic.html) |

## GA・リージョン・契約条件を個別確認した記録

ここに掲載するのは**根拠付きで個別確認した項目だけ**です。各列の「未確認」は不提供を意味しません。
Full Shutdownの製品について、リージョン別の新規利用可否は「対象外（終了済み）」と表示します。

| 公式名称 | GA・提供段階 | 東京 | 大阪 | 契約条件 | 根拠の適用範囲 | AWS一次資料 |
|---|---|---|---|---|---|---|
| Aurora DSQL | GA確認 | サービス利用可能（公式） | サービス利用可能（公式） | 従量課金・前払い費用なし（DPU／ストレージ） | 2025-05-27 GAを公式発表。東京・大阪の利用可能リージョンを公式User Guideで確認。料金は使用量課金で、各地域の最新単価・アカウント権限は別途確認。 | [AWS 1](https://aws.amazon.com/about-aws/whats-new/2025/05/amazon-aurora-dsql-generally-available/) / [AWS 2](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/) / [AWS 3](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/billing-metering.html) |
| Amazon Q Business | Maintenance（新規顧客受付停止） | 未確認 | 未確認 | 新規顧客受付停止。AWS公式文書間で開始日が2026-07-30／2026-07-31と異なるため、既存顧客以外の新規利用は停止済みとして扱い、厳密な停止日は要確認 | Q Business案内およびAPI文書は2026-07-31以降の新規受付停止（7/30より前に登録）を案内。一方2026-06-30のAWS What's Newは7/30開始と記載。両方を保持し一方の日時に確定しない。東京・大阪の既存顧客の利用状況は未検証。 | [AWS 1](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html) / [AWS 2](https://aws.amazon.com/about-aws/whats-new/2026/06/aws-service-availability/) |
| Service Quotas | 未確認 | APIエンドポイント掲載のみ | APIエンドポイント掲載のみ | 未確認 | 東京・大阪に公式APIエンドポイントが列挙されている。ただし単独でGAや全機能の提供／契約可否を証明しない。 | [AWS 1](https://docs.aws.amazon.com/general/latest/gr/servicequotas.html) |
| Support | 未確認 | 未確認 | 未確認 | AWS Support API利用にはBusiness Support+／Enterprise Support／Unified Operations等の対象サポートプランが必要（例外条件あり） | この条件はSupport APIの利用権限であり、AWS Support全般の契約要件とは同一視しない。 | [AWS 1](https://docs.aws.amazon.com/awssupport/latest/APIReference/Welcome.html) / [AWS 2](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_DescribeServices.html) |
| AWS WAF Classic | Full Shutdown（2026-10-07） | 対象外（終了済み） | 対象外（終了済み） | 新規導入不可（Full Shutdown） | AWS公式のFull Shutdown台帳に掲載。最新AWS WAFとは異なる旧製品。 | [AWS 1](https://docs.aws.amazon.com/general/latest/gr/full_shutdown_services.html) |
| AWS RTB Fabric | GA（2025-10-23確認） | サービス提供確認（2026-09-18公式発表） | 2026-09-18のAWS公式提供リージョン一覧に記載なし（最新状況要確認） | 事前コミットメント不要（AWS公式発表）。詳細契約・利用条件は個別確認 | 公式GA発表と2026-09-18時点の6リージョン一覧。東京は列挙。大阪は列挙なしだが、不提供と断定せず要再確認。 | [AWS 1](https://aws.amazon.com/about-aws/whats-new/2025/10/aws-rtb-fabric-generally-available/) / [AWS 2](https://aws.amazon.com/about-aws/whats-new/2026/09/aws-rtb-fabric-configurable-availability-zone-affinity/) |
| Nova Act | GA（2025-12-02公式発表） | 未確認（2025-12-02 GA発表時は米国東部のみ） | 未確認（2025-12-02 GA発表時は米国東部のみ） | 未確認 | GA時点で米国東部（バージニア北部）を提供。2026-11時点の東京・大阪や個別契約条件までは確定していない。 | [AWS 1](https://aws.amazon.com/about-aws/whats-new/2025/12/build-automate-production-ui-workflows-nova-act/) |
| Amazon WorkSpaces Thin Client | Sunset（2027-03-31終了予定） | 対象地域・販売国の確認が必要（物理端末） | 対象地域・販売国の確認が必要（物理端末） | 新規顧客受付停止。既存登録端末は終了日まで月額6米ドル/台（公式文書の開始日表記に差があるため要確認） | 公式文書に2026-03-31と2026-04-20の新規受付停止日に関する表記差あり。物理端末の販売地域をAWSリージョン対応と同一視しない。 | [AWS 1](https://docs.aws.amazon.com/workspaces-thin-client/latest/ug/workspacesthinclient-end-of-support.html) |
| Amazon Glacier | Maintenance（旧vault型の新規顧客受付停止） | 未確認（旧顧客向けの利用条件・地域を個別確認） | 未確認（旧顧客向けの利用条件・地域を個別確認） | Amazon Glacier旧vault APIは2025-12-15から新規顧客の受付を停止。既存顧客データはアクセス可能、S3 Glacierのストレージクラスは別の現行製品 | AWS公式Pricingが旧vault型Amazon Glacierの2025-12-15新規受付停止を明記。Product LifecycleはAmazon S3 Glacier DirectとしてMaintenance、AWS Storage Blogは旧Glacier Direct APIとの同一性を説明。S3 Glacier Flexible/Deep ArchiveなどのS3ストレージクラスをMaintenance扱いしない。 | [AWS 1](https://aws.amazon.com/s3/glacier/pricing/) / [AWS 2](https://docs.aws.amazon.com/amazonglacier/latest/dev/intro.html) / [AWS 3](https://docs.aws.amazon.com/general/latest/gr/maintenance_services.html) / [AWS 4](https://aws.amazon.com/blogs/storage/how-reuters-built-easily-accessible-large-scale-news-archives-on-aws/) |
| VPC Lattice | GA（2023-03-31 AWS公式発表） | 提供確認（公式FAQに明記） | 提供確認（公式FAQに明記） | 使用量に基づく課金。新規受付・別途契約・必要サポートプランは未確認 | 2023-03-31 GA発表。現在のAWS公式FAQは東京・大阪の両方を提供リージョンとして列挙。料金ページに利用量課金あり。新規受付・サポート・販売チャネルの制限を否定する根拠は未確認。 | [AWS 1](https://aws.amazon.com/about-aws/whats-new/2023/03/general-availability-amazon-vpc-lattice/) / [AWS 2](https://aws.amazon.com/vpc/lattice/faqs/) / [AWS 3](https://aws.amazon.com/vpc/lattice/pricing/) |
| Firehose | サービス運用を公式文書で確認（最新GA状態は未確認） | APIエンドポイント掲載のみ（サービス提供の全機能は未確認） | APIエンドポイント掲載のみ（サービス提供の全機能は未確認） | データ処理量ベースの課金、最低利用料・初期設定費なし（2024年公式発表）。新規受付・販売チャネル等は未確認 | Amazon Kinesis Data Firehose→Amazon Data Firehoseの改称を公式2024-02-09発表で確認。東京/大阪は公式General Reference APIエンドポイントに掲載（新規契約可否・各ソース連携の提供保証ではない）。 | [AWS 1](https://aws.amazon.com/about-aws/whats-new/2024/02/amazon-data-firehose-formerly-kinesis-data-firehose/) / [AWS 2](https://docs.aws.amazon.com/general/latest/gr/fh.html) / [AWS 3](https://aws.amazon.com/firehose/pricing/) |
| AWS Private CA | 地域型のマネージド認証局（GA発表日未確認） | 公式VPCエンドポイント対応地域（CAの提供確認は要追加調査） | 公式VPCエンドポイント対応地域（CAの提供確認は要追加調査） | CAの運用・証明書発行で課金。事前契約・新規顧客受付・販売経路は未確認 | 公式ユーザーガイドでCAはRegionリソースと記載、VPCエンドポイント提供地域に東京・大阪を確認。ただしPrivateLink利用可能＝サービス全機能提供とは扱わない。 | [AWS 1](https://docs.aws.amazon.com/privateca/latest/userguide/) / [AWS 2](https://docs.aws.amazon.com/privateca/latest/userguide/vpc-endpoints.html) / [AWS 3](https://aws.amazon.com/private-ca/pricing/) |
| Kinesis Data Streams | サービスドキュメント・課金体系確認（GA発表日未確認） | APIエンドポイント掲載・VPCエンドポイント機能対応（サービス全体は要追加確認） | APIエンドポイント掲載・VPCエンドポイント機能対応（サービス全体は要追加確認） | 従量/プロビジョンド等の課金モード。On-demand Advantageには最低利用容量の課金あり。事前契約が必要という意味ではない | 東京・大阪のAPIエンドポイントおよびVPC endpoint policyの対象リージョンをAWS公式文書で確認。GA/新規受付/コミットメントはAPIがあるだけでは判断しない。 | [AWS 1](https://docs.aws.amazon.com/general/latest/gr/ak.html) / [AWS 2](https://docs.aws.amazon.com/streams/latest/dev/vpc.html) / [AWS 3](https://aws.amazon.com/kinesis/data-streams/pricing/) |
| Amazon ML | 新規ユーザー受付停止（公式Developer Guide）／既存ユーザー向けDocs継続。Full Shutdownとは断定しない | 既存顧客の利用リージョンは未確認 | 既存顧客の利用リージョンは未確認 | 新規ユーザー受付停止（公式）。旧ユーザーの継続条件・サポートプランは未確認 | 公式ガイドに no longer updating / no longer accepting new users と明記。正式ライフサイクル3表未掲載をGAとみなさず、新規導入候補から除外。既存ユーザーへの利用停止やFull Shutdownは推定しない。 | [AWS 1](https://docs.aws.amazon.com/machine-learning/latest/dg/what-is-amazon-machine-learning.html) |
| Amazon SimpleDB | GA・現行の新規利用条件は未確認（古いFAQでは利用開始案内あり） | 旧FAQでは東京での利用を記載。2026-11の新規提供は未確認 | 確認したFAQに大阪の記載なし。未提供とは判断しない | 旧FAQではセットアップ料・事前コミットメント不要と記載。現行新規顧客受付は未確認 | AWS公式FAQは『AWSアカウントがあれば利用開始可能』と記すが更新日不明で2026年の新規顧客受付保証にはならない。終了・受付停止を示す明示的な公式告知は今回の確認範囲で見つかっていない。 | [AWS 1](https://aws.amazon.com/simpledb/faqs/) / [AWS 2](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/Endpoints.html) |

## 次の検証

1. 128項目の一次分類について、公式ドキュメントを基に製品本体・機能・旧名称を追加で確定する。
2. 東京・大阪を優先に、AWS Capabilities by Regionと個別サービス文書で地域可用性を検証する。
3. 新規顧客受付、料金モデル、契約条件、サポートプランを個別に確認する。
4. 終了済み・Maintenance製品を新規採用可能と誤認しないよう再確認する。

再生成：python scripts/render_aws_open_items.py --write / 検証：同 --check。
分類原本：[open-items-classification.json](open-items-classification.json)。
確認根拠：[availability-evidence.json](availability-evidence.json)。
