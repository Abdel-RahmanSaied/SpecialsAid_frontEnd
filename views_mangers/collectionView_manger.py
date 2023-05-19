from PyQt5 import QtWidgets, QtCore
from views import collection_view
from PyQt5.QtCore import pyqtSignal
import requests


class CollectionScreen(QtWidgets.QWidget, collection_view.Ui_Form):
    loginAcceptedSignal = QtCore.pyqtSignal()

    def __init__(self):
        super(CollectionScreen, self).__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    w = CollectionScreen()
    w.show()
    app.exec_()
