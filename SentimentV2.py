import os
import tweepy as tw
import pandas as pd
import requests
import df
bearer_token='AAAAAAAAAAAAAAAAAAAAAIoZbgEAAAAA2ZKX19DgAuBJiiQqqkJHRkqil%2Fk%3Dt5TKQDRnV278J2CFWzaSDhPRrmS6Kn1akiYm72YtCFh7mV7Owm'

client=tw.Client(bearer_token,return_type = requests.Response)
search_word=["nft","football"]
import json
cc=0
query="nft "
import pandas as pd
totalcount=0
next_token=""
while(totalcount<1005):
	if(totalcount==0):
		print("First Query")
		tweets=client.search_recent_tweets(query=search_word[1],tweet_fields=['created_at','geo'],place_fields=['country_code','full_name'],expansions='geo.place_id',max_results=100)
	else:
		print("Subsequent query with count",totalcount," and next token",next_token)
		tweets=client.search_recent_tweets(query=search_word[1],tweet_fields=['created_at','geo'],place_fields=['country_code','full_name'],expansions='geo.place_id',max_results=100,next_token=next_token)
	# Save data as dictionary
	tweets_dict = tweets.json() 
	# Extract "data" value from dictionary
	tweets_data = tweets_dict['data']
	'''
	if 'places' in tweets_dict: 
		places={p["id"]: p for p in tweets_dict['places']}
		for place in places:
			with open('places_meta.ndjson','a+') as jf:
				jf.write(json.dumps(place))
				jf.write("\n")
	for tweet in tweets_data:
		with open('tweets_nft_vlocation.ndjson','a+') as of:
			of.write(json.dumps(tweet))
			of.write("\n")
	'''
	with open('tweets_football.ndjson','a+') as of:
		of.write(json.dumps(tweets_dict))
		of.write("\n")
	next_token=tweets_dict['meta']['next_token']
	totalcount+=len(tweets_dict['data'])
	df.to_csv("tweets_football.csv",mode="a")