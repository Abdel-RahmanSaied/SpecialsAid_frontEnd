from PyQt5 import QtWidgets, QtCore
from views import add_collection_view
from PyQt5.QtCore import pyqtSignal
import requests


class AddCollectionScreen(QtWidgets.QWidget, add_collection_view.Ui_Form):
    loginAcceptedSignal = QtCore.pyqtSignal()

    def __init__(self):
        super(AddCollectionScreen, self).__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    w = AddCollectionScreen()
    w.show()
    app.exec_()
