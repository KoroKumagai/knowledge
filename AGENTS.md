# AGENTS.md

このファイルは、本リポジトリで作業するAIコーディングエージェント（Claude Code、Codex など）向けの共通ガイドです。人間向けの概要は [README.md](README.md) を参照してください。

## リポジトリの概要

個人の学習・検討ログと技術ナレッジを Markdown で整理したナレッジベースです。アプリケーションのビルドはありません。主な成果物は日本語の Markdown 文書で、`cloud/` 配下のみ公式カタログ監査用の JSON データ・Python スクリプト・GitHub Actions による整合性検証があります。

| ディレクトリ | 内容 |
|---|---|
| `profile/` | 名前表記・ポートフォリオ関連 |
| `projects/` | 自分で構築・検証したプロジェクトのメモ（OpenProject など） |
| `process/` | 開発プロセス・ブランチ戦略・環境設計 |
| `cs/` | カスタマーサクセス（戦略・方法論・参考文献） |
| `cloud/` | AWS / Azure / Google Cloud / OCI / Cloudflare のサービス整理と公式カタログ監査 |
| `scripts/` | `cloud/` の台帳生成・検証スクリプト（Python） |
| `.github/workflows/` | 整合性CIと、手動実行の公式カタログ更新提案Workflow |

## 執筆ルール

- **言語:** 本文は日本語。製品名・API名・公式表記は原文のまま（公式の誤字も「原文ママ」として保持し、勝手に直さない）。
- **ファイル名:** kebab-case の英小文字（例: `environments-and-branch-strategy.md`）。
- **日付:** 基準日・取得日・検証日を明記する（例: `**基準日:** 2026-11-14（JST）`）。時点依存の情報には必ず日付と出典URLを添える。
- **出典:** 事実の主張は一次資料（公式ドキュメント・公式発表）へのリンクで裏付ける。推測で提供状況（GA・Preview・終了など）を書かない。未確認のものは「未確認」と明示する。
- **リンク:** リポジトリ内のリンクは相対パス。ファイルを移動・改名したらリンク切れを直す。
- 既存の文体・表形式・見出し構成に合わせる。新しいディレクトリを作ったら [README.md](README.md) のディレクトリ構成も更新する。

## `cloud/` の編集ルール

`cloud/` は件数・相互参照・生成物がスクリプトで検証されています。編集前に [cloud/README.md](cloud/README.md) の「分類基準」と、AWS は [cloud/aws/README.md](cloud/aws/README.md)・[cloud/aws/availability-policy.md](cloud/aws/availability-policy.md)、Cloudflare は [cloud/cloudflare/README.md](cloud/cloudflare/README.md) を読むこと。

- **横断比較と各社別の区別:** 2社以上で同目的のサービスが実在する場合のみ `service-comparison.md` に載せる。各社独自のものは `<provider>/services.md`。横断表へ移した製品は個別表の主表に重複させず「横断比較へ移動した項目」に記録する。
- **掲載と利用可否は別:** 公式カタログに載っていることを GA・新規利用可能の根拠にしない。ライフサイクル（Maintenance / Sunset / Full Shutdown）は公式表に基づき、推測で再分類しない。子機能の終了を親サービスの終了として扱わない。
- **生成物を手で編集しない:** 以下はスクリプトが生成する。元データ（JSON）またはスクリプトを直し、再生成すること。
  - `cloud/aws/catalog.md`, `lifecycle.md`, `lifecycle-unmatched.md`, `coverage.md` … `scripts/refresh_aws_service_catalog.py`（ネットワーク取得・`beautifulsoup4` が必要）
  - `cloud/aws/products.md`, `products-coverage.md`, `products-source.json` … `scripts/refresh_aws_marketing_products.py`
  - `cloud/aws/open-items.md` … `python scripts/render_aws_open_items.py --write`（元: `open-items-classification.json`, `availability-evidence.json`）
  - `cloud/aws/availability-decisions.md` … `python scripts/check_aws_audit_decisions.py --write`（元: `availability-decisions.json`）
  - `cloud/cloudflare/catalog.md` … `scripts/refresh_cloudflare_directory.py`（提供段階は `catalog-status.json` を手動保守）
  - 上記の refresh スクリプトは `cloud/README.md` や各社 `README.md` の件数も書き換える。
- **手動保守のファイル:** `cloud/cloudflare/products.md` の製品行・対応付け・分類は手動で保守する（再生成用のJSONはない）。製品の追加・改称時はこの表を直接編集する。ただし `refresh_cloudflare_directory.py` が `**Docs照合元コミット:**` と Docs エントリ件数を書き換え、参照中の YAML が upstream から削除されていないか検証するため、これらの記載形式は崩さないこと。
- **手動対応表:** 名称の別名・対応付けは `products-mapping.json` / `lifecycle-mapping.json` に根拠付きで追加する。曖昧一致で済ませない。
- 件数（例: 237カード、269項目）を本文に書く場合は、検証スクリプトが照合する箇所と一致させる。

## 検証コマンド

`cloud/` または `scripts/` を変更したら、コミット前に CI（`.github/workflows/cloud-doc-consistency.yml`）と同じ検証を実行し、すべて通ることを確認する。標準ライブラリのみで動作し、ネットワーク不要です（Python 3.12 以上）。

```bash
python -m py_compile scripts/*.py
python scripts/check_cloud_consistency.py
python scripts/check_cloudflare_catalog.py
python scripts/check_aws_service_catalog.py
python scripts/check_aws_marketing_products.py
python scripts/render_aws_open_items.py --check
python scripts/check_aws_audit_decisions.py --self-test-retirement
python scripts/check_aws_audit_decisions.py --check
python scripts/check_aws_audit_decisions.py --as-of 2027-06-01 --quiet-warnings
python scripts/probe_aws_ssm_regions.py --self-test
```

- 検証から180日を超えた根拠は WARN になる（CI は失敗しない）。WARN を消すために検証日だけを更新しない。再確認した場合のみ日付と出典を更新する。
- `cloud/` 以外の Markdown のみの変更には自動検証はない。リンクと表の崩れを目視確認する。

## GitHub Actions

- `cloud-doc-consistency.yml`: `cloud/**`・`scripts/**` 関連の push / PR で検証を実行。
- `refresh-*.yml`: 手動実行（`workflow_dispatch`）で公式カタログを取得し、検証後にレビュー用 PR を作成する。main への直接 push・自動マージはしない。
- `probe-aws-ssm-regions.yml`: 読み取り専用 OIDC による SSM 公開パラメータの試験（手動実行）。権限（`permissions`）を広げない。
- 新しい検証スクリプトを追加したら、`cloud-doc-consistency.yml` の `paths` と実行ステップにも追加する。

## コミット・PR

- [Conventional Commits](https://www.conventionalcommits.org/ja/v1.0.0/) に従う。主なタイプ: `docs:`, `fix(docs):`, `feat:`, `chore(repo):`, `ci:`, `test:`, `build:`。対象が明確ならスコープを付ける（例: `docs(aws):`, `docs(cloudflare):`, `ci(aws):`）。
- コミットメッセージ・PR本文は日本語・英語どちらでもよい。変更の根拠（公式出典URL・検証日）を記載する。
- 関連 Issue があれば PR で参照する（例: AWS監査は #11 系）。
- `.obsidian/` は `.gitignore` 対象。コミットしない。

## ライセンス

内容は CC BY 4.0（[LICENSE](LICENSE)）。外部資料を引用する場合は出典を明記し、大量の転載（料金表のコピーなど）は避けてリンクで示す。
