import os
import tweepy
import datetime
auth = tweepy.OAuthHandler(os.environ['TWITTER_API_KEY'], os.environ['TWITTER_API_SECRET_KEY'])
auth.set_access_token(os.environ['TWITTER_ACCESS_TOKEN'], os.environ['TWITTER_ACCESS_TOKEN_SECRET'])
api = tweepy.API(auth)
#current_time = datetime.datetime.now()
#api.update_status(status= current_time)
#print("Done! ")

with open('quotes.json', 'r') as f:
    quotes = json.load(f)
    
index_file = 'index.txt'
if not os.path.exists(index_file):
    index = 0
else:
    with open(index_file, 'r') as f:
        index = int(f.read())
# Get the quote to tweet
quote = quotes[index]

# Compose the tweet text
tweet_text = f'"{quote["text"]}" - {quote["author"]}'

# Post the tweet
api.update_status(tweet_text)
print(f'Tweeted: {tweet_text}')
# Increment the index and write it to the index file
index = (index + 1) % len(quotes)
with open(index_file, 'w') as f:
    f.write(str(index))
