from PyQt5 import QtWidgets, QtCore
from views import home_view
from PyQt5.QtCore import pyqtSignal
import requests


class HomeScreen(QtWidgets.QWidget, home_view.Ui_Form):
    loginAcceptedSignal = QtCore.pyqtSignal(str)

    def __init__(self):
        super(HomeScreen, self).__init__()
        self.setupUi(self)
        self.tabWidget.tabBar().setCurrentIndex(0)
        self.login_btn.clicked.connect(self.handle_login)

        self.msg = QtWidgets.QMessageBox()
        self.msg.setStyleSheet("min-width: 20cm; ")

    def handle_login(self):
        if self.checkFields():
            username = self.username_lin.text()
            password = self.Password_lin.text()

            if self.checkAuth(username, password):
                self.clear()
                self.msg.information(self, "Success", "Login Successful")



    def checkFields(self):
        username = self.username_lin.text()
        password = self.Password_lin.text()
        if len(username) == 0:
            self.msg.critical(self, "Error", "Please enter a username")
        elif len(password) == 0:
            self.msg.critical(self, "Error", "Please enter a password")
        else:
            return True

    def checkAuth(self, username, password):
        url = "https://specialaid.pythonanywhere.com/auth/login/"
        data = {
            "username": username,
            "password": password
        }
        try:
            reply = requests.post(url, data=data)
        except (requests.ConnectionError, requests.Timeout) as exception:
            print(exception)
            self.msg.critical(self, "Error", "No internet connection.")
        else:
            if reply.status_code == 200:
                userToken = reply.json()['token']
                self.loginAcceptedSignal.emit(userToken)
                return True
            elif reply.status_code == 401:
                self.msg.critical(self, "Error", reply.json()['Response'])
            else:
                self.msg.critical(self, "Error", "Something went wrong.")



    def clear(self):
        self.username_lin.setText("")
        self.Password_lin.setText("")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    w = HomeScreen()
    w.show()
    app.exec_()
