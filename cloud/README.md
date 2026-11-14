# クラウドサービス整理

**基準日:** 2026-11-14（JST）  
**対象:** AWS / Azure / Google Cloud / Oracle Cloud Infrastructure / Cloudflare

## ディレクトリ

```text
cloud/
├── README.md
├── service-comparison.md   # 5社で共通の用途を比較できるサービスのみ
├── aws/
│   └── services.md          # AWS独自・個別扱い
├── azure/
│   └── services.md          # Azure独自・個別扱い
├── google/
│   └── services.md          # Google Cloud独自・個別扱い
├── oracle/
│   └── services.md          # OCI独自・個別扱い
├── cloudflare/
│   └── services.md          # Cloudflare独自・個別扱い
└── oracle-cloud.md          # 既存のOCIメモ（変更なし）
```

## 分類基準

1. **横断比較:** 同じ目的のマネージドサービスや実行環境として、各社で直接選択肢に挙げられる場合のみ [service-comparison.md](service-comparison.md) へ載せる。機能の一部のみの類似や、構成上の代替は同一行に押し込まない。
2. **各社別:** その会社特有の製品体系、別物の実行モデル、機能を組み合わせて初めて類似するものは各社一覧へ分離する。**独自一覧への掲載は他社に類似製品が皆無という意味ではない**。
3. **1サービス1種類とは限らない:** 同じサービスが横断比較と各社別の両方に載る場合は、横断では機能軸、各社別ではベンダー固有の機能・設計制約を扱う。
4. **現行掲載と利用可否は別:** 廃止済み・終了予定・プレビュー・リージョン限定は採用前に必ず確認。
5. **全件網羅の基準:** 公式製品/サービスカタログで掲載される粒度。個別API、料金SKU、リージョン、Marketplace出品商品は別の対象。今回の個別一覧は全件網羅を**完了していない**ため、空白を「サービスなし」と解釈しない。

## 一覧

| 区分 | ファイル | 備考 |
|---|---|---|
| 5社横断 | [機能比較](service-comparison.md) | 直接比較可能な39項目 |
| AWS | [個別一覧](aws/services.md) | 独自・個別扱い候補30件 |
| Azure | [個別一覧](azure/services.md) | 独自・個別扱い候補29件 |
| Google Cloud | [個別一覧](google/services.md) | 独自・個別扱い候補29件 |
| OCI | [個別一覧](oracle/services.md) | 独自・個別扱い候補29件 |
| Cloudflare | [個別一覧](cloudflare/services.md) | 独自・個別扱い候補43件 |

## 全製品の確認元

- AWS: [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html) / [全製品](https://aws.amazon.com/products/)
- Azure: [製品ディレクトリ](https://azure.microsoft.com/en-us/products/)
- Google Cloud: [Products at a glance](https://docs.cloud.google.com/docs/product-list)
- Oracle Cloud: [OCI Documentation - Services](https://docs.oracle.com/en-us/iaas/Content/)
- Cloudflare: [Docs directory](https://developers.cloudflare.com/directory/)

## 更新時の手順

1. 5社の公式カタログに対して一覧を突合し、未収録品、改称品、廃止済み品、終了予定品を確認。
2. 同じ役割の5社製品として意味のある対応だけを横断表へ残す。対応先がない製品を「—」の列で水増しせず、各社ディレクトリに記録。
3. 「実行モデル」「ステートの扱い」「SQL・API互換性」「認証・権限」「リージョン・SLA」「価格」「IaC対応」を比較する。単純なサービス名の類似で結論を出さない。
4. 見直した日付と参照先を更新し、可能なら変更の根拠をコミットまたはPRに記載する。

> 全サービスカタログとの自動突合、完全なGA/終了ステータスの検証は別途必要。上記件数は今回の**採録件数**であり、各社の総サービス数ではない。
