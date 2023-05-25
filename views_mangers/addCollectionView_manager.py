from PyQt5 import QtWidgets, QtCore
from views import add_collection_view
from PyQt5.QtCore import pyqtSignal
import requests
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from views_mangers.progrssBar import WaitingScreen


class AddCollectionScreen(QtWidgets.QWidget, add_collection_view.Ui_Form):
    loginAcceptedSignal = QtCore.pyqtSignal()
    refreshSignal_collections = QtCore.pyqtSignal()

    def __init__(self):
        super(AddCollectionScreen, self).__init__()
        self.setupUi(self)
        self.base_url = 'https://specialaid.pythonanywhere.com/'
        self.token = ''
        self.upload_collection_btn.clicked.connect(self.run)
        self.choose_file_btn.clicked.connect(self.getfiles)
        self.firstTime = False
        self.fileName = None

        self.msg = QtWidgets.QMessageBox()
        self.msg.setStyleSheet("min-width: 20cm; ")

    def run(self):
        headers = {"Accept": "application/json ; indent=4", "Authorization": f"Token {self.token}"}
        name = self.collection_name_lin.text()
        dimension_of_symbols = "2*2"

        if not name:
            self.msg.critical(self, "Error", "Please enter a name")
        elif not self.fileName:
            self.msg.critical(self, "Error", "Please choose a file")
            self.getfiles(event=None)

        else:
            data = {
                "name": name,
                "dimension_of_symbols": dimension_of_symbols,
            }
            try:
                files = [
                    ('collection_image', (self.fileName, open(self.fileName, 'rb').read(), 'image/jpeg'))
                ]
            except Exception as filesError:
                self.msg.critical(self, "Error", f"Error in files {filesError}")
            else:
                self.waitingScreen = WaitingScreen()
                self.waitingScreen.show()
                QtWidgets.QApplication.processEvents()  # Process pending events to update the waiting screen
                self.uploadCollection(data, files, headers)
                self.refreshSignal_collections.emit()
    def uploadCollection(self, data, files, headers):
        url = f"{self.base_url}symbols/symbols_collection/"
        try:
            response = requests.post(url=url, data=data, files=files, headers=headers)
            self.waitingScreen.close()
        except requests.exceptions.RequestException as e:
            self.msg.critical(self, "Error", f"An error occurred while making the request with error code: {e}")
        else:
            if response.status_code == 201:
                self.msg.information(self, "Success", "Collection Uploaded Successfully")
                self.collection_name_lin.setText("")
                self.collection_location_lin.setText("")
                self.fileName = None
            else:
                self.msg.critical(self, "Error",
                                  f"An error occurred while making the request with error code: {response.status_code}")

    def getfiles(self, event):
        self.fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Single File', '',
                                                                 'Images (*.png *.jpeg *.jpg)')
        if not self.fileName:
            self.msg.critical(self, "Error", "Please choose a file")
            self.collection_location_lin.setText("Please choose a file")
        else:
            self.collection_location_lin.setText(self.fileName)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    w = AddCollectionScreen()
    w.show()
    app.exec_()
