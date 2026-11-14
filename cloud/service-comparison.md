# 主要クラウドサービス機能比較（2026年11月版）

**対象:** AWS / Microsoft Azure / Google Cloud / Oracle Cloud Infrastructure (OCI) / Cloudflare  
**確認基準日:** 2026-11-14（JST）  
**目的:** 新規選定・移行検討のための**機能別比較**。特定ベンダーの名称体系に縛られず、2026年時点のサービスを整理する。

> [Google公式の旧比較表](https://docs.cloud.google.com/docs/get-started/aws-azure-gcp-service-comparison?hl=ja) は最終更新 **2024-12-03** のため、同表の転記ではなく、各ベンダーの現行製品ディレクトリ・廃止告知を基準に**独自に再編成**した。以下は実務での比較対象となる代表的サービス一覧であり、各社の全製品を網羅したカタログではない。全行についてGA・SKU・リージョン・販売条件まで検証したものではない。

## 対応表（97項目）

**表記:** `—`=同種の直接相当サービスなし（他サービスの組合せで実現できる場合あり）。`（構成）`=複数サービスを組合せて実装。`（部分）`/`（用途限定）`=目的が近いが非互換。Cloudflareはエッジ・開発プラットフォームであり、VM・VPC・ブロックストレージ・マネージドKubernetes・汎用DWHなどは原則比較対象外。

| 領域 | 機能 | AWS | Azure | Google Cloud | OCI | Cloudflare | 比較上の注意 |
|---|---|---|---|---|---|---|---|
| 計算 | 仮想マシン | EC2 | Virtual Machines | Compute Engine | Compute | — | Cloudflareは汎用VMを提供しない |
| 計算 | ベアメタル | EC2 Bare Metal | BareMetal Infrastructure（特殊用途） | Bare Metal Machine | Compute Bare Metal | — | 専用物理ホストとベアメタルは要件を区別 |
| 計算 | GPU計算 | EC2 GPU / EC2 Trn | GPU Virtual Machines | Compute Engine GPU / Cloud TPU | GPU Compute | Workers AI（推論限定） | GPUインスタンスとモデル推論APIは別 |
| 計算 | VM自動スケール | EC2 Auto Scaling | VM Scale Sets | Managed Instance Groups | Instance Pools / Autoscaling | — | — |
| 計算 | VM OS管理 | Systems Manager | Azure Update Manager | VM Manager | OS Management Hub | — | — |
| 計算 | VMへの非公開接続 | Systems Manager Session Manager | Azure Bastion | IAP TCP forwarding | Bastion | Cloudflare Access / Tunnel（別モデル） | 接続認証とネットワーク構成は異なる |
| 計算 | マネージドバッチ | AWS Batch | Azure Batch | Batch | Batch | Containers + Workflows（用途限定） | スケジューラ・実行時間が異なる |
| 計算 | VMware | Amazon EVS | Azure VMware Solution | Google Cloud VMware Engine | Oracle Cloud VMware Solution | — | — |
| コンテナ | Kubernetes | EKS | AKS | GKE | OKE | — | Cloudflare ContainersはKubernetesではない |
| コンテナ | オーケストレーション | ECS | Container Apps / AKS | Cloud Run / GKE | OKE / Container Instances | Containers（小規模・用途別） | オートスケールとサービス発見に差 |
| コンテナ | サーバーレスコンテナ | ECS Fargate / App Runner | Azure Container Apps | Cloud Run | Container Instances | Containers | 実行モデルは同一ではない |
| コンテナ | コンテナレジストリ | ECR | Azure Container Registry | Artifact Registry | OCIR | — | Cloudflare Containersのイメージ管理を別途確認 |
| コンテナ | サービス間通信 | ECS Service Connect / VPC Lattice | Container Apps / Service Mesh | Cloud Service Mesh | OKE Service Mesh（構成） | Workers service bindings | 旧AWS App Meshは終了 |
| サーバーレス | 関数実行 | Lambda | Azure Functions | Cloud Run functions | Functions | Workers | Workersはエッジ系ランタイム |
| サーバーレス | アプリPaaS | Elastic Beanstalk / App Runner | App Service | App Engine / Cloud Run | Compute + DevOps（構成） | Workers | 汎用PaaSの対応言語は異なる |
| サーバーレス | HTTPコンテナ実行 | App Runner / ECS Fargate | Container Apps | Cloud Run | Container Instances | Containers + Workers | 起動・スケール・制約が異なる |
| サーバーレス | 定期起動 | EventBridge Scheduler | Functions Timer Trigger / Container Apps Jobs | Cloud Scheduler | Resource Scheduler / Events + Functions | Cron Triggers | OCI Resource Schedulerはリソーススケジュールでありジョブcronとは異なる |
| サーバーレス | ワークフロー | Step Functions | Logic Apps / Durable Functions | Workflows | Process Automation | Workflows | ビジネスプロセスとコードワークフローは異なる |
| サーバーレス | イベント連携 | EventBridge | Event Grid | Eventarc | Events | Workers + Queues（構成） | Cloudflareには同型イベントバスなし |
| サーバーレス | ジョブキュー | SQS | Service Bus / Queue Storage | Cloud Tasks / Pub/Sub（異なる） | Queue | Queues | 配信保証と再試行を要比較 |
| サーバーレス | Pub/Sub | SNS / EventBridge | Service Bus Topics | Pub/Sub | Notifications / Streaming | Queues + Workers（構成） | 同等のトピックモデルとは限らない |
| サーバーレス | Kafka | MSK | Event Hubs Kafka endpoint | Managed Service for Apache Kafka | Streaming with Apache Kafka | — | Kafka互換性を確認 |
| サーバーレス | データストリーム | Kinesis | Event Hubs | Pub/Sub / Dataflow | Streaming | Queues（部分） | ストリームとキューは異なる |
| ネットワーク | プライベートネットワーク | VPC | Virtual Network | VPC | VCN | — | TunnelはVPCではない |
| ネットワーク | L4負荷分散 | Network Load Balancer | Azure Load Balancer | Cloud Load Balancing | Network Load Balancer | Spectrum（対応プロトコル限定） | — |
| ネットワーク | L7負荷分散 | Application Load Balancer | Application Gateway / Front Door | Cloud Load Balancing | Load Balancer | Load Balancing | — |
| ネットワーク | CDN | CloudFront | Front Door | Cloud CDN / Media CDN | Web Application Acceleration（用途による） | CDN | OCIは一般CDNとの機能差を確認 |
| ネットワーク | 権威DNS | Route 53 | Azure DNS | Cloud DNS | DNS | DNS | — |
| ネットワーク | 専用線 | Direct Connect | ExpressRoute | Cloud Interconnect | FastConnect | Cloudflare Network Interconnect | — |
| ネットワーク | サイト間VPN | Site-to-Site VPN | VPN Gateway | Cloud VPN | Site-to-Site VPN | Magic WAN / Cloudflare One | 実装や対象範囲が異なる |
| ネットワーク | NAT | NAT Gateway | NAT Gateway | Cloud NAT | NAT Gateway | — | — |
| ネットワーク | WAF | AWS WAF | Web Application Firewall | Cloud Armor | Web Application Firewall | WAF | AWS WAF Classicは終了 |
| ネットワーク | DDoS対策 | Shield | DDoS Protection | Cloud Armor | DDoS Protection | DDoS Protection | — |
| ネットワーク | ゼロトラストアプリ保護 | Verified Access | Entra Private Access | Identity-Aware Proxy | Identity Domains / Bastion（部分） | Cloudflare Access | IAPはCloudflare Accessと用途が近い |
| ネットワーク | 外向け接続トンネル | —（別構成） | —（別構成） | —（別構成） | —（別構成） | Cloudflare Tunnel | トンネルはVPNではない |
| ネットワーク | DNS・Webエッジ最適化 | Route 53 + CloudFront | Front Door | Cloud DNS + Cloud CDN | DNS + Web Application Acceleration | Argo Smart Routing / DNS | — |
| ネットワーク | ボット対策 | WAF Bot Control | Front Door WAF Bot Protection | Google Cloud Fraud Defense / Cloud Armor | WAF Bot Management | Bot Management / Turnstile | 旧reCAPTCHA Enterpriseの名称変更に注意 |
| ストレージ | オブジェクト | S3 | Blob Storage | Cloud Storage | Object Storage | R2 | R2はS3 API互換（非完全） |
| ストレージ | アーカイブ | S3 Glacier | Blob Archive | Cloud Storage Archive | Archive Storage | R2（アーカイブ階層同等なし） | 保存単価だけでなく復旧時間比較 |
| ストレージ | ブロック | EBS | Managed Disks | Hyperdisk / Persistent Disk | Block Volume | — | — |
| ストレージ | 共有ファイル | EFS / FSx | Azure Files / Azure NetApp Files | Filestore / NetApp Volumes | File Storage | — | — |
| ストレージ | 高性能並列ファイル | FSx for Lustre | Azure Managed Lustre | Managed Lustre | File Storage with Lustre | — | — |
| データベース | PostgreSQL | RDS PostgreSQL / Aurora | Database for PostgreSQL | Cloud SQL / AlloyDB | OCI Database with PostgreSQL | 外部DB + Hyperdrive | HyperdriveはDBサービスではない |
| データベース | MySQL | RDS MySQL / Aurora | Database for MySQL | Cloud SQL | MySQL HeatWave | 外部DB + Hyperdrive | — |
| データベース | SQL Server | RDS SQL Server | Azure SQL Database / SQL Managed Instance | Cloud SQL for SQL Server | Compute上のSQL Server等 | — | OCIはマネージド同等の提供形態を確認 |
| データベース | Oracle Database | RDS for Oracle / Oracle AI Database@AWS | Oracle AI Database@Azure | Oracle AI Database@Google Cloud | Base Database / Exadata / Autonomous AI Database | — | マルチクラウドDBはOracle製品として確認 |
| データベース | サーバーレスRDB | Aurora Serverless | Azure SQL Database serverless | Spanner / AlloyDB（異種モデル） | Autonomous AI Database | D1（SQLite） | SQL互換性は一律ではない |
| データベース | 分散SQL | Aurora DSQL | Cosmos DB for PostgreSQL（要提供確認） | Spanner / Spanner Omni | Globally Distributed Autonomous AI Database | D1（異なる） | トランザクション整合性・SQL仕様が大きく違う |
| データベース | ドキュメントNoSQL | DocumentDB | Cosmos DB | Firestore | Autonomous AI JSON Database | D1 / KV（部分） | Cloudflareには同型の汎用文書DBなし |
| データベース | Key-Value NoSQL | DynamoDB | Cosmos DB | Bigtable / Firestore | NoSQL Database | Workers KV | Workers KVは結果整合性 |
| データベース | 状態を持つアプリ実行 | DynamoDB + Lambda（構成） | Durable Functions（構成） | Firestore + Cloud Run（構成） | NoSQL + Functions（構成） | Durable Objects | Durable ObjectsはDB単体ではない |
| データベース | Redis系キャッシュ | ElastiCache / MemoryDB | Azure Managed Redis | Memorystore | OCI Cache | KV / Cache API（部分） | Azure Cache for Redisは廃止予定 |
| データベース | 全文検索 | OpenSearch Service | Azure AI Search | Vertex AI Search等 | OCI Search with OpenSearch | Workers + 外部検索（構成） | 検索エンジンとAI検索は異なる |
| データ分析 | データウェアハウス | Redshift | Fabric Data Warehouse / Synapse | BigQuery | Autonomous AI Database（分析用途） | — | — |
| データ分析 | SQLによるデータレイク検索 | Athena | Synapse serverless SQL / Fabric | BigQuery | Autonomous AI Database / Data Flow（構成） | R2 + 外部エンジン | — |
| データ分析 | ETL・ELT | Glue | Data Factory | Dataflow / Data Fusion / Dataform | Data Integration | Workers / Workflows（部分） | Cloudflareは大規模ETL基盤ではない |
| データ分析 | Spark | EMR | Azure Databricks | Managed Service for Apache Spark | Data Flow | — | — |
| データ分析 | Airflow | MWAA | Azure Managed Airflow（提供状況確認） | Managed Service for Apache Airflow | Data Integration（異なる） | — | ワークフロー連携とAirflowは違う |
| データ分析 | データカタログ | DataZone / Glue Data Catalog | Microsoft Purview | Knowledge Catalog | Data Catalog | — | Google旧Dataplex Universal Catalog等の呼称変更に注意 |
| データ分析 | BI | QuickSight | Power BI / Fabric | Looker / Data Studio | Analytics Cloud | Web Analytics（用途限定） | Web Analyticsは汎用BIではない |
| データ分析 | CDC | DMS | Data Factory（構成） | Datastream | GoldenGate | — | — |
| 開発 | CI/CD | CodeBuild / CodePipeline / CodeDeploy | Azure DevOps / GitHub Actions | Cloud Build / Cloud Deploy | DevOps | Workers Builds / GitHub Actions | — |
| 開発 | ソースコード管理 | CodeCommit（新規利用条件注意） | Azure Repos / GitHub | Secure Source Manager | DevOps Code Repositories | 外部Gitプロバイダー | — |
| 開発 | IaC | CloudFormation / CDK / Terraform | ARM / Bicep / Terraform | Infra Manager / Config Connector | Resource Manager（Terraform） | Terraform Provider / Wrangler | Cloudflare Wranglerは汎用Terraformの代わりではない |
| 開発 | CLI | AWS CLI | Azure CLI | gcloud CLI | OCI CLI | Wrangler / cf CLI（導入状況確認） | — |
| 開発 | API管理 | API Gateway | API Management | Apigee / API Gateway | API Gateway | API Shield + Workers（部分） | 完全なAPI管理機能は異なる |
| 開発 | 静的Webホスティング | Amplify Hosting / S3 + CloudFront | Static Web Apps | Firebase Hosting / Cloud Storage | Object Storage + Web Application Acceleration（構成） | Workers Static Assets / Pages | Pagesは引き続き存在 |
| 開発 | Webアプリホスティング | Amplify Hosting / App Runner | App Service / Static Web Apps | Firebase App Hosting / Cloud Run | Compute / OKE | Workers / Containers | Node.js・SSR互換性検証が必要 |
| 開発 | シークレット | Secrets Manager | Key Vault | Secret Manager | Vault / Secret Management Service | Workers Secrets / Secrets Store | 権限とローテーション要件を確認 |
| 開発 | 開発環境 | Cloud9（既存利用中心）/ CloudShell | Dev Box / Cloud Shell | Cloud Workstations / Cloud Shell | Cloud Shell | Workers Playground / ローカルWrangler | 製品の新規提供条件を確認 |
| 開発 | アーティファクト保管 | CodeArtifact / ECR | Azure Artifacts / ACR | Artifact Registry | Artifact Registry / OCIR | 外部レジストリ | — |
| セキュリティ | クラウドIAM | IAM / IAM Identity Center | Azure RBAC / Microsoft Entra ID | Cloud IAM / Cloud Identity | OCI IAM / Identity Domains | Cloudflare IAM / Access（別レイヤー） | Cloudflare AccessはクラウドIAMそのものではない |
| セキュリティ | 顧客向け認証 | Cognito | Entra External ID | Identity Platform | Identity Domains（要件次第） | Access（従業員・限定利用向け） | 一般消費者向けCIAMとは差がある |
| セキュリティ | 鍵管理 | KMS / CloudHSM | Key Vault / Managed HSM | Cloud KMS / Cloud HSM | Vault / Dedicated KMS | Keyless SSL / Secrets（部分） | — |
| セキュリティ | 監査 | CloudTrail | Activity Log | Cloud Audit Logs | Audit | Audit Logs | ログの対象と保持が異なる |
| セキュリティ | セキュリティ姿勢管理 | Security Hub / Config | Defender for Cloud / Azure Policy | Security Command Center | Cloud Guard / Security Zones | Security Center（エッジ中心） | — |
| セキュリティ | ネットワークファイアウォール | Network Firewall | Azure Firewall | Cloud NGFW | Network Firewall | Magic Firewall | 保護対象が異なる |
| セキュリティ | DLP | Macie | Microsoft Purview | Sensitive Data Protection | Data Safe（DB中心） | Data Loss Prevention（Zero Trust） | 対象範囲が違う |
| 運用 | ログ | CloudWatch Logs | Azure Monitor Logs | Cloud Logging | Logging / Log Analytics | Workers Logs / Logpush | — |
| 運用 | 監視 | CloudWatch | Azure Monitor | Cloud Monitoring | Monitoring | Workers Observability / Analytics | 対象範囲に差 |
| 運用 | 分散トレース | X-Ray / Application Signals | Application Insights | Cloud Trace | Application Performance Monitoring | Workers Traces | — |
| 運用 | 監査・資産発見 | AWS Config / Resource Explorer | Azure Resource Graph | Cloud Asset Inventory | Resource Search | Cloudflare API / Terraform State（部分） | — |
| 運用 | バックアップ | AWS Backup | Azure Backup | Backup and DR | Autonomous Recovery Service / Backup | D1 / R2の個別機能 | 包括的バックアップ製品と違う |
| 運用 | コスト管理 | Cost Explorer / Budgets | Cost Management | Cloud Billing / Recommender | Cost Management / FinOps Hub | Billing / Analytics | — |
| AI・ML | 基盤モデルAPI | Bedrock | Microsoft Foundry / Azure OpenAI | Gemini Enterprise Agent Platform / Gemini API | Generative AI | Workers AI | モデル・エンドポイント・規約差 |
| AI・ML | AIエージェント基盤 | Bedrock Agents / AgentCore | Microsoft Foundry Agent Service | Gemini Enterprise Agent Platform | Generative AI Agents | Agents SDK / Workers / Workflows | 実行権限・状態管理に差 |
| AI・ML | モデル学習・MLOps | SageMaker AI | Azure Machine Learning | Vertex AI（既存製品）/ Gemini Enterprise Agent Platform | Data Science | Workers AI（推論中心） | Cloudflareは汎用学習基盤ではない |
| AI・ML | ベクトル検索 | OpenSearch / Aurora pgvector | Azure AI Search / PostgreSQL pgvector | Vector Search / AlloyDB | AI Vector Search / Oracle AI Database | Vectorize | — |
| AI・ML | AIモデルゲートウェイ | API Gateway + Bedrock（構成） | API Management + Foundry（構成） | Apigee（構成） | API Gateway + Generative AI（構成） | AI Gateway | Cloudflare AI Gatewayは推論要求の監視・制御 |
| AI・ML | 開発者向けAI支援 | Amazon Q Developer（IDEプラグイン終了予定） | GitHub Copilot | Gemini Code Assist | OCI Code Assist（提供条件確認） | — | 導入形式とサポート終了を要確認 |
| エッジ | エッジ関数 | Lambda@Edge / CloudFront Functions | Front Door Rules（用途限定） | Cloud Run + CDN（構成） | Functions + Web Application Acceleration（構成） | Workers | — |
| エッジ | 画像最適化 | CloudFront + Lambda（構成） | Front Door + Functions（構成） | Cloud Run + CDN（構成） | Functions（構成） | Images / Image Transformations | — |
| エッジ | 動画配信 | MediaConvert / MediaPackage | Front Door + 外部配信構成 | Transcoder API / Media CDN | Media Services | Stream | 動画処理・DRMを比較 |
| エッジ | CAPTCHA・チャレンジ | WAF Challenge | Azure WAF（構成） | Google Cloud Fraud Defense | WAF（構成） | Turnstile | — |
| エッジ | メール転送 | SES inbound（構成） | Communication Services（送信中心） | 外部サービス（構成） | Email Delivery（送信中心） | Email Routing | 転送とメール送信は違う |
| エッジ | ブラウザ実行 | Lambda + Chromium（構成） | Container Apps + Browser（構成） | Cloud Run + Browser（構成） | Container Instances（構成） | Browser Rendering | — |
| エッジ | Web分析 | CloudWatch RUM | Application Insights | Google Analytics（別製品） | Analytics Cloud（異なる） | Web Analytics | 対象と指標が異なる |

## 2024年版からの代表的な変更・追加・廃止

| プロバイダー | 現行の比較で注意すべき変更 | 対応 |
|---|---|---|
| AWS | **AWS App Mesh** は 2026-09-30 にサポート終了。**AWS Proton** と **AWS WAF Classic** は 2026-10-07 にサポート終了。**Amazon Pinpoint** は 2026-10-30 にサポート終了。 | これらを新規構築の推奨先から除外。ECS Service Connect / AWS WAF 等を機能別に参照（Pinpointは用途別に別途移行設計）。 |
| AWS | **Amazon Q Developer IDE plugins** は 2027-04-30 サポート終了予定（2026-11時点）。**Amazon DevOps Guru** は 2027-09-29 サポート終了予定。 | 「現存」と「新規採用推奨」を明確に分ける。 |
| Azure | **Azure Cache for Redis** は廃止予定。Enterprise/Enterprise Flash: **2027-03-31**、Basic/Standard/Premium: **2028-09-30**。 | 新規比較は **Azure Managed Redis** を優先。 |
| Google Cloud | 現行製品一覧に **Gemini Enterprise Agent Platform**、**Knowledge Catalog**、**Managed Service for Apache Spark**、**Managed Lustre**、**Spanner Omni** などが掲載。 | 旧名称や旧製品表の行をそのまま踏襲しない。 |
| Google Cloud | **reCAPTCHA Enterprise** は **Google Cloud Fraud Defense** に改称（2026-07-16の変更履歴）。旧Datastoreの製品概要記載はFirestoreへ集約。 | 新しい名称を基本とし、元の用途が異なる場合は注意。 |
| OCI | 公式一覧に **OCI Batch**、**AI Data Platform**、**Generative AI Agents**、**Oracle AI Database@AWS / @Azure / @Google Cloud**、**Streaming with Apache Kafka** などを掲載。 | Oracle DB、マルチクラウド、GPU、データ統合の独自領域も評価。 |
| Cloudflare | **Containers / Workflows / Workers AI / AI Gateway / Vectorize / D1 / R2 / Queues / Durable Objects** などを含む現行の開発基盤を追加。 | 同等機能と部分的代替を区別。Cloudflare Containersは汎用Kubernetesではない。 |

### 誤対応を防ぐための留意点

1. **D1 ≠ Aurora / Cloud SQL / OCI PostgreSQL**: D1はSQLiteベース。RDB移行ではSQL仕様、書込み、接続、運用API、トランザクションを必ず再設計する。既存PostgreSQL接続にはHyperdrive等を検討。
2. **Workers ≠ VM / Lambda / ECSの完全互換**: エッジ実行特性、リクエスト境界、CPU時間、ネットワーク、Node互換性、ログ、バックグラウンド処理を確認。
3. **OCI Autonomous AI Database ≠ PostgreSQLやBigQueryと完全互換**: Oracle DBとしての特性がある。ライセンス、SQL移植、トランザクション、分析方式を評価。
4. **Cloudflare Access ≠ Cognito**: 社内・許可ユーザー向け認証ゲートと、一般消費者向けCIAMの要件は異なる。
5. **IaCの管理範囲は違う**: CloudFormation/CDK、ARM/Bicep、Infra Manager、OCI Resource Manager、Terraform Provider/Wranglerで対応リソースや状態管理を比較する。
6. **製品の掲載とGAは別**: 一次資料で地域、契約、価格、SLA、プレビュー区分、廃止予定を最終確認する。

## 一次資料

- [Google Cloud: 製品ディレクトリ](https://docs.cloud.google.com/docs/product-list)
- [Google Cloud: 製品一覧](https://cloud.google.com/products)
- [Google Cloud: 公式変更履歴](https://cloud.google.com/legal-change-log)
- [Google Cloud: 旧3社比較（2024-12-03更新）](https://docs.cloud.google.com/docs/get-started/aws-azure-gcp-service-comparison?hl=ja)
- [AWS: Services in Sunset（廃止・終了予定）](https://docs.aws.amazon.com/general/latest/gr/sunset_services.html)
- [AWS: 製品一覧](https://aws.amazon.com/products/)
- [Microsoft Azure: 製品一覧](https://azure.microsoft.com/en-us/products/)
- [Microsoft Learn: Azure Cache for Redis廃止FAQ](https://learn.microsoft.com/en-us/azure/azure-cache-for-redis/retirement-faq)
- [OCI: 全サービス公式ドキュメント](https://docs.oracle.com/en-us/iaas/Content/)
- [Cloudflare: 開発者向け製品](https://developers.cloudflare.com/)
- [Cloudflare: Containers更新履歴](https://developers.cloudflare.com/changelog/product/containers/)
- [Cloudflare: Workers更新履歴](https://developers.cloudflare.com/changelog/product/workers/)
- [Cloudflare: D1更新履歴](https://developers.cloudflare.com/changelog/product/d1/)

## メンテナンス方針

- 変更時は**基準日・追加/改称/終了/終了予定・公式根拠URL**をセットで更新。
- サービスを削除する場合、既存ユーザーに影響する場合は「終了済み」「終了予定」「新規受付停止」を区別して変更履歴に残す。
- 特定のクラウドへ移行する際はこの表のみで確定せず、**リージョン、価格、SLA、障害ドメイン、運用・監査、認可境界、IaC対応、API互換性**で比較する。
