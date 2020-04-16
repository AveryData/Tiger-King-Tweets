#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 18:10:25 2020

@author: averysmith
"""

import twitterscraper
import pandas as pd
import time

print('Web Scraping .....')
time.sleep(1)
print('@joe_exotic')
time.sleep(1)
print(('...........'))
time.sleep(1)
print('----------------')
time.sleep(1)
print('The Tiger King')
time.sleep(5)

# Scrape Tweets
handle = 'joe_exotic'
out = twitterscraper.query_tweets_from_user(handle)

# Create Empty storage
df = pd.DataFrame()
Date = []
Text = []
Likes = []
Retweets = []
# Read data into respective columns
for tweet in out:
    Date.append(tweet.timestamp)
    Text.append(tweet.text)
    Likes.append(tweet.likes)
    Retweets.append(tweet.retweets)

# Turn into csv
df['Date'] = Date
df['Text'] = Text
df['Likes'] = Likes
df['Retweets'] = Retweets
df.to_csv('JoeExoticTweets.csv' )

print('----------------------------')
print('----------------------------')
print('----------------------------')
time.sleep(1)
print('Tweets scraped!!!')
time.sleep(1)
print('-------------------------------')
print('Total Number? ' + str(len(df)))