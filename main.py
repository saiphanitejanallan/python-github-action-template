import os
import tweepy
import datetime
import json

import requests
auth = tweepy.OAuthHandler(os.environ['TWITTER_API_KEY'], os.environ['TWITTER_API_SECRET_KEY'])
auth.set_access_token(os.environ['TWITTER_ACCESS_TOKEN'], os.environ['TWITTER_ACCESS_TOKEN_SECRET'])
api = tweepy.API(auth)
#current_time = datetime.datetime.now()
#api.update_status(status= current_time)
#print("Done! ")

with open('quotes.json', 'r') as f:
    quotes = json.load(f)
    
#index = int(os.environ['CURRENT_INDEX'])
# Load last tweeted quote index from a file
if os.path.exists('last_tweet_index.txt'):
    with open('last_tweet_index.txt', 'r') as f:
        last_tweet_index = int(f.read().strip())
else:
    last_tweet_index = -1

next_tweet_index = (last_tweet_index + 1) 
print(f'index : {next_tweet_index}')
# Get the quote to tweet
quote = quotes[next_tweet_index]

# Compose the tweet text
tweet_text = f'"{quote["quote"]}" - {quote["character"]}'
image_url = quote['image']
filename = f"image.jpg"
image = requests.get(image_url).content
with open(filename, "wb") as f:
    f.write(image)
media_upload = api.media_upload(filename)
tweet_media_id = media_upload.media_id
api.update_status(status=tweet_text, media_ids=[tweet_media_id])
print(f'Tweeted: {tweet_text}')
with open('last_tweet_index.txt', 'w') as f:
    f.write(str(next_tweet_index))
