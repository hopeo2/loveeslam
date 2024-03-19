import tweepy
import os
import time
from dotenv import load_dotenv


load_dotenv()

consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")
bearer_token = os.getenv("BEARER_TOKEN")

client = tweepy.Client(bearer_token=bearer_token,
                       consumer_key=consumer_key,
                       consumer_secret=consumer_secret,
                       access_token=access_token,
                       access_token_secret=access_token_secret)

var = 0

while True:
    text = "hello💀" + str(var)
    client.create_tweet(text=text)
    print(f"tweet send >> {text}")
    var += 1
    time.sleep(5)
