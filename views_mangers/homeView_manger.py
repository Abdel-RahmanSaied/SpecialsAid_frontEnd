from PyQt5 import QtWidgets, QtCore
from views import home_view
from PyQt5.QtCore import pyqtSignal
import requests


class HomeScreen(QtWidgets.QWidget, home_view.Ui_Form):
    loginAcceptedSignal = QtCore.pyqtSignal()

    def __init__(self):
        super(HomeScreen, self).__init__()
        self.setupUi(self)
        self.tabWidget.tabBar().setCurrentIndex(0)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    w = HomeScreen()
    w.show()
    app.exec_()
