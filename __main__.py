import json

from views_mangers.welcomeView_Manger import WelcomeScreen
from views_mangers.homeView_manger import HomeScreen
from views_mangers.mainCollectionView_manger import MainViewScreen
from views_mangers.collectionsView_manger import CollectionsScreen
from views_mangers.collectionView_manger import CollectionScreen
from views.dark_sheet import Theme_Modes
from views_mangers.addCollectionView_manager import AddCollectionScreen
from views_mangers.addSymbolView_manger import AddSymbolScreen
from views_mangers.mySymbolsView_manger import MySymbolsScreen

from views_mangers.textToTalk import TextToSpeech

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QTimer, QThread, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QImage, QPixmap, QPainter

from setting import styleSheets


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
        self.fullText = ""
        self.token = ""

        # install widget
        self.welcomeScreen = WelcomeScreen()
        self.homeScreen = HomeScreen()
        self.mainScreen = MainViewScreen()
        self.collecionsScreen = CollectionsScreen()
        self.addcollectionScreen = AddCollectionScreen()
        self.addSymbolScreen = AddSymbolScreen()
        self.mySymbolsScreen = MySymbolsScreen()
        self.collectionViewScreen = CollectionScreen()

        self.textToSpeech = TextToSpeech()

        # add widgets to the stack
        self.addWidget(self.welcomeScreen)  # 0 done
        self.addWidget(self.homeScreen)  # 1 done
        self.addWidget(self.mainScreen)  # 2 done
        self.addWidget(self.collecionsScreen)  # 3 done
        self.addWidget(self.addcollectionScreen)  # 4 done
        self.addWidget(self.addSymbolScreen)  # 5 done
        self.addWidget(self.mySymbolsScreen)  # 6 done
        self.addWidget(self.collectionViewScreen)  # 7 done
        # install welcome signals

        self.welcomeScreen.DoneSignal.connect(self.handleEndTutorial)
        if not self.inToutorialMode():
            self.handleHomeScreen()

        # install home buttons
        self.homeScreen.me_btn.clicked.connect(self.handleMainScreen)
        self.homeScreen.loginAcceptedSignal.connect(self.handle_login)
        self.homeScreen.symbols_btn.clicked.connect(lambda: self.setCurrentIndex(6))

        # install main buttons
        self.mainScreen.back_btn.clicked.connect(lambda: self.setCurrentIndex(1))

        # install collections buttons
        self.collecionsScreen.back_to_home_btn.clicked.connect(lambda: self.setCurrentIndex(1))

        #install collections view buttons
        self.collectionViewScreen.back_btn.clicked.connect(lambda : self.setCurrentIndex(2))
        self.collectionViewScreen.delete_btn.clicked.connect(self.clearLblText)
        self.collectionViewScreen.play_btn.clicked.connect(self.textToTalkFull)
        self.collectionViewScreen.textSignal.connect(self.textToTalk)

        # install add collection buttons
        self.addcollectionScreen.back_to_home_btn.clicked.connect(lambda: self.setCurrentIndex(1))
        self.addcollectionScreen.add_symbol_btn.clicked.connect(lambda: self.setCurrentIndex(5))

        # install add symbol buttons
        self.addSymbolScreen.back_to_home_btn.clicked.connect(lambda: self.setCurrentIndex(1))
        self.addSymbolScreen.add_collection_btn.clicked.connect(lambda: self.setCurrentIndex(4))

        # install my symbols buttons
        self.mySymbolsScreen.back_btn.clicked.connect(lambda: self.setCurrentIndex(1))

        # install play button
        self.mainScreen.play_btn.clicked.connect(self.textToTalkFull)
        # install clear button
        self.mainScreen.delete_btn.clicked.connect(self.clearLblText)

        # install text to talk signals
        self.mainScreen.textSignal.connect(self.textToTalk)
        self.mainScreen.collectionIDSignal.connect(self.handleMainToCollection)
        self.mySymbolsScreen.symbolIDSignal.connect(self.handleMySymbols)
        # self.mainScreen.textToTalkFullSignal.connect(self.textToTalkFull)
        # self.mainScreen.clearTextToTalkSignal.connect(self.clearTextToTalk)

    def textToTalk(self, obj, text):
        self.fullText += " " + text
        self.setLblText(obj)
        self.textToSpeech.speechText(text)

    def setLblText(self, obj):
        self.collectionViewScreen.text_to_talk_lbl.setText(self.fullText)
        self.mainScreen.text_to_talk_lbl.setText(self.fullText)

    def clearLblText(self):
        self.fullText = ""
        self.collectionViewScreen.text_to_talk_lbl.setText(self.fullText)
        self.mainScreen.text_to_talk_lbl.setText(self.fullText)
        self.textToSpeech.clearList()

    def textToTalkFull(self):
        self.textToSpeech.speechFullText()

    def clearTextToTalk(self):
        self.textToSpeech.clearList()

    def handleTextlabel(self, text):
        fullText = self.text_to_talk_lbl.text()
        fullText += " " + text
        self.text_to_talk_lbl.setText(fullText)

    def handleHomeScreen(self):
        self.setCurrentIndex(1)

    def handle_login(self, token):
        self.token = token
        self.addcollectionScreen.token = token
        self.addSymbolScreen.token = token
        self.setCurrentIndex(4)

    def handleMainScreen(self):
        if self.mainScreen.firstTime:
            self.mainScreen.run()
            self.mainScreen.firstTime = False
        self.setCurrentIndex(2)
        self.clear_login()

    def handleMainToCollection(self, collectionID):
        self.collectionViewScreen.collectionID = collectionID
        self.collectionViewScreen.run()
        self.setCurrentIndex(7)

    def handleMySymbols(self, symbolID):
        if self.mainScreen.firstTime:
            self.mainScreen.run()
            self.mainScreen.firstTime = False
        self.setCurrentIndex(6)

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
        self.homeScreen.username_lin.setText("")
        self.homeScreen.Password_lin.setText("")


if __name__ == "__main__":
    # import qdarkstyle
    app = QtWidgets.QApplication([])
    w = SpecialsAid()
    w.show()
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()
