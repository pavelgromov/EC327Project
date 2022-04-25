#import files
import authenticate
from stockAnalysisFunctions import *
from authenticate import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import *
import sys
import wheel
import pandas as pd
import loadGUI
##QtWidgets.QtWidget(MainWindow)=getStockPrice('AAPL')
# Testing functions with AAPL
##print(str(getStockPrice('AAPL')))

##print(str(getOpenPrice('AAPL')))

# Creates generic list of stocks that user can add to
listOfStocks = ['AAPL', 'SPY', 'MSFT', 'TSLA']
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label=getOpenPrice('AAPL')
        self.show()
app =QApplication(sys.argv)
window=Window()
sys.exit(app.exec())
##inputStock=self.QTextEdit()
# Command-line tool to see where stocks opened, and where they are now
##for x in listOfStocks:
    ##print(x + " opened at " + str(getOpenPrice(x)) + ", and is now at " + str(getStockPrice(x)))


