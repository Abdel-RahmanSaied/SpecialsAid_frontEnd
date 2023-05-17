from PyQt5 import QtWidgets, QtCore
from views import home_view
from PyQt5.QtGui import QPixmap, QPainter


class HomeScreen(QtWidgets.QWidget, home_view.Ui_MainWindow):
    loginAcceptedSignal = QtCore.pyqtSignal()

    def __init__(self):
        super(HomeScreen, self).__init__()
        self.setupUi(self)



if __name__ == "__main__":
    import qdarkstyle
    app = QtWidgets.QApplication([])
    w = HomeScreen()
    w.show()
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()