from PyQt5 import QtWidgets, QtCore
from views import add_collection_view
from PyQt5.QtCore import pyqtSignal
import requests
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *



class AddCollectionScreen(QtWidgets.QWidget, add_collection_view.Ui_Form):
    loginAcceptedSignal = QtCore.pyqtSignal()
    def __init__(self):
        super(AddCollectionScreen, self).__init__()
        self.setupUi(self)
        self.base_url = 'https://specialaid.pythonanywhere.com/'
        self.token = ''
        self.upload_collection_btn.clicked.connect(self.run)
        self.choose_file_btn.clicked.connect(self.getfiles)

    def getfiles(self , event):
        msg = QtWidgets.QMessageBox()
        self.fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Single File', '', 'Images (*.png, *.jpeg , *.jpg) ')
        return self.fileName
    def run(self):
        headers = {"Accept": "application/json ; indent=4",
                   "Content-Type": "application/json", "Authorization": f"Token {self.token}"}
        msg = QtWidgets.QMessageBox()
        msg.setStyleSheet("min-width: 10em; ")
        try :
            self.test_url = f"{self.base_url}symbols/symbols_collection/"

            name = self.collection_name_lin.text()
            dimension_of_symbols = "2*2"

        except Exception as param_errors :
            print("labels error", param_errors)

        try :

            data = {

                "name": name,
                "dimension_of_symbols": dimension_of_symbols,
            }
        except Exception as x:
            print("data error", x)
        try:
            files=[
            ('collection_image', (self.fileName, open(self.fileName, 'rb').read(), 'image/jpeg'))

            ]

        except Exception as RRR:
            msg.setWindowTitle("Warning")
            msg.setText("You Must Select A Photo")
            msg.exec_()
        try :
            response = requests.post(self.test_url, json=data, files=files, headers=headers,)
            if response.status_code == 201:
                msg.setWindowTitle("Successfully")
                msg.setText("Collection has been uploaded successfully")
                msg.setWindowTitle("Success")
                msg.exec_()
            else:
                msg.setWindowTitle("Warning")
                msg.setText(str(response.json()["Response"]))
                msg.exec_()
        except requests.exceptions.RequestException as e:
            print("response error:", e)
            msg.setWindowTitle("Warning")
            msg.setText("An error occurred while making the request")
            msg.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    w = AddCollectionScreen()
    w.show()
    app.exec_()
