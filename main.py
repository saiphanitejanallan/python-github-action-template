import os
import tweepy
import datetime
auth = tweepy.OAuthHandler(os.environ['TWITTER_API_KEY'], os.environ['TWITTER_API_SECRET_KEY'])
auth.set_access_token(os.environ['TWITTER_ACCESS_TOKEN'], os.environ['TWITTER_ACCESS_TOKEN_SECRET'])
api = tweepy.API(auth)
current_time = datetime.datetime.now()
api.update_status(status= current_time)
print("Done! ")
