# Cloudflare：個別サービス一覧

> **対象:** 2社以上で比較できる共通機能とは区別して扱うサービス・独自製品・独特の統合体系。これは独自性のある**候補一覧**であり、各社全製品の網羅・GAを保証するものではありません。

参照: [公式サービスディレクトリ](https://developers.cloudflare.com/directory/)（2026-11-14時点の参照）

エッジ・Zero Trust・開発者プラットフォームで、VM中心のクラウドと構成概念が異なる製品を収録。

**区分の注意:** 比較表と重複する製品は原則として掲載しません。このリストに載る製品でも、部分的な競合・他社での複合構成はあり得ます。製品の存否と採用可否は個別に確認してください。

## エッジ・Web

| サービス | 用途 |
|---|---|
| Durable Objects | 状態を持つアクター型処理 |
| D1 | SQLiteベースのサーバーレスDB |
| Hyperdrive | 外部DBへの接続最適化 |
| Cache Reserve | キャッシュ長期保持 |
| Argo Smart Routing | ネットワーク経路最適化 |
| Browser Run | ブラウザ自動化・ヘッドレス実行（旧Browser Rendering） |

## セキュリティ・ネットワーク

| サービス | 用途 |
|---|---|
| Cloudflare Access | アプリへのZTNA |
| Cloudflare Tunnel | 外部へ公開するトンネル |
| Cloudflare Gateway | DNS/HTTPネットワーク保護 |
| Cloudflare WARP | 端末からCloudflareネットワークに接続 |
| Cloudflare WAN | 企業WAN（旧Magic WAN） |
| Magic Transit | ネットワークDDoS保護 |
| Cloudflare Network Firewall | ネットワークファイアウォール（旧Magic Firewall） |
| Turnstile | CAPTCHA代替の検証 |
| API Shield | API保護 |
| Cloudflare One | Zero Trust/SASE製品群 |
| AI Crawl Control | AIクローラ制御 |

## AI・メディア

| サービス | 用途 |
|---|---|
| AI Gateway | AI APIの監視・制御 |
| AI Search | RAG検索 |
| Agent Memory | エージェントのメモリ機能（private beta。一般提供ではない） |
| Cloudflare Images | 画像保存・変換 |
| Cloudflare Realtime | SFU / STUN / TURN / RealtimeKit を含むリアルタイム通信製品群（旧Calls） |

## 運用・その他

| サービス | 用途 |
|---|---|
| Email Routing | Email Serviceの受信・転送機能（送信用Email Sendingとは区別） |
| Web Analytics | プライバシー配慮のWeb計測 |
| Cloudflare Radar | ネットワーク/インターネット可視化 |
| Cloudflare Zaraz | タグ管理 |
| 1.1.1.1 | パブリックDNSリゾルバ |

## 横断比較へ移動した項目

- Agents SDK
- Pages
- Workers Static Assets
- Bot Management
- Cloudflare Stream
- Containers
- Logpush
- Queues
- R2
- Vectorize
- Workers
- Workers AI
- Workers KV
- Workers Logs
- Workflows

## 機能・旧名のため除外・統合した項目

- **Cloudflare Calls** — Cloudflare Realtimeの旧名。Realtimeに統合

[横断比較表](../service-comparison.md)の該当領域を参照してください。
