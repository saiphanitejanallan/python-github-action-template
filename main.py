import os
import tweepy
import datetime
auth = tweepy.OAuthHandler(os.environ['TWITTER_API_KEY'], os.environ['TWITTER_API_SECRET_KEY'])
auth.set_access_token(os.environ['TWITTER_ACCESS_TOKEN'], os.environ['TWITTER_ACCESS_TOKEN_SECRET'])
api = tweepy.API(auth)
#current_time = datetime.datetime.now()
#api.update_status(status= current_time)
#print("Done! ")

with open('/path/to/quotes.json', 'r') as f:
    quotes = json.load(f)
    
index = int(sys.argv[1])
# Get the quote to tweet
quote = quotes[index]

# Compose the tweet text
tweet_text = f'"{quote["text"]}" - {quote["author"]}'

# Post the tweet
api.update_status(tweet_text)
print(f'Tweeted: {tweet_text}')
