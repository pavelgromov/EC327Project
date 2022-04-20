# Install Libraries
from textblob import TextBlob
import sys
import tweepy
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import nltk
## Polygon.io modules
import polygon
from setuptools import setup, find_packages
from polygon import WebSocketClient, STOCKS_CLUSTER
import os
import sys
##import pycountry
##import re
import string
##Initialize the Twitter API
apiKey='XtJ91BCEHLOrx9cKn91FLtmf4'
apiSecretKey='UeV7mL55dTxlh1S3t8NUUwHhbEQOPEwMDQeeU2UFxsGNgpgrUv'
bearToken='AAAAAAAAAAAAAAAAAAAAAIoZbgEAAAAADI59EaPi1JkkvfMphi7skeRhNaY%3DKDgMmE9DsJwAfthQBZmOaUDCEPe8iuNn6EY81lwka4feweJkqH'
author=tweepy.AppAuthHandler(apiKey,apiSecretKey)
author
api=tweepy.API(author)

##Initialize the Polygon API
polyApiKey='0dQTVnBrippZ1p5OmMHXgv6pa0A8k8aq'


