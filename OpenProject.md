
## Google Cloud
無料枠のスペックが適さなかった。

Computeで無料枠を使うため、us-west1-aにした。CO2削減も出来るので。

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