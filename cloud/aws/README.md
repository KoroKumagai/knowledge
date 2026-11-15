# AWS公式サービス目録の監査

**取得日:** 2026-11-14

Cloudflareで採用した「全件の公式目録」と「編集された独自・横断比較」を分ける方針をAWSにも適用。

| ファイル | 役割 |
|---|---|
| [products.md](products.md) | 公式Products検索のサービス区分 **237カード** を全件収録（2026-11-14 UTC、32カテゴリ） |
| [products-source.json](products-source.json) | 公式サイト内部の検索エンドポイントの totalHits・取得日・製品ID・掲載名・URL・カテゴリの取得記録 |
| [products-coverage.md](products-coverage.md) | Products **237カード** とGeneral Reference **269項目**を相互照合。未対応を残す |
| [open-items.md](open-items.md) | **未対応33カードと95参照項目**の暫定分類、GA・東京/大阪リージョン・契約条件の検証台帳（**公式根拠付き個別確認5件**） |
| [open-items-classification.json](open-items-classification.json) | 対応未確定128項目の原票ID付き分類データ（独立サービス／機能／開発ツール／旧製品など） |
| [availability-evidence.json](availability-evidence.json) | 公式根拠に基づくGA・リージョン・契約条件の確認記録と未確認の区別 |
| [products-mapping.json](products-mapping.json) | 同一名称でない場合の手動確認済み別名／非同等の製品群・機能の分類 |
| [catalog.md](catalog.md) | General Referenceの **269件**（サービスエンドポイント/クォータ一覧）の全件採録 |
| [lifecycle.md](lifecycle.md) | Maintenance **56件**、Sunset **16件**、Full Shutdown **62件** の公式表を全件採録 |
| [lifecycle-unmatched.md](lifecycle-unmatched.md) | 未対応 **74 / 134件** の明示的な照合残と一次資料。マッピングは [lifecycle-mapping.json](lifecycle-mapping.json) で管理 |
| [coverage.md](coverage.md) | 既存[個別一覧](services.md)22件と公式参照名の突合。移動済みの項目は[横断表](../service-comparison.md)で管理 |
| [services.md](services.md) | AWS独自・個別扱いの人手で編集した一覧（全製品カタログとは別） |

## スコープの境界

- **全件の範囲はGeneral Reference「Service endpoints and quotas」ページのServices節です。**
- **公式Productsのserviceタグ付きカード237件**も収録済み。Productsページが使用する**非公開・仕様保証のない検索エンドポイント**から取得し、`totalHits`と取得件数の一致を検証しています。ただしAWS公式の全機能・全SKU・Marketplace製品・全GAサービスの総数ではありません。
- 製品のサブ機能・API・マーケットプレイス商品・リージョン・SKUと、エンドポイント・クォータの掲載項目は同じ粒度ではありません。
- AWSのライフサイクル表は**サービスと機能の両方**を含みます。終了日を過ぎたSunset掲載項目も、正式なFull Shutdown掲載がなければ推測で改分類しません。
- ライフサイクルの個別機能を本体に結び付ける際は、明示的な別名/完全一致/境界付き接頭辞のみを使います。未照合は別表で可視化し、製品本体の新規提供を保証しません。
- Products台帳ではサービス本体の状態と、**製品が利用する関連サービスの状態**を区別します。関連サービスはMaintenance／Sunset／Full Shutdownの各段階を表示できますが、関連サービスの終了が製品本体の終了を意味するわけではありません。明示的な別名は `lifecycle_aliases`、関連・依存関係は `lifecycle_related` で管理します。
- 出典に掲載されていないサービスや、新しい製品名への移行があっても、そのサービスが存在しないとは判断できません。

## 公式ProductsとGeneral Referenceの差分（2026-11-14 UTC）

