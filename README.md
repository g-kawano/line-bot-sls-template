# line-bot-sls-template

## 概要
LINE Bot で使用する messging-api の AWS 実行環境を serverless framework デプロイできるテンプレートです。

## 環境
- python 3.8
- Pipenv version 2018.11.26
- serverless framework 2.15.0

## 構成
画像

## 環境変数
- serverless.yml 
    - LINE_CHANNEL_SECRET: LINE MessagingAPI アカウントのLシークレット
    - LINE_CHANNEL_ACCESS_TOKEN: LINE MessagingAPI アカウントのアクセストークン

## デプロイ
```
npx serverless deploy
```

## 注意
あくまで検証用途のため、ロギング、例外処理等は実装していません。
