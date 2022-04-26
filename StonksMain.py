import sys
from stockAnalysisFunctions import *
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QTextEdit
from PyQt5 import QtCore, QtGui, QtWidgets, uic 
import newGui
import pandas as pd
import numpy
class StonksGui(QtWidgets.QMainWindow, newGui.Ui_MainWindow):
	def __init__(self, parent=None):
		super(StonksGui, self).__init__(parent)
		self.setupUi(self)
		price=0
		pricezero=str(price)
		self.label.setText(pricezero)
		self.label_2.setText(pricezero)
		self.enterPressed()

	def initUI(self):
		self.label.setText('Word')

	def enterPressed(self):
		self.pushButton.clicked.connect(self.getinfo)

	def getinfo(self):
		stock=self.lineEdit.text()
		currPrice=str(getStockPrice(stock))
		self.label.setText(currPrice)

	
def main():
	app = QApplication(sys.argv)
	form=StonksGui()
	form.show()
	app.exec()

if __name__== '__main__':
	main()
