from PyQt5 import QtWidgets, QtCore
from views import my_symbols_view
from PyQt5.QtCore import pyqtSignal
import requests


class MySymbolsScreen(QtWidgets.QWidget, my_symbols_view.Ui_Form):
    loginAcceptedSignal = QtCore.pyqtSignal()

    def __init__(self):
        super(MySymbolsScreen, self).__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    w = MySymbolsScreen()
    w.show()
    app.exec_()
