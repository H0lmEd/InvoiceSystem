from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QFormLayout, QLabel,
        QLineEdit, QCheckBox, QTextEdit, QPushButton, QVBoxLayout, QGroupBox)
from PyQt5.QtWidgets import QButtonGroup, QInputDialog, QMessageBox, QToolButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, Qt
import os

class jobDisplayWidget(QWidget):
    def __init__(self,jobNumber, parent=None):
        super(jobDisplayWidget, self).__init__(parent)

        self.jobNumber = jobNumber
        layout = QFormLayout()
        iconFolder = os.path.join(os.path.dirname(__file__), os.pardir, 'icons/')

        staffLabel = QLabel('Booked in by:')
        self.staffEdit = QLineEdit(self)

        jobNoLabel = QLabel('Job Number:')
        jobNoEdit = QLineEdit(self)
        jobNoEdit.setReadOnly(True)
        jobNoEdit.setPlaceholderText(str(self.jobNumber))
        
        itemLabel = QLabel('Items:')
        self.itemEdit = QLineEdit(self)
        self.itemEdit.setClearButtonEnabled(True)
        
        psuLabel = QLabel('Power Supply provided:')
        self.psuButtonGroup = QButtonGroup(self)
        psuBox = QHBoxLayout()
        self.psuY = QCheckBox('yes', self)
        self.psuN = QCheckBox('no', self)
        self.psuNA = QCheckBox('N/A', self)
        psuBox.addWidget(self.psuY)
        psuBox.addWidget(self.psuN)
        psuBox.addWidget(self.psuNA)

        self.psuButtonGroup.addButton(self.psuY)
        self.psuButtonGroup.addButton(self.psuN)
        self.psuButtonGroup.addButton(self.psuNA)

        conditionLabel = QLabel('Condition:')
        self.condition = QLineEdit(self)
        
        problemLabel = QLabel('Job Description:')
        self.problemEdit = QTextEdit()

        passwordsLabel = QLabel('Passwords:')
        self.passwordWidgets = QVBoxLayout()
        self.passButtonGroup = QButtonGroup(self)
        self.passwords = QTextEdit(self)

        self.passwordBox = QHBoxLayout()
        self.passwordCheckYes = QCheckBox('Yes', self)
        self.passwordCheckNo = QCheckBox('No', self)
        self.passButtonGroup.addButton(self.passwordCheckYes)
        self.passButtonGroup.addButton(self.passwordCheckNo)

        self.passwordBox.addWidget(self.passwordCheckYes)
        self.passwordBox.addWidget(self.passwordCheckNo)
        self.passwordWidgets.addLayout(self.passwordBox)
        self.passwordWidgets.addWidget(self.passwords)
        

        importantDataLabel = QLabel('Important Data on System:')
        self.importantDataWidgets = QVBoxLayout()
        self.importantData = QLineEdit(self)
        self.importantData.setReadOnly(True)

        self.importantDataBox = QHBoxLayout()
        self.importantDataCheckYes = QCheckBox('Yes', self)
        self.importantDataCheckNo = QCheckBox('No', self)
        self.importantDataBox.addWidget(self.importantDataCheckYes)
        self.importantDataBox.addWidget(self.importantDataCheckNo)
        self.importantDataWidgets.addLayout(self.importantDataBox)
        self.importantDataWidgets.addWidget(self.importantData)

        self.importantDataGrp = QButtonGroup(self)
        self.importantDataGrp.addButton(self.importantDataCheckYes)
        self.importantDataGrp.addButton(self.importantDataCheckNo)

        dataBackupLabel = QLabel('Important Data Backed up:')
        self.dataBackupCheckYes = QCheckBox('Yes', self)
        self.dataBackupCheckNo = QCheckBox('No', self)
        self.dataBackupBox = QHBoxLayout()
        self.dataBackupBox.addWidget(self.dataBackupCheckYes)
        self.dataBackupBox.addWidget(self.dataBackupCheckNo)

        self.dataBackupGrp = QButtonGroup(self)
        self.dataBackupGrp.addButton(self.dataBackupCheckYes)
        self.dataBackupGrp.addButton(self.dataBackupCheckNo)
        

        self.nextButton = QToolButton(self)
        self.nextButton.setToolButtonStyle(2)
        self.nextButton.setText("Personal Details")
        self.nextButton.setIcon(QIcon(iconFolder + 'forward.png'))
        self.nextButton.setIconSize(QSize(12, 12))
      
        titleBox = QGroupBox("New Job")
        titleBox.setAlignment(Qt.AlignRight)

        layout.addRow(staffLabel, self.staffEdit)
        layout.addRow(jobNoLabel, jobNoEdit)
        layout.addRow(itemLabel, self.itemEdit)
        layout.addRow(psuLabel, psuBox)
        layout.addRow(conditionLabel, self.condition)
        layout.addRow(problemLabel, self.problemEdit)
        layout.addRow(passwordsLabel, self.passwordWidgets)
        layout.addRow(importantDataLabel, self.importantDataWidgets)
        layout.addRow(dataBackupLabel, self.dataBackupBox)
        layout.addRow(self.nextButton)
        titleBox.setLayout(layout)

        mainLayout = QVBoxLayout(self)
        mainLayout.addWidget(titleBox)
        self.setLayout(mainLayout)

    def importantDataChecked(self):
        if self.importantDataGrp.checkedId() == -2:
            self.importantData.setReadOnly(False)
        elif self.importantDataGrp.checkedId() == -3:
            self.importantData.setReadOnly(True)
