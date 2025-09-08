## Google Cloud
無料枠のスペックが適さなかった。

Computeで無料枠を使うため、us-west1-aにした。CO2削減も出来るので。

## Oracle Cloud
2025-09-08 19:00 (JST) ごろ、大阪だと可用性ドメインの容量不足でエラー。大阪は可用性ドメイン数が1つしかない。Oracle Cloudを利用する際は、[[Oracle Cloud Infrastructure#リージョン選択|可用性ドメイン数が多いリージョンの活用を検討]]する。
```
APIエラー 可用性ドメインVM.Standard.A1.FlexのシェイプAD-1の容量が不足しています。別の可用性ドメインでインスタンスを作成するか、後で再試行してください。フォルト・ドメインを指定した場合は、フォルト・ドメインを指定せずにインスタンスを作成します。それでも問題が解決しない場合は、後で再試行してください。ホスト容量についてさらに学習します。
```

## 起動

```
# 永続ディレクトリ
sudo mkdir -p /var/lib/openproject/{pgdata,assets}

# 秘密鍵はランダムで
SECRET=$(head /dev/urandom | tr -dc A-Za-z0-9 | head -c 32)

# 起動（-d で常駐）
docker run -d --name openproject -p 8080:80 \
  -e OPENPROJECT_SECRET_KEY_BASE="$SECRET" \
  -e OPENPROJECT_HOST__NAME=openproject.example.com \
  -e OPENPROJECT_HTTPS=false \
  -v /var/lib/openproject/pgdata:/var/openproject/pgdata \
  -v /var/lib/openproject/assets:/var/openproject/assets \
  openproject/openproject:16
```

## Cloudflare Tunnel セットアップ

### cloudflared インストール

```
curl -fsSL https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb -o cloudflared.deb
sudo dpkg -i cloudflared.deb
```

### Cloudflare にログインしてトンネル作成

```
cloudflared tunnel login
```

### トンネル作成

```
cloudflared tunnel create openproject
```

## Cloudflare DNS とルーティング設定

### config.yml 作成
```
mkdir -p ~/.cloudflared
nano ~/.cloudflared/config.yml
```

```
tunnel: <トンネルID>
credentials-file: /home/USER/.cloudflared/<トンネルID>.json

ingress:
  - hostname: openproject.example.com
    service: http://localhost:8080
  - service: http_status:404
```

### Cloudflare DNS にレコード追加

```
cloudflared tunnel route dns openproject openproject.example.com
```


### Cloudflare Tunnel 常駐化

```
sudo cloudflared service install
sudo systemctl enable cloudflared
sudo systemctl start cloudflared
```

### Cloudflare Zero Trust (Access) で保護

1. Cloudflare ダッシュボード → Zero Trust → Access → Applications
2. 「Add Application」→ Self-hosted
3. ドメイン: openproject.bbbb.dev
4. 認証方法: Google Workspace / Gmail を選択
5. ポリシー: 「特定の Google アカウントのみアクセス許可」