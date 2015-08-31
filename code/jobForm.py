from PyQt5.QtWidgets import QWidget

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
        problemEdit = QTextEdit()
        #problemEdit.setFixedHeight(100)
        
        importantDataLabel = QLabel('Any important data on the system?')
        importantDataCheckYes = QCheckBox('Yes', self)
        importantDataCheckNo = QCheckBox('No', self)
        importantDataBox = QHBoxLayout()
        importantDataBox.addWidget(importantDataCheckYes)
        importantDataBox.addWidget(importantDataCheckNo)
        
        dataBackupLabel = QLabel('Data backed up?')
        dataBackupCheckYes = QCheckBox('Yes', self)
        dataBackupCheckNo = QCheckBox('Yes', self)
        dataBackupBox = QHBoxLayout()
        dataBackupBox.addWidget(dataBackupCheckYes)
        dataBackupBox.addWidget(dataBackupCheckNo)
        
        # Back up check boxes set up
        dataBackupGrp = QButtonGroup(self)
        dataBackupGrp.addButton(dataBackupCheckYes)
        dataBackupGrp.addButton(dataBackupCheckNo)
        
        # Important Data check Boxes Set Up
        importantDataGrp = QButtonGroup(self)
        importantDataGrp.addButton(importantDataCheckYes)
        importantDataGrp.addButton(importantDataCheckNo)
#        importantDataGrp.buttonClicked.connect(dataClicked)

        # PSU check Boxes set up
        self.psuButtonGroup.addButton(psuY)
        self.psuButtonGroup.addButton(psuN)
        self.psuButtonGroup.addButton(psuNA)
        # if psuButtonGroup.checkedButton == 0, none clicked
        nextButton = QPushButton("Next", self)
        #nextButton.clicked.connect(lambda: progressWidget.changeValue(1))
        nextButton.clicked.connect(self.errorChecking)
        olayout.addRow(itemLabel, self.itemEdit)
        olayout.addRow(psuLabel, psuBox)
        olayout.addRow(problemLabel, problemEdit)
        olayout.addRow(importantDataLabel, importantDataBox)
        olayout.addRow(dataBackupLabel, dataBackupBox)
        olayout.addRow(nextButton)
        self.setLayout(olayout)
    def errorChecking(self):
        if self.itemEdit.text() == "":
            statusText = "Error: Enter items"
            pass
        elif self.psuButtonGroup.checkedButton == 0:
            statusText = "Error: PSU??"

        print ("Items:", self.itemEdit.text())
        
