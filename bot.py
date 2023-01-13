import tweepy
import os
auth = tweepy.OAuthHandler("CONSUMER_KEY", os.getenv("TWITTER_CONSUMER_KEY"))
auth.set_access_token("ACCESS_TOKEN", os.getenv("TWITTER_ACCESS_TOKEN"))
api = tweepy.API(auth)
current_time = datetime.datetime.now()
api.update_status(status= current_time)
print("Done!")