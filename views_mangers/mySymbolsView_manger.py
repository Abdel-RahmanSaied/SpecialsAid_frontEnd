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
        self.threadpool = QtCore.QThreadPool()

    def run(self):
        worker = ApiWorker(self.base_url + "symbols/symbols/")
        worker.setAutoDelete(True)
        self.loading = WaitingScreen()
        worker.signals.finished.connect(self.handleFrameContent)
        self.loading.show()
        self.threadpool.start(worker)

    # def handleSymbols(self, data):
    #     # print(data)
    #     dataCount = data['count']
    #     # self.create_copies_of_frame(dataCount)
    #     print(data['count'])
    #     # for i in range(dataCount):
    #     #     self.symbol_icon.clicked.connect(lambda ch, i=i: self.handleCollectionBtn(data['results'][i]['id']))
    #     #     self.threadpool.globalInstance().findChild(QtCore.QThreadPool, 'globalInstance')
    #     #     self.threadpool.start(
    #     #         lambda i = i: self.setButtonIcon(self.symbol_icon[i], data['results'][i]['image']))
    #     #     self.threadpool.start(lambda i = i: self.setTextLabel(self.symbol_label[i], data['results'][i]['name']))
    #     self.loading.close()

    def handleFrameContent(self, data):
        dataCount = data['count']
        for id in range(dataCount):
            frame = self.addFrame(id)
            layoutWidget = self.addLayoutWidget(frame, id)
            gridLayout = self.addGridLayout(layoutWidget, id)
            label = self.addLabel(layoutWidget, id)
            button = self.addSymbolButton(layoutWidget, id)
            self.addGridLayoutWidget_forBtn(gridLayout, button, id)
            self.addGridLayoutWidget_forLabel(gridLayout, label, id)
            self.gridLayout_4.addWidget(frame, id // 5, id % 5)  # Add the frame to the grid layout

            self.setFrameContentData(button, label, data, id)
            # self.threadpool.globalInstance().findChild(QtCore.QThreadPool, 'globalInstance')
            # self.threadpool.start(lambda id=id: self.setButtonIcon(button, data['results'][id]['image']))
            # self.threadpool.start(lambda id=id: self.setTextLabel(label, data['results'][id]['name']))
            # button.clicked.connect(lambda ch, id=id: self.handleCollectionBtn(data['results'][id]['id']))

        self.loading.close()

    def addFrame(self, id):
        frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        frame.setMinimumSize(QtCore.QSize(135, 170))
        frame.setMaximumSize(QtCore.QSize(135, 180))
        frame.setStyleSheet("")
        frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        frame.setFrameShadow(QtWidgets.QFrame.Raised)
        frame.setObjectName(f"frame_{id}")
        return frame

    def addLayoutWidget(self, frame, id):
        layoutWidget = QtWidgets.QWidget(frame)
        layoutWidget.setGeometry(QtCore.QRect(0, 0, 132, 175))
        layoutWidget.setObjectName(f"layout_{id}")
        return layoutWidget

    def addGridLayout(self, layoutWidget, id):
        gridLayout = QtWidgets.QGridLayout(layoutWidget)
        gridLayout.setContentsMargins(0, 0, 0, 0)
        gridLayout.setObjectName(f"gridLayout_{id}")
        return gridLayout

    def addSymbolButton(self,layoutWidget, id):
        symbol_icon_btn = QtWidgets.QPushButton(layoutWidget)
        symbol_icon_btn.setMinimumSize(QtCore.QSize(130, 150))
        symbol_icon_btn.setMaximumSize(QtCore.QSize(132, 150))
        symbol_icon_btn.setStyleSheet("background-color: rgb(255, 255, 255,0);\n"
                                           "\n"
                                           "border-color: rgb(255, 255, 255);")
        symbol_icon_btn.setText("")
        symbol_icon_btn.setObjectName(f"symbol_icon_btn_{id}")
        return symbol_icon_btn

    def addLabel(self, layoutWidget, id):
        label = QtWidgets.QLabel(layoutWidget)
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setObjectName(f"label_{id}")
        label.setText("Label")
        return label

    def addGridLayoutWidget_forBtn(self, gridLayout, symbol_icon_btn, id):
        gridLayout.addWidget(symbol_icon_btn, 0, 0, 1, 1)

    def addGridLayoutWidget_forLabel(self, gridLayout, symbol_label, id):
        gridLayout.addWidget(symbol_label, 1, 0, 1, 1)


    def setFrameContentData(self, btn, label, data, id):
        btn.clicked.connect(lambda ch, id=id: self.handleCollectionBtn(data['results'][id]['id']))
        self.threadpool.globalInstance().findChild(QtCore.QThreadPool, 'globalInstance')
        self.threadpool.start(lambda id=id: self.setButtonIcon(btn, data['results'][id]['image']))
        self.threadpool.start(lambda id=id: self.setTextLabel(label, data['results'][id]['name']))

    def setButtonIcon(self, btn, url):
        photo = self.get_image(url)
        icon = QIcon(photo)
        btn.setIcon(icon)
        btn.setIconSize(QtCore.QSize(180, 180))

    def setTextLabel(self, label, text):
        # label = self.findChild(QtWidgets.QLabel, label)
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