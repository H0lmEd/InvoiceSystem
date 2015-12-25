from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QFormLayout, QLabel,
        QCheckBox, QTextEdit, QPushButton, QVBoxLayout, QGroupBox, QLineEdit)
from PyQt5.QtWidgets import QButtonGroup, QInputDialog, QMessageBox, QToolButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, Qt
from customWidgets import validationImage
import os

class jobDisplayWidget(QWidget):
    def __init__(self,jobNumber, parent=None):
        super(jobDisplayWidget, self).__init__(parent)

        self.jobNumber = jobNumber
        layout = QFormLayout()

        staffLabel = QLabel('Booked in by:')
        self.staffEdit = QLineEdit(self)
        self.staffVal = validationImage(self)
        staffErrorBox = QHBoxLayout()
        staffErrorBox.addWidget(self.staffEdit)
        staffErrorBox.addWidget(self.staffVal)

        jobNoLabel = QLabel('Job Number:')
        self.jobNoEdit = QLineEdit(self)
        self.jobNoEdit.setReadOnly(True)
        jobNoVal = validationImage(self)
        self.jobNoEdit.setPlaceholderText(str(self.jobNumber))
        jobNoBox = QHBoxLayout()
        jobNoBox.addWidget(self.jobNoEdit)
        jobNoBox.addWidget(jobNoVal)
        
        itemLabel = QLabel('Items:')
        self.itemEdit = QLineEdit(self)
        self.itemEdit.setClearButtonEnabled(True)
        self.itemVal = validationImage(self)
        self.itemBox = QHBoxLayout()
        self.itemBox.addWidget(self.itemEdit)
        self.itemBox.addWidget(self.itemVal)

        
        psuLabel = QLabel('Power Supply provided:')
        self.psuButtonGroup = QButtonGroup(self)
        psuBox = QHBoxLayout()
        self.psuY = QCheckBox('Yes', self)
        self.psuN = QCheckBox('No', self)
        self.psuNA = QCheckBox('N/A', self)
        self.psuVal = validationImage(self)
        psuBox.addWidget(self.psuY)
        psuBox.addWidget(self.psuN)
        psuBox.addWidget(self.psuNA)
        psuBox.addWidget(self.psuVal)

        self.psuButtonGroup.addButton(self.psuY)
        self.psuButtonGroup.addButton(self.psuN)
        self.psuButtonGroup.addButton(self.psuNA)

        conditionLabel = QLabel('Condition:')
        self.condition = QLineEdit(self)
        self.conditionVal = validationImage(self)
        conditionBox = QHBoxLayout()
        conditionBox.addWidget(self.condition)
        conditionBox.addWidget(self.conditionVal)

        
        problemLabel = QLabel('Job Description:')
        self.problemEdit = QTextEdit()
        self.problemVal = validationImage(self)
        problemBox = QHBoxLayout()
        problemBox.addWidget(self.problemEdit)
        problemBox.addWidget(self.problemVal)

        passwordsLabel = QLabel('Passwords:')
        self.passwordWidgets = QVBoxLayout()
        self.passButtonGrp = QButtonGroup(self)
        self.passwords = QTextEdit(self)
        self.passwordsVal = validationImage(self)
        self.passwordFieldBox = QHBoxLayout()
        self.passwordFieldBox.addWidget(self.passwords)
        self.passwordFieldBox.addWidget(self.passwordsVal)

        self.passwordBox = QHBoxLayout()
        self.passwordCheckYes = QCheckBox('Yes', self)
        self.passwordCheckNo = QCheckBox('No', self)
        self.passwordCheckVal = validationImage(self)

        self.passButtonGrp.addButton(self.passwordCheckYes)
        self.passButtonGrp.addButton(self.passwordCheckNo)

        self.passwordBox.addWidget(self.passwordCheckYes)
        self.passwordBox.addWidget(self.passwordCheckNo)
        self.passwordBox.addWidget(self.passwordCheckVal)
        self.passwordWidgets.addLayout(self.passwordBox)
        self.passwordWidgets.addLayout(self.passwordFieldBox)
        

        importantDataLabel = QLabel('Important Data on System:')
        self.importantDataWidgets = QVBoxLayout()
        self.importantData = QLineEdit(self)
        self.importantData.setReadOnly(True)
        self.importantDataVal = validationImage(self)
        self.importantDataFieldBox = QHBoxLayout()
        self.importantDataFieldBox.addWidget(self.importantData)
        self.importantDataFieldBox.addWidget(self.importantDataVal)


        self.importantDataBox = QHBoxLayout()
        self.importantDataCheckYes = QCheckBox('Yes', self)
        self.importantDataCheckNo = QCheckBox('No', self)
        self.importantDataCheckVal = validationImage(self)

        self.importantDataBox.addWidget(self.importantDataCheckYes)
        self.importantDataBox.addWidget(self.importantDataCheckNo)
        self.importantDataBox.addWidget(self.importantDataCheckVal)

        self.importantDataWidgets.addLayout(self.importantDataBox)
        self.importantDataWidgets.addLayout(self.importantDataFieldBox)

        self.importantDataGrp = QButtonGroup(self)
        self.importantDataGrp.addButton(self.importantDataCheckYes)
        self.importantDataGrp.addButton(self.importantDataCheckNo)

        dataBackupLabel = QLabel('Important Data Backed up:')
        self.dataBackupCheckYes = QCheckBox('Yes', self)
        self.dataBackupCheckNo = QCheckBox('No', self)
        self.dataBackupCheckVal = validationImage(self)

        self.dataBackupBox = QHBoxLayout()
        self.dataBackupBox.addWidget(self.dataBackupCheckYes)
        self.dataBackupBox.addWidget(self.dataBackupCheckNo)
        self.dataBackupBox.addWidget(self.dataBackupCheckVal)

        self.dataBackupGrp = QButtonGroup(self)
        self.dataBackupGrp.addButton(self.dataBackupCheckYes)
        self.dataBackupGrp.addButton(self.dataBackupCheckNo)
        
        self.nextButton = QPushButton("Next")
        self.nextButton.setIcon(QIcon.fromTheme("gtk-apply"))
        nextButtonLayout = QHBoxLayout()
        nextButtonLayout.addStretch(1)
        nextButtonLayout.addWidget(self.nextButton)
        self.nextButton.setIconSize(QSize(16, 16))

      
        titleBox = QGroupBox("New Job")
        titleBox.setAlignment(Qt.AlignHCenter)

        layout.addRow(staffLabel, staffErrorBox)
        layout.addRow(jobNoLabel, jobNoBox)
        layout.addRow(itemLabel, self.itemBox)
        layout.addRow(psuLabel, psuBox)
        layout.addRow(conditionLabel, conditionBox)
        layout.addRow(problemLabel, problemBox)
        layout.addRow(passwordsLabel, self.passwordWidgets)
        layout.addRow(importantDataLabel, self.importantDataWidgets)
        layout.addRow(dataBackupLabel, self.dataBackupBox)
        layout.addRow("",nextButtonLayout)
        titleBox.setLayout(layout)

        mainLayout = QVBoxLayout(self)
        mainLayout.addWidget(titleBox)
        self.setLayout(mainLayout)

    def importantDataChecked(self):
        if self.importantDataGrp.checkedId() == -2:
            self.importantData.setReadOnly(False)
        elif self.importantDataGrp.checkedId() == -3:
            self.importantData.setReadOnly(True)

    def passwordsChecked(self):
        if self.passButtonGrp.checkedId() == -2:
            self.passwords.setReadOnly(False)
        elif self.passButtonGrp.checkedId() == -3:
            self.passwords.setReadOnly(Trie)
