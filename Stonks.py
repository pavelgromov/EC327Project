#import files
import authenticate
from stockAnalysisFunctions import *
from authenticate import *
import importGUI
#import Modules
# import wheel
import pandas as pd
# import pip
# from setuptools import setup, find_packages
# import numpy as np
# import time
# from stockAnalysisFunctions import *
QtWidgets.QtWidget(MainWindow)=getStockPrice('AAPL')
# Testing functions with AAPL
##print(str(getStockPrice('AAPL')))

##print(str(getOpenPrice('AAPL')))

# Creates generic list of stocks that user can add to
listOfStocks = ['AAPL', 'SPY', 'MSFT', 'TSLA']

# Command-line tool to see where stocks opened, and where they are now
for x in listOfStocks:
    print(x + " opened at " + str(getOpenPrice(x)) + ", and is now at " + str(getStockPrice(x)))


