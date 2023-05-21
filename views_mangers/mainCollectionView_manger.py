from PyQt5 import QtWidgets, QtCore, QtGui
from views import main_view
from views_mangers.progrssBar import WaitingScreen
from PyQt5.QtCore import pyqtSignal
import requests
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QWidget

from views_mangers.textToTalk import TextToSpeech

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
    textSignal = pyqtSignal(object, str)
    collectionIDSignal = pyqtSignal(int)

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

        self.i_btn.clicked.connect(self.handleIbtn)
        self.iWant_btn.clicked.connect(self.handleIWant_btn)
        self.iDontWant_btn.clicked.connect(self.handleIDontWant_btn)
        self.yes_btn.clicked.connect(self.handleYes_btn)
        self.no_btn.clicked.connect(self.handleNo_btn)

    def run(self):
        worker = ApiWorker(self.base_url + "symbols/symbols_collection/")
        worker.setAutoDelete(True)
        self.loading = WaitingScreen()
        worker.signals.finished.connect(self.handleCollection)
        worker.signals.setButtonIcon.connect(self.setButtonIcon)
        self.loading.show()
        self.threadpool.start(worker)

    def sendTextSignal(self, text):
        self.textSignal.emit('text_to_talk_lbl', text)

    def handleIbtn(self):
        self.sendTextSignal('i')
    def handleIWant_btn(self):
        self.sendTextSignal('want')
    def handleIDontWant_btn(self):
        self.sendTextSignal('dont want')

    def handleYes_btn(self):
        self.sendTextSignal('yes')
    def handleNo_btn(self):
        self.sendTextSignal('no')


    def handleCollection(self, data):
        dataCount = [data['count'] if data['count'] < 9 else 9][0]
        for i in range(dataCount):
            self.btnList[i].clicked.connect(lambda ch, i=i: self.handleCollectionBtn(data['results'][i]['id']))
            self.threadpool.globalInstance().findChild(QtCore.QThreadPool, 'globalInstance')
            self.threadpool.start(
                lambda i=i: self.setButtonIcon(self.btnList[i], data['results'][i]['collection_image']))
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
        self.collectionIDSignal.emit(id)

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
