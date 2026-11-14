# Cloudflare：個別サービス一覧

> **対象:** 5社横断で同一機能として単純比較しにくいサービス・独自製品・独特の統合体系。これは独自性のある**候補一覧**であり、各社全製品の網羅・GAを保証するものではありません。

参照: [公式サービスディレクトリ](https://developers.cloudflare.com/directory/)（2026-11-14時点の参照）

エッジ・Zero Trust・開発者プラットフォームで、VM中心のクラウドと構成概念が異なる製品を収録。

**区分の注意:** 比較表と重複する製品は原則として掲載せず、製品に固有の機能や利用上の制限を重点的に記載します。 このリストに載る製品でも、部分的な競合・他社での複合構成はあり得ます。製品の存否と採用可否は個別に確認してください。

## エッジ・Web

| サービス | 各社固有の設計上の特徴・用途 |
|---|---|
| Durable Objects | 状態を持つアクター型処理 |
| D1 | SQLiteベースのサーバーレスDB |
| Hyperdrive | 外部DBへの接続最適化 |
| Cache Reserve | キャッシュ長期保持 |
| Argo Smart Routing | ネットワーク経路最適化 |
| Workers Static Assets | 静的サイト配信 |
| Pages | 静的/フロントエンド開発基盤 |
| Queues | キュー |
| Workflows | 耐久ワークフロー |
| Browser Rendering | ヘッドレスブラウザ |

## セキュリティ・ネットワーク

| サービス | 各社固有の設計上の特徴・用途 |
|---|---|
| Cloudflare Access | アプリへのZTNA |
| Cloudflare Tunnel | 外部へ公開するトンネル |
| Cloudflare Gateway | DNS/HTTPネットワーク保護 |
| Cloudflare WARP | 端末からCloudflareネットワークに接続 |
| Magic WAN | 企業WAN |
| Magic Transit | ネットワークDDoS保護 |
| Magic Firewall | ネットワークファイアウォール |
| Bot Management | Bot保護 |
| Turnstile | CAPTCHA代替の検証 |
| API Shield | API保護 |
| Cloudflare One | Zero Trust/SASE製品群 |
| AI Crawl Control | AIクローラ制御 |

## AI・メディア

| サービス | 各社固有の設計上の特徴・用途 |
|---|---|
| AI Gateway | AI APIの監視・制御 |
| AI Search | RAG検索 |
| Agents SDK | エージェント実装フレームワーク |
| Agent Memory | エージェントのメモリ機能（private beta。一般提供ではない） |
| Cloudflare Images | 画像保存・変換 |
| Cloudflare Realtime | SFU / STUN / TURN / RealtimeKit を含むリアルタイム通信製品群（旧Calls） |

## 運用・その他

| サービス | 各社固有の設計上の特徴・用途 |
|---|---|
| Email Routing | メールの受信転送 |
| Web Analytics | プライバシー配慮のWeb計測 |
| Cloudflare Radar | ネットワーク/インターネット可視化 |
| Workers Logs | Workersログ |
| Logpush | ログの外部送信 |
| Cloudflare Zaraz | タグ管理 |
| 1.1.1.1 | パブリックDNSリゾルバ |

## 横断比較へ移動した項目

- Workers
- Workers KV
- R2
- Containers
- Workers AI
- Vectorize
- Cloudflare Stream
- Cloudflare Calls

同目的のサービスは[横断比較](../service-comparison.md)に集約。単独製品ではなくサービス内の機能は一覧から除外しました。
