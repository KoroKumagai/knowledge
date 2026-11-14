# AWS公式サービス目録の監査

**取得日:** 2026-11-14

Cloudflareで採用した「全件の公式目録」と「編集された独自・横断比較」を分ける方針をAWSにも適用。

| ファイル | 役割 |
|---|---|
| [catalog.md](catalog.md) | General Referenceの **269件**（サービスエンドポイント/クォータ一覧）の全件採録 |
| [lifecycle.md](lifecycle.md) | Maintenance **56件**、Sunset **16件**、Full Shutdown **62件** の公式表を全件採録 |
| [lifecycle-unmatched.md](lifecycle-unmatched.md) | 未対応 **74 / 134件** の明示的な照合残と一次資料。マッピングは [lifecycle-mapping.json](lifecycle-mapping.json) で管理 |
| [coverage.md](coverage.md) | 既存[個別一覧](services.md)22件と公式参照名の突合。移動済みの項目は[横断表](../service-comparison.md)で管理 |
| [services.md](services.md) | AWS独自・個別扱いの人手で編集した一覧（全製品カタログとは別） |

## スコープの境界

- **全件の範囲はGeneral Reference「Service endpoints and quotas」ページのServices節です。**
- 公式の[マーケティング用製品ページ](https://aws.amazon.com/products/)は検索と絞り込みで掲載内容が変わるため、そこにある全製品の収録を確認したものではありません。
- 製品のサブ機能・API・マーケットプレイス商品・リージョン・SKUと、エンドポイント・クォータの掲載項目は同じ粒度ではありません。
- AWSのライフサイクル表は**サービスと機能の両方**を含みます。終了日を過ぎたSunset掲載項目も、正式なFull Shutdown掲載がなければ推測で改分類しません。
- ライフサイクルの個別機能を本体に結び付ける際は、明示的な別名/完全一致/境界付き接頭辞のみを使います。未照合は別表で可視化し、製品本体の新規提供を保証しません。
- 出典に掲載されていないサービスや、新しい製品名への移行があっても、そのサービスが存在しないとは判断できません。

## 現行名称の注意（2026-11時点）

- **AWS Quick** は2026-11-09に旧Amazon Quickから改称。AWS Quick SightはそのBI機能。既存QuickSight APIと概念上別のため、公式参照表の名称を強制的に置換しません。
  [公式告知](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-quick-aws-quick/)
- **Amazon Pinpoint** は2026-10-30にサポート終了。
  [AWS公式](https://docs.aws.amazon.com/pinpoint/latest/userguide/migrate.html)
- **AWS App Mesh / AWS Proton / AWS WAF Classic** は2026年にサポート終了した製品。公式目録に残っていても新規採用を推奨しません。
  [AWS公式ライフサイクル](https://docs.aws.amazon.com/general/latest/gr/full_shutdown_services.html)

## 更新手順

- `python -m pip install beautifulsoup4` で依存ライブラリを導入。
- `python scripts/refresh_aws_service_catalog.py` で4つのAWS公式参照ページを読み、未照合一覧を含む5つのMarkdownを再生成。
- `python scripts/check_aws_service_catalog.py` で件数・重複・ライフサイクル参照・22件対応表を検証。
- 生成結果は**必ずレビュー用PR**で確認。公式ページのレイアウトが変わった場合は最低件数・必須サービス名の検査で失敗させます。

## 次の段階

- マーケティング用AWS Productsの全件を別ソースで取得し、サービスエンドポイント目録と差集合を作る。
- 公式参照項目のうち独立サービス・機能・旧製品を区別し、横断表と個別一覧の分類漏れをなくす。
- 主要サービスの地域、GA、価格、契約条件を別途確認する。
