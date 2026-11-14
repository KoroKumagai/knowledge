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

**検証済み提供段階の保守:** [`catalog-status.json`](catalog-status.json) は一次資料URLと確認日を手動保守するデータです。Docs索引の再生成ではGA/ベータの判定を自動更新しません。確認日が古くなった項目は個別再確認が必要です。

**掲載区分:** [products.md](products.md)では同名／改称／表記ゆれ／機能・製品群を分けています。機能の対応付けは同じ独立製品があることの証明ではありません。

## 提供状況・改称履歴の参照先

2026年の重要な変更と確認済みの提供段階は、[catalog.md の「提供状況・改称の確認履歴」](catalog.md) と [catalog-status.json](catalog-status.json) に一元化しています。READMEでは重複掲載せず、根拠URLと検証日を含む元データを更新してください。

## 更新・チェック

- `python scripts/refresh_cloudflare_directory.py`: 公式GitHubの新しい固定コミットから `catalog.md` と `products.md` のソースSHAを同期し、READMEのDocs件数も更新。標準ライブラリのみで実行できます。
- `python scripts/check_cloudflare_catalog.py`: Docs / Productsのコミット一致、Productsが参照する全YAMLの存在、個別一覧の名称、分類、件数を検査。
- `Propose Cloudflare docs directory refresh` を手動起動すると、カタログ再生成と2本の整合性テストを実施して**レビュー用PRを作成**します。`main`には直接pushしません。`GITHUB_TOKEN` が作成したPRはGitHubの通常のPRチェックを自動起動しないため、**PR作成前のWorkflow内テストを必須**にしています。リポジトリのActions設定で「Allow GitHub Actions to create and approve pull requests」の有効化が必要です。

**今後:** 新旧名称と独立サービス/機能の分類をさらに確認し、GA・リージョン・料金・プランについて、利用判断に必要な優先製品から検証。Cloudflareが更新できたら他4社も同じ方式を検討します。
