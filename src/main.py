# しし絶起アラート (shishi-zekki-alert)

import os, json, datetime, time
from dotenv import load_dotenv
from requests_oauthlib import OAuth1Session

APP_NAME = "shishi-zekki-alert"
APP_VERSION = "1.0"
APP_COPYRIGHT = "(c) 2023 Sora Arakawa all rights reserved."
SAVE_FILE_PATH = "/src/savedata"

def main():
    load_dotenv()
    TWITTER_ID = os.getenv("TWITTER_ID")
    CONSUMER_KEY = os.getenv("CONSUMER_KEY")
    CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
    TOKEN = os.getenv("TOKEN")
    TOKEN_SECRET = os.getenv("TOKEN_SECRET")
    TWEET_TEXT = os.getenv("TWEET_TEXT")
    TWEET_HASHTAG = os.getenv("TWEET_HASHTAG")
    twitter = OAuth1Session(CONSUMER_KEY, CONSUMER_SECRET, TOKEN, TOKEN_SECRET)
    params = {
        "expansions": "author_id",
        "tweet.fields": "created_at,public_metrics",
        "user.fields": "name",
        "max_results": 10,
    }
    tweet_id = ""
    if os.path.isfile(SAVE_FILE_PATH):
        f = open(SAVE_FILE_PATH, "r")
        tweet_id = f.read()
        f.close()
    print(APP_NAME)
    print("Version " + APP_VERSION)
    print(APP_COPYRIGHT)
    print("----------")
    while True:
        dt_now = datetime.datetime.now()
        print("Twitter timeline check: " + dt_now.strftime('%Y/%m/%d %H:%M'))
        res = twitter.get(f"https://api.twitter.com/2/users/{TWITTER_ID}/tweets", params = params)
        if res.status_code == 200:
            tl = json.loads(res.text)
            for i in range(len(tl["data"])):
                if tl["data"][i]["text"].find(os.getenv("TWITTER_KEYWORD")) >= 0 and tweet_id != tl["data"][i]["id"]:
                    payload = {"text": f"{dt_now.strftime('%Y/%m/%d %H:%M')} {TWEET_TEXT}\n{TWEET_HASHTAG}"}
                    response = twitter.post("https://api.twitter.com/2/tweets", json = payload)
                    print("Automatically tweet: " + tl["data"][i]["id"])
                    f = open(SAVE_FILE_PATH, "w")
                    f.write(tl["data"][i]["id"])
                    f.close()
                    tweet_id = tl["data"][i]["id"]
                    break
        time.sleep(60)

if __name__ == "__main__":
    main()
