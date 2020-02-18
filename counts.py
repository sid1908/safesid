import tweepy
from tweepy import OAuthHandler 
# keys and tokens from the Twitter Dev Console 
consumer_key = 'MaD9iDFIJzfW2oL3er0FF2iiw'
consumer_secret = 'IaPzwPNONUvhtEmFkJhWYngh16lPgNJMD7YcRl9Of7MgEGBvFY'
access_token = '152928771-lifgXaUQYMQczX3CYZRDWo6oUR18Ah0ehHiz77U7'
access_token_secret = 'YJeNg3TL7ALjklI5Z0bCznRESxLzZL4pdyQueckZYRyMR'

# create OAuthHandler object 
auth = OAuthHandler(consumer_key, consumer_secret) 

# set access token and secret 
auth.set_access_token(access_token, access_token_secret) 
# create tweepy API object to fetch tweets 
api = tweepy.API(auth)
tweets = [] 
# call twitter api to fetch tweets
query = "#StreetDancer3D" 
fetched_tweets = api.search(q="#StreetDancer3D", lang="en", count=10, tweet_mode="extended") 
for tweet in fetched_tweets:
    tweet_id = tweet.id
    tweet = api.get_status(tweet_id)
    print(tweet.retweet_count)
    print(tweet.favorite_count)