import tweepy
import time
from config import BEARER_TOKEN

def get_recent_tweets(query, max_results=5):
    try:
        client = tweepy.Client(bearer_token=BEARER_TOKEN)
        tweets = client.search_recent_tweets(query=query, max_results=max_results)
        return [tweet.text for tweet in tweets.data] if tweets.data else []
    except tweepy.TooManyRequests:
        print("Rate limit hit. Please wait before retrying.")
        return ["Error: Rate limit exceeded. Please wait and try again."]
    
def get_recent_tweets(query, max_results=5):
    return [
        f"This is a sample tweet about {query}.",
        f"{query} is trending on Twitter right now!",
        f"I don't like {query} at all.",
        f"What are your thoughts on {query}?",
        f"{query} makes me happy!",
    ]

