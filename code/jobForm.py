from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QFormLayout, QLabel, 
                                QLineEdit, QCheckBox, QTextEdit, QPushButton)
from PyQt5.QtWidgets import QButtonGroup, QInputDialog, QMessageBox


# TO BE ADDED HERE:
# - Error dialogs prettier
# - Number Generator
# - Save file as number
# - Important Data cancel check no box
# - Prettier
# - Add stuff to file to section off job details


class newJobForm(QWidget):
    def __init__(self, parent=None):
        super(newJobForm, self).__init__(parent)
        olayout = QFormLayout()
        def importantDataDialog():
            data, ok = QInputDialog.getText(self, "Important Data",
                    "Important Data:")

            if ok:
                self.importData = str(data)
            else:
                errorMsg = QMessageBox()
                errorMsg.setText("Error")
                errorMsg.setInformativeText("You need to enter what important data is kept on the system")
                errorMsg.exec_()
        
        def jobNumber():
            jobNoFile = open(".jobNum", "r+")
            self.jobNum = int(jobNoFile.read())
            newJobNum = self.jobNum + 1
            jobNoFile.seek(0)
            jobNoFile.truncate()
            jobNoFile.write(str(newJobNum))
            return self.jobNum
        #Widgets 
        jobNoLabel = QLabel('Job Number:')
        jobNoEdit = QLineEdit(self)
        jobNoEdit.setReadOnly(True)
        jobNoEdit.setPlaceholderText(str(jobNumber()))
	#jobTitle = QLabel("<u>Job Details</u>")
        itemLabel = QLabel('Items:')
        self.itemEdit = QLineEdit(self)
        self.itemEdit.setClearButtonEnabled(True)
        self.itemEdit.setFrame(False)
        
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
       
        importantDataCheckYes.clicked.connect(importantDataDialog)
        dataBackupLabel = QLabel('Data backed up?')
        dataBackupCheckYes = QCheckBox('Yes', self)
        dataBackupCheckNo = QCheckBox('No', self)
        self.dataBackupBox = QHBoxLayout()
        self.dataBackupBox.addWidget(dataBackupCheckYes)
        self.dataBackupBox.addWidget(dataBackupCheckNo)
        
        # Back up check boxes set up
        self.dataBackupGrp = QButtonGroup(self)
        self.dataBackupGrp.addButton(dataBackupCheckYes)
        self.dataBackupGrp.addButton(dataBackupCheckNo)
        
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
        olayout.addRow(jobNoLabel, jobNoEdit)
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
            if self.psuButtonGroup.checkedId == -2:
                custPsu = "Yes"
            elif self.psuButtonGroup.checkedId() == -3:
                custPsu = "No"
            else:
                custPsu = "N/A"
            custProblem = self.problemEdit.toPlainText()
            if self.importantDataGrp.checkedId() == -1:
                custData = "Yes"
            else:
                custData = "No"
            if self.dataBackupGrp.checkedId() == -1:
                custBackup = "Yes"
            else:
                custBackup = "No"
            fileSaveTo = open("Example.txt", "w")
            fileSaveTo.write("Items: "+custItems)
            fileSaveTo.write("\nPSU: "+custPsu)
            fileSaveTo.write("\nProblem: "+custProblem)
            fileSaveTo.write("\nData: "+custData)
            fileSaveTo.write("\nbackup: "+custBackup)
        statusText = "No Eeorrs"
        print(self.psuButtonGroup.checkedId())
        if self.itemEdit.text() == "":
            statusText = "Error: Enter items"
            pass
        elif self.psuButtonGroup.checkedId() == -1:
            statusText = "Error: PSU??"
            pass
        elif self.problemEdit.toPlainText() == "":
            statusText = "Error: No Prob?"
            pass
        elif self.importantDataGrp.checkedId() == -1:
            statusText = "Error: DATA?!!"
            pass
        elif self.dataBackupGrp.checkedId() == -1:
            statusText = "Error: BACKup?"
            pass
        else:
            statusText = "job Details saved"
            writeToFile()
        #statBar = sBar(self)
        #statBar.showMessage(statusText)
        statusMsg = QMessageBox()
        statusMsg.setText(statusText)
        statusMsg.exec_()
        print ("Items:", self.itemEdit.text())
        
