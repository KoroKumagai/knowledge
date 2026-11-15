# クラウドサービス整理

**基準日:** 2026-11-14（JST）  
**対象:** AWS / Azure / Google Cloud / Oracle Cloud Infrastructure / Cloudflare

## ディレクトリ

```text
cloud/
├── README.md
├── service-comparison.md   # 2社以上で用途を比較できるサービス
├── aws/
│   ├── README.md            # AWS公式カタログ監査概要
│   ├── catalog.md           # エンドポイント/クォータの全件台帳
│   ├── products.md          # AWS公式Products 237カードの全件
│   ├── products-source.json # 公式API応答を正規化した取得記録
│   ├── products-coverage.md # 237カードと269項目の相互差分
│   ├── products-mapping.json # 検証済み別名・関連別粒度の定義
│   ├── open-items.md       # 33カード/95参照項目の一次分類と提供条件の検証
│   ├── open-items-classification.json # 暫定分類のソースデータ
│   ├── availability-evidence.json  # 公式GA・リージョン・契約条件の個別根拠
│   ├── lifecycle.md         # Maintenance / Sunset / Full Shutdown
│   ├── lifecycle-unmatched.md  # 公式エンドポイントと未対応のライフサイクル項目
│   ├── lifecycle-mapping.json  # 手動確認した製品名と機能の対応表
│   ├── coverage.md          # 個別一覧と公式参照項目との照合
│   └── services.md          # AWS独自・個別扱い
├── azure/
│   └── services.md          # Azure独自・個別扱い
├── google/
│   └── services.md          # Google Cloud独自・個別扱い
├── oracle/
│   └── services.md          # OCI独自・個別扱い
├── cloudflare/
│   ├── README.md            # Cloudflareの監査概要
│   ├── catalog.md           # 公式Docs目録の全件スナップショット
│   ├── products.md          # 公式Productsとの照合表
│   ├── catalog-status.json  # 提供状況の検証日・根拠URL
│   └── services.md          # Cloudflare独自・個別扱い
└── oracle-cloud.md          # OCIの運用メモ（既存ファイル・変更なし）
```

## 分類基準

1. **横断比較:** 2社以上で同目的のサービスが実在し、選定の対象になる場合のみ [service-comparison.md](service-comparison.md) へ載せる。機能の一部のみの類似や、構成上の代替は同一行に押し込まない。
2. **各社別:** その会社特有の製品体系、別物の実行モデル、機能を組み合わせて初めて類似するものは各社一覧へ分離する。**独自一覧への掲載は他社に類似製品が皆無という意味ではない**。
3. **移動履歴:** 横断表へ移した製品を個別一覧の主表に重複させず、「横断比較へ移動した項目」に記録する。独立サービスでない機能や旧名称は「機能・旧名のため除外・統合した項目」に分け、理由を明記する。
4. **重複排除:** 同じサービスの重複掲載は原則避ける。比較可能なサービスは横断表を優先し、独自技術・機能の説明が不可欠な場合は個別表から横断表を参照する。
5. **現行掲載と利用可否は別:** 廃止済み・終了予定・プレビュー・リージョン限定は採用前に必ず確認。
6. **全件網羅の基準:** 公式製品/サービスカタログで掲載される粒度。サービス内の個別機能（例: Distributed Map、BigQuery ML）、個別API、料金SKU、リージョン、Marketplace出品商品は別の対象。今回の個別一覧は全件網羅を**完了していない**ため、空白を「サービスなし」と解釈しない。

## 一覧

| 区分 | ファイル | 備考 |
|---|---|---|
| 複数社比較 | [機能比較](service-comparison.md) | 比較可能な50項目 |
| AWS | [個別一覧](aws/services.md) | 採録候補22件 |
| Azure | [個別一覧](azure/services.md) | 採録候補16件 |
| Google Cloud | [個別一覧](google/services.md) | 採録候補15件 |
| OCI | [個別一覧](oracle/services.md) | 採録候補25件 |
| Cloudflare | [個別一覧](cloudflare/services.md) | 採録候補27件 |

## 公式カタログ網羅性の進捗

- **Cloudflare（公式Docs/Productsの掲載単位）:** [調査結果](cloudflare/README.md) に収録済み（公式Docs索引195件・公式Products68件）。提供状況の全件検証は未完了。
- **AWS（Products / General Reference）:** [調査結果](aws/README.md) に、Productsのservice区分237カード、General Reference269項目の全件スナップショットと差分を収録。**未対応33カード・95参照項目の一次分類済み**、GA・リージョン・契約条件は[根拠付き5項目から調査中](aws/open-items.md)。全件の提供可否の判断は未完了。
- **Azure / Google Cloud / OCI:** 現時点では公式カタログとの全件照合が未完了。
- 共通比較表・個別一覧の行数は全製品数ではありません。公式目録の採録件数と、実務上の機能比較件数を分けて管理します。

## 全製品の確認元

- AWS: [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html) / [全製品](https://aws.amazon.com/products/)
- Azure: [製品ディレクトリ](https://azure.microsoft.com/en-us/products/)
- Google Cloud: [Products at a glance](https://docs.cloud.google.com/docs/product-list)
- Oracle Cloud: [OCI Documentation - Services](https://docs.oracle.com/en-us/iaas/Content/)
- Cloudflare: [Docs directory](https://developers.cloudflare.com/directory/)

## 更新時の手順

1. 5社の公式カタログに対して一覧を突合し、未収録品、改称品、廃止済み品、終了予定品を確認。
2. 2社以上で同じ用途を比較できるサービスを横断表に置く。該当するサービスがない場合は「対象外」と明示し、複数サービスの組合せを単品の同等品として扱わない。
3. 「実行モデル」「ステートの扱い」「SQL・API互換性」「認証・権限」「リージョン・SLA」「価格」「IaC対応」を比較する。単純なサービス名の類似で結論を出さない。
4. 見直した日付と参照先を更新し、可能なら変更の根拠をコミットまたはPRに記載する。

> 全サービスの完全なGA/終了ステータス検証は別途必要。Cloudflareの公式目録については195件の監査スナップショットを作成しましたが、上記の個別一覧件数は各社の総サービス数ではありません。

## 更新時の確認事項（TODO）

- 各社の公式カタログとの全件照合は未完了。網羅率を保証しない。
- 2026-11時点のプレビュー・リージョン・終了予定を製品単位で再確認する。
- 具体的な導入検討時は類似製品の機能範囲・契約条件の差を公式仕様で確認する。
