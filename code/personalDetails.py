# When customer is new, pcEdit = Box layout of label + button
# When customer isnt new, pcEdit = QLineEdit





from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QFormLayout, QLabel, QLineEdit,
                                QCheckBox, QTextEdit, QPushButton)
from PyQt5.QtWidgets import QButtonGroup, QInputDialog, QMessageBox, QVBoxLayout, QToolButton, QStyle
from PyQt5.QtCore import QSize,pyqtSignal
from PyQt5.QtGui import QIcon
import json
import PyQt5.QtGui
import PyQt5.QtCore
import PyQt5.QtWidgets
import urllib
import requests
class ButtonLineEdit(QLineEdit):
    buttonClicked = pyqtSignal(bool)

    def __init__(self, icon_file, parent=None):
        super(ButtonLineEdit, self).__init__(parent)

        self.button = QToolButton(self)
        self.button.setIcon(QIcon(icon_file))
        self.button.setStyleSheet('border: 0px; padding: 0px;') #No Padding
        #self.button.setCursor(ArrowCursor)
        self.button.clicked.connect(self.buttonClicked.emit)

        frameWidth = self.style().pixelMetric(QStyle.PM_DefaultFrameWidth)# Set to label length
        buttonSize = self.button.sizeHint()

        self.setStyleSheet('QLineEdit {padding-right: %dpx; }' % (buttonSize.width() + frameWidth + 1))
        self.setMinimumSize(max(self.minimumSizeHint().width(), buttonSize.width() + frameWidth*2 + 2),
                            max(self.minimumSizeHint().height(), buttonSize.height() + frameWidth*2 + 2))

    def resizeEvent(self, event):
        buttonSize = self.button.sizeHint()
        frameWidth = self.style().pixelMetric(QStyle.PM_DefaultFrameWidth)
        self.button.move(self.rect().right() - frameWidth - buttonSize.width(),
                         (self.rect().bottom() - buttonSize.height() + 1)/2)
        super(ButtonLineEdit, self).resizeEvent(event)

def buttonClicked():
    print("ButtonClicked")

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
                apiKey = '?api-key=JWsM4KuOz0aUHRyBntyd2A1611'
                url = 'https://api.getaddress.io/v2/uk/' + self.pcLineEdit.text() +'/' + getHomeNo()+ apiKey
                apiKey = 'JWsM4KuOz0aUHRyBntyd2A1611'
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
            self.pcLineEdit = QLineEdit(self)
            self.pcBtn = QPushButton('Look Up', self)
            self.pcBtn.clicked.connect(pcLookup)
            self.pcEdit.addWidget(self.pcLineEdit)
            self.pcEdit.addWidget(self.pcBtn)
        else:
            self.pcEdit = QLineEdit(self)
            
        #WIDGETS
        instr = QLabel("""Enter your postcode and click \"Look Up\" to populate the 
                \"Home Address\" field with your address automatically""")
        nameLabel = QLabel('Full Name:')
        self.nameEdit = QLineEdit(self)
        
        addrLabel = QLabel('Home Address:')
        self.addrLineOne = QLineEdit(self)
        self.addrLineOne.setReadOnly(True)

        self.addrLineTwo = QLineEdit(self)
        self.addrLineTwo.setReadOnly(True)
        self.addrLineTwo.setFrame(True)
        addrBox = QVBoxLayout()
        addrBox.addWidget(self.addrLineOne)
        addrBox.addWidget(self.addrLineTwo)
        #self.addrEdit.setPlaceholderText("123 New Street\nArea\nTown")
        pcLabel = QLabel('Post Code:')

        self.nextButton = QPushButton("Next")
        

        testEdit = ButtonLineEdit('test.png')
        testEdit.buttonClicked.connect(buttonClicked)





        layout.addRow(instr)
        layout.addRow(nameLabel, self.nameEdit)
        layout.addRow(pcLabel, self.pcEdit)
        layout.addRow(addrLabel, addrBox)
        layout.addRow(self.nextButton)
        layout.addRow(testEdit)
        self.setLayout(layout)
    def notTheAddress(self):
        instructions = QMessageBox.information(self, 'Info',
                "Enter the customer's address manually")
        self.addrLineOne.clear()
        self.addrLineTwo.clear()
        self.addrLineOne.setPlaceholderText("3 New Street")
        self.addrLineTwo.setPlaceholderText("Chesterfield")
        self.addrLineOne.setReadOnly(False)
        self.addrLineTwo.setReadOnly(False)
