# Install Libraries
import yfinance as yf
# from textblob import TextBlob
# import sys
import tweepy
# import matplotlib.pyplot as plt
# import pandas as pd
# import numpy as np
# import nltk
# ## Polygon.io modules
# from polygon import RESTClient
# import datetime
# import polygon
# from setuptools import setup, find_packages
# from polygon import WebSocketClient, STOCKS_CLUSTER
# import os
# import sys
# ##import pycountry
# ##import re
# import string
##Initialize the Twitter API
apiKey='uhyiFL7RgdPSz606cTUyBCi0n'
apiSecretKey='I2UFh9SVvbA2JXjowapb39IlrzNk6C38DPRf8I63smuSjyOV1I'
bearToken='AAAAAAAAAAAAAAAAAAAAAIoZbgEAAAAAi7Qg67XSOnwbDuQ5Xxltf3djyZg%3DCjfKZ0knyALCTJBRTxlu1fmumEFQxfbtEEWccC3z7YQ91CqWBg'
author=tweepy.AppAuthHandler(apiKey,apiSecretKey)
##author
api=tweepy.API(author)

##Initialize the Polygon API
##message='Successful Connection'
##polyApiKey='0dQTVnBrippZ1p5OmMHXgv6pa0A8k8aq'



