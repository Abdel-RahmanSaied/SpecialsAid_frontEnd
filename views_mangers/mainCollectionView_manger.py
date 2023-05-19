from PyQt5 import QtWidgets, QtCore
from views import main_view
from PyQt5.QtCore import pyqtSignal
import requests


class MainViewScreen(QtWidgets.QWidget, main_view.Ui_Form):
    loginAcceptedSignal = QtCore.pyqtSignal()

    def __init__(self):
        super(MainViewScreen, self).__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    w = MainViewScreen()
    w.show()
    app.exec_()
