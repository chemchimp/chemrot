import os
import random
import tweepy

# Load API credentials from GitHub Secrets
api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_KEY_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

# Initialize Tweepy client for v2
client = tweepy.Client(
    consumer_key=api_key,
    consumer_secret=api_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

# Read tweets from tweets.txt
with open("tweets.txt", "r") as f:
    tweets = [line.strip() for line in f if line.strip()]

# Pick one tweet at random
tweet_text = random.choice(tweets)

# Post the tweet
response = client.create_tweet(text=tweet_text)

if response.data:
    print(f"Tweet posted! ID: {response.data['id']}")
else:
    print("Failed to post tweet:", response)
