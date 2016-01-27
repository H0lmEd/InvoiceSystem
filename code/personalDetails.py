# When customer is new, pcEdit = Box layout of label + button
# When customer isnt new, pcEdit = QLineEdit
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from customWidgets import *
import os
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
                numberDialog = numberData.getText(self, "Home Number",
                        "Home Number:")
                if numberDialog:
                    return str(numberDialog[0])
            try:
                apiKey = '?api-key=W9SLQuBlykSwXw1A4oNPOw2705'
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
                
                confirm = QMessageBox.question(self, 'Confirm',
                        ("Does this look correct?\n%s\n%s"%(firstLine,secondLine)),
                            QMessageBox.Yes|QMessageBox.No)
                if confirm == QMessageBox.Yes:
                    self.addrLineOne.setText(firstLine)
                    self.addrLineTwo.setText(secondLine)
                else:
                    self.notTheAddress()
            except urllib.error.HTTPError:
                reply = QMessageBox.critical(self, "Error", 
                        "Check your info and try again", QMessageBox.Ok)
            except urllib.error.URLError:
                reply = QMessageBox.critical(self, "Error",
                        "No Internet connection detected.\nRetry?", QMessageBox.Yes|QMessageBox.No)
                if reply == QMessageBox.No:
                    self.notTheAddress()
        self.pcVal = validationImage(self)
        if newCustomer==True:
            self.pcEdit = QHBoxLayout()
            self.pcLineEdit = QLineEdit(self)
            self.pcBtn = QPushButton('Look Up', self)
            self.pcBtn.clicked.connect(pcLookup)
            self.pcEdit.addWidget(self.pcLineEdit)
            self.pcEdit.addWidget(self.pcBtn)
            self.pcEdit.addWidget(self.pcVal)

        else:
            self.pcEdit = QLineEdit(self)
            
        #WIDGETS
        instr = QLabel("""Enter the customer's details. Fields marked with a (*) are required""")
        nameLabel = QLabel('* Full Name:')
        self.nameEdit = QLineEdit(self)
        self.nameVal = validationImage(self)
        nameBox = QHBoxLayout()
        nameBox.addWidget(self.nameEdit)
        nameBox.addWidget(self.nameVal)


        emailLabel = QLabel('Email Address:')
        self.emailAddr = QLineEdit(self)
        self.emailVal = validationImage(self)
        emailBox = QHBoxLayout()
        emailBox.addWidget(self.emailAddr)
        emailBox.addWidget(self.emailVal)

        phoneLabel = QLabel('Home Phone Number:')
        self.phoneNo = QLineEdit(self) # add multi box with aread code
        self.phoneVal = validationImage(self)
        phoneBox = QHBoxLayout()
        phoneBox.addWidget(self.phoneNo)
        phoneBox.addWidget(self.phoneVal)

        mobileLabel = QLabel('* Mobile Phone Number:')
        self.mobileNo = QLineEdit(self)
        self.mobileVal = validationImage(self)
        mobileBox = QHBoxLayout()
        mobileBox.addWidget(self.mobileNo)
        mobileBox.addWidget(self.mobileVal)
        
        pcLabel = QLabel('* Post Code:')
        addrLabel = QLabel('* Home Address:')
        self.addrLineOne = QLineEdit(self)
        self.addrLineOne.setReadOnly(True)
        self.addrLineOneVal = validationImage(self)
        addrLineOneBox = QHBoxLayout()
        addrLineOneBox.addWidget(self.addrLineOne)
        addrLineOneBox.addWidget(self.addrLineOneVal)

        self.addrLineTwo = QLineEdit(self)
        self.addrLineTwo.setReadOnly(True)
        self.addrLineTwo.setFrame(True)
        self.addrLineTwoVal = validationImage(self)
        addrLineTwoBox = QHBoxLayout()
        addrLineTwoBox.addWidget(self.addrLineTwo)
        addrLineTwoBox.addWidget(self.addrLineTwoVal)

        addrBox = QVBoxLayout()
        addrBox.addLayout(addrLineOneBox)
        addrBox.addLayout(addrLineTwoBox)

        self.nextButton = QPushButton("Save")
        self.nextButton.setIcon(QIcon.fromTheme("document-save"))
        

        nextBox = QHBoxLayout()
        nextBox.addStretch(1)
        nextBox.addWidget(self.nextButton)


        titleBox = QGroupBox("Customer Details")


        layout.addRow(instr)
        layout.addRow(nameLabel, nameBox)
        layout.addRow(emailLabel, emailBox)
        layout.addRow(phoneLabel, phoneBox)
        layout.addRow(mobileLabel, mobileBox)
        layout.addRow(pcLabel, self.pcEdit)
        layout.addRow(addrLabel, addrBox)
        layout.addRow("", nextBox)
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
