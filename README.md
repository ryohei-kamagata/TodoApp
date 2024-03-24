# TodoAp

### コンテナ起動方法

`docker-compose.yml`があるフォルダで以下のコマンドを実行

```
docker-compose build --no-cache
```

次に以下のコマンドを実行

```
docker-compose up -d
```

`http://localhost:3000/docs`にアクセスすると swagger を確認できる
`http://localhost:8080`にアクセスすると画面が表示される

### 画面開発時

`frontend`ディレクトリで以下のコマンドを実行

```
npm run dev
```

`http://localhost:8080`にアクセスするとローカル環境で画面が表示される

### API 詳細

### TES
