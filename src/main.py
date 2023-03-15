# shishi-zekki-alert
# (c) 2023 Sora Arakawa all rights reserved.

import os, json, datetime
from dotenv import load_dotenv
from requests_oauthlib import OAuth1Session

load_dotenv()
TWITTER_ID = os.getenv("TWITTER_ID")
CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
TOKEN = os.getenv("TOKEN")
TOKEN_SECRET = os.getenv("TOKEN_SECRET")
twitter = OAuth1Session(CONSUMER_KEY, CONSUMER_SECRET, TOKEN, TOKEN_SECRET)
params = {
    "expansions": "author_id",
    "tweet.fields": "created_at,public_metrics",
    "user.fields": "name",
    "max_results": 10,
}

res = twitter.get(f"https://api.twitter.com/2/users/{TWITTER_ID}/tweets", params = params)
if res.status_code == 200:
    tl = json.loads(res.text)
    for i in range(len(tl["data"])):
        if tl["data"][i]["text"].find(os.getenv("TWITTER_KEYWORD")) >= 0:
            print(tl["data"][i]["id"])
    dt_now = datetime.datetime.now()
    payload = {"text": f"{dt_now.strftime('%Y/%m/%d %H:%M')} 投稿"}
    response = twitter.post("https://api.twitter.com/2/tweets", json = payload)
