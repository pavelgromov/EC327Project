import authenticate
import yfinance as yf
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