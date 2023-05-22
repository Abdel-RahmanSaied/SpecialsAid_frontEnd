from PyQt5 import QtCore, QtGui, QtNetwork, QtWidgets
import sys


class CheckConnectivity(QtCore.QObject):
    def __init__(self, *args, **kwargs):
        QtCore.QObject.__init__(self, *args, **kwargs)
        url = QtCore.QUrl("https://specialaid.pythonanywhere.com/symbols/symbols_collection/")
        req = QtNetwork.QNetworkRequest(url)
        self.net_manager = QtNetwork.QNetworkAccessManager()
        self.res = self.net_manager.get(req)
        self.res.finished.connect(self.processRes)
        self.res.error.connect(self.processErr)
        self.msg = QtWidgets.QMessageBox()

    @QtCore.pyqtSlot()
    def processRes(self):
        if self.res.bytesAvailable():
            self.msg.information(None, "Info", "You are connected to the Internet.")
        self.res.deleteLater()

    @QtCore.pyqtSlot(QtNetwork.QNetworkReply.NetworkError)
    def processErr(self, code):
        self.msg.critical(None, "Info", "You are not connected to the Internet.")
        print(code)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ic = CheckConnectivity()
    sys.exit(app.exec_())
