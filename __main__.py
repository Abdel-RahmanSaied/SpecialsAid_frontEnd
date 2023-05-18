from PyQt5 import QtWidgets, QtGui, QtCore
from views_mangers.welcomeView_Manger import WelcomeScreen

from PyQt5.QtCore import QTimer, QThread, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QImage, QPixmap, QPainter
class SpecialsAid(QtWidgets.QStackedWidget):
    def __init__(self, name=None, *args, **kwargs):
        super(SpecialsAid, self).__init__()

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/7069717.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Specials Aid"))
        self.showMaximized()

        self.base_url = "https://illacc.pythonanywhere.com"

        #install widget
        self.welcomeScreen = WelcomeScreen()

        # add widgets to the stack
        self.addWidget(self.welcomeScreen) #0 done


    def clear_login(self):
        self.login_manger.username_lin.clear()
        self.login_manger.password_lin.clear()



if __name__ == "__main__":
    # import qdarkstyle
    app = QtWidgets.QApplication([])
    w = SpecialsAid()
    w.show()
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()