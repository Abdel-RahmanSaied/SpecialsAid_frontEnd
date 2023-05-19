from PyQt5 import QtWidgets, QtCore, QtGui
from views import main_view
from views_mangers.progrssBar import WaitingScreen
from PyQt5.QtCore import pyqtSignal
import requests
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QWidget

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

class MainViewScreen(QtWidgets.QWidget, main_view.Ui_Form):
    loginAcceptedSignal = QtCore.pyqtSignal()

    def __init__(self):
        super(MainViewScreen, self).__init__()
        self.setupUi(self)
        self.base_url = "https://specialaid.pythonanywhere.com/"
        self.firstTime = True

        self.btnList = [
            self.collect1_btn, self.collect1_btn_2, self.collect1_btn_3, self.collect1_btn_4, self.collect1_btn_5,
            self.collect1_btn_6, self.collect1_btn_7, self.collect1_btn_8, self.collect1_btn_9,
        ]

        self.labelsList = ['textCollection_lbl', 'textCollection_lbl_2', 'textCollection_lbl_3', 'textCollection_lbl_4',
                           'textCollection_lbl_5', 'textCollection_lbl_6', 'textCollection_lbl_7',
                           'textCollection_lbl_8', 'textCollection_lbl_9']

        self.threadpool = QtCore.QThreadPool()

    def run(self):
        worker = ApiWorker(self.base_url + "symbols/symbols_collection/")
        worker.setAutoDelete(True)
        self.loading = WaitingScreen()
        worker.signals.finished.connect(self.handleCollection)
        worker.signals.setButtonIcon.connect(self.setButtonIcon)
        self.loading.show()
        self.threadpool.start(worker)

    def handleCollection(self, data):
        for i in range(len(data['results'])):
            self.btnList[i].clicked.connect(lambda ch, i=i: self.handleCollectionBtn(data['results'][i]['id']))
            self.threadpool.globalInstance().findChild(QtCore.QThreadPool, 'globalInstance')
            self.threadpool.start(lambda i=i: self.setButtonIcon(self.btnList[i], data['results'][i]['collection_image']))
            self.threadpool.start(lambda i=i: self.setTextLabel(self.labelsList[i], data['results'][i]['name']))
        self.loading.close()

    def setButtonIcon(self, btn, url):
        photo = self.get_image(url)
        icon = QIcon(photo)
        btn.setIcon(icon)
        btn.setIconSize(QtCore.QSize(180, 180))

    def setTextLabel(self, label, text):
        label = self.findChild(QtWidgets.QLabel, label)
        label.setText(text)

    def handleCollectionBtn(self, id):
        print(id)

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
    w = MainViewScreen()
    w.show()
    w.run()
    app.exec_()
