from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QFormLayout, QLabel, QLineEdit,
                                QCheckBox, QTextEdit, QPushButton)
from PyQt5.QtWidgets import QButtonGroup, QInputDialog, QMessageBox
import json
import urllib
import requests
class custDetailForm(QWidget):
    def __init__(self, parent=None):
        super(custDetailForm, self).__init__(parent)
        layout = QFormLayout()
        def pcLookup():
            try:
                url = 'https://api.getaddress.io/v2/uk/S403LQ/3'
                apiKey = 'qcvy-u9WH02l9QCKJclAFA1568'
                payload = {'api_key': apiKey}
                req = urllib.request.Request(url + urllib.parse.urlencode(payload))
                res = urllib.request.urlopen(req)
                response = json.load(res.read())
                print(response)
                #headr = {'apikey': 'qcvy-u9WH02l9QCKJclAFA1568'}
                #response.add_header("apikey","qcvy-u9WH02l9QCKJclAFA1568")
                #rawData = urllib.request.urlopen(response)
                #string = rawData.read().decode('utf-8')
                data = response.json()
                print(data)
                
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
