from PyQt5 import QtWidgets, QtCore, QtGui
from views import collection_view
from PyQt5.QtCore import pyqtSignal
import requests
from views_mangers.progrssBar import WaitingScreen
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QWidget

class ApiWorkerSignals(QtCore.QObject):
    finished = QtCore.pyqtSignal(dict)
    setButtonIcon = QtCore.pyqtSignal(object, str)

class ApiWorker(QtCore.QRunnable):
    def __init__(self, url, collectionID):
        super(ApiWorker, self).__init__()
        self.url = url
        self.collectionID = collectionID
        self.signals = ApiWorkerSignals()

    def run(self):
        data = self.getUrlData(self.url, self.collectionID)
        self.signals.finished.emit(data)

    def getUrlData(self, url, collectionID):
        params = {"collection__id": collectionID}
        response = requests.get(url=url, params=params)
        data = response.json()
        return data

    def get_image(self, url):
        response = requests.get(url)
        photo = response.content
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(photo)
        return pixmap

class CollectionScreen(QtWidgets.QWidget, collection_view.Ui_Form):
    textSignal = pyqtSignal(object, str)

    def __init__(self):
        super(CollectionScreen, self).__init__()
        self.setupUi(self)

        self.base_url = "https://specialaid.pythonanywhere.com/"
        self.threadpool = QtCore.QThreadPool()
        self.collectionID = 25

        self.btnList = [
            self.collect1_btn, self.collect1_btn_1, self.collect1_btn_2, self.collect1_btn_3,
            self.collect1_btn_4, self.collect1_btn_5,
            self.collect1_btn_6, self.collect1_btn_7, self.collect1_btn_8, self.collect1_btn_9,
            self.collect1_btn_10, self.collect1_btn_11, self.collect1_btn_12, self.collect1_btn_13,
            self.collect1_btn_14, self.collect1_btn_14
        ]
        self.lblList = [
            self.textCollection_lbl_10, self.textCollection_lbl, self.textCollection_lbl_2,
            self.textCollection_lbl_3, self.textCollection_lbl_4, self.textCollection_lbl_5,
            self.textCollection_lbl_6, self.textCollection_lbl_7, self.textCollection_lbl_8,
            self.textCollection_lbl_9, self.textCollection_lbl_11, self.textCollection_lbl_12,
            self.textCollection_lbl_13, self.textCollection_lbl_14, self.textCollection_lbl_15,

        ]

        # self.run()

    def sendTextSignal(self, text):
        self.textSignal.emit('text_to_talk_lbl', text)
    def run(self):
        worker = ApiWorker(self.base_url + "symbols/symbols/", self.collectionID)
        worker.setAutoDelete(True)
        self.loading = WaitingScreen()
        worker.signals.finished.connect(self.handleCollection)
        worker.signals.setButtonIcon.connect(self.setButtonIcon)
        self.clearButtons()
        self.loading.show()
        self.threadpool.start(worker)

    def handleCollection(self, data):
        dataCount = [data['count'] if data['count'] < 15 else 15][0]
        for i in range(dataCount):
            btn = self.btnList[i]
            # try :
            #     btn.clicked.disconnect()
            # except:
            #     pass
            btn.clicked.connect(lambda ch, i=i: self.handleSymbolBtn(data['results'][i]['id'], data['results'][i]['text_to_talk']))
            self.threadpool.globalInstance().findChild(QtCore.QThreadPool, 'globalInstance')
            self.threadpool.start(
                lambda i=i: self.setButtonIcon(self.btnList[i], data['results'][i]['image']))
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

    def get_image(self, url):
        response = requests.get(url)
        photo = response.content
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(photo)
        return pixmap

    def handleSymbolBtn(self, id, textToTalk):
        self.sendTextSignal(textToTalk)


    def clearButtons(self):
        for btn in self.btnList:
            btn.setIcon(QIcon())
            btn.setIconSize(QtCore.QSize(180, 180))
            try:
                btn.clicked.disconnect()
            except:
                pass



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    w = CollectionScreen()
    w.show()
    app.exec_()
