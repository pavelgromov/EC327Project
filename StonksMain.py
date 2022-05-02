from configparser import ExtendedInterpolation
from errno import ENETRESET
import sys
# import importPackages
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
    def __init__(self, parent=None):
        super(StonksGui, self).__init__(parent)
        self.setupUi(self)
        price = 0
        pricezero = str(price)
        self.label_5.setText("Stock Twitter Analysis")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setText(pricezero)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setText(pricezero)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setText(pricezero)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setText(pricezero)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setText(pricezero)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setText("Current Price:")
        self.label_4.setText("Last Open Price:")
        self.label_7.setText("Last Close Price:")
        self.label_9.setText("52 Week High:")
        self.label_10.setText("52 Week Low:")
        self.label_12.setText(" ")
        self.label_13.setText(" ")
        # self.checkenter()
        self.pushButton.clicked.connect(self.enterPressed)
        self.enterPressed()

    def initUI(self):
        self.label.setText('Word')

    def enterPressed(self):
        stock=self.lineEdit.text()
        stocklist=pd.read_csv('nasdaq-listed-symbols_csv.csv')
        if stock=='':
            self.label_5.setText("Stock Twitter Analysis")
        elif stock!='':
            i=0
            while(i<len(stocklist)):
                if stocklist[i]!=stock:
                    self.label_5.setText("Stock Twitter Analysis")
                    i=i+1
                elif stocklist[i]==stock:
                    self.getinfo()
                    self.makePlot()
            #self.pushButton.clicked.connect(self.getinfo)
            #self.pushButton.clicked.connect(self.makePlot)
        #self.pushButton.clicked.connect(self.getinfo)

    def getinfo(self):
        stock=self.lineEdit.text()
        stock = stock.capitalize()
        self.label_5.setText("Stock Twitter Analysis")
        currPrice = str(round(getStockPrice(stock), 2))
        self.label.setText(currPrice)
        YearHigh = str(round(getYearlyHigh(stock), 2))
        self.label_8.setText(YearHigh)
        YearLow = str(round(getYearlyLow(stock), 2))
        self.label_11.setText(YearLow)
        openPrice = str(round(getOpenPrice(stock), 2))
        self.label_2.setText(openPrice)
        closePrice = str(round(getClosePrice(stock), 2))
        self.label_6.setText(closePrice)
        # openPrice = str(round(getOpenPrice(stock),2))
        # YearLow = str(round(getYearlyLow(stock),2))
        # closePrice=str(round(getClosePrice(stock),2))
        # self.label.setText(currPrice)
        # self.label_2.setText(openPrice)
        # self.label_6.setText(closePrice)
        # self.label_8.setText(YearHigh)
        # self.label_11.setText(YearLow)

    def makePlot(self):
        Figure(figsize=(331, 241), dpi=1)
        stock = self.lineEdit.text()
        if stock == '':
            self.label_5.setText("Stock Twitter Analysis")

        else:
            tweets = get_tweets(stock)
            if tweets == '':
                self.label_5.setText("Stock Twitter Analysis")
            else:
                score = getPolarity(tweets)
                label = 'Negative', 'Neutral', 'Positive'
                chunks = [score[0]*100, score[1]*100, score[2]*100]
                sep = (0, 0, 0.1)
                fig1, ax1 = plot.subplots()
                ax1.pie(chunks, explode=sep, labels=label, autopct='%1.1f%%')
                ax1.axis('equal')
                plot.savefig("stockfigure.jpg")
                image = Image.open('stockfigure.jpg')
                image_name = 'stockfigure.jpg'
                wordcloudname = 'stockWordCloud.jpg'
                pixmap = QPixmap(image_name)
                pixmap2 = QPixmap(wordcloudname)
                self.label_12.setScaledContents(True)
                self.label_12.setPixmap(pixmap)
                self.label_13.setPixmap(pixmap2)


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=2, height=1, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


def main():
    app = QApplication(sys.argv)

    form = StonksGui()
    form.show()
    app.exec()


if __name__ == '__main__':
    main()
