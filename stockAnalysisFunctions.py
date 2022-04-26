import authenticate
import yfinance as yf
import datetime
from datetime import date
from authenticate import *


# Gets today's date and formats it in a way that is used by yfinance
todaysDate = date.today()
todaysDate = todaysDate.strftime("%Y-%m-%d")

def getStockPrice(ticker):
    '''gets current price of a stock'''
    tick=yf.Ticker(ticker)
    data=tick.history()
    lastPrice=data['Close'].iloc[-1]
    return lastPrice

def getOpenPrice(ticker):
    '''gets opening price of a stock'''
    tick = yf.Ticker(ticker)
    data = tick.history()
    openPrice = data['Open'][todaysDate]
    return openPrice

def getClosePrice(ticker):
    '''gets closing price of a stock'''
    tick = yf.Ticker(ticker)
    data = tick.history(period='1d')
    closePrice = data['Close'][0]
    return closePrice

def getYearlyHigh(ticker):
    timeframe=yf.download(ticker,period="1y",auto_adjust=True,prepost=True,threads=True)
    yearHigh=timeframe['High'].max()
    return yearHigh

def getYearlyLow(ticker):
    timeframe=yf.download(ticker,period="1y",auto_adjust=True,prepost=True,threads=True)
    yearLow=timeframe['High'].min()
    return yearLow
