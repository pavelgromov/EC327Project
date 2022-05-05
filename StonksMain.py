import os
import sys
import venv
venv.create('/Stonks')
import importPackages
from configparser import ExtendedInterpolation
from errno import ENETRESET
import sys
import matplotlib.pyplot as plot
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from stockAnalysisFunctions import *
from SentimentV3 import *
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QTextEdit, QGraphicsScene, QGraphicsView
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtGui import QPixmap
import newGui
import pandas as pd
import numpy
from PIL import Image


class StonksGui(QtWidgets.QMainWindow, newGui.Ui_MainWindow, QGraphicsView, QGraphicsScene):
    def __init__(self, parent=None):                    #This section initializes the GUI. IT sets the labels,titles, and button names, as well as all the initial prices to zero.
        super(StonksGui, self).__init__(parent)
        self.setupUi(self)
        price = 0
        pricezero = str(price)
        self.label_5.setText("Stock Twitter Analysis")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter) #aligns the text in the center
        self.label.setText(pricezero)   #set the initial prices to zero 
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setText(pricezero)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setText(pricezero)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setText(pricezero)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setText(pricezero)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setText("Current Price:")      #label all the buttons and outputs 
        self.label_4.setText("Last Open Price:")
        self.label_7.setText("Last Close Price:")
        self.label_9.setText("52 Week High:")
        self.label_10.setText("52 Week Low:")
        self.label_12.setText(" ")
        self.label_13.setText(" ")
        self.pushButton.clicked.connect(self.enterPressed)      #check if enter is pressed 
        self.enterPressed()                 

    def initUI(self):
        self.label.setText('Word')

    def enterPressed(self):
        stock=self.lineEdit.text()      #find stock name entered
        stocklist=pd.read_csv('nasdaq-listed-symbols_csv.csv')  #create existing stock list name 
        if stock=='':       #if stock is empty do nothing
            self.label_5.setText("Stock Twitter Analysis")
        elif stock!='':     
            for row in stocklist.index:             #if the stock is not empty, check the list
                if stocklist.loc[row,'Symbol']!=stock:      #if the stock is not in the list, do nothing
                    self.label_5.setText("Stock Twitter Analysis")  
                elif stocklist.loc[row,'Symbol']==stock:    #if the stock is in the list, get the info and make the plots.
                    self.getinfo()      #get the stock info
                    self.makePlot()     #make the stock plots

    def getinfo(self):
        stock=self.lineEdit.text()  #get the stock entered
        stock = stock.capitalize()  #capitalize the stock 
        self.label_5.setText("Stock Twitter Analysis")
        currPrice = str(round(getStockPrice(stock), 2)) #get the current price
        self.label.setText(currPrice)   #set the current price label to the price
        YearHigh = str(round(getYearlyHigh(stock), 2)) #get year high price
        self.label_8.setText(YearHigh)     #set the yearhigh label to the price
        YearLow = str(round(getYearlyLow(stock), 2))    #get the year low price
        self.label_11.setText(YearLow)  #set the year low label to the price
        openPrice = str(round(getOpenPrice(stock), 2))  #get the open price 
        self.label_2.setText(openPrice) #set the open price label to the open price
        closePrice = str(round(getClosePrice(stock), 2))    #get the close price 
        self.label_6.setText(closePrice)    #set the close price label to the close price

    def makePlot(self):
        Figure(figsize=(331, 241), dpi=1)                   #set figure size
        stock = self.lineEdit.text()                        #retrieve inputted stock
        if stock == '':                                     #check if the line edit is empty
            self.label_5.setText("Stock Twitter Analysis")    #set title if empty. this is the same as doing nothing

        else:
            tweets = get_tweets(stock)                      #get tweets 
            if tweets == '':                                   #if tweets are empty, do nothing again.
                self.label_5.setText("Stock Twitter Analysis")
            else:
                score = getPolarity(tweets)                 #if it is not empty, proceed with same the plot
                label = 'Negative', 'Neutral', 'Positive'      #find percentage of sentiment
                chunks = [score[0]*100, score[1]*100, score[2]*100] #convert to percentage out of 100%
                sep = (0, 0, 0.1)
                fig1, ax1 = plot.subplots() #make plot
                ax1.pie(chunks, explode=sep, labels=label, autopct='%1.1f%%')
                ax1.axis('equal')   #make the cirlce equal
                plot.savefig("stockfigure.jpg") #save the figure in the jpeg
                image = Image.open('stockfigure.jpg')
                image_name = 'stockfigure.jpg'
                wordcloudname = 'stockWordCloud.jpg'    #get the wordcloud jpeg
                pixmap = QPixmap(image_name)    #set the pie chart to display 
                pixmap2 = QPixmap(wordcloudname)    #set the wordcloud to display 
                self.label_12.setScaledContents(True)   #scale the images to the right size 
                self.label_12.setPixmap(pixmap)
                self.label_13.setPixmap(pixmap2)


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=2, height=1, dpi=100):    #initialize the size of the GUI
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


def main():
    app = QApplication(sys.argv)        #run the GUI
    form = StonksGui()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
