import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QTextEdit
from PyQt5 import QtCore, QtGui, QtWidgets, uic 
import newGui
class StonksGui(QtWidgets.QMainWindow, newGui.Ui_MainWindow):
	def __init__(self, parent=None):
		super(StonksGui, self).__init__(parent)
		self.setupUi(self)
		##self.centralWidget=QtWidgets.QWidget(MainWindow)
    
def main():
	app = QApplication(sys.argv)
	form=StonksGui()
	form.show()
	app.exec()

if __name__== '__main__':
	main()

##app = QApplication(sys.argv)
##UIWindow = UI()
##app.exec_()