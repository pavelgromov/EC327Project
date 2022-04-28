import sys
# from typing_extensions import Self
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


class StonksGui(QtWidgets.QMainWindow, newGui.Ui_MainWindow,QGraphicsView,QGraphicsScene):
    def __init__(self, parent=None):
        super(StonksGui, self).__init__(parent)
        self.setupUi(self)
        price = 0
        pricezero = str(price)
        self.label.setText(pricezero)
        self.label_2.setText(pricezero)
        self.label_6.setText(pricezero)
        self.label_8.setText(pricezero)
        self.label_11.setText(pricezero)
        self.enterPressed()
        self.label_3.setText("Current Price:")
        self.label_4.setText("Last Open Price:")
        self.label_7.setText("Last Close Price:")
        self.label_9.setText("52 Week High:")
        self.label_10.setText("52 Week Low:")

    def initUI(self):
        self.label.setText('Word')

    def enterPressed(self):
        self.pushButton.clicked.connect(self.getinfo)
        self.pushButton.clicked.connect(self.makePlot)

    def getinfo(self):
        stock = self.lineEdit.text()
        currPrice = str(getStockPrice(stock))
        openPrice = str(getOpenPrice(stock))
        YearHigh = str(getYearlyHigh(stock))
        YearLow = str(getYearlyLow(stock))
        # closePrice=str(getClosePrice(stock))
        self.label.setText(currPrice)
        self.label_2.setText(openPrice)
        # self.label_6.setText(closePrice)
        self.label_8.setText(YearHigh)
        self.label_11.setText(YearLow)

    def makePlot(self):
        Figure(figsize=(331,241),dpi=1)
        stock = self.lineEdit.text()
        tweets = get_tweets(stock)
        score = getPolarity(tweets)
        label = 'Negative', 'Neutral', 'Postive'
        chunks = [score[0]*100, score[1]*100, score[2]*100]
        sep = (0, 0, 0.1)
        fig1, ax1 = plot.subplots()
        ax1.pie(chunks, explode=sep, labels=label, autopct='%1.1f%%')
        ax1.axis('equal')
        plot.savefig("stockfigure.jpg")
        image=Image.open('stockfigure.jpg')
        image_name='stockfigure.jpg'
        wordcloudname='stockWordCloud.jpg'
        pixmap=QPixmap(image_name)
        pixmap2=QPixmap(wordcloudname)
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

