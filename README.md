# nainen

## Django開発をする際
### **Djangoをvenvで開発を行う**
1. 作業ブランチにチェックアウト
2. venvに入る
 > ```$ .\.venv\Scripts\activate``` (windows)

 > ```$ source .venv/bin/activate```(Linux・Mac)
3. 作業 ([以下を参考](#django開発一番始めに行うこと))
4. 作業終了時  
 ```$ deactivate```
### パッケージのインストール
> ```(.venv)$ pip install [package name]```

※ その他pipコマンドは各自で調べながら作業してください  
※ コミット、プッシュする際、.venvディレクトリはgitの追跡に**含めないでください**

### **Django開発時に行うこと(初回1回のみ)**
1. ``settings_local_sample.pyファイル`` を ``django/config/`` にコピーする
2. ``django/config/`` にある、``settings_local_sample.py`` を ``settings_local.py`` に名前を変更する
3. nainenディレクトリで以下を実行  
``$ python manage.py shell``
4. 対話モードに移行するので、以下を実行  
>``>>> from django.core.management.utils import get_random_secret_key``  
``>>> get_random_secret_key()``  
'xxx-xxxx'  
これをコピーして、settings_local.pyの **SECRETT_KEY =** に貼り付ける
5. 作業に入る

### ローカルのDBを利用する間の手順
※AWSを利用するようになったらここは必要なくなる
1. ``django/config/settings_local.py`` に書いてある``DATABASES`` の ``NAME`` と ``PASSWORD`` を自分のローカルのPCの情報に書き換える
2. DATABASESに沿って、ローカルのMySQLにデータベースにデータベースを作成  
※作り方は各自で調べる

*****

## Androidアプリ開発をする際の手順
### **-  ローカルにandroid_appプロジェクトがない場合**
1. Android Studioを起動する
2. 新規プロジェクトとして```android_appプロジェクト```を作成する  
※この際、プロジェクトはどこに作成してもよい（gitの管理以外の場所）  
例）Desktop配下とか、Document配下とか

### **- ローカルにandroid_appプロジェクトがある場合**
1. androidブランチにチェックアウト
2. ```$ git pull android``` の実行  
※もしupdateされたら、下の**androidブランチにupdateがあった際**を参考にして対応してください
3. ローカルにある自分のAndroidStudioプロジェクトにブランチ内のファイルをコピペする  
（他の人が開発したファイルで上書きする）  
```nainen\android_app\src\```以下のファイルを、  
```android_app\app\```以下にコピペする
4. 開発する
5. android-xxx(画面や機能ごとにブランチ作成)ブランチにチェックアウト
6. ローカルの```AndroidStudioProjects\android_app\app\```の```srcディレクトリ```を```nainen\android_app\```にコピペする
7. リモートのandroid-xxxブランチにプッシュする

<details><summary>androidブランチにupdateがあった際</summary>

1. android-xxx(任意のブランチ名)にチェックアウトする  
```$ git checkout android-xxx(任意のブランチ名)```
2. androidブランチをandroid-xxx(任意のブランチ名)にマージする  
```$ git merge android```
3. 上の**ローカルにandroid_appプロジェクトがある場合**へ移動  

</details>

*****

## iPhoneアプリを開発する際の手順

*****
## コミットする際参考にしてください
https://qiita.com/itosho/items/9565c6ad2ffc24c09364
(空行はいらない)