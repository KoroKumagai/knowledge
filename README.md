# Knowledge Base

このリポジトリは、個人の学習・検討ログや技術ナレッジを整理したものです。  
あくまで自分用の整理ですが、他の方の参考になれば幸いです。

## ディレクトリ構成
- **profile/**  
  個人の名前表記やポートフォリオ関連の整理
- **projects/**  
  OpenProjectなど、自分で構築・検証したプロジェクトのメモ
- **process/**  
  開発プロセス管理、ブランチ戦略、環境設計に関する知識整理
- **cs/**  
  カスタマーサクセスの戦略（KPI・ライフサイクル・セグメンテーション等）と方法論（オンボーディング・定着・拡大等）
- **cloud/**  
  AWS / Azure / Google Cloud / OCI / Cloudflare のサービス整理。横断比較と各社別の一覧に加え、AWS・Cloudflareは公式カタログとの全件照合と提供状況の確認記録を収録（概要は [cloud/README.md](cloud/README.md)）
- **scripts/**  
  `cloud/` の台帳を生成・検証するPythonスクリプト
- **.github/workflows/**  
  `cloud/` の整合性チェック（CI）と、公式カタログを取得してレビュー用PRを作る手動実行のWorkflow

## 掲載内容の扱い
- `cloud/` の一覧は、基準日・取得日時点の公式情報に基づく整理です。公式カタログへの掲載は、GA・新規利用可能・特定リージョンでの提供を意味しません。採用前に公式情報を確認してください。
- 確認できていない項目は「未確認」と明記しています。

## コントリビューション・AIエージェント向けガイド
作業ルール（執筆ルール、`cloud/` の編集ルール、検証コマンド、レビュー方針）は [AGENTS.md](AGENTS.md) にまとめています。Claude Code は [CLAUDE.md](CLAUDE.md) から同じ内容を読み込みます。

## コミットメッセージ規約
このリポジトリでは [Conventional Commits](https://www.conventionalcommits.org/ja/v1.0.0/) に準拠したコミットメッセージを推奨しています。対象が明確な場合はスコープを付けます（例: `docs(aws):`、`docs(cloudflare):`、`ci(aws):`）。

### 主に利用するタイプ
- **docs:** ドキュメントの追加・更新（例: 記事追加、誤字修正）
- **fix:** 内容・データ・スクリプトの誤りの修正（ドキュメントのみなら `fix(docs):`）
- **feat:** 新しい記事やナレッジの追加
- **refactor:** 動作や内容を変えないスクリプト・データ構造の整理
- **test:** 検証スクリプト・テストの追加や修正
- **ci:** GitHub Actions の設定変更
- **build:** 生成・取得用スクリプトや依存関係の変更
- **chore(repo):** リポジトリの構成変更、ファイル整理

### メッセージ例
* docs: add note on Oracle Cloud region selection  
* fix(docs): update broken links after file rename  
* chore(repo): restructure directories and rename files to kebab-case  
* feat: add environments and branch strategy article
* docs(aws): 旧Glacierの対応根拠を公式直接資料に整理

## ライセンス
このリポジトリの内容は **CC BY 4.0** で公開しています。  
利用の際は以下のクレジットを表示してください:

> © 2025 Koro Kumagai, licensed under CC BY 4.0
