from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QFormLayout, QLabel, QLineEdit,
                                QCheckBox, QTextEdit, QPushButton)
from PyQt5.QtWidgets import QButtonGroup, QInputDialog, QMessageBox, QVBoxLayout
from PyQt5.QtCore import QSize
import json
import urllib
import requests

class ButtonLineEdit(QtGui.QLineEdit):
    buttonClicked = QtCore.pyqtSignal(bool)

    def __init__(self, icon_file, parent=None):
        super(ButtonLineEdit, self).__init__(parent)

        self.button = QtGui.QToolButton(self)
        self.button.setIcon(QtGui.QIcon(icon_file))
        self.button.setStyleSheet('border: 0px; padding: 0px;')
        self.button.setCursor(QtCore.Qt.ArrowCursor)
        self.button.clicked.connect(self.buttonClicked.emit)

        frameWidth = self.style().pixelMetric(QtGui.QStyle.PM_DefaultFrameWidth)
        buttonSize = self.button.sizeHint()

        self.setStyleSheet('QLineEdit {padding-right: %dpx; }' % (buttonSize.width() + frameWidth + 1))
        self.setMinimumSize(max(self.minimumSizeHint().width(), buttonSize.width() + frameWidth*2 + 2),
                            max(self.minimumSizeHint().height(), buttonSize.height() + frameWidth*2 + 2))

    def resizeEvent(self, event):
        buttonSize = self.button.sizeHint()
        frameWidth = self.style().pixelMetric(QtGui.QStyle.PM_DefaultFrameWidth)
        self.button.move(self.rect().right() - frameWidth - buttonSize.width(),
                         (self.rect().bottom() - buttonSize.height() + 1)/2)
        super(ButtonLineEdit, self).resizeEvent(event)



class custDetailForm(QWidget):
    def __init__(self, parent=None):
        super(custDetailForm, self).__init__(parent)
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
                url = 'https://api.getaddress.io/v2/uk/' + self.pcEdit.text() +'/' + getHomeNo()+ apiKey
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
        #WIDGETS
        instr = QLabel("""Enter your postcode and click \"Look Up\" to populate the 
                \"Home Address\" field with your address automatically""")
        nameLabel = QLabel('Full Name:')
        self.nameEdit = QLineEdit(self)
        
        addrLabel = QLabel('Home Address:')
        self.addrLineOne = QLineEdit(self)
        self.addrLineOne.setPlaceholderText("123 New Street")

        self.addrLineTwo = QLineEdit(self)
        self.addrLineTwo.setPlaceholderText("Chesterfield")
        addrBox = QVBoxLayout()
        addrBox.addWidget(self.addrLineOne)
        addrBox.addWidget(self.addrLineTwo)
        #self.addrEdit.setPlaceholderText("123 New Street\nArea\nTown")
        pcLabel = QLabel('Post Code:')
        pcBox = QHBoxLayout()
        self.pcEdit = QLineEdit(self)
        pcBtn = QPushButton('Look up', self)
        pcBtn.clicked.connect(pcLookup)
        pcBox.addWidget(self.pcEdit)
        pcBox.addWidget(pcBtn)
        self.nextButton = QPushButton("Next")



        layout.addRow(instr)
        layout.addRow(nameLabel, self.nameEdit)
        layout.addRow(addrLabel, addrBox)
        layout.addRow(pcLabel, pcBox)
        layout.addRow(self.nextButton)
        self.setLayout(layout)
    def notTheAddress(self):
        instructions = QMessageBox.information(self, 'Info',
                "Enter the customer's address manually")
        self.addrEdit.setPlaceHolderText("3 New Street\nChesterfield")