- AWS Products：**237カード**。同名でもIDが異なるカードがあります（AWS DevOps Agent、Amazon SageMaker AIが各2枚）。
- General Reference：**269参照項目**。両者は同じ単位ではなく、マーケティング製品の一部はエンドポイントとして独立していません。
- 突合：[products-coverage.md](products-coverage.md) に**同名75件、確認済み別名101件、関連・別粒度28件、目録外・未対応33件**を記録。269項目側の未対応は95件。
- AWS公式Productsに残る旧名称「AWS Personal Health Dashboard」は、2022年の[AWS Health Dashboardへの改称](https://docs.aws.amazon.com/health/latest/ug/doc-history.html)に基づきGeneral ReferenceのAWS Healthへ対応。
- Amazon DocumentDBの製品名に含まれる `compatability` は公式掲載の誤字をそのまま収録（原文ママ）。
- AWS公式のマーケティング分類（badge）をそのまま採録。分類名に不自然なものがあっても独自の推測で書き換えません。
- AWS公式サイト内部の検索エンドポイントには [Kiro](https://kiro.dev/) のような外部ドメインの製品ページも登録されています。ドメインだけで除外せず、発見元の公式データと製品IDを保持します。
- **Productsへの掲載は新規利用可能・GAの証明ではありません。** 停止品の採用判断は[lifecycle.md](lifecycle.md)と個別の公式発表を確認します。
- [products-coverage.md](products-coverage.md) は**Maintenance・Sunset・Full Shutdownを、General Referenceとの照合状況に関係なく表示**します。照合済みと提供中を混同せず、関連サービスの終了を製品本体の終了と混同しないようにしています。
- [products.md](products.md)ではライフサイクルの列を追加し、**サービス本体に完全一致（または明示的別名）したMaintenance・Sunset・Full Shutdown**を表示。SageMakerなどの一部機能の終了を、親サービス全体の終了とは扱いません。
- **QLDBの正式名称差**も手動別名で照合。[AWS Full Shutdown一覧](https://docs.aws.amazon.com/general/latest/gr/full_shutdown_services.html)に掲載されています。

## 現行名称の注意（2026-11時点）

- **AWS Quick** は2026-11-09に旧Amazon Quickから改称。AWS Quick SightはそのBI機能。既存QuickSight APIと概念上別のため、公式参照表の名称を強制的に置換しません。
  [公式告知](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-quick-aws-quick/)
- **Amazon Pinpoint** は2026-10-30にサポート終了。
  [AWS公式](https://docs.aws.amazon.com/pinpoint/latest/userguide/migrate.html)
- **AWS App Mesh / AWS Proton / AWS WAF Classic** は2026年にサポート終了した製品。公式目録に残っていても新規採用を推奨しません。
  [AWS公式ライフサイクル](https://docs.aws.amazon.com/general/latest/gr/full_shutdown_services.html)

## 公式名称と公式サイトの更新差

- **AWS Quick**：公式発表のとおり2026-11-09に改称。Products APIでは「AWS Quick」が掲載される一方、「Amazon QuickSight」の旧表示名が残っています。これは [AWS Quick Sight](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-quick-aws-quick/) との**確認済み別名**としてマッピングしています。マーケティング表示を黙って書き換えていません。
- **AWS App Mesh**：Products APIには掲載されますが、ライフサイクルではFull Shutdown。GA/契約可能性をAPI掲載だけで判断してはいけません。
- **Amazon WorkSpaces Thin Client**：AWS公式Sunsetでは「Amazon WorkSpaces – Thin Client」と掲載。名前の差を明示的に対応付け、**2027-03-31終了予定**として表示します。
- **AWS IoT Button**：関連する**AWS IoT 1-Click**は2025-01-29にFull Shutdownですが、IoT Button本体の終了とは区別します。
- **Amazon QLDB**：General Referenceの対応先未確定でも、公式Full Shutdown（2025-07-31）は[products-coverage.md](products-coverage.md)に注記します。

## 更新手順

### Productsの製品カードと差分表

- `python scripts/refresh_aws_marketing_products.py`：AWS公式Productsページで使われる**内部検索エンドポイント（非公開・仕様保証なし）**の `service` 区分全件を取得。形式・件数・IDが一致しなければ失敗させ、取得不完全なデータを正常扱いしない。
- `python scripts/check_aws_marketing_products.py`：公式取得記録、各製品のライフサイクル、General Reference差分、対応定義、README件数を検証。
- GitHub Actions **Propose AWS marketing Products refresh**：手動実行で取得・検証し、結果をレビュー用PRにする。mainへの直接push・自動マージなし。
- `GITHUB_TOKEN`によるPR作成では別のPR CIが自動起動しないため、**PR作成前に全チェックを実行**。リポジトリのPR作成権限が必要。Workflowの手動起動～PR生成までのE2Eテストは未実施。

### General Reference・ライフサイクル

- `python -m pip install beautifulsoup4`：AWS General Reference HTML解析用の依存ライブラリ。
- `python scripts/refresh_aws_service_catalog.py`：エンドポイント・クォータとライフサイクルのAWS公式4ページを取得し、既存台帳を再生成。
- `python scripts/check_aws_service_catalog.py`：公式参照269項目、Maintenance・Sunset・Full Shutdown、未対応台帳と個別一覧との整合性を検証。
- GitHub Actions **Propose AWS official service catalog refresh**：手動実行でレビュー用PRを提案。提供状態や構造が変わった場合には公式根拠をレビューし、無条件に提供中とみなさない。

## 未対応項目の一次分類と提供条件調査（2026-11-15）

- [open-items.md](open-items.md)に**Products側33カード、General Reference側95参照項目をすべて一次分類**。既存の237/269件や分類75/101/28/33は変更していません。
- **一次分類は仮説**です。原票の名称・機能説明・公式エンドポイント参照を根拠にした作業上の分類であり、GA・独立サービス・契約可能性の確定ではありません。
- GA・東京/大阪の提供・契約条件の**個別確認は5項目から着手**。Aurora DSQL、Amazon Q Business、Service Quotas、Support API、WAF Classicの公式根拠を[別データ](availability-evidence.json)で管理しています。全128件の検証完了を主張しません。
- 各リージョンでのAWS公式データは[AWS Capabilities by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/)が優先参照先です。公式の[S3公開データ取得](https://aws.amazon.com/blogs/storage/building-automated-aws-regional-availability-checks-with-amazon-s3/)にはAWS認証・IAM権限が必要なため、このPRでは一括取得は実施していません。
- `python scripts/render_aws_open_items.py --write`で台帳再生成、`--check`で元データ・検証根拠・Markdownの全件整合性をチェックします。

## 公式Products照合の残課題

- 未対応33カード／General Reference側95項目は**一次分類済み・完全照合は継続中**。分類は[監査台帳](open-items.md)から確認し、独立製品・旧称・機能の差は公式根拠で確定します。**対応先未確定とAWS製品の不存在・利用不可は同義ではありません。**
- 掲載製品すべてのGA、プレビュー、提供リージョン、契約条件、価格を一件ずつ検証したわけではありません。
- 公式Productsが今後改称・増減した場合は取得データを差分レビューし、[明示的な対応マップ](products-mapping.json)と根拠を更新してください。

## 次の段階

- **公式Productsのservice区分237カードとGeneral Reference269項目との全件取得・差分化は完了。** 未対応33カードおよびGeneral Reference側95項目について、製品群・独立サービス・旧製品の単位を追加確認する。
- 公式参照項目のうち独立サービス・機能・旧製品を区別し、横断表と個別一覧の分類漏れをなくす。
- 主要サービスの地域、GA、価格、契約条件を別途確認する。
