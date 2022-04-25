import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QTextEdit
from PyQt5 import uic

class UI(QMainWindow):
	def __init__(self):
		super(UI, self).__init__()
		##self.centralWidget=QtWidgets.QWidget(MainWindow)
		uic.loadUi("GUI.ui", self)

		self.show()

app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()