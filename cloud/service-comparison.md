# 主要クラウドサービス横断比較（2026年11月版）

**対象:** AWS / Azure / Google Cloud / OCI / Cloudflare  
**確認基準日:** 2026-11-14（JST）

> **比較の方針:** 5社でほぼ同じ役割として検討できるサービスのみを横断表へ掲載しています。完全互換という意味ではありません。各社独自・部分的類似・複数サービス構成のサービスは、各社ディレクトリで独立して整理しています。現行カタログの全件網羅はまだ未完了です。

- [AWS 個別サービス](aws/services.md)
- [Azure 個別サービス](azure/services.md)
- [Google Cloud 個別サービス](google/services.md)
- [Oracle Cloud 個別サービス](oracle/services.md)
- [Cloudflare 個別サービス](cloudflare/services.md)

## 5社の機能横断表（39項目）

比較可能とは機能の検討軸が共通であることを意味し、API・動作・SLA・価格・リージョン・IAMモデルが同一であることを保証しません。

| 領域 | 機能 | AWS | Azure | Google Cloud | OCI | Cloudflare | 比較上の注意 |
|---|---|---|---|---|---|---|---|
| コンテナ | オーケストレーション | ECS | Container Apps / AKS | Cloud Run / GKE | OKE / Container Instances | Containers（小規模・用途別） | オートスケールとサービス発見に差 |
| コンテナ | サーバーレスコンテナ | ECS Fargate / App Runner | Azure Container Apps | Cloud Run | Container Instances | Containers | 実行モデルは同一ではない |
| サーバーレス | 関数実行 | Lambda | Azure Functions | Cloud Run functions | Functions | Workers | Workersはエッジ系ランタイム |
| ネットワーク | L4負荷分散 | Network Load Balancer | Azure Load Balancer | Cloud Load Balancing | Network Load Balancer | Spectrum（対応プロトコル限定） | — |
| ネットワーク | L7負荷分散 | Application Load Balancer | Application Gateway / Front Door | Cloud Load Balancing | Load Balancer | Load Balancing | — |
| ネットワーク | CDN | CloudFront | Front Door | Cloud CDN / Media CDN | Web Application Acceleration（用途による） | CDN | OCIは一般CDNとの機能差を確認 |
| ネットワーク | 権威DNS | Route 53 | Azure DNS | Cloud DNS | DNS | DNS | — |
| ネットワーク | 専用線 | Direct Connect | ExpressRoute | Cloud Interconnect | FastConnect | Cloudflare Network Interconnect | — |
| ネットワーク | WAF | AWS WAF | Web Application Firewall | Cloud Armor | Web Application Firewall | WAF | AWS WAF Classicは終了 |
| ネットワーク | DDoS対策 | Shield | DDoS Protection | Cloud Armor | DDoS Protection | DDoS Protection | — |
| ネットワーク | 外向け接続トンネル | —（別構成） | —（別構成） | —（別構成） | —（別構成） | Cloudflare Tunnel | トンネルはVPNではない |
| ネットワーク | DNS・Webエッジ最適化 | Route 53 + CloudFront | Front Door | Cloud DNS + Cloud CDN | DNS + Web Application Acceleration | Argo Smart Routing / DNS | — |
| ネットワーク | ボット対策 | WAF Bot Control | Front Door WAF Bot Protection | Google Cloud Fraud Defense / Cloud Armor | WAF Bot Management | Bot Management / Turnstile | 旧reCAPTCHA Enterpriseの名称変更に注意 |
| ストレージ | オブジェクト | S3 | Blob Storage | Cloud Storage | Object Storage | R2 | R2はS3 API互換（非完全） |
| ストレージ | アーカイブ | S3 Glacier | Blob Archive | Cloud Storage Archive | Archive Storage | R2（アーカイブ階層同等なし） | 保存単価だけでなく復旧時間比較 |
| データベース | PostgreSQL | RDS PostgreSQL / Aurora | Database for PostgreSQL | Cloud SQL / AlloyDB | OCI Database with PostgreSQL | 外部DB + Hyperdrive | HyperdriveはDBサービスではない |
| データベース | MySQL | RDS MySQL / Aurora | Database for MySQL | Cloud SQL | MySQL HeatWave | 外部DB + Hyperdrive | — |
| データベース | サーバーレスRDB | Aurora Serverless | Azure SQL Database serverless | Spanner / AlloyDB（異種モデル） | Autonomous AI Database | D1（SQLite） | SQL互換性は一律ではない |
| データベース | Key-Value NoSQL | DynamoDB | Cosmos DB | Bigtable / Firestore | NoSQL Database | Workers KV | Workers KVは結果整合性 |
| 開発 | CI/CD | CodeBuild / CodePipeline / CodeDeploy | Azure DevOps / GitHub Actions | Cloud Build / Cloud Deploy | DevOps | Workers Builds / GitHub Actions | — |
| 開発 | ソースコード管理 | CodeCommit（新規利用条件注意） | Azure Repos / GitHub | Secure Source Manager | DevOps Code Repositories | 外部Gitプロバイダー | — |
| 開発 | IaC | CloudFormation / CDK / Terraform | ARM / Bicep / Terraform | Infra Manager / Config Connector | Resource Manager（Terraform） | Terraform Provider / Wrangler | Cloudflare Wranglerは汎用Terraformの代わりではない |
| 開発 | CLI | AWS CLI | Azure CLI | gcloud CLI | OCI CLI | Wrangler / cf CLI（導入状況確認） | — |
| 開発 | Webアプリホスティング | Amplify Hosting / App Runner | App Service / Static Web Apps | Firebase App Hosting / Cloud Run | Compute / OKE | Workers / Containers | Node.js・SSR互換性検証が必要 |
| 開発 | シークレット | Secrets Manager | Key Vault | Secret Manager | Vault / Secret Management Service | Workers Secrets / Secrets Store | 権限とローテーション要件を確認 |
| 開発 | 開発環境 | Cloud9（既存利用中心）/ CloudShell | Dev Box / Cloud Shell | Cloud Workstations / Cloud Shell | Cloud Shell | Workers Playground / ローカルWrangler | 製品の新規提供条件を確認 |
| 開発 | アーティファクト保管 | CodeArtifact / ECR | Azure Artifacts / ACR | Artifact Registry | Artifact Registry / OCIR | 外部レジストリ | — |
| セキュリティ | クラウドIAM | IAM / IAM Identity Center | Azure RBAC / Microsoft Entra ID | Cloud IAM / Cloud Identity | OCI IAM / Identity Domains | Cloudflare IAM / Access（別レイヤー） | Cloudflare AccessはクラウドIAMそのものではない |
| セキュリティ | 顧客向け認証 | Cognito | Entra External ID | Identity Platform | Identity Domains（要件次第） | Access（従業員・限定利用向け） | 一般消費者向けCIAMとは差がある |
| セキュリティ | セキュリティ姿勢管理 | Security Hub / Config | Defender for Cloud / Azure Policy | Security Command Center | Cloud Guard / Security Zones | Security Center（エッジ中心） | — |
| 運用 | ログ | CloudWatch Logs | Azure Monitor Logs | Cloud Logging | Logging / Log Analytics | Workers Logs / Logpush | — |
| 運用 | 分散トレース | X-Ray / Application Signals | Application Insights | Cloud Trace | Application Performance Monitoring | Workers Traces | — |
| 運用 | バックアップ | AWS Backup | Azure Backup | Backup and DR | Autonomous Recovery Service / Backup | D1 / R2の個別機能 | 包括的バックアップ製品と違う |
| 運用 | コスト管理 | Cost Explorer / Budgets | Cost Management | Cloud Billing / Recommender | Cost Management / FinOps Hub | Billing / Analytics | — |
| AI・ML | 基盤モデルAPI | Bedrock | Microsoft Foundry / Azure OpenAI | Gemini Enterprise Agent Platform / Gemini API | Generative AI | Workers AI | モデル・エンドポイント・規約差 |
| AI・ML | AIエージェント基盤 | Bedrock Agents / AgentCore | Microsoft Foundry Agent Service | Gemini Enterprise Agent Platform | Generative AI Agents | Agents SDK / Workers / Workflows | 実行権限・状態管理に差 |
| AI・ML | モデル学習・MLOps | SageMaker AI | Azure Machine Learning | Vertex AI（既存製品）/ Gemini Enterprise Agent Platform | Data Science | Workers AI（推論中心） | Cloudflareは汎用学習基盤ではない |
| AI・ML | ベクトル検索 | OpenSearch / Aurora pgvector | Azure AI Search / PostgreSQL pgvector | Vector Search / AlloyDB | AI Vector Search / Oracle AI Database | Vectorize | — |
| エッジ | 動画配信 | MediaConvert / MediaPackage | Front Door + 外部配信構成 | Transcoder API / Media CDN | Media Services | Stream | 動画処理・DRMを比較 |

## サービスの廃止・改称・変更履歴

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
