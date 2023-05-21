from PyQt5 import QtWidgets, QtCore
from views import add_symbol_view
from PyQt5.QtCore import pyqtSignal
import requests


class AddSymbolScreen(QtWidgets.QWidget, add_symbol_view.Ui_Form):

    def __init__(self):
        super(AddSymbolScreen, self).__init__()
        self.setupUi(self)
        self.base_url = 'https://specialaid.pythonanywhere.com/'
        self.token = ''
        self.upload_symbol_btn.clicked.connect(self.run)
        self.choose_file_btn.clicked.connect(self.getfiles)
        self.fileName = None
        self.msg = QtWidgets.QMessageBox()
        self.msg.setStyleSheet("min-width: 20cm; ")
        self.load_collections()

    def load_collections(self):
        self.collections_url = f"{self.base_url}symbols/symbols_collection/"
        try:
            response = requests.get(url=self.collections_url,headers={"Accept": "application/json ; indent=4"})
            response.raise_for_status()
            collections_data = response.json()
            collections = collections_data.get('results', [])
            if isinstance(collections, list):
                self.collection_combobox.addItems([collection['name'] for collection in collections])
            else:
                self.msg.critical(self, "Error", "Invalid response format")
        except requests.exceptions.RequestException as e:
            self.msg.critical(self, "Error", f"Error in load collections: {e}")
            
    def run(self):
        headers = {"Accept": "application/json", "Authorization": f"Token {self.token}"}
        #how to get element index by its key
        name = self.symbol_name_lin.text()
        collection = self.collection_combobox.currentText()
        text_to_talk = self.text_to_talk_lin.text()
        if not name:
            self.msg.critical(self, "Error", "Please enter a name")
        elif not self.fileName:
            self.msg.critical(self, "Error", "Please choose a file")
            self.getfiles(event=None)
        else:
            data = {
                "name": name,
                "collection": collection,
                "text_to_talk": text_to_talk,
            }
            try:
                files = [
                    ('symbol_image', (self.fileName, open(self.fileName, 'rb').read(), 'image/jpeg'))
                ]
                self.uploadSymbol(data, files, headers)
            except Exception as filesError:
                self.msg.critical(self, "Error", f"Error in files {filesError}")

    def uploadSymbol(self, data, files, headers):
        url = f"{self.base_url}symbols/symbols/"
        try:
            response = requests.post(url=url, data=data, files=files, headers=headers)
            if response.status_code == 201:
                self.msg.information(self, "Success", "Symbol added successfully")
                self.symbol_name_lin.setText("")
                self.collection_combobox.setCurrentIndex(0)
                self.text_to_talk_lin.setText("")
                self.fileName = None
            else:
                response_data = response.json()
                error_message = response_data.get("detail", "Unknown error")
                self.msg.critical(self, "Error", f"Symbol upload failed: {error_message}")
        except Exception as e:
            self.msg.critical(self, "Error", f"Error in upload symbol {e}")

    def getfiles(self, event):
        self.fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Single File', '',
                                                                 'Images (*.png *.jpeg *.jpg)')
        if not self.fileName:
            self.msg.critical(self, "Error", "Please choose a file")
            self.symbol_location_lin.setText("Please choose a file")
        else:
            self.symbol_location_lin.setText(self.fileName)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    w = AddSymbolScreen()
    w.show()
    app.exec_()
