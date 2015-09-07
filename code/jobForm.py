from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QFormLayout, QLabel, 
                                QLineEdit, QCheckBox, QTextEdit, QPushButton)
from PyQt5.QtWidgets import QButtonGroup


class newJobForm(QWidget):
    def __init__(self, parent=None):
        super(newJobForm, self).__init__(parent)
        olayout = QFormLayout()
        #Widgets 
	
	#jobTitle = QLabel("<u>Job Details</u>")
        itemLabel = QLabel('Items:')
        self.itemEdit = QLineEdit(self)
        
        psuLabel = QLabel('Power Supply?') 
        self.psuButtonGroup = QButtonGroup(self)
        psuBox = QHBoxLayout()
        psuY = QCheckBox('Yes', self)
        psuN = QCheckBox('No', self)
        psuNA = QCheckBox('N/A', self)
        psuBox.addWidget(psuY)
        psuBox.addWidget(psuN)
        psuBox.addWidget(psuNA)
        
        problemLabel = QLabel('Job Description:')
        self.problemEdit = QTextEdit()
        #problemEdit.setFixedHeight(100)
        
        importantDataLabel = QLabel('Any important data on the system?')
        importantDataCheckYes = QCheckBox('Yes', self)
        importantDataCheckNo = QCheckBox('No', self)
        self.importantDataBox = QHBoxLayout()
        self.importantDataBox.addWidget(importantDataCheckYes)
        self.importantDataBox.addWidget(importantDataCheckNo)
        
        dataBackupLabel = QLabel('Data backed up?')
        dataBackupCheckYes = QCheckBox('Yes', self)
        dataBackupCheckNo = QCheckBox('Yes', self)
        self.dataBackupBox = QHBoxLayout()
        self.dataBackupBox.addWidget(dataBackupCheckYes)
        self.dataBackupBox.addWidget(dataBackupCheckNo)
        
        # Back up check boxes set up
        dataBackupGrp = QButtonGroup(self)
        dataBackupGrp.addButton(dataBackupCheckYes)
        dataBackupGrp.addButton(dataBackupCheckNo)
        
        # Important Data check Boxes Set Up
        self.importantDataGrp = QButtonGroup(self)
        self.importantDataGrp.addButton(importantDataCheckYes)
        self.importantDataGrp.addButton(importantDataCheckNo)
#        importantDataGrp.buttonClicked.connect(dataClicked)

        # PSU check Boxes set up
        self.psuButtonGroup.addButton(psuY)
        self.psuButtonGroup.addButton(psuN)
        self.psuButtonGroup.addButton(psuNA)
        # if psuButtonGroup.checkedButton == 0, none clicked
        self.nextButton = QPushButton("Next", self)
        olayout.addRow(itemLabel, self.itemEdit)
        olayout.addRow(psuLabel, psuBox)
        olayout.addRow(problemLabel, self.problemEdit)
        olayout.addRow(importantDataLabel, self.importantDataBox)
        olayout.addRow(dataBackupLabel, self.dataBackupBox)
        olayout.addRow(self.nextButton)
        self.setLayout(olayout)
    def errorChecking(self):
        def writeToFile():
            custItems = self.itemEdit.text()
            if self.psuButtonGroup.checkedButton == 1:
                custPsu = "Yes"
            else:
                custPsu = "No"
            custProblem = self.problemEdit.text()
            if self.importantDataGrp.checkedButton == 1:
                custData = "Yes"
            else:
                custData = "No"
            if self.dataBackupBox.checkedButton == 1:
                custBackup = "Yes"
            else:
                custBackup = "No"
            fileSaveTo = open("randNum.txt", "w")
            fileSaveTo.write(custItems)
            fileSaveTo.write(custPsu)
            fileSaveTo.write(custProblem)
            fileSaveTo.write(custData)
            fileSaveTo.write(custBackup)
        statusText = "No Eeorrs"
        if self.itemEdit.text() == "":
            statusText = "Error: Enter items"
            pass
        elif self.psuButtonGroup.checkedButton == 0:
            statusText = "Error: PSU??"
            pass
        elif self.problemEdit.text() == "":
            statusText = "Error: No Prob?"
            pass
        elif self.importantDataGrp.checkedButton == 0:
            statusText = "Error: DATA?!!"
            pass
        elif self.dataBackupBox.checkedButton == 0:
            statusText = "Error: BACKup?"
            pass
        else:
            statusText = "job Details saved"
            writeToFile()
        #statBar = sBar(self)
        #statBar.showMessage(statusText)

        print ("Items:", self.itemEdit.text())
        
