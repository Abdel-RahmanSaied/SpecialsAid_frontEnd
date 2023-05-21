from PyQt5 import QtWidgets, QtCore, QtGui
from views import my_symbols_view
from PyQt5.QtCore import pyqtSignal
from views_mangers.progrssBar import WaitingScreen
from PyQt5.QtWidgets import *
import requests
from PyQt5.QtGui import QPixmap, QPainter


class ApiWorkerSignals(QtCore.QObject):
    finished = QtCore.pyqtSignal(dict)
    setButtonIcon = QtCore.pyqtSignal(object, str)


class ApiWorker(QtCore.QRunnable):
    def __init__(self, url):
        super(ApiWorker, self).__init__()
        self.url = url
        self.signals = ApiWorkerSignals()

    def run(self):
        data = self.getUrlData(self.url)
        self.signals.finished.emit(data)

    def getUrlData(self, url):
        response = requests.get(url)
        data = response.json()
        return data

    def get_image(self, url):
        response = requests.get(url)
        photo = response.content
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(photo)
        return pixmap


class MySymbolsScreen(QtWidgets.QWidget, my_symbols_view.Ui_Form):
    DoneSignal = QtCore.pyqtSignal()
    collectionIDSignal = pyqtSignal(int)

    def __init__(self):
        super(MySymbolsScreen, self).__init__()
        self.setupUi(self)
        self.base_url = "https://specialaid.pythonanywhere.com/"
        self.firstTime = True
        self.symbol_frame=self.frame_2
        self.symbol_label=self.label_2
        self.threadpool = QtCore.QThreadPool()

    def run(self):
        worker = ApiWorker(self.base_url + "symbols/symbols/")
        worker.setAutoDelete(True)
        self.loading = WaitingScreen()
        worker.signals.finished.connect(self.handleSymbols)
        self.loading.show()
        self.threadpool.start(worker)

    def handleSymbols(self, data):
        data = [data]
        for i in range(data):
            self.threadpool.globalInstance().findChild(QtCore.QThreadPool, 'globalInstance')
            self.threadpool.start(
                lambda i=i: self.setButtonIcon(self.symbol_frame[i], data['results'][i]['image']))
                self.threadpool.start(lambda i=i: self.setTextLabel(self.symbol_label[i], data['results'][i]['name']))
        self.loading.close()




if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    w = MySymbolsScreen()
    w.show()
    app.exec_()