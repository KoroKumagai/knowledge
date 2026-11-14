# Azure：個別サービス一覧

> **対象:** 5社横断で同一機能として単純比較しにくいサービス・独自製品・独特の統合体系。これは独自性のある**候補一覧**であり、各社全製品の網羅・GAを保証するものではありません。

参照: [公式サービスディレクトリ](https://azure.microsoft.com/en-us/products/)（2026-11-14時点の参照）

Microsoft製品群・ID・業務基盤との結合度が強く、AWSなどの単一サービスへ機械的に対応付けできないものを収録。

**区分の注意:** 比較表と重複する製品は原則として掲載せず、製品に固有の機能や利用上の制限を重点的に記載します。 このリストに載る製品でも、部分的な競合・他社での複合構成はあり得ます。製品の存否と採用可否は個別に確認してください。

## Microsoft連携・ハイブリッド

| サービス | 各社固有の設計上の特徴・用途 |
|---|---|
| Azure Arc | ハイブリッド・マルチクラウド管理 |
| Azure Local | Azure管理面に統合したオンプレミス/HCI基盤 |
| Azure Lighthouse | 顧客テナント管理 |
| Azure Virtual Desktop | 仮想デスクトップ |
| Windows 365 | クラウドPC（Azureとの関係を区別） |
| Azure Update Manager | サーバー更新管理 |

## ID・統制

| サービス | 各社固有の設計上の特徴・用途 |
|---|---|
| Microsoft Entra ID | Microsoft ID基盤 |
| Microsoft Entra Private Access | ZTNA |
| Microsoft Entra Internet Access | インターネットアクセス保護 |
| Microsoft Purview | データガバナンス |

## データ・アプリ

| サービス | 各社固有の設計上の特徴・用途 |
|---|---|
| Microsoft Fabric | 統合分析SaaS |
| Azure Data Explorer | Kustoクエリ分析 |
| Azure Communication Services | 通信API |
| Azure SignalR Service | リアルタイム通信 |
| Azure Fluid Relay | 共同編集状態の同期 |
| Azure Maps | 地図API |

## AI・開発・運用

| サービス | 各社固有の設計上の特徴・用途 |
|---|---|
| Microsoft Foundry | AIアプリ・エージェントプラットフォーム |
| Foundry Agent Service | AIエージェント基盤 |
| Azure Copilot | Azure運用支援 |
| Azure Managed Grafana | Grafanaマネージド提供 |

## 横断比較へ移動した項目

- Azure Migrate
- Microsoft Entra External ID
- Microsoft Defender for Cloud
- Azure Policy
- Azure Digital Twins
- Azure PlayFab
- Azure Dev Box
- Azure Chaos Studio
- Azure Managed Redis

同目的のサービスは[横断比較](../service-comparison.md)に集約。単独製品ではなくサービス内の機能は一覧から除外しました。
