from PyQt5 import QtWidgets, QtCore, QtGui
from views import my_symbols_view
from PyQt5.QtCore import pyqtSignal
from views_mangers.progrssBar import WaitingScreen
from PyQt5.QtWidgets import *
import requests
from PyQt5.QtGui import QIcon, QPixmap


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
    textSignal = pyqtSignal(object, str)
    symbolIDSignal = pyqtSignal(int)

    def __init__(self):
        super(MySymbolsScreen, self).__init__()
        self.setupUi(self)
        self.base_url = "https://specialaid.pythonanywhere.com/"
        self.firstTime = True
        self.symbol_frame = self.frame_2
        self.symbol_icon = self.symbol_icon_btn
        self.symbol_label = self.label_2
        self.threadpool = QtCore.QThreadPool()

        self.run()

    def run(self):
        worker = ApiWorker(self.base_url + "symbols/symbols/")
        worker.setAutoDelete(True)
        self.loading = WaitingScreen()
        worker.signals.finished.connect(self.handleSymbols)
        self.loading.show()
        self.threadpool.start(worker)

    def handleSymbols(self, data):
        print(data)
        dataCount = data['count']
        print(dataCount)
        # for i in range(dataCount):
        #     self.symbol_icon.clicked.connect(lambda ch, i=i: self.handleCollectionBtn(data['results'][i]['id']))
        #     self.threadpool.globalInstance().findChild(QtCore.QThreadPool, 'globalInstance')
        #     self.threadpool.start(
        #         lambda i = i: self.setButtonIcon(self.symbol_icon[i], data['results'][i]['image']))
        #     self.threadpool.start(lambda i = i: self.setTextLabel(self.symbol_label[i], data['results'][i]['name']))
        self.loading.close()

    def add_frame(self):
        new_frame = self.symbol_frame.clone()
        for i in range(self.dataCount):
            new_frame(i).setObjectName("symbol_frame{}".format(i))

        # def frame_copy(frame, self,):
    #     original_stylesheet =self.symbol_frame.styleSheet()
    #     copied_frames = []
    #     for i in range(self.handleSymbols.num_data):
    #         new_frame = self.symbol_frame.clone()
    #         new_frame.setObjectName("symbol_frame{}".format(i))
    #         new_frame.setStyleSheet(original_stylesheet)
    #         # Copy child widgets from the original frame to the new frame
    def setButtonIcon(self, btn, url):
        photo = self.get_image(url)
        icon = QIcon(photo)
        btn.setIcon(icon)
        btn.setIconSize(QtCore.QSize(180, 180))

    def setTextLabel(self, label, text):
        label = self.findChild(QtWidgets.QLabel, label)
        label.setText(text)

    def handleCollectionBtn(self, id):
        self.symbolIDSignal.emit(id)

    def get_image(self, url):
        response = requests.get(url)
        photo = response.content
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(photo)
        return pixmap

    def closeEvent(self, event):
        self.threadpool.clear()
        event.accept()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    w = MySymbolsScreen()
    w.show()
    app.exec_()
