## Eato
### サービス概要

飲食店を検索できるサービスです。

### 開発環境
#### 開発環境の構築
##### ソースコードのダウンロード

まずソースコードをGitなどを使ってダウンロードしましょう。

```bash
# HTTPSの場合
git clone https://github.com/S-H-GAMELINKS/eato.git

# SSHの場合
git clone git@github.com:S-H-GAMELINKS/eato.git

```

##### Dockerコンテナのイメージをビルド

ダウンロードしてきた`eato`ディレクトリまでターミナルで移動し、`docker-compose build`コマンドでコンテナのイメージをビルドします。

```bash
docker-compose build
```

エラーなどなく終了すればOKです。

#### マイグレーションの実行

データベースにこれまでのマイグレーションファイルの変更を適用します。

```bash
docker-compose run --rm web python manage.py migrate
```

エラーなどなく終了すればOKです。

##### アプリを起動してみる。

最後に`docker-compose up`をターミナルで実行して、アプリを起動してみましょう。

```bash
docker-compose up
```

起動後、`localhost:8000/restaurants`とブラウザに入力してDjangoの画面が表示されていればOKです。

#### Webサーバーの起動

Webサーバーを起動する際には以下のコマンドを実行します。

```bash
docker-compose up
```

#### アプリの追加

`restaurants`の他にアプリを作る場合は以下のコマンドを実行します。

```bash
docker-compose run --rm web python manage.py startapp <作成したいアプリ名>
```

アプリを追加するのは`restasyurants`のように一塊の処理を実装したい時などになります。
なので、`users`や`reviews`などのようにユーザー用の画面やレビュー用の画面などを作成したい場合に最初にアプリを追加します。

#### テスト

テストを実行して、変更した内容でた正しく動作しているか確認する際には、以下のコマンドを実行します。

```bash
docker-compose run --rm web python manage.py test
```

#### モデルからマイグレーションファイルを作成

新規作成したモデルをもとにマイグレーションファイルを作成する場合は以下のコマンドを実行します。

```bash
docker-compose run --rm web python manage.py makemigrations <モデルを編集したアプリ名>
```

アプリ名の部分には`restaurants`や`users`など変更したモデルが保存されているディレクトリ名を渡します。

#### マイグレーション

マイグレーションファイルを作成後、データベースに変更を適用する場合は以下のコマンドを実行します。

```bash
docker-compose run --rm web python manage.py migrate
```
