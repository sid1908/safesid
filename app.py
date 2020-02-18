# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 11:41:27 2019

@author: sidan
"""
from flask import Flask, render_template, request, redirect, url_for
import tweepy
import re
from tweepy import OAuthHandler 
from textblob import TextBlob
from textblob import *
import pie
import csv
import login
import time
from models import *
from nltk.corpus import stopwords
import numpy as np
import pandas as pd
from datetime import date

app = Flask(__name__)

@app.route('/')
def h():
    return render_template('home.html')

@app.route('/home/')
def home():
    return redirect(url_for('h'))

@app.route('/login/')
def login():
    return render_template('login.html')

@app.route('/search/', methods=['POST'])
def search():
    username = request.form['username']
    password = request.form['password']
    return (login.login(username,password))

@app.route('/tech/')
def tech():
     return render_template('tech.html', posts=Post.select().order_by(Post.date.desc()))

@app.route('/about/')
def about():
     return render_template('about.html')

class TwitterClient(object): 
    ''' 
    Generic Twitter Class for sentiment analysis. 
    '''
    def __init__(self): 
        ''' 
        Class constructor or initialization method. 
        '''
        # keys and tokens from the Twitter Dev Console 
        consumer_key = 'MaD9iDFIJzfW2oL3er0FF2iiw'
        consumer_secret = 'IaPzwPNONUvhtEmFkJhWYngh16lPgNJMD7YcRl9Of7MgEGBvFY'
        access_token = '152928771-lifgXaUQYMQczX3CYZRDWo6oUR18Ah0ehHiz77U7'
        access_token_secret = 'YJeNg3TL7ALjklI5Z0bCznRESxLzZL4pdyQueckZYRyMR'

        # attempt authentication 
        try: 
            # create OAuthHandler object 
            self.auth = OAuthHandler(consumer_key, consumer_secret) 
            # set access token and secret 
            self.auth.set_access_token(access_token, access_token_secret) 
            # create tweepy API object to fetch tweets 
            self.api = tweepy.API(self.auth) 
        except: 
            print("Error: Authentication Failed") 

    def clean_tweet(self, tweet): 
        ''' 
        Utility function to clean tweet text by removing links, special characters 
        using simple regex statements. 
        '''
        letters_only_text = re.sub("[^a-zA-Z]", " ", tweet)
        words = letters_only_text.lower().split()
        stopword_set = set(stopwords.words("english"))
        meaningful_words = [w for w in words if w not in stopword_set]
        t1 = " ".join(meaningful_words)
        t2 = TextBlob(t1)
        t2 = t2.lower()
        t2 = t2.correct()
        return (str(t2))
        
    def get_tweet_sentiment(self, tweet): 
        ''' 
        Utility function to classify sentiment of passed tweet 
        using textblob's sentiment method 
        '''
        # create TextBlob object of passed tweet text 
        analysis = TextBlob(self.clean_tweet(tweet))
        #emojis rectification
        t = analysis.split(' ')
        db = pd.read_csv("emojis.csv")
        for t in t:
                    temp = db['Unicode'] == str(t) 
                    temp1 = db['Bytes'] == str(t)
                    temp2 = db[temp | temp1]
                    e = temp2['Sentiment']
        # set sentiment 
        if analysis.sentiment.polarity > 0: 
            return 'positive'
        elif analysis.sentiment.polarity == 0: 
            return 'neutral'
        else: 
            return 'negative'

    def get_tweets(self, query, count = 10): 
        ''' 
        Main function to fetch tweets and parse them. 
        '''
        # empty list to store parsed tweets 
        tweets = [] 

        try: 
            # call twitter api to fetch tweets 
            fetched_tweets = self.api.search(q=query, lang="en", count=count, tweet_mode="extended") 

            # parsing tweets one by one 
            for tweet in fetched_tweets: 
                # empty dictionary to store required params of a tweet 
                parsed_tweet = {} 

                # saving text of tweet 
                parsed_tweet['text'] = tweet.full_text
                # saving sentiment of tweet 
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.full_text) 

                # appending parsed tweet to tweets list 
                if tweet.retweet_count > 0: 
                    # if tweet has retweets, ensure that it is appended only once 
                    if parsed_tweet not in tweets: 
                        tweets.append(parsed_tweet) 
                else: 
                    tweets.append(parsed_tweet) 
            # return parsed tweets
            print(tweets)
            return tweets
                        
        except tweepy.TweepError as e: 
            # print error (if any) 
            print("Error : " + str(e)) 

@app.route('/predict', methods=['POST'])
def main():
    # creating object of TwitterClient Class 
    api = TwitterClient()
    # calling hashtags 
    db = pd.read_csv("db.csv")
    str1 = str(request.form['search']).upper()
    str2 = str(request.form['options']).upper()
    temp = db['DEVICE_NAME'] == str1
    temp1 = db['DEVICE_TYPE'] == str2
    temp2 = db[temp & temp1]
    q = temp2['HASHTAGS'].item()
    print(q)
        # calling function to get tweets 
    tweets = api.get_tweets(query = str(q), count = 200) 
    # picking positive tweets from tweets 
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive'] 
    # percentage of positive tweets
    pper = 100*len(ptweets)/len(tweets)
    # picking negative tweets from tweets
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative'] 
    # percentage of negative tweets
    nper = 100*len(ntweets)/len(tweets)
    # percentage of neutral tweets
    nuper = 100 - (nper + pper)
    # printing first 5 positive tweets
    ptweets1 = [tweet['text'] for tweet in ptweets[:10]]
    # printing first 5 negative tweets 
    ntweets1 = [tweet['text'] for tweet in ntweets[:10]]
    localtime = time.asctime( time.localtime(time.time()) )
    fields=[str1,str2,q,pper,nper,nuper,100,localtime]
    with open(r'C:\Users\Aumento 101\Downloads\flask_major\s2s.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(fields)
    
    print("success",pper,nper,nuper,localtime)
    return(pie.pie(pper,nper,nuper,ptweets1,ntweets1))
    

if __name__ == "__main__":
        app.debug = True
        app.run()

                    

