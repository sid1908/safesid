# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 11:12:06 2020

@author: Aumento 101
"""

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
fetched_tweets = api.search(q="#StreetDancer3D", lang="en", count=100, tweet_mode="extended") 

# parsing tweets one by one 
for tweet in fetched_tweets:
    tweet_id = tweet.id_str
    tweet_mess = api.list_direct_messages(tweet_id)
    tweet_status =api.get_status(tweet_id)
    print("tweet_id:",tweet_id)
    print('\n')
    print('tweet_mess',tweet_mess)
    print('\n')
    print("tweet",tweet.full_text,"\n")