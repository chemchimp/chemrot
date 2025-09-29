import os
import random
import tweepy

# Load API credentials from GitHub Secrets
api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_KEY_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

# Debugging: verify the secrets are loaded (REMOVE before public push!)
# print(api_key, api_secret, access_token, access_token_secret)

# Authenticate with X (formerly Twitter)
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Read tweets from tweets.txt in root directory
with open("tweets.txt", "r") as f:
    tweets = [line.strip() for line in f if line.strip()]

# Pick one tweet at random
tweet = random.choice(tweets)

# Post the tweet
api.update_status(tweet)
print(f"Tweet posted: {tweet}")
