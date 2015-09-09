from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QFormLayout, QLabel, QLineEdit,
                                QCheckBox, QTextEdit, QPushButton)
from PyQt5.QtWidgets import QButtonGroup, QInputDialog, QMessageBox
import json
import urllib.request
class custDetailForm(QWidget):
    def __init__(self, parent=None):
        super(custDetailForm, self).__init__(parent)
        layout = QFormLayout()
        def pcLookup():
            try:
                response = urllib.request.Request('http://uk-postcodes.com/postcode/s403lq.json')
                print(response)
                response.add_header("APIKEY")
                rawData = urlopen(response)
                string = rawData.read().decode('utf-8')
                data = json.loads(string)
                
            except ConnectionError as d:
                print (d)
                print ("error")
            print (data)
        #WIDGETS
        nameLabel = QLabel('Full Name:')
        self.nameEdit = QLineEdit(self)

        addrLabel = QLabel('Home Address:')
        self.addrEdit = QTextEdit(self)
        pcLabel = QLabel('Post Code:')
        self.pcEdit = QLineEdit(self)
        pcBtn = QPushButton('Look up', self)
        pcBtn.clicked.connect(pcLookup)





        layout.addRow(nameLabel, self.nameEdit)
        layout.addRow(addrLabel, self.addrEdit)
        layout.addRow(pcLabel, self.pcEdit)
        layout.addRow(pcBtn)
        self.setLayout(layout)
