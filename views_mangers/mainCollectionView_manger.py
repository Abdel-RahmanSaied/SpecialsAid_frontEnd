from PyQt5 import QtWidgets, QtCore, QtGui
from views import main_view
from PyQt5.QtCore import pyqtSignal
import requests
from PyQt5.QtGui import QIcon, QPixmap, QImage, QPalette, QBrush


class MainViewScreen(QtWidgets.QWidget, main_view.Ui_Form):
    loginAcceptedSignal = QtCore.pyqtSignal()
    def __init__(self):
        super(MainViewScreen, self).__init__()
        self.setupUi(self)
        # self.IMainPhotoUrl = "https://storage.googleapis.com/symbols/arasaac/I.png"
        # self.IWantPhotoUrl = "https://storage.googleapis.com/symbols/arasaac/I%20want.png"
        # self.IDontWantPhotoUrl = "https://storage.googleapis.com/symbols/arasaac/I%20do%20not%20want.png"
        # self.setConstrainPhotos()

    def getPhoto(self, url):
        response = requests.get(url)
        photo = response.content
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(photo)
        return pixmap

    # def setConstrainPhotos(self):
    #     self.i_btn.setIcon(QIcon(self.getPhoto(self.IMainPhotoUrl)))
    #     self.iWant_btn.setIcon(QIcon(self.getPhoto(self.IWantPhotoUrl)))
    #     self.iDontWant_btn.setIcon(QIcon(self.getPhoto(self.IDontWantPhotoUrl)))
    #     self.i_btn.setIconSize(QtCore.QSize(180, 180))
    #     self.iWant_btn.setIconSize(QtCore.QSize(180, 180))
    #     self.iDontWant_btn.setIconSize(QtCore.QSize(180, 180))




if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    w = MainViewScreen()
    w.show()
    app.exec_()
