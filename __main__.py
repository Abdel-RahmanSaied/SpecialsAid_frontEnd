from PyQt5 import QtWidgets, QtGui, QtCore
from views_mangers.loginView_Manger import LoginScreen

import sys
from PyQt5.QtCore import QTimer, QThread, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QImage, QPixmap, QPainter
class SpecialsAid(QtWidgets.QStackedWidget):
    def __init__(self, name=None, *args, **kwargs):
        super(SpecialsAid, self).__init__()

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":ICONS/icons/output.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Email Saver"))


        # Load the background image from a file
        self.bg_image = QPixmap("forms/icons/back.jpg")# for pyinstaller

        self.base_url = "https://illacc.pythonanywhere.com"

        #install widget
        self.login_manger = LoginScreen()

        # self.showFullScreen()


        # add widgets to the stack
        self.addWidget(self.login_manger) #0 done

        #istall back-btns
        # self.parkinson_manager.back_btn.clicked.connect(lambda: self.setCurrentIndex(3))



    def clear_login(self):
        self.login_manger.username_lin.clear()
        self.login_manger.password_lin.clear()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), self.bg_image)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    w = SpecialsAid()
    w.show()
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()