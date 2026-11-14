# 主要クラウドサービス横断比較（2026年11月版）

**対象:** AWS / Azure / Google Cloud / OCI / Cloudflare  
**確認基準日:** 2026-11-14（JST）

> **比較の方針:** 2社以上で同じ用途として検討できるサービスのみを横断表へ掲載しています。完全互換という意味ではありません。比較不能なサービスや独自の製品体系は、各社ディレクトリで独立して整理しています。現行カタログの全件網羅はまだ未完了です。

- [AWS 個別サービス](aws/services.md)
- [Azure 個別サービス](azure/services.md)
- [Google Cloud 個別サービス](google/services.md)
- [Oracle Cloud 個別サービス](oracle/services.md)
- [Cloudflare 個別サービス](cloudflare/services.md)

## 比較可能な機能の横断表（48項目）

**選定基準:** 2社以上で同じ目的のサービスが提供され、構成方式の検討が可能な機能に限定します。直接該当しない場合は「対象外」と明示し、他社製品や組合せを無理に代入しません。「対象外」はその事業者が別方式で用途を実現できないという意味ではありません。**全5社で同等のサービスがあるという意味ではありません。** API・SLA・価格の完全互換はありません。

| 領域 | 機能 | AWS | Azure | Google Cloud | OCI | Cloudflare | 比較上の注意 |
|---|---|---|---|---|---|---|---|
| コンテナ | Kubernetes | EKS | AKS | GKE | OKE | 対象外 | Cloudflare ContainersはKubernetesではない |
| コンテナ | サーバーレスコンテナ | ECS on Fargate / App Runner | Azure Container Apps | Cloud Run | Container Instances | Containers | 実行制約・起動/スケール特性は異なる |
| サーバーレス | 関数実行 | Lambda | Azure Functions | Cloud Run functions | Functions | Workers | Workersの実行制限に注意 |
| メッセージング | 非同期メッセージ/ジョブキュー | Amazon SQS | Azure Service Bus Queue / Queue Storage | Cloud Tasks | OCI Queue | Cloudflare Queues | Cloud Tasksはタスク配送型。再試行・順序保証などの差に注意 |
| ワークフロー | ワークフローオーケストレーション | AWS Step Functions | Azure Logic Apps / Durable Functions | Google Cloud Workflows | OCI Process Automation | Cloudflare Workflows | 業務フロー・コード実行・永続化モデルで差がある |
| ネットワーク | L4ロードバランシング | Network Load Balancer | Azure Load Balancer | Cloud Load Balancing | Network Load Balancer | Spectrum | Spectrumはプロトコル対応範囲が異なる |
| ネットワーク | L7ロードバランシング | Application Load Balancer | Application Gateway / Front Door | Cloud Load Balancing | Load Balancer | Load Balancing | レイヤー・リバースプロキシ構成が異なる |
| ネットワーク | CDN | CloudFront | Front Door | Cloud CDN / Media CDN | 対象外 | CDN | OCIのWeb Application Accelerationは同種の汎用CDNではない |
| ネットワーク | 権威DNS | Route 53 | Azure DNS | Cloud DNS | DNS | DNS | 権威DNSが対象 |
| ネットワーク | 専用接続 | Direct Connect | ExpressRoute | Cloud Interconnect | FastConnect | Cloudflare Network Interconnect | 接続先・契約・構成が異なる |
| ネットワーク | WAF | AWS WAF | Azure Web Application Firewall | Cloud Armor | Web Application Firewall | WAF | AWS WAF Classicはサポート終了 |
| ネットワーク | DDoS対策 | AWS Shield | Azure DDoS Protection | Cloud Armor | OCI DDoS Protection | DDoS Protection | 保護対象・課金範囲を比較 |
| ネットワーク | Bot対策 | AWS WAF Bot Control | Front Door WAF Bot Protection | Cloud Armor / Google Cloud Fraud Defense | OCI WAF Bot Management | Bot Management | Cloudflare Turnstileは別途ボット判定フローを構成 |
| ストレージ | オブジェクトストレージ | S3 | Blob Storage | Cloud Storage | Object Storage | R2 | R2はS3 APIと完全互換ではない |
| ストレージ | アーカイブストレージ | S3 Glacier | Blob Archive | Cloud Storage Archive | Archive Storage | 対象外 | R2に同等の独立したアーカイブ階層なし |
| データベース | マネージドPostgreSQL | RDS PostgreSQL / Aurora PostgreSQL | Azure Database for PostgreSQL | Cloud SQL PostgreSQL / AlloyDB | OCI Database with PostgreSQL | 対象外 | Hyperdriveは外部DB接続製品 |
| データベース | マネージドMySQL | RDS MySQL / Aurora MySQL | Azure Database for MySQL | Cloud SQL MySQL | MySQL HeatWave | 対象外 | HyperdriveはDBではない |
| データベース | マネージドKey-Value / NoSQL | DynamoDB | Cosmos DB | Bigtable / Firestore | OCI NoSQL Database | Workers KV | Workers KVは結果整合性やクエリ機能が異なる |
| データベース | マネージドRedis系キャッシュ | Amazon ElastiCache | Azure Managed Redis | Memorystore | OCI Cache | 対象外 | Cloudflare KV / Cache APIはRedis互換ではない |
| 開発 | CI/CD | CodeBuild / CodePipeline | Azure Pipelines | Cloud Build / Cloud Deploy | OCI DevOps | Workers Builds | Workers BuildsはWorkers向け |
| 開発 | IaC | CloudFormation / CDK | ARM / Bicep | Infrastructure Manager | Resource Manager（Terraform） | Terraform Provider / Wrangler | Terraform利用可否と管理対象リソースを区別 |
| 開発 | CLI | AWS CLI | Azure CLI | gcloud CLI | OCI CLI | Wrangler | WranglerはCloudflareの開発・管理CLI |
| 開発 | シークレット管理 | Secrets Manager | Key Vault | Secret Manager | OCI Vault | Secrets Store / Workers Secrets | 自動更新・権限・管理粒度に差 |
| 開発 | 開発環境・クラウドシェル | AWS CloudShell | Azure Cloud Shell / Dev Box | Cloud Shell / Cloud Workstations | OCI Cloud Shell | 対象外 | Workers Playgroundは一般用途のCloud Shellではない |
| 開発 | ソースコード管理 | AWS CodeCommit | Azure Repos | Secure Source Manager | OCI DevOps Code Repositories | 対象外 | Gitリポジトリの管理機能・認可モデルに差 |
| 開発 | Webアプリホスティング | AWS Amplify Hosting / App Runner | Azure App Service | Firebase App Hosting / Cloud Run | 対象外 | Cloudflare Pages / Workers Static Assets | SSRの実行方式・デプロイ仕様は異なる |
| セキュリティ | クラウド設定・姿勢管理 | Security Hub / AWS Config | Defender for Cloud / Azure Policy | Security Command Center | Cloud Guard | 対象外 | Cloudflare Security Centerはエッジ中心 |
| セキュリティ | 顧客向け認証（CIAM） | Amazon Cognito | Microsoft Entra External ID | Identity Platform / Firebase Authentication | OCI Identity Domains | 対象外 | Cloudflare Accessは限定ユーザー/社内アプリ向け。一般消費者向けCIAMとは別 |
| 運用 | ログ | CloudWatch Logs | Azure Monitor Logs | Cloud Logging | OCI Logging | Workers Logs / Logpush | ログ対象と保持方式が異なる |
| 運用 | 分散トレース | AWS X-Ray | Application Insights | Cloud Trace | Application Performance Monitoring | Workers Traces | 対応トレース形式に差 |
| 運用 | バックアップ管理 | AWS Backup | Azure Backup | Backup and DR | Autonomous Recovery Service | 対象外 | D1 / R2個別機能は統合バックアップ製品ではない |
| 運用 | コスト管理 | Cost Explorer / Budgets | Cost Management | Cloud Billing / Recommender | Cost Management | Billing / Analytics | 機能・配賦単位が異なる |
| 運用 | カオスエンジニアリング | AWS Fault Injection Service | Azure Chaos Studio | 対象外 | 対象外 | 対象外 | AWSとAzureは同種の障害注入サービス |
| 運用 | 災害復旧レプリケーション | AWS Elastic Disaster Recovery | Azure Site Recovery | 対象外 | 対象外 | 対象外 | サーバー複製対象・復旧方式に違い |
| 運用 | マネージドGrafana | Amazon Managed Grafana | Azure Managed Grafana | 対象外 | 対象外 | 対象外 | 自己管理のGrafanaとは区別 |
| AI・ML | 基盤モデル推論API | Bedrock | Microsoft Foundry / Azure OpenAI | Gemini Enterprise Agent Platform / Gemini API | OCI Generative AI | Workers AI | 対応モデルとデプロイ方式が異なる |
| AI・ML | AIエージェント構築・運用 | Bedrock AgentCore | Microsoft Foundry Agent Service | Gemini Enterprise Agent Platform | OCI Generative AI Agents | Agents SDK / Workers | AgentCoreは従来のBedrock Agents Classicと別 |
| AI・ML | モデル学習・MLOps | SageMaker AI | Azure Machine Learning | Gemini Enterprise Agent Platform（旧Vertex AI） | OCI Data Science | 対象外 | Workers AIは汎用モデル学習基盤ではない |
| AI・ML | ベクトル検索 | OpenSearch / Aurora pgvector | Azure AI Search / PostgreSQL pgvector | Vector Search on Gemini Enterprise Agent Platform / AlloyDB | Oracle AI Database AI Vector Search | Vectorize | DB統合機能・単体サービスの差 |
| AI・ML | 音声認識 | Amazon Transcribe | Azure AI Speech | Speech-to-Text | OCI Speech | 対象外 | 言語・文字起こしの仕様は異なる |
| AI・ML | 音声合成 | Amazon Polly | Azure AI Speech | Text-to-Speech | OCI Speech | 対象外 | モデル/言語/合成品質に差 |
| AI・ML | 機械翻訳 | Amazon Translate | Azure AI Translator | Translation AI | OCI Language | 対象外 | OCR等との統合度は異なる |
| AI・ML | 文書理解 | Amazon Textract | Azure AI Document Intelligence | Document AI | OCI Document Understanding | 対象外 | 帳票・OCR・抽出モデルの提供範囲に差 |
| IoT・ゲーム | デジタルツイン | AWS IoT TwinMaker | Azure Digital Twins | 対象外 | 対象外 | 対象外 | 同種の用途でもデータモデルを要比較 |
| IoT・ゲーム | ゲームバックエンド | Amazon GameLift Servers | Azure PlayFab | 対象外 | 対象外 | 対象外 | サーバー運用とBaaSで機能範囲が違う |
| 位置情報 | 地図・位置情報API | Amazon Location Service | Azure Maps | Google Maps Platform | 対象外 | 対象外 | SDK・課金・地図データ範囲が異なる |
| メディア | マネージド動画配信・ストリーミング | Amazon IVS | 対象外 | 対象外 | 対象外 | Cloudflare Stream | ライブ/オンデマンドの対応範囲に差。Media CDNは配信CDNで別の比較軸 |
| 移行 | サーバー移行 | AWS Application Migration Service | Azure Migrate | Google Cloud Migrate to Virtual Machines | OCI Cloud Migrations | 対象外 | 支援対象と移行方式が異なる |

## サービスの廃止・改称・変更履歴

| プロバイダー | 現行の比較で注意すべき変更 | 対応 |
|---|---|---|
| AWS | **AWS App Mesh** は 2026-09-30 にサポート終了。**AWS Proton** と **AWS WAF Classic** は 2026-10-07 にサポート終了。**Amazon Pinpoint** は 2026-10-30 にサポート終了。 | これらを新規構築の推奨先から除外。ECS Service Connect / AWS WAF 等を機能別に参照（Pinpointは用途別に別途移行設計）。 |
| AWS | **Amazon Q Developer IDE plugins** は 2027-04-30 サポート終了予定（2026-11時点）。**Amazon DevOps Guru** は 2027-09-29 サポート終了予定。 | 「現存」と「新規採用推奨」を明確に分ける。 |
| AWS | **Amazon Bedrock Agents Classic**（旧Amazon Bedrock Agents）、**Amazon Kendra**、**Amazon Q Business** は2026-06-30にメンテナンス移行、2026-07-30以降新規顧客利用不可。 | AgentCoreを新規エージェント開発の中心として検討。Q BusinessについてはAmazon Quick Suiteを移行候補として検証。[AWS告知](https://aws.amazon.com/about-aws/whats-new/2026/06/aws-service-availability/) |
| AWS | **AWS CodeCommit** は2025-11-25から新規顧客に再提供。 | 旧「新規利用条件注意」を削除。[変更履歴](https://docs.aws.amazon.com/codecommit/latest/userguide/history.html) |
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
5. **IaCの管理範囲は違う**: CloudFormation/CDK、ARM/Bicep、Infrastructure Manager、OCI Resource Manager、Terraform Provider/Wranglerで対応リソースや状態管理を比較する。
6. **製品の掲載とGAは別**: 一次資料で地域、契約、価格、SLA、プレビュー区分、廃止予定を最終確認する。

## 一次資料

- [Google Cloud: 製品ディレクトリ](https://docs.cloud.google.com/docs/product-list)
- [Google Cloud: 製品一覧](https://cloud.google.com/products)
- [Google Cloud: 公式変更履歴](https://cloud.google.com/legal-change-log)
- [Google Cloud: 旧3社比較（2024-12-03更新）](https://docs.cloud.google.com/docs/get-started/aws-azure-gcp-service-comparison?hl=ja)
- [AWS: Services in Sunset（廃止・終了予定）](https://docs.aws.amazon.com/general/latest/gr/sunset_services.html)
- [AWS: 2026年サービス提供変更](https://aws.amazon.com/about-aws/whats-new/2026/06/aws-service-availability/)
- [AWS: CodeCommit変更履歴](https://docs.aws.amazon.com/codecommit/latest/userguide/history.html)
- [Google Cloud: Vertex AI製品の名称変更（Vector Search等）](https://docs.cloud.google.com/gemini-enterprise-agent-platform/vertex-ai-name-changes)
- [Cloudflare: Stream公式](https://developers.cloudflare.com/stream/)
- [Azure: Managed Redisへの移行](https://learn.microsoft.com/en-us/azure/azure-cache-for-redis/retirement-faq)
- [Google Cloud: Agent Platform後継説明](https://cloud.google.com/blog/products/ai-machine-learning/introducing-gemini-enterprise-agent-platform)
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
