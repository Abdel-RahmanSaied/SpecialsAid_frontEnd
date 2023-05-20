from PyQt5 import QtWidgets, QtCore
from views import home_view
from PyQt5.QtCore import pyqtSignal
import requests


class HomeScreen(QtWidgets.QWidget, home_view.Ui_Form):
    loginAcceptedSignal = QtCore.pyqtSignal()

    def __init__(self):
        super(HomeScreen, self).__init__()
        self.setupUi(self)
        self.tabWidget.tabBar().setCurrentIndex(0)
        self.login_btn.clicked.connect(self.handle_login)
        self.base_url = "https://specialaid.pythonanywhere.com/auth/login/"
        self.userToken = ''

    def handle_login(self):
        msg = QtWidgets.QMessageBox()
        username = self.username_lin.text()
        password = self.Password_lin.text()
        if len(username) == 0:
            msg.setWindowTitle("Warning")
            msg.setText("you must fill all fields !")
            msg.exec_()
        elif len(password) == 0:
            msg.setWindowTitle("Warning")
            msg.setText("you must fill all fields !")
            msg.exec_()
        else:
            data = {
                "username": username,
                "password": password

            }
            try:
                self.user_check = requests.post(self.base_url, data=data)
                self.json_response = self.user_check.json()
                self.json_statusCode = self.user_check.status_code
            except (requests.ConnectionError, requests.Timeout) as exception:
                print(exception)
                msg.setWindowTitle("Warning")
                msg.setText("No internet connection.")
                msg.exec_()
            try:
                if self.json_statusCode == 200:
                    self.userToken = self.json_response['token']
                    self.username = self.json_response['email']
                    self.loginAcceptedSignal.emit()

                elif self.json_statusCode == 401:
                    msg.setWindowTitle("Warning")
                    msg.setText("username or password was incorrect")
                    msg.exec_()
                else:
                    msg.setWindowTitle("Warning")
                    msg.setText(str(self.user_check['Error']))
                    msg.exec_()

            except Exception as error:
                print(error)
                msg.setWindowTitle("Warning")
                msg.setText("Something went wrong.")
                msg.exec_()

            except Exception as error:
                print(error)

    def clear(self):
        self.username_lin.setText("")
        self.Password_lin.setText("")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    w = HomeScreen()
    w.show()
    app.exec_()
