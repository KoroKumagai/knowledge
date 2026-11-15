# AWS未対応128項目：判定規約とSSMリージョン取得PoC

## 適用範囲

[親Issue #11](https://github.com/KoroKumagai/knowledge/issues/11) の完了とは、「128件すべてがGAである」ではなく、**各次元で確認済み／公式記載なし／対象外／未確認を判定し、未確認を残作業として明示すること**です。

判定原票は [availability-decisions.json](availability-decisions.json)、確認事実は [availability-evidence.json](availability-evidence.json)、再生成結果は [availability-decisions.md](availability-decisions.md)。

- **確認済み**：公式一次資料が条件を明示（受付停止も確認済み）。根拠URL・検証日・適用範囲を必須
- **公式記載なし**：照会したAWS公式資料の範囲を記録し「不提供」にはしない。根拠を伴う
- **対象外（ツール）**：CLI、SDK、Corretto、Kiro等にはクラウドリージョンの概念がない
- **対象外（グローバル）**：公式資料でグローバルと確認した製品に限る。リージョン固有のAPI例外は分離する
- **対象外（物理端末）**：東京/大阪のAWSリージョンではなく製品の販売国・対象ユーザーを確認する
- **対象外（終了済み）**：Full Shutdown公式台帳のサービス本体のみ。機能単位の終了を親へ伝播しない
- **未確認**：未調査・認証待ち・資料矛盾など。**利用不可という意味ではない**

対象の7次元：提供段階、東京、大阪、新規顧客受付、必要サポートプラン、事前契約／コミットメント、購入経路制限。

**Preview**は、AWS公式製品ページのPreview記載、What's NewでのPreview告知、または公式開発者ガイドのPreviewバナーで判定。対象の機能／地域／版と日時を明記します。ライフサイクルの3表にないことだけではPreviewを否定しません。

料金の単価や月額はコピーペーストせず、[availability-evidence.json](availability-evidence.json)の`pricing_url`へリンク。Kinesisの**最低従量課金**と商用契約上の**事前コミットメント**は別の概念です。

## 再確認の期限

判定済み項目の`verified_on`（YYYY-MM-DD）から**180日超**で`scripts/check_aws_audit_decisions.py`がWARN。最初は**CIを落とさず**レビューの再確認対象にします。すべて未確認の行に形式上の検証日を付けて完了扱いにはしません。

```bash
python scripts/check_aws_audit_decisions.py --check
python scripts/check_aws_audit_decisions.py --as-of 2027-06-01
python scripts/probe_aws_ssm_regions.py --self-test
```

## SSM公開パラメータ利用の判定

**決定：採用候補として、AWS OIDC経由の読み取り専用PoCを先行。**

AWS公式は、`/aws/service/global-infrastructure/services/<service-id>/regions`でリージョン候補を提供します。ただし、この結果があっても**製品GA・機能GA・新規顧客受付・契約可能性を証明しません**。不明なID・空のリストから「非提供」を推論しません。

- 公式資料：[SSMパラメータ一覧](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-public-parameters-global-infrastructure.html) / [必要IAM権限](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-setting-up.html)
- 対象は第1段のVPC Lattice / Firehose / Private CA / Kinesis / ML / SimpleDBの6項目。IDは推定候補としてコード内に登録し、取得前にSSMの公式サービス名一覧と照合。
- **取得元リージョンはus-east-1**。このSSMパスは任意リージョンから利用できるとは限りません。
- `NextToken`で全ページ取得。結果は`aws-ssm-region-probe.json`としてGitHub Actionsの**Artifactに30日保存**し、mainの監査表は自動上書きしません。
- [手動Workflow](../../.github/workflows/probe-aws-ssm-regions.yml)：`AWS_AUDIT_ROLE_ARN`がGitHub Repository Variablesに設定されているときのみ実行。設定しない場合はSKIP。
- 公式リージョン名とAWS CLI/SDKのservice IDが常に一致するわけではありません。サービス識別子の対応を確認してから適用します。

### 必要なAWS側設定（接続前は実行しない）

1. GitHub OIDC Provider `token.actions.githubusercontent.com`をAWS IAMに作成（`aud=sts.amazonaws.com`）。
2. **`KoroKumagai/knowledge`のmainブランチだけを許可**する信頼ポリシーで読取専用Roleを作成。GitHubのOIDC `sub`は設定や作成時期によって変わるため、IAMの実際のsubject値を確認して厳密に制限する。
3. ロールの許可は`ssm:GetParametersByPath`と`/aws/service/global-infrastructure/services`以下への読み取りのみ（Public ParameterのARN表現と対応IAMロールを検証する）。`ssm:PutParameter`や、他の顧客パラメータの読み出し権限は**付けない**。
4. Actions `Settings → Secrets and variables → Actions → Variables`で`AWS_AUDIT_ROLE_ARN`を登録し、**手動Workflow実行を承認**する。IAMアクセスキーは保存しない。

信頼ポリシー例（AWS側のOIDCの`sub`形式に合わせ調整。例をそのまま適用しない）：

```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Principal": {"Federated": "arn:aws:iam::<ACCOUNT_ID>:oidc-provider/token.actions.githubusercontent.com"},
    "Action": "sts:AssumeRoleWithWebIdentity",
    "Condition": {"StringEquals": {
      "token.actions.githubusercontent.com:aud": "sts.amazonaws.com",
      "token.actions.githubusercontent.com:sub": "repo:KoroKumagai/knowledge:ref:refs/heads/main"
    }}
  }]
}
```

**本PRではAWSアカウント／IAMロールを操作しておらず、実際のSSM結果は未取得です。** 初回OIDC実行、IAMアクセス境界と公式データの照合は [Issue #17](https://github.com/KoroKumagai/knowledge/issues/17)で追跡してください。
