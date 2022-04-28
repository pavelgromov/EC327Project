import os
import csv
import json
##from turtle import clear
import matplotlib.pyplot as plot
import requests
import pandas as pd
import tweepy as tw
from datetime import datetime, timedelta
import vaderSentiment
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAIoZbgEAAAAA2ZKX19DgAuBJiiQqqkJHRkqil%2Fk%3Dt5TKQDRnV278J2CFWzaSDhPRrmS6Kn1akiYm72YtCFh7mV7Owm'
analyzer = SentimentIntensityAnalyzer()
sentiments = []


client=tw.Client(bearer_token,return_type=requests.Response)
    


def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers

def clean(tweet):
    return str(tweet).encode('ascii', 'ignore').decode('UTF-8')


def connect_to_endpoint(url, headers):
    response = requests.request("GET", url, headers=headers)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

def get_tweets(stock):
    ticker=str(stock)
    start_time=datetime.now()
    expansions=None
    endtime= datetime.now() - timedelta(days=7)
    
    result=client.search_recent_tweets(ticker,max_results=100)
    result=result.json()
    ##print(result.json())
    #print(result)
    
    #res=clean(result)
    #list=json.loads(res)
    result=json.dumps(result, indent=4, sort_keys=True)
    with open('result.json()', 'w') as f:
        json.dump(result, f)
    return result
    
def getPolarity(tweets):
    score=analyzer.polarity_scores(tweets)
    print(score)
    scores=score.values()
    scores_list=list(scores)
    negative=scores_list[0]
    return scores_list

def makePlot(stock):
    tweets=get_tweets(stock)
    score=getPolarity(tweets)
    label='Negative', 'Neutral', 'Postive'
    chunks=[score[0]*100, score[1]*100, score[2]*100]
    sep=(0,0,0.1)
    fig1,ax1=plot.subplots()
    ax1.pie(chunks,explode=sep,labels=label,autopct='%1.1f%%')
    ax1.axis('equal')
    plot.show()

    
##tweets=get_tweets()
stock='TWTR'
makePlot(stock)
##scores=getPolarity(tweets)
##print(scores)
'''
    score=analyzer.polarity_scores(result)
    scores=score.values()
    scores_list=list(scores)
    negative=scores_list[0]
    #print(result)
    #print(scores_list[0])
    return result'''

'''
query = "Arsenal Edu lang:en -is:retweet"  # ENTER THE TEXT EDIT FIELD HERE
limit = "100"
tweet_list = []
next_token = ""
'''
'''
for i in range(20):
    data = get_tweets(
        query,
        limit,
        next_token
    )
    data=json.loads(data)
    next_token=data['meta']['next_token']
    tweet_list += data['data']

tweets_df=pd.DataFrame(tweet_list)
tweets_df
'''
'''
from textblob import TextBlob


def get_subjectivity(tweet):
    return round(TextBlob(tweet).sentiment.subjectivity, 2)

def get_polarity(tweet):
    return round(TextBlob(tweet).sentiment.polarity, 2)
'''
'''
tweets_df['text']=tweets_df['text'].apply(clean)
tweets_df['subjectivity']=tweets_df['text'].apply(get_subjectivity)
tweets_df['polarity']=tweets_df['text'].apply(get_polarity)
tweets_df.drop(tweets_df[tweets_df['polarity'] == 0].index, inplace = True)
tweets_df.drop_duplicates(subset = 'text', keep = "first", inplace = True)
tweets_df
'''