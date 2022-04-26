import sys
import subprocess

# Install Libraries

# implement pip as a subprocess:
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'textblob'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'tweepy'])

# Import Libraries

from textblob import TextBlob
import sys
import tweepy
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import nltk
import pycountry
import re
import string

from PIL import Image
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from langdetect import detect
from nltk.stem import SnowballStemmer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import CountVectorizer

# Authentication
consumerKey = uhyiFL7RgdPSz606cTUyBCi0n
consumerSecret = I2UFh9SVvbA2JXjowapb39IlrzNk6C38DPRf8I63smuSjyOV1I
accessToken = 1514971266347724800-sCUjbmDCl8M6yFVHejzPLfdafRSDuY
accessTokenSecret = VedK3nJLo3v1DXo7QolsvirgYC9fglUNzBx7PdqVyhUzD

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

#Sentiment Analysis

def percentage(part,whole):
    return 100 * float(part)/float(whole) 

keyword = AAPL #user input from text box in GUI
noOfTweet = 250 #we set here


tweets = tweepy.Cursor(api.search, q=keyword).items(noOfTweet)


positive  = 0
negative = 0
neutral = 0
polarity = 0
tweet_list = []
neutral_list = []
negative_list = []
positive_list = []

for tweet in tweets:
    
    #print(tweet.text)
    tweet_list.append(tweet.text)
    analysis = TextBlob(tweet.text)
    score = SentimentIntensityAnalyzer().polarity_scores(tweet.text)
    neg = score['neg']
    neu = score['neu']
    pos = score['pos']
    comp = score['compound']
    polarity += analysis.sentiment.polarity
    
    if neg > pos:
        negative_list.append(tweet.text)
        negative += 1

    elif pos > neg:
        positive_list.append(tweet.text)
        positive += 1
    
    elif pos == neg:
        neutral_list.append(tweet.text)
        neutral += 1
        
positive = percentage(positive, noOfTweet)
negative = percentage(negative, noOfTweet)
neutral = percentage(neutral, noOfTweet)
polarity = percentage(polarity, noOfTweet)
positive = format(positive, '.1f')
negative = format(negative, '.1f')
neutral = format(neutral, '.1f')

#Creating PieCart

labels = ['Positive ['+str(positive)+'%]' , 'Neutral ['+str(neutral)+'%]','Negative ['+str(negative)+'%]']
sizes = [positive, neutral, negative]
colors = ['yellowgreen', 'blue','red']
patches, texts = plt.pie(sizes,colors=colors, startangle=90)
plt.style.use('default')
plt.legend(labels)
plt.title("Sentiment Analysis Result for stock:  "+keyword+"" )
plt.axis('equal')
plt.show() #Shows the pie chart with percentages
