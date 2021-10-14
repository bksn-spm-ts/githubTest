# README

TODO
- コード内にはclient_idとclient_secretを埋める欄が全部で３つありますので埋めてください
- まずは https://localhost:8000 を開き、証明書を信頼してください
- その後、 https://localhost:8000/oauthDemo へリクエストすると動きます

# サーバの起動(SSLで8000版で起動する必要がある）

$ python manage.py runsslserver localhost:8000 --certificate foobar.crt --key foobar.key

# 各種ビュー

今回は説明のためにビューを分けたが、関数一つでパラメータで分岐しても良い

## index

認可コードを取得するためのURLを生成する

## callback

認可コードをURLから取得し、トークンを要求する

- 認可コードをURLから取得する
- POSTリクエストを投げてトークンを取得する
- 返ってきたJSONデータをテンプレートに渡して表示する

