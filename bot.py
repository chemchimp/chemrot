import os
import random
import tweepy

api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_KEY_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

with open("tweets.txt", "r") as f:
    tweets = [line.strip() for line in f if line.strip()]

tweet = random.choice(tweets)
api.update_status(tweet)
print(f"Tweet posted: {tweet}")
