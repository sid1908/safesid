# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 19:42:31 2020

@author: Aumento 101
"""

import tweepy
from tweepy import OAuthHandler 

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

query = "#SAP" 
trends = api.trends_place(1)
fetched_tweets = api.search(q="#CAA", lang="en", count=15000, tweet_mode="extended") 
print(fetched_tweets)