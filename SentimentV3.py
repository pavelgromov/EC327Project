import os
import csv
import json
import re
import numbers
##from turtle import clear
import matplotlib.pyplot as plot
import requests
import pandas as pd
import tweepy as tw
from datetime import datetime, timedelta
from wordcloud import WordCloud
import vaderSentiment
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAIoZbgEAAAAA2ZKX19DgAuBJiiQqqkJHRkqil%2Fk%3Dt5TKQDRnV278J2CFWzaSDhPRrmS6Kn1akiYm72YtCFh7mV7Owm'     #bearer token for twitter API
analyzer = SentimentIntensityAnalyzer()     #Sentiment analyzer
sentiments = []


client=tw.Client(bearer_token,return_type=requests.Response)
    

def get_tweets(stock):                              #this function get the tweets from the twitter api 
    ticker=str(stock)                               #set stock name
    start_time=datetime.now()                       #set start time
    expansions=None
    endtime= datetime.now() - timedelta(days=7)       
    result=client.search_recent_tweets(ticker,max_results=100,tweet_fields="text")      #search 100 most recent tweets
    result=result.json()        #convert to json
    result=json.dumps(result, indent=4, sort_keys=True)
    with open('result.json', 'w') as f:
        json.dump(result, f)
    res=clean(result)
    list=json.loads(res)
    return result
   
def getPolarity(tweets):
    cleaning=tweets
    score=analyzer.polarity_scores(tweets)      #get polarity of the tweets
    scores=score.values()                       
    scores_list=list(scores)                #create score list
    negative=scores_list[0]                 
    cleaning=clean(cleaning)                #remove extraneous words
    wordcloud=WordCloud().generate(cleaning)        #generate wordcloud with the words
    wordcloud.to_file('stockWordCloud'+'.jpg')      #save to jpeg file

    return scores_list

def clean(tweets):
    tweets=str(tweets)
    numbers = ['1','2','3','4','5','6','7','8','9','0']
    dumbwords=["id","RT","text", "u"]
    result= tweets.lower()
    result = re.sub(r"https\S+", "", result)            #the following lines are trying to remove links and other extra strings in the tweets
    result = re.sub(r"www.\S+", "", result)
    result= re.sub("@[A-Za-z0-9_]+","", result)
    result= re.sub("#[A-Za-z0-9_]+","", result)
    result= re.sub('[()!?]', ' ', result)
    result= re.sub('\[.*?\]',' ', result)
    results=re.sub("[0-9]"," ",result)
    result= re.sub("[^a-z0-9]"," ", result)
    stopwords = ["for", "on", "an", "a", "of", "and", "in", "the", "to", "from", "id","RT","text"]
    result=[x for x in result if not x in numbers]
    result= [w for w in result if not w in stopwords]
    result= [w for w in result if not w in dumbwords]
    result= " ".join(word for word in result)
    result=[word for word in result if word not in dumbwords]
    return tweets
   
