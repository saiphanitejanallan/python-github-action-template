import os
import tweepy
import datetime
import json
auth = tweepy.OAuthHandler(os.environ['TWITTER_API_KEY'], os.environ['TWITTER_API_SECRET_KEY'])
auth.set_access_token(os.environ['TWITTER_ACCESS_TOKEN'], os.environ['TWITTER_ACCESS_TOKEN_SECRET'])
api = tweepy.API(auth)
#current_time = datetime.datetime.now()
#api.update_status(status= current_time)
#print("Done! ")

with open('quotes.json', 'r') as f:
    quotes = json.load(f)
    
index = int(os.environ['CURRENT_INDEX'])
print(f'index : {index}')
# Get the quote to tweet
quote = quotes[index]

# Compose the tweet text
tweet_text = f'"{quote["text"]}" - {quote["author"]}'

# Post the tweet
api.update_status(tweet_text)
print(f'Tweeted: {tweet_text}')
# Increment the index and write it to the index file
index = index + 1
os.environ['CURRENT_VALUE'] = str(index)
print(f'current value after increased: {os.environ['CURRENT_VALUE']})
