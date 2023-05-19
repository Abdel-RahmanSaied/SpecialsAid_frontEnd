import json

from views_mangers.welcomeView_Manger import WelcomeScreen
from views_mangers.homeView_manger import HomeScreen
from views_mangers.mainCollectionView_manger import MainViewScreen

from PyQt5 import QtWidgets, QtGui, QtCore
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

        self.base_url = "https://specialaid.pythonanywhere.com/"

        # install widget
        self.welcomeScreen = WelcomeScreen()
        self.homeScreen = HomeScreen()
        self.mainScreen = MainViewScreen()

        # add widgets to the stack
        self.addWidget(self.welcomeScreen)  # 0 done
        self.addWidget(self.homeScreen)  # 1 done
        self.addWidget(self.mainScreen)  # 2 done

        # install welcome signals
        self.welcomeScreen.DoneSignal.connect(self.handleEndTutorial)
        if not self.inToutorialMode():
            self.handleHomeScreen()

        # install home buttons
        self.homeScreen.me_btn.clicked.connect(self.handleMainScreen)

    def handleHomeScreen(self):
        self.setCurrentIndex(1)

    def handleMainScreen(self):
        self.setCurrentIndex(2)

    def handleEndTutorial(self):
        self.handleHomeScreen()
        with open('setting/setting.json', ) as file:
            setting = json.load(file)
            setting['inStartupMode'] = False
        # Write updated setting back to file
        with open('setting/setting.json', 'w') as file:
            json.dump(setting, file)

    def inToutorialMode(self):
        with open('setting/setting.json', ) as s:
            setting = json.load(s)
        return setting.get('inStartupMode')

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
