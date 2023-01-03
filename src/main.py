# shishi-zekki-alert
# (c) 2023 Sora Arakawa all rights reserved.

import os
import twitter
from dotenv import load_dotenv

load_dotenv()
auth = twitter.OAuth(consumer_key = os.getenv("CONSUMER_KEY"),
                     consumer_secret = os.getenv("CONSUMER_SECRET"),
                     token = os.getenv("TOKEN"),
                     token_secret = os.getenv("TOKEN_SECRET"))
t = twitter.Twitter(auth = auth)

t.statuses.update(status = "Twitter投稿テスト")
