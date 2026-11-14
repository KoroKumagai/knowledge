# Cloudflare サービスカタログの調査

**調査日:** 2026-11-14

このディレクトリは2つの役割に分かれます。公式サービス一覧の**網羅性を追跡する一次資料ベースの台帳**と、5社比較では対応付けが難しいサービスをまとめた**編集済み一覧**です。

| ファイル | 用途 |
|---|---|
| [catalog.md](catalog.md) | Cloudflare公式DocsのYAMLディレクトリ **195エントリ**全件。公開138、非表示57。出典YAMLとステータス確認済み分の根拠あり |
| [products.md](products.md) | 公式Cloudflare Productsに掲載された**68項目**をDocs索引と照合。同名49、別名・機能名19 |
| [services.md](services.md) | 5社横断比較へ移しにくい個別サービスを整理した編集済み一覧（**27件**） |
| [../service-comparison.md](../service-comparison.md) | 2社以上で比較できる用途・サービスの横断表 |

## 網羅性の定義

- **Docs全件監査:** upstreamの `cloudflare/cloudflare-docs` の `production` ブランチの `src/content/directory/*.yaml` を固定コミットで全件取得。195件を漏れなく一覧化。ただしこれにはDocs集、設定機能、公開非表示のメタデータも含まれ、195個の独立した商用サービスを意味しません。
- **商用製品カタログとの比較:** 別途公式Productsの68項目を抽出し、Docsの現行名/類似製品群と1件ずつ突合しました。19件の別名・機能名との対応は同一サービスという主張ではなく、検証・保守用の案内です。
- **提供状況:** GAやベータの根拠が確認できた製品のみ状態と公式リンクを記載しています。非表示メタデータは廃止済みを意味しません。全製品の地域・プラン・SLA・GAの網羅的検証は未完了です。

## 2026年の重要差分

- **AI Search:** 2026-10-01 GA。[公式](https://developers.cloudflare.com/changelog/post/2026-10-01-ai-search-generally-available/)
- **Cloudflare CLI（cf）:** 2026-09-28にbeta公開。[公式](https://developers.cloudflare.com/changelog/post/2026-09-28-cloudflare-cli-beta/)
- **Basin:** 2026-10-01 GA。旧 Data Platform、Pipelines、R2 Data Catalog、R2 SQL は Basin、Basin Pipelines、Basin Catalog、Basin SQL に改称。[公式](https://developers.cloudflare.com/changelog/post/2026-10-01-basin-ga/)
- **Agent Memory:** private beta。[公式](https://developers.cloudflare.com/agent-memory/)
- **K2:** public beta。[公式](https://developers.cloudflare.com/k2/platform/pricing/)
- **Artifacts:** open beta。[公式](https://developers.cloudflare.com/changelog/product/artifacts/)
- **Email Service:** Email Sendingはpublic beta。[公式](https://developers.cloudflare.com/email-service/)
- **Workers VPC:** beta。[公式](https://developers.cloudflare.com/workers-vpc/get-started/)
- **Cloudflare Wallets:** 現時点ではウォレット名の予約のみ。[公式](https://developers.cloudflare.com/wallets/)

## 更新・チェック

- `python scripts/refresh_cloudflare_directory.py`: 公式GitHubの新しい固定コミットから `catalog.md` を全件再生成。標準ライブラリのみで実行できます。
- `python scripts/check_cloudflare_catalog.py`: 195件/68件など、ソース単位の欠落、重複、READMEの件数を検査。
- GitHub ActionsでCIを実施し、公式索引の更新は手動実行で再取得します。

**今後:** 新旧名称と独立サービス/機能の分類をさらに確認し、GA・リージョン・料金・プランについて、利用判断に必要な優先製品から検証。Cloudflareが更新できたら他4社も同じ方式を検討します。
