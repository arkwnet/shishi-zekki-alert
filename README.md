# しし絶起アラート (shishi-zekki-alert)

## 概要

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">おはようございます🌞 <a href="https://t.co/JVTuwe5Fc2">pic.twitter.com/JVTuwe5Fc2</a></p>&mdash; ぴﾞっﾞぴﾞびえ(꜆ ˙ᗜ˙ )꜆ (@shishi_zibie) <a href="https://twitter.com/shishi_zibie/status/1636629615778357248?ref_src=twsrc%5Etfw">March 17, 2023</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">2023/03/17 16:25 絶起<a href="https://twitter.com/hashtag/%E3%81%97%E3%81%97%E7%B5%B6%E8%B5%B7%E3%82%A2%E3%83%A9%E3%83%BC%E3%83%88?src=hash&amp;ref_src=twsrc%5Etfw">#しし絶起アラート</a></p>&mdash; arkw (@arkw0) <a href="https://twitter.com/arkw0/status/1636629842987991040?ref_src=twsrc%5Etfw">March 17, 2023</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

特定ユーザのタイムラインを定期巡回し、キーワードが含まれる時に日時・テキスト・ハッシュタグの 3 点を自動ツイートします。

## 動作環境

Linux (WSL 可) + Docker + Docker Compose で動作します。
開発環境は以下の通りです。

-   Windows 11 + WSL 2 (Ubuntu)
-   Docker 20.10.22
-   Docker Compose 2.15.1

## 使い方

### 事前準備

`src` ディレクトリ内に `.env` ファイルを作成し、以下の内容を記述してください。

```
TWITTER_ID=巡回するユーザのID (スクリーンネームではない。例: @arkw0なら3232415294)
TWITTER_KEYWORD="自動ツイートのトリガーとするキーワード"
CONSUMER_KEY=Twitter APIのコンシューマキー
CONSUMER_SECRET=Twitter APIのコンシューマシークレット
TOKEN=Twitter APIのアクセストークン
TOKEN_SECRET=Twitter APIのアクセストークンシークレット
TWEET_TEXT="自動ツイートに含むテキスト"
TWEET_HASHTAG="自動ツイートに含むハッシュタグ"
```

Twitter のユーザ ID は [idtwi](https://idtwi.com/) などのサービスで調べることができます。

### コンテナのビルド

```
docker-compose build
```

### コンテナの起動

```
docker-compose up -d
```

バックグラウンド動作させたくない場合は、`-d` オプションを外してください。

## ライセンス

要相談
