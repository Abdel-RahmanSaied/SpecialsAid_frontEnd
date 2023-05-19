from PyQt5 import QtWidgets, QtCore
from views import collections_view
from PyQt5.QtCore import pyqtSignal
import requests


class CollectionsScreen(QtWidgets.QWidget, collections_view.Ui_Form):
    loginAcceptedSignal = QtCore.pyqtSignal()

    def __init__(self):
        super(CollectionsScreen, self).__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    w = CollectionsScreen()
    w.show()
    app.exec_()
