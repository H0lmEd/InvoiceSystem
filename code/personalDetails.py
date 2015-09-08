from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QFormLayout, QLabel, QLineEdit,
                                QCheckBox, QTextEdit, QPushButton)
from PyQt5.QtWidgets import QButtonGroup, QInputDialog, QMessageBox
import requests


class custDetailForm(QWidget):
    def __init__(self, parent=None):
        super(custDetailForm, self).__init__(parent)
        layout = QFormLayout()
        def pcLookup():
            data = requests.get("http://api.postcodes.io/postcodes/"+"S403LQ").text
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
