from PyQt5 import QtWidgets, QtCore
from views import home_view
from PyQt5 import QtWidgets
from views import welcome_view
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import *
import requests
from PyQt5.QtGui import QPixmap, QPainter


class WelcomeScreen(QtWidgets.QWidget, welcome_view.Ui_Form):
    loginAcceptedSignal = QtCore.pyqtSignal()

    def __init__(self):
        super(WelcomeScreen, self).__init__()
        self.setupUi(self)



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    w = WelcomeScreen()
    w.show()
    app.exec_()