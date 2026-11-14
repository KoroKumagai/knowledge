# AWS公式サービス目録の監査

**取得日:** 2026-11-14

Cloudflareで採用した「全件の公式目録」と「編集された独自・横断比較」を分ける方針をAWSにも適用。

| ファイル | 役割 |
|---|---|
| [products.md](products.md) | 公式Products検索のサービス区分 **237カード** を全件収録（2026-11-14 UTC、32カテゴリ） |
| [products-source.json](products-source.json) | 公式APIの totalHits・取得日・製品ID・掲載名・URL・カテゴリの取得記録 |
| [products-coverage.md](products-coverage.md) | Products **237カード** とGeneral Reference **269項目**を相互照合。未対応を残す |
| [products-mapping.json](products-mapping.json) | 同一名称でない場合の手動確認済み別名／非同等の製品群・機能の分類 |
| [catalog.md](catalog.md) | General Referenceの **269件**（サービスエンドポイント/クォータ一覧）の全件採録 |
| [lifecycle.md](lifecycle.md) | Maintenance **56件**、Sunset **16件**、Full Shutdown **62件** の公式表を全件採録 |
| [lifecycle-unmatched.md](lifecycle-unmatched.md) | 未対応 **74 / 134件** の明示的な照合残と一次資料。マッピングは [lifecycle-mapping.json](lifecycle-mapping.json) で管理 |
| [coverage.md](coverage.md) | 既存[個別一覧](services.md)22件と公式参照名の突合。移動済みの項目は[横断表](../service-comparison.md)で管理 |
| [services.md](services.md) | AWS独自・個別扱いの人手で編集した一覧（全製品カタログとは別） |

## スコープの境界

- **全件の範囲はGeneral Reference「Service endpoints and quotas」ページのServices節です。**
- **公式Productsのserviceタグ付きカード237件**も収録済み。AWS公式検索APIの totalHits と実取得件数の一致を確認しています。ただしAWS公式の全機能・全SKU・Marketplace製品・全GAサービスの総数ではありません。
- 製品のサブ機能・API・マーケットプレイス商品・リージョン・SKUと、エンドポイント・クォータの掲載項目は同じ粒度ではありません。
- AWSのライフサイクル表は**サービスと機能の両方**を含みます。終了日を過ぎたSunset掲載項目も、正式なFull Shutdown掲載がなければ推測で改分類しません。
- ライフサイクルの個別機能を本体に結び付ける際は、明示的な別名/完全一致/境界付き接頭辞のみを使います。未照合は別表で可視化し、製品本体の新規提供を保証しません。
- 出典に掲載されていないサービスや、新しい製品名への移行があっても、そのサービスが存在しないとは判断できません。

## 公式ProductsとGeneral Referenceの差分（2026-11-14 UTC）

- AWS Products：**237カード**。同名でもIDが異なるカードがあります（AWS DevOps Agent、Amazon SageMaker AIが各2枚）。
- General Reference：**269参照項目**。両者は同じ単位ではなく、マーケティング製品の一部はエンドポイントとして独立していません。
- 突合：[products-coverage.md](products-coverage.md) に**同名75件、確認済み別名100件、関連・別粒度22件、目録外・未対応40件**を記録。269項目側の未対応は95件。
- AWS公式のマーケティング分類（badge）をそのまま採録。分類名に不自然なものがあっても独自の推測で書き換えません。
- AWS公式APIには [Kiro](https://kiro.dev/) のような外部ドメインの製品ページも登録されています。ドメインだけで除外せず、発見元の公式データと製品IDを保持します。
- **Productsへの掲載は新規利用可能・GAの証明ではありません。** 停止品の採用判断は[lifecycle.md](lifecycle.md)と個別の公式発表を確認します。

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

## 更新手順

- `python scripts/refresh_aws_marketing_products.py` でAWS公式Productsのservice区分カードを再取得し、差分表を再生成（標準ライブラリのみ）。
- `python scripts/check_aws_marketing_products.py` でAPI全件・ID・分類・269参照項目との差分・マッピングを検証。
- `python -m pip install beautifulsoup4` で従来のGeneral Reference解析用ライブラリを導入。
- `python scripts/refresh_aws_service_catalog.py` で4つのAWS公式参照ページを読み、未照合一覧を含む5つのMarkdownを再生成。
- `python scripts/check_aws_service_catalog.py` で件数・重複・ライフサイクル参照・22件対応表を検証。
- 生成結果は**必ずレビュー用PR**で確認。公式ページのレイアウトが変わった場合は最低件数・必須サービス名の検査で失敗させます。

## 次の段階

- **公式Productsのservice区分237カードとGeneral Reference269項目との全件取得・差分化は完了。** 未対応40カードおよびGeneral Reference側95項目について、製品群・独立サービス・旧製品の単位を追加確認する。
- 公式参照項目のうち独立サービス・機能・旧製品を区別し、横断表と個別一覧の分類漏れをなくす。
- 主要サービスの地域、GA、価格、契約条件を別途確認する。
