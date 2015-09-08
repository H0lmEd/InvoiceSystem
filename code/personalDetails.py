from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QFormLayout, QLabel, QLineEdit,
                                QCheckBox, QTextEdit, QPushButton)
from PyQt5.QtWidgets import QButtonGroup, QInputDialog, QMessageBox
import urllib
import urllib2
import json


class custDetailForm(QWidget):
    def __init__(self, parent=None):
        super(custDetailForm, self).__init__(parent)
        layout = QFormLayout()
        def pcLookup():
            url = "https://pcls1.craftyclicks.co.uk/json/"
                
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
