from PyQt5 import QtWidgets, QtCore
from views import welcome_view
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import *
import requests
from PyQt5.QtGui import QPixmap, QPainter


class WelcomeScreen(QtWidgets.QWidget, welcome_view.Ui_Form):
    DoneSignal = QtCore.pyqtSignal()

    def __init__(self):
        super(WelcomeScreen, self).__init__()
        self.setupUi(self)

        self.tabWidget.tabBar().setVisible(False)
        self.nest_to_tab_2_btn.clicked.connect(lambda : self.tabWidget.setCurrentIndex(1))
        self.bck_to_tab1_btn.clicked.connect(lambda : self.tabWidget.setCurrentIndex(0))

        self.next_to_tab3_btn.clicked.connect(lambda : self.tabWidget.setCurrentIndex(2))
        self.back_to_tab2_btn.clicked.connect(lambda : self.tabWidget.setCurrentIndex(1))
        self.done_btn.clicked.connect(lambda : self.DoneSignal.emit())






if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    w = WelcomeScreen()
    w.show()
    app.exec_()