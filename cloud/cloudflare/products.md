# Cloudflare公式ProductsとDocs索引の照合

**照合日：2026-11-14**（公式Webページのスナップショット）  
**Docs照合元コミット:** `34d908abc615fdf22eeb386b171b9657b9abcf38`

対象: [Cloudflare Products](https://www.cloudflare.com/products/) 掲載の **68製品・ソリューション**。各製品が [公式Docsソース全件索引](catalog.md) の195エントリのどれに対応するかを記録する。

各行の `*.yaml` は上記固定コミットの `src/content/directory/` 配下にある公式ソースファイルです。これらは [catalog.md](catalog.md) にも載り、再生成時に相互突合します。長い固定コミットURLは表へ重複掲載しません。

**分類:** 「同名」＝名称一致、「改称」＝旧新名称、「表記ゆれ」＝表記差、「機能・製品群」＝目的が近い機能/製品集合（**同一サービスと断定しない**）。補足欄で根拠や差を示します。

**注意:** 公式マーケティングページと公式Docsは、ブランド・SKU・機能・製品群の掲載粒度が異なる。対応候補は**機能の完全一致を意味しない**。特に旧称・新名称の移行期は正式な現行名称をDocs側で確認する。

製品ページが68項目であることは、Cloudflare全機能が68種類という意味ではない。Docs索引にある管理機能、開発者向け機能、ベータ等も [catalog.md](catalog.md) に収録している。

## Compute（10件）

| 公式Products掲載名 | 対応Docs・ソースYAML | 分類 | 補足 |
|---|---|---|---|
| Browser Run | [公式](https://developers.cloudflare.com/browser-run/) `browser-run.yaml` | 同名 | 旧Browser Rendering（2026-04-15改称） |
| Cloudflare Pages | [公式](https://developers.cloudflare.com/pages/) `pages.yaml` | 表記ゆれ | Docs側と名称の接頭辞/表記が異なる |
| Containers | [公式](https://developers.cloudflare.com/containers/) `containers.yaml` | 同名 | — |
| Durable Objects | [公式](https://developers.cloudflare.com/durable-objects/) `durable-objects.yaml` | 同名 | — |
| Email Service | [公式](https://developers.cloudflare.com/email-service/) `email-service.yaml` | 同名 | — |
| Sandboxes | [公式](https://developers.cloudflare.com/sandbox/) `sandbox.yaml` | 同名 | — |
| Workers | [公式](https://developers.cloudflare.com/workers/) `workers.yaml` | 同名 | — |
| Workers for Platforms | [公式](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/) `workers-for-platforms.yaml` | 同名 | — |
| Workers Observability | [公式](https://developers.cloudflare.com/observability/) `observability.yaml` | 機能・製品群 | 関連領域：機能集合 |
| Workflows | [公式](https://developers.cloudflare.com/workflows/) `workflows.yaml` | 同名 | — |

## Storage（9件）

| 公式Products掲載名 | Docs索引との対応 | 判定 |
|---|---|---|---|
| Artifacts | [公式](https://developers.cloudflare.com/artifacts/) `artifacts.yaml` | 同名 | — |
| Cache Reserve | [公式](https://developers.cloudflare.com/cache/advanced-configuration/cache-reserve/) `cache-reserve.yaml` | 同名 | — |
| D1 | [公式](https://developers.cloudflare.com/d1/) `d1.yaml` | 同名 | — |
| Basin | [公式](https://developers.cloudflare.com/basin/) `basin.yaml` | 同名 | 旧Data Platform |
| Hyperdrive | [公式](https://developers.cloudflare.com/hyperdrive/) `hyperdrive.yaml` | 同名 | — |
| K2 | [公式](https://developers.cloudflare.com/k2/) `k2.yaml` | 同名 | public beta |
| KV | [公式](https://developers.cloudflare.com/kv/) `kv.yaml` | 同名 | — |
| Queues | [公式](https://developers.cloudflare.com/queues/) `queues.yaml` | 同名 | — |
| R2 | [公式](https://developers.cloudflare.com/r2/) `r2.yaml` | 同名 | — |

## AI（6件）

| 公式Products掲載名 | Docs索引との対応 | 判定 |
|---|---|---|---|
| Agents | [公式](https://developers.cloudflare.com/agents/) `agents.yaml` | 同名 | — |
| AI Gateway | [公式](https://developers.cloudflare.com/ai-gateway/) `ai-gateway.yaml` | 同名 | — |
| AI Search | [公式](https://developers.cloudflare.com/ai-search/) `ai-search.yaml` | 同名 | — |
| Vectorize | [公式](https://developers.cloudflare.com/vectorize/) `vectorize.yaml` | 同名 | — |
| Web3 | [公式](https://developers.cloudflare.com/web3/) `web3.yaml` | 同名 | — |
| Workers AI | [公式](https://developers.cloudflare.com/workers-ai/) `workers-ai.yaml` | 同名 | — |

## Media（3件）

| 公式Products掲載名 | Docs索引との対応 | 判定 |
|---|---|---|---|
| Images | [公式](https://developers.cloudflare.com/images/) `images.yaml` | 表記ゆれ | Docs側と名称の接頭辞/表記が異なる |
| RealtimeKit | [公式](https://developers.cloudflare.com/realtime/realtimekit/) `realtime-kit.yaml` | 同名 | — |
| Stream | [公式](https://developers.cloudflare.com/stream/) `stream.yaml` | 同名 | — |

## Security（9件）

| 公式Products掲載名 | Docs索引との対応 | 判定 |
|---|---|---|---|
| Bot Management | [公式](https://developers.cloudflare.com/bots/) `bots.yaml` | 機能・製品群 | DocsではBots |
| Client-Side Security | [公式](https://developers.cloudflare.com/client-side-security/) `client-side-security.yaml` | 同名 | — |
| DDoS Protection | [公式](https://developers.cloudflare.com/ddos-protection/) `ddos-protection.yaml` | 同名 | — |
| Magic Transit | [公式](https://developers.cloudflare.com/magic-transit/) `magic-transit.yaml` | 同名 | — |
| Network Firewall | [公式](https://developers.cloudflare.com/cloudflare-network-firewall/) `cloudflare-network-firewall.yaml` | 表記ゆれ | Docs側と名称の接頭辞/表記が異なる |
| Rate Limiting | [公式](https://developers.cloudflare.com/waf/rate-limiting-rules/) `rate-limiting.yaml` | 同名 | — |
| SSL | [公式](https://developers.cloudflare.com/ssl/) `ssl.yaml` | 機能・製品群 | 広い製品カテゴリ |
| Turnstile | [公式](https://developers.cloudflare.com/turnstile/) `turnstile.yaml` | 同名 | — |
| WAF | [公式](https://developers.cloudflare.com/waf/) `waf.yaml` | 同名 | — |

## Network（21件）

| 公式Products掲載名 | Docs索引との対応 | 判定 |
|---|---|---|---|
| Advanced Certificate Manager | [公式](https://developers.cloudflare.com/ssl/) `ssl.yaml` | 機能・製品群 | SSL/TLSの機能・プラン |
| Analytics | [公式](https://developers.cloudflare.com/analytics/) `analytics.yaml` | 同名 | — |
| API Shield | [公式](https://developers.cloudflare.com/api-shield/) `api-shield.yaml` | 同名 | — |
| Argo Smart Routing | [公式](https://developers.cloudflare.com/argo-smart-routing/) `argo-smart-routing.yaml` | 同名 | — |
| CDN | [公式](https://developers.cloudflare.com/cache/) `cache.yaml` | 機能・製品群 | 関連領域：CDNとCacheは完全同義ではない |
| China Network | [公式](https://developers.cloudflare.com/china-network/) `china-network.yaml` | 同名 | — |
| Custom Domain Protection | [公式](https://developers.cloudflare.com/registrar/) `registrar.yaml` | 機能・製品群 | Registrarの上位セキュリティ機能 |
| DDoS for Web | [公式](https://developers.cloudflare.com/ddos-protection/) `ddos-protection.yaml` | 機能・製品群 | DDoSのWeb用途 |
| DNS | [公式](https://developers.cloudflare.com/dns/) `dns.yaml` | 同名 | — |
| Email Routing | [公式](https://developers.cloudflare.com/email-service/) `email-service.yaml` | 機能・製品群 | 統合サービスの受信転送機能 |
| Keyless SSL | [公式](https://developers.cloudflare.com/ssl/keyless-ssl/) `keyless-ssl.yaml` | 同名 | — |
| Load Balancing | [公式](https://developers.cloudflare.com/load-balancing/) `load-balancing.yaml` | 同名 | — |
| Log Explorer | [公式](https://developers.cloudflare.com/observability/logs/log-explorer/) `log-explorer.yaml` | 同名 | — |
| Network Flow | [公式](https://developers.cloudflare.com/network-flow/) `network-flow.yaml` | 同名 | — |
| Network Interconnect | [公式](https://developers.cloudflare.com/network-interconnect/) `network-interconnect.yaml` | 同名 | — |
| Page Shield | [公式](https://developers.cloudflare.com/client-side-security/) `client-side-security.yaml` | 改称 | 現在のClient-side securityに対応する旧製品名。Products上の重複ブランド表記 |
| RDP | [公式](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) `access.yaml` | 機能・製品群 | RDPリモートアクセス用途：完全同等ではない |
| Spectrum | [公式](https://developers.cloudflare.com/spectrum/) `spectrum.yaml` | 同名 | — |
| Spectrum for Minecraft | [公式](https://developers.cloudflare.com/spectrum/) `spectrum.yaml` | 機能・製品群 | Spectrumの用途別商品 |
| TURN / SFU | [公式](https://developers.cloudflare.com/realtime/) `realtime.yaml` | 機能・製品群 | Realtimeの構成機能 |
| Waiting Room | [公式](https://developers.cloudflare.com/waiting-room/) `waiting-room.yaml` | 同名 | — |

## SASE / Zero Trust（10件）

| 公式Products掲載名 | Docs索引との対応 | 判定 |
|---|---|---|---|
| Access | [公式](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) `access.yaml` | 同名 | — |
| AI Security for Apps | [公式](https://developers.cloudflare.com/waf/detections/ai-security-for-apps/) `ai-security-for-apps.yaml` | 機能・製品群 | 公式ソースYAMLはディレクトリ非表示 |
| Browser Isolation | [公式](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/) `browser-isolation.yaml` | 同名 | — |
| CASB | [公式](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/) `casb.yaml` | 同名 | — |
| Data Loss Prevention | [公式](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/) `dlp.yaml` | 同名 | — |
| Email Security | [公式](https://developers.cloudflare.com/cloudflare-one/email-security/) `email-security-cf1.yaml` | 同名 | — |
| Gateway | [公式](https://developers.cloudflare.com/cloudflare-one/traffic-controls/) `gateway.yaml` | 同名 | — |
| Mesh | [公式](https://developers.cloudflare.com/mesh/) `mesh.yaml` | 表記ゆれ | Docs側と名称の接頭辞/表記が異なる |
| Secure Web Gateway | [公式](https://developers.cloudflare.com/cloudflare-one/traffic-controls/) `gateway.yaml` | 機能・製品群 | 同製品群の機能名称 |
| WAN | [公式](https://developers.cloudflare.com/cloudflare-wan/) `cloudflare-wan.yaml` | 表記ゆれ | Docs側と名称の接頭辞/表記が異なる |

## 掲載名の更新履歴

- 2026-10-01: Cloudflare Data Platform は **Basin** に改称、一般提供開始。[公式発表](https://developers.cloudflare.com/changelog/post/2026-10-01-basin-ga/)
- 2026-10-01: **K2** を公開ベータとして製品一覧に追加。[公式発表](https://blog.cloudflare.com/cloudflare-k2-streams)

## 照合結果

- 同名: **49件**
- 改称: **1件**
- 表記ゆれ: **5件**
- 機能・製品群の対応候補: **13件**
- Docs索引との1対1対応未特定: **0件**

この表で示した「機能・製品群」の一部は機能粒度の関連づけであり、同一サービスとは断定しません。追加の公式資料を調べる際のトリアージ用です。
