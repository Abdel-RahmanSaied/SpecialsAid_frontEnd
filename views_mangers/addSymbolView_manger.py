from PyQt5 import QtWidgets, QtCore
from views import add_symbol_view
from PyQt5.QtCore import pyqtSignal
import requests


class AddSymbolScreen(QtWidgets.QWidget, add_symbol_view.Ui_Form):
    loginAcceptedSignal = QtCore.pyqtSignal()

    def __init__(self):
        super(AddSymbolScreen, self).__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    w = AddSymbolScreen()
    w.show()
    app.exec_()
