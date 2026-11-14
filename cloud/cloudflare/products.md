# Cloudflare公式ProductsとDocs索引の照合

**照合日：2026-11-14**（公式Webページのスナップショット）

対象: [Cloudflare Products](https://www.cloudflare.com/products/) 掲載の **68製品・ソリューション**。各製品が [公式Docsソース全件索引](catalog.md) の195エントリのどれに対応するかを記録する。

**注意:** 公式マーケティングページと公式Docsは、ブランド・SKU・機能・製品群の掲載粒度が異なる。対応候補は**機能の完全一致を意味しない**。特に旧称・新名称の移行期は正式な現行名称をDocs側で確認する。

製品ページが68項目であることは、Cloudflare全機能が68種類という意味ではない。Docs索引にある管理機能、開発者向け機能、ベータ等も [catalog.md](catalog.md) に収録している。

## Compute（10件）

| 公式Products掲載名 | Docs索引との対応 | 判定 |
|---|---|---|
| Browser Run | [公式](https://developers.cloudflare.com/browser-run/) [browser-run.yaml](https://github.com/cloudflare/cloudflare-docs/blob/34d908abc615fdf22eeb386b171b9657b9abcf38/src/content/directory/browser-run.yaml) | 同名 |
| Cloudflare Pages | [公式](https://developers.cloudflare.com/pages/) [pages.yaml](https://github.com/cloudflare/cloudflare-docs/blob/34d908abc615fdf22eeb386b171b9657b9abcf38/src/content/directory/pages.yaml) | 名称表記 |
| Containers | [公式](https://developers.cloudflare.com/containers/) [containers.yaml](https://github.com/cloudflare/cloudflare-docs/blob/34d908abc615fdf22eeb386b171b9657b9abcf38/src/content/directory/containers.yaml) | 同名 |
| Durable Objects | [公式](https://developers.cloudflare.com/durable-objects/) [durable-objects.yaml](https://github.com/cloudflare/cloudflare-docs/blob/34d908abc615fdf22eeb386b171b9657b9abcf38/src/content/directory/durable-objects.yaml) | 同名 |
| Email Service | [公式](https://developers.cloudflare.com/email-service/) [email-service.yaml](https://github.com/cloudflare/cloudflare-docs/blob/34d908abc615fdf22eeb386b171b9657b9abcf38/src/content/directory/email-service.yaml) | 同名 |
| Sandboxes | [公式](https://developers.cloudflare.com/sandbox/) [sandbox.yaml](https://github.com/cloudflare/cloudflare-docs/blob/34d908abc615fdf22eeb386b171b9657b9abcf38/src/content/directory/sandbox.yaml) | 同名 |
| Workers | [公式](https://developers.cloudflare.com/workers/) [workers.yaml](https://github.com/cloudflare/cloudflare-docs/blob/34d908abc615fdf22eeb386b171b9657b9abcf38/src/content/directory/workers.yaml) | 同名 |
| Workers for Platforms | [公式](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/) [workers-for-platforms.yaml](https://github.com/cloudflare/cloudflare-docs/blob/34d908abc615fdf22eeb386b171b9657b9abcf38/src/content/directory/workers-for-platforms.yaml) | 同名 |
| Workers Observability | [公式](https://developers.cloudflare.com/observability/) [observability.yaml](https://github.com/cloudflare/cloudflare-docs/blob/34d908abc615fdf22eeb386b171b9657b9abcf38/src/content/directory/observability.yaml) | 関連領域：機能集合 |
| Workflows | [公式](https://developers.cloudflare.com/workflows/) [workflows.yaml](https://github.com/cloudflare/cloudflare-docs/blob/34d908abc615fdf22eeb386b171b9657b9abcf38/src/content/directory/workflows.yaml) | 同名 |

## Storage（9件）

| 公式Products掲載名 | Docs索引との対応 | 判定 |
|---|---|---|
| Artifacts | [公式](https://developers.cloudflare.com/artifacts/) [artifacts.yaml](https://github.com/cloudflare/cloudflare-docs/blob/34d908abc615fdf22eeb386b171b9657b9abcf38/src/content/directory/artifacts.yaml) | 同名 |
| Cache Reserve | [公式](https://developers.cloudflare.com/cache/advanced-configuration/cache-reserve/) [cache-reserve.yaml](https://github.com/cloudflare/cloudflare-docs/blob/34d908abc615fdf22eeb386b171b9657b9abcf38/src/content/directory/cache-reserve.yaml) | 同名 |
| D1 | [公式](https://developers.cloudflare.com/d1/) [d1.yaml](https://github.com/cloudflare/cloudflare-docs/blob/34d908abc615fdf22eeb386b171b9657b9abcf38/src/content/directory/d1.yaml) | 同名 |
| Basin | [公式](https://developers.cloudflare.com/basin/) [basin.yaml](https://github.com/cloudflare/cloudflare-docs/blob/34d908abc615fdf22eeb386b171b9657b9abcf38/src/content/directory/basin.yaml) | 同名（旧Data Platform） |
| Hyperdrive | [公式](https://developers.cloudflare.com/hyperdrive/) [hyperdrive.yaml](https://github.com/cloudflare/cloudflare-docs/blob/34d908abc615fdf22eeb386b171b9657b9abcf38/src/content/directory/hyperdrive.yaml) | 同名 |
| K2 | [公式](https://developers.cloudflare.com/k2/) [k2.yaml](https://github.com/cloudflare/cloudflare-docs/blob/34d908abc615fdf22eeb386b171b9657b9abcf38/src/content/directory/k2.yaml) | 同名（public beta） |
| KV | [公式](https://developers.cloudflare.com/kv/) [kv.yaml](https://github.com/cloudflare/cloudflare-docs/blob/34d908abc615fdf22eeb386b171b9657b9abcf38/src/content/directory/kv.yaml) | 同名 |
| Queues | [公式](https://developers.cloudflare.com/queues/) [queues.yaml](https://github.com/cloudflare/cloudflare-docs/blob/34d908abc615fdf22eeb386b171b9657b9abcf38/src/content/directory/queues.yaml) | 同名 |
| R2 | [公式](https://developers.cloudflare.com/r2/) [r2.yaml](https://github.com/cloudflare/cloudflare-docs/blob/34d908abc615fdf22eeb386b171b9657b9abcf38/src/content/directory/r2.yaml) | 同名 |

## AI（6件）

| 公式Products掲載名 | Docs索引との対応 | 判定 |
|---|---|---|
| Agents | [公式](https://developers.cloudflare.com/agents/) [agents.yaml](https://github.com/cloudflare/cloudflare-docs/blob/34d908abc615fdf22eeb386b171b9657b9abcf38/src/content/directory/agents.yaml) | 同名 |
| AI Gateway | [公式](https://developers.cloudflare.com/ai-gateway/) [ai-gateway.yaml](https://github.com/cloudflare/cloudflare-docs/blob/34d908abc615fdf22eeb386b171b9657b9abcf38/src/content/directory/ai-gateway.yaml) | 同名 |
| AI Search | [公式](https://developers.cloudflare.com/ai-search/) [ai-search.yaml](https://github.com/cloudflare/cloudflare-docs/blob/34d908abc615fdf22eeb386b171b9657b9abcf38/src/content/directory/ai-search.yaml) | 同名 |
| Vectorize | [公式](https://developers.cloudflare.com/vectorize/) [vectorize.yaml](https://github.com/cloudflare/cloudflare-docs/blob/34d908abc615fdf22eeb386b171b9657b9abcf38/src/content/directory/vectorize.yaml) | 同名 |
| Web3 | [公式](https://developers.cloudflare.com/web3/) [web3.yaml](https://github.com/cloudflare/cloudflare-docs/blob/34d908abc615fdf22eeb386b171b9657b9abcf38/src/content/directory/web3.yaml) | 同名 |
| Workers AI | [公式](https://developers.cloudflare.com/workers-ai/) [workers-ai.yaml](https://github.com/cloudflare/cloudflare-docs/blob/34d908abc615fdf22eeb386b171b9657b9abcf38/src/content/directory/workers-ai.yaml) | 同名 |

## Media（3件）

| 公式Products掲載名 | Docs索引との対応 | 判定 |
|---|---|---|
| Images | [公式](https://developers.cloudflare.com/images/) [images.yaml](https://github.com/cloudflare/cloudflare-docs/blob/34d908abc615fdf22eeb386b171b9657b9abcf38/src/content/directory/images.yaml) | 名称表記 |
| RealtimeKit | [公式](https://developers.cloudflare.com/realtime/realtimekit/) [realtime-kit.yaml](https://github.com/cloudflare/cloudflare-docs/blob/34d908abc615fdf22eeb386b171b9657b9abcf38/src/content/directory/realtime-kit.yaml) | 同名 |
| Stream | [公式](https://developers.cloudflare.com/stream/) [stream.yaml](https://github.com/cloudflare/cloudflare-docs/blob/34d908abc615fdf22eeb386b171b9657b9abcf38/src/content/directory/stream.yaml) | 同名 |

## Security（9件）

| 公式Products掲載名 | Docs索引との対応 | 判定 |
|---|---|---|
| Bot Management | [公式](https://developers.cloudflare.com/bots/) [bots.yaml](https://github.com/cloudflare/cloudflare-docs/blob/34d908abc615fdf22eeb386b171b9657b9abcf38/src/content/directory/bots.yaml) | DocsではBots |
| Client-Side Security | [公式](https://developers.cloudflare.com/client-side-security/) [client-side-security.yaml](https://github.com/cloudflare/cloudflare-docs/blob/34d908abc615fdf22eeb386b171b9657b9abcf38/src/content/directory/client-side-security.yaml) | 同名 |
| DDoS Protection | [公式](https://developers.cloudflare.com/ddos-protection/) [ddos-protection.yaml](https://github.com/cloudflare/cloudflare-docs/blob/34d908abc615fdf22eeb386b171b9657b9abcf38/src/content/directory/ddos-protection.yaml) | 同名 |
| Magic Transit | [公式](https://developers.cloudflare.com/magic-transit/) [magic-transit.yaml](https://github.com/cloudflare/cloudflare-docs/blob/34d908abc615fdf22eeb386b171b9657b9abcf38/src/content/directory/magic-transit.yaml) | 同名 |
| Network Firewall | [公式](https://developers.cloudflare.com/cloudflare-network-firewall/) [cloudflare-network-firewall.yaml](https://github.com/cloudflare/cloudflare-docs/blob/34d908abc615fdf22eeb386b171b9657b9abcf38/src/content/directory/cloudflare-network-firewall.yaml) | 名称表記 |
| Rate Limiting | [公式](https://developers.cloudflare.com/waf/rate-limiting-rules/) [rate-limiting.yaml](https://github.com/cloudflare/cloudflare-docs/blob/34d908abc615fdf22eeb386b171b9657b9abcf38/src/content/directory/rate-limiting.yaml) | 同名 |
| SSL | [公式](https://developers.cloudflare.com/ssl/) [ssl.yaml](https://github.com/cloudflare/cloudflare-docs/blob/34d908abc615fdf22eeb386b171b9657b9abcf38/src/content/directory/ssl.yaml) | 広い製品カテゴリ |
| Turnstile | [公式](https://developers.cloudflare.com/turnstile/) [turnstile.yaml](https://github.com/cloudflare/cloudflare-docs/blob/34d908abc615fdf22eeb386b171b9657b9abcf38/src/content/directory/turnstile.yaml) | 同名 |
| WAF | [公式](https://developers.cloudflare.com/waf/) [waf.yaml](https://github.com/cloudflare/cloudflare-docs/blob/34d908abc615fdf22eeb386b171b9657b9abcf38/src/content/directory/waf.yaml) | 同名 |

## Network（21件）

| 公式Products掲載名 | Docs索引との対応 | 判定 |
|---|---|---|
| Advanced Certificate Manager | [公式](https://developers.cloudflare.com/ssl/) [ssl.yaml](https://github.com/cloudflare/cloudflare-docs/blob/34d908abc615fdf22eeb386b171b9657b9abcf38/src/content/directory/ssl.yaml) | SSL/TLSの機能・プラン |
| Analytics | [公式](https://developers.cloudflare.com/analytics/) [analytics.yaml](https://github.com/cloudflare/cloudflare-docs/blob/34d908abc615fdf22eeb386b171b9657b9abcf38/src/content/directory/analytics.yaml) | 同名 |
| API Shield | [公式](https://developers.cloudflare.com/api-shield/) [api-shield.yaml](https://github.com/cloudflare/cloudflare-docs/blob/34d908abc615fdf22eeb386b171b9657b9abcf38/src/content/directory/api-shield.yaml) | 同名 |
| Argo Smart Routing | [公式](https://developers.cloudflare.com/argo-smart-routing/) [argo-smart-routing.yaml](https://github.com/cloudflare/cloudflare-docs/blob/34d908abc615fdf22eeb386b171b9657b9abcf38/src/content/directory/argo-smart-routing.yaml) | 同名 |
| CDN | [公式](https://developers.cloudflare.com/cache/) [cache.yaml](https://github.com/cloudflare/cloudflare-docs/blob/34d908abc615fdf22eeb386b171b9657b9abcf38/src/content/directory/cache.yaml) | 関連領域：CDNとCacheは完全同義ではない |
| China Network | [公式](https://developers.cloudflare.com/china-network/) [china-network.yaml](https://github.com/cloudflare/cloudflare-docs/blob/34d908abc615fdf22eeb386b171b9657b9abcf38/src/content/directory/china-network.yaml) | 同名 |
| Custom Domain Protection | [公式](https://developers.cloudflare.com/registrar/) [registrar.yaml](https://github.com/cloudflare/cloudflare-docs/blob/34d908abc615fdf22eeb386b171b9657b9abcf38/src/content/directory/registrar.yaml) | Registrarの上位セキュリティ機能 |
| DDoS for Web | [公式](https://developers.cloudflare.com/ddos-protection/) [ddos-protection.yaml](https://github.com/cloudflare/cloudflare-docs/blob/34d908abc615fdf22eeb386b171b9657b9abcf38/src/content/directory/ddos-protection.yaml) | DDoSのWeb用途 |
| DNS | [公式](https://developers.cloudflare.com/dns/) [dns.yaml](https://github.com/cloudflare/cloudflare-docs/blob/34d908abc615fdf22eeb386b171b9657b9abcf38/src/content/directory/dns.yaml) | 同名 |
| Email Routing | [公式](https://developers.cloudflare.com/email-service/) [email-service.yaml](https://github.com/cloudflare/cloudflare-docs/blob/34d908abc615fdf22eeb386b171b9657b9abcf38/src/content/directory/email-service.yaml) | 統合サービスの受信転送機能 |
| Keyless SSL | [公式](https://developers.cloudflare.com/ssl/keyless-ssl/) [keyless-ssl.yaml](https://github.com/cloudflare/cloudflare-docs/blob/34d908abc615fdf22eeb386b171b9657b9abcf38/src/content/directory/keyless-ssl.yaml) | 同名 |
| Load Balancing | [公式](https://developers.cloudflare.com/load-balancing/) [load-balancing.yaml](https://github.com/cloudflare/cloudflare-docs/blob/34d908abc615fdf22eeb386b171b9657b9abcf38/src/content/directory/load-balancing.yaml) | 同名 |
| Log Explorer | [公式](https://developers.cloudflare.com/observability/logs/log-explorer/) [log-explorer.yaml](https://github.com/cloudflare/cloudflare-docs/blob/34d908abc615fdf22eeb386b171b9657b9abcf38/src/content/directory/log-explorer.yaml) | 同名 |
| Network Flow | [公式](https://developers.cloudflare.com/network-flow/) [network-flow.yaml](https://github.com/cloudflare/cloudflare-docs/blob/34d908abc615fdf22eeb386b171b9657b9abcf38/src/content/directory/network-flow.yaml) | 同名 |
| Network Interconnect | [公式](https://developers.cloudflare.com/network-interconnect/) [network-interconnect.yaml](https://github.com/cloudflare/cloudflare-docs/blob/34d908abc615fdf22eeb386b171b9657b9abcf38/src/content/directory/network-interconnect.yaml) | 同名 |
| Page Shield | [公式](https://developers.cloudflare.com/client-side-security/) [client-side-security.yaml](https://github.com/cloudflare/cloudflare-docs/blob/34d908abc615fdf22eeb386b171b9657b9abcf38/src/content/directory/client-side-security.yaml) | Docs上はClient-side security |
| RDP | [公式](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) [access.yaml](https://github.com/cloudflare/cloudflare-docs/blob/34d908abc615fdf22eeb386b171b9657b9abcf38/src/content/directory/access.yaml) | RDPリモートアクセス用途：完全同等ではない |
| Spectrum | [公式](https://developers.cloudflare.com/spectrum/) [spectrum.yaml](https://github.com/cloudflare/cloudflare-docs/blob/34d908abc615fdf22eeb386b171b9657b9abcf38/src/content/directory/spectrum.yaml) | 同名 |
| Spectrum for Minecraft | [公式](https://developers.cloudflare.com/spectrum/) [spectrum.yaml](https://github.com/cloudflare/cloudflare-docs/blob/34d908abc615fdf22eeb386b171b9657b9abcf38/src/content/directory/spectrum.yaml) | Spectrumの用途別商品 |
| TURN / SFU | [公式](https://developers.cloudflare.com/realtime/) [realtime.yaml](https://github.com/cloudflare/cloudflare-docs/blob/34d908abc615fdf22eeb386b171b9657b9abcf38/src/content/directory/realtime.yaml) | Realtimeの構成機能 |
| Waiting Room | [公式](https://developers.cloudflare.com/waiting-room/) [waiting-room.yaml](https://github.com/cloudflare/cloudflare-docs/blob/34d908abc615fdf22eeb386b171b9657b9abcf38/src/content/directory/waiting-room.yaml) | 同名 |

## SASE / Zero Trust（10件）

| 公式Products掲載名 | Docs索引との対応 | 判定 |
|---|---|---|
| Access | [公式](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) [access.yaml](https://github.com/cloudflare/cloudflare-docs/blob/34d908abc615fdf22eeb386b171b9657b9abcf38/src/content/directory/access.yaml) | 同名 |
| AI Security for Apps | [公式](https://developers.cloudflare.com/waf/detections/ai-security-for-apps/) [ai-security-for-apps.yaml](https://github.com/cloudflare/cloudflare-docs/blob/34d908abc615fdf22eeb386b171b9657b9abcf38/src/content/directory/ai-security-for-apps.yaml) | 公式ソースYAMLはディレクトリ非表示 |
| Browser Isolation | [公式](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/) [browser-isolation.yaml](https://github.com/cloudflare/cloudflare-docs/blob/34d908abc615fdf22eeb386b171b9657b9abcf38/src/content/directory/browser-isolation.yaml) | 同名 |
| CASB | [公式](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/) [casb.yaml](https://github.com/cloudflare/cloudflare-docs/blob/34d908abc615fdf22eeb386b171b9657b9abcf38/src/content/directory/casb.yaml) | 同名 |
| Data Loss Prevention | [公式](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/) [dlp.yaml](https://github.com/cloudflare/cloudflare-docs/blob/34d908abc615fdf22eeb386b171b9657b9abcf38/src/content/directory/dlp.yaml) | 同名 |
| Email Security | [公式](https://developers.cloudflare.com/cloudflare-one/email-security/) [email-security-cf1.yaml](https://github.com/cloudflare/cloudflare-docs/blob/34d908abc615fdf22eeb386b171b9657b9abcf38/src/content/directory/email-security-cf1.yaml) | 同名 |
| Gateway | [公式](https://developers.cloudflare.com/cloudflare-one/traffic-controls/) [gateway.yaml](https://github.com/cloudflare/cloudflare-docs/blob/34d908abc615fdf22eeb386b171b9657b9abcf38/src/content/directory/gateway.yaml) | 同名 |
| Mesh | [公式](https://developers.cloudflare.com/mesh/) [mesh.yaml](https://github.com/cloudflare/cloudflare-docs/blob/34d908abc615fdf22eeb386b171b9657b9abcf38/src/content/directory/mesh.yaml) | 名称表記 |
| Secure Web Gateway | [公式](https://developers.cloudflare.com/cloudflare-one/traffic-controls/) [gateway.yaml](https://github.com/cloudflare/cloudflare-docs/blob/34d908abc615fdf22eeb386b171b9657b9abcf38/src/content/directory/gateway.yaml) | 同製品群の機能名称 |
| WAN | [公式](https://developers.cloudflare.com/cloudflare-wan/) [cloudflare-wan.yaml](https://github.com/cloudflare/cloudflare-docs/blob/34d908abc615fdf22eeb386b171b9657b9abcf38/src/content/directory/cloudflare-wan.yaml) | 名称表記 |

## 掲載名の更新履歴

- 2026-10-01: Cloudflare Data Platform は **Basin** に改称、一般提供開始。[公式発表](https://developers.cloudflare.com/changelog/post/2026-10-01-basin-ga/)
- 2026-10-01: **K2** を公開ベータとして製品一覧に追加。[公式発表](https://blog.cloudflare.com/cloudflare-k2-streams)

## 照合結果

- 同名（旧名補足を含む）: **49件**
- 別名・旧称・機能/製品群への暫定対応: **19件**
- Docs索引との1対1対応未特定: **0件**

この表で示した「別名・旧称」の一部は機能粒度の関連づけであり、同一サービスとは断定しません。追加の公式資料を調べる際のトリアージ用です。
