# nainen

## 作業する際
### venvで開発を行う
1. 作業ブランチにチェックアウト
2. venvに入る
 > ```$ .\.venv\Scripts\activate``` (windows)

 > ```$ source .venv/bin/activate```(Linux・Mac)
3. 作業
4. 作業終了時  
 ```$ deactivate```
### パッケージのインストール
> ```(.venv)$ pip install [package name]```

※ その他pipコマンドは各自で調べながら作業してください

## Androidアプリ開発をする際の手順
1. androidブランチにチェックアウト
2. ```$ git pull android``` の実行
3. ローカルにある自分のAndroidStudioプロジェクトにブランチ内のファイルをコピペする  
（他の人が開発したファイルで上書きする）
4. 開発
5. android-xxx(画面や機能ごとにブランチ作成)ブランチにチェックアウト
6. リモートのandroid-xxxブランチにプッシュする

## コミットする際参考にしてください
https://qiita.com/itosho/items/9565c6ad2ffc24c09364
(空行はいらない)