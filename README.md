# nainen

## 作業する際
### **Djangoをvenvで開発を行う**
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