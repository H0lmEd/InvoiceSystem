from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QFormLayout, QLabel,
        QLineEdit, QCheckBox, QTextEdit, QPushButton, QVBoxLayout)
from PyQt5.QtWidgets import QButtonGroup, QInputDialog, QMessageBox, QToolButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
import os

class jobDisplayWidget(QWidget):
    def __init__(self,jobNumber, parent=None):
        super(jobDisplayWidget, self).__init__(parent)
        self.jobNumber = jobNumber
        layout = QFormLayout(self)
        iconFolder = os.path.join(os.path.dirname(__file__), os.pardir, 'icons/')

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

        problemLabel = QLabel('Job Description:')
        self.problemEdit = QTextEdit()

        importantDataLabel = QLabel('Important Data on System:')
        self.importantDataWidgets = QVBoxLayout()
        self.importantData = QLineEdit(self)
        self.importantData.setReadOnly(True)

        self.importantDataBox = QHBoxLayout()
        importantDataCheckYes = QCheckBox('Yes', self)
        importantDataCheckNo = QCheckBox('No', self)
        self.importantDataBox.addWidget(importantDataCheckYes)
        self.importantDataBox.addWidget(importantDataCheckNo)
        self.importantDataWidgets.addLayout(self.importantDataBox)
        self.importantDataWidgets.addWidget(self.importantData)

        self.importantDataGrp = QButtonGroup(self)
        self.importantDataGrp.addButton(importantDataCheckYes)
        self.importantDataGrp.addButton(importantDataCheckNo)

        dataBackupLabel = QLabel('Important Data Backed up:')
        dataBackupCheckYes = QCheckBox('Yes', self)
        dataBackupCheckNo = QCheckBox('No', self)
        self.dataBackupBox = QHBoxLayout()
        self.dataBackupBox.addWidget(dataBackupCheckYes)
        self.dataBackupBox.addWidget(dataBackupCheckNo)

        self.dataBackupGrp = QButtonGroup(self)
        self.dataBackupGrp.addButton(dataBackupCheckYes)
        self.dataBackupGrp.addButton(dataBackupCheckNo)

        self.nextButton = QToolButton(self)
        self.nextButton.setToolButtonStyle(2)
        self.nextButton.setText("Personal Details")
        self.nextButton.setIcon(QIcon(iconFolder + 'forward.png'))
        self.nextButton.setIconSize(QSize(12, 12))
        
        layout.addRow(jobNoLabel, jobNoEdit)
        layout.addRow(itemLabel, self.itemEdit)
        layout.addRow(psuLabel, psuBox)
        layout.addRow(problemLabel, self.problemEdit)
        layout.addRow(importantDataLabel, self.importantDataWidgets)
        layout.addRow(dataBackupLabel, self.dataBackupBox)
        layout.addRow(self.nextButton)
        self.setLayout(layout)

    def importantDataChecked(self):
        if self.importantDataGrp.checkedId() == -2:
            self.importantData.setReadOnly(False)
        elif self.importantDataGrp.checkedId() == -3:
            self.importantData.setReadOnly(True)
