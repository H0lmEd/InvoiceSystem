# When customer is new, pcEdit = Box layout of label + button
# When customer isnt new, pcEdit = ButtonLineEdit





from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QFormLayout, QLabel,
                                QCheckBox, QTextEdit, QPushButton)
from PyQt5.QtWidgets import QButtonGroup, QInputDialog, QMessageBox, QVBoxLayout, QToolButton, QStyle, QGroupBox
from PyQt5.QtCore import QSize,pyqtSignal
from PyQt5.QtGui import QIcon
from customButton import ButtonLineEdit
import json
import os
import PyQt5.QtGui
import PyQt5.QtCore
import PyQt5.QtWidgets
import urllib
import requests


class custDetailForm(QWidget):
    def __init__(self, newCustomer, parent=None):
        super(custDetailForm,self).__init__(parent)
        layout = QFormLayout()

        def pcLookup():
            def getHomeNo():
                numberData = QInputDialog()
                numberData.setInputMode(2)
                print(numberData.inputMode())
                numberData.setComboBoxEditable(True)
                numberDialog = numberData.getText(self, "Home Number",
                        "Home Number:")
                print(numberData, numberDialog)
                if numberDialog:
                    print(str(numberDialog[0]))
                    return str(numberDialog[0])
            try:
                apiKey = '?api-key=k-0nPmNhZ06jmM4g29K8yw1962'
                url = 'https://api.getaddress.io/v2/uk/' + self.pcLineEdit.text() +'/' + getHomeNo()+ apiKey
                req = urllib.request.Request(url)
                res = urllib.request.urlopen(req)
                addrResponse = str(res.read())
                commaSep = addrResponse.split(',')
                
                splitAddrLine = commaSep[2].split("\"")
                firstLine = splitAddrLine[3]
                
                splitTownLine = commaSep[7]
                secondLine = splitTownLine[1:len(splitTownLine)]

                userAddress = (firstLine,'\n'+secondLine)
                print(commaSep)
                print(userAddress)
                
                confirm = QMessageBox.question(self, 'Confirm',
                        ("Does this look correct?\n%s\n%s"%(firstLine,secondLine)),
                            QMessageBox.Yes|QMessageBox.No)
                if confirm == QMessageBox.Yes:
                    self.addrLineOne.setText(firstLine)
                    self.addrLineTwo.setText(secondLine)
                else:
                    self.notTheAddress()
            except urllib.error.HTTPError as d:
                print (d)
                print ("error")
                
                reply = QMessageBox.critical(self, "Error", 
                        "Check your info and try again", QMessageBox.Ok)
                
        if newCustomer==True:
            self.pcEdit = QHBoxLayout()
            self.pcLineEdit = ButtonLineEdit(self)
            self.pcBtn = QPushButton('Look Up', self)
            self.pcBtn.clicked.connect(pcLookup)
            self.pcEdit.addWidget(self.pcLineEdit)
            self.pcEdit.addWidget(self.pcBtn)
        else:
            self.pcEdit = ButtonLineEdit(self)
            
        #WIDGETS
        instr = QLabel("""Enter the customer's details. Fields marked with
                        a (*) are required""")
        nameLabel = QLabel('* Full Name:')
        self.nameEdit = ButtonLineEdit(self)

        emailLabel = QLabel('Email Address:')
        self.emailAddr = ButtonLineEdit(self)

        phoneLabel = QLabel('Home Phone Number:')
        self.phoneNo = ButtonLineEdit(self) # add multi box with aread code

        mobileLabel = QLabel('* Mobile Phone Number:')
        self.mobileNo = ButtonLineEdit(self)
        
        pcLabel = QLabel('* Post Code:')

        addrLabel = QLabel('* Home Address:')
        self.addrLineOne = ButtonLineEdit(self)
        self.addrLineOne.setReadOnly(True)

        self.addrLineTwo = ButtonLineEdit(self)
        self.addrLineTwo.setReadOnly(True)
        self.addrLineTwo.setFrame(True)
        addrBox = QVBoxLayout()
        addrBox.addWidget(self.addrLineOne)
        addrBox.addWidget(self.addrLineTwo)
        #self.addrEdit.setPlaceholderText("123 New Street\nArea\nTown")

        self.nextButton = QPushButton("Next")
        



        titleBox = QGroupBox("Customer Details")


        layout.addRow(instr)
        layout.addRow(nameLabel, self.nameEdit)
        layout.addRow(emailLabel, self.emailAddr)
        layout.addRow(phoneLabel, self.phoneNo)
        layout.addRow(mobileLabel, self.mobileNo)
        layout.addRow(pcLabel, self.pcEdit)
        layout.addRow(addrLabel, addrBox)
        layout.addRow(self.nextButton)
        titleBox.setLayout(layout)

        mainLayout = QVBoxLayout(self)
        mainLayout.addWidget(titleBox)
        self.setLayout(mainLayout)
    def notTheAddress(self):
        instructions = QMessageBox.information(self, 'Info',
                "Enter the customer's address manually")
        self.addrLineOne.clear()
        self.addrLineTwo.clear()
        self.addrLineOne.setPlaceholderText("3 New Street")
        self.addrLineTwo.setPlaceholderText("Chesterfield")
        self.addrLineOne.setReadOnly(False)
        self.addrLineTwo.setReadOnly(False)
