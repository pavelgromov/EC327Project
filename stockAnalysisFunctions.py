import authenticate
import yfinance as yf
from authenticate import *

def getStockPrice(ticker):
    tick=yf.Ticker(ticker)
    data=tick.history()
    lastPrice=data['Close'].iloc[-1]
    print(lastPrice)

