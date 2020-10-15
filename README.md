# Project set up
> docker-compose build

> docker-compose up -d

### set up vue

> docker-compose exec vue sh

> npm install

> npm run serve

> locolhost:8888　にアクセス ***(vuetifyの画面が出ればok)***

> ctrl+c ***(localサーバー停止)***

> exit ***(vueコンテナから抜ける)***

### check database
> docker-compose exec db sh

> mysql -u root -p

> パスワードを聞かれるので root と入力

> show databases; ***(autumn_hackというデータベースが存在すればok)***

> use autumn_hack;

> show tables; ***(user, task というテーブルがあればok)***

> SELECT * FROM user; ***(2行分データが存在していればok)***

> \q ***(mysqlからログアウト)***

> exit ***(dbコンテナから抜ける)***

### set up flask and check database connection
> docker-compose exec flask sh

> flask run --host 0.0.0.0 --port 5000

> localhost:5000 ***(Hello worldが表示されればok)***

> localhost:5000/json ***(jsonで何かしらデータが返ればok)***

> ctrl + c ***(localサーバー停止)***

> exit ***(flaskコンテナから抜ける)***

# その他dockerのコマンド
> docker-compose down ***(コンテナの削除)***

> docker-compose ps ***(起動中のコンテナを表示)***

> docker-compose logs ***(logを表示)***

> docker-compose logs flask ***(特定のコンテナのlogを見たいときはこのように記述)***


# 自動化
> docker-compose.ymlから　command: npm run serve　と command: flask run --host 0.0.0.0 --port 5000　のコメントを外してください

> 以降docker-compose up -d のみで localhost:8888 と localhost:5000 が立ち上がります。

# データベースの初期化について
> docker-compose up -d を実行したときに/db/data　フォルダが存在しなかった場合 /db/sql/init.sql が実行されることでデータベースの初期化を行っています。

#### 再度データの初期化を行いたいときは
> /db/data フォルダを削除

> /db/sql/init.sql に任意のsql文を追記

> docker-compose build

> docker-compose up -d

