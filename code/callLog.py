from PyQt5.QtWidgets import (QWidget, QFormLayout, QVBoxLayout, QHBoxLayout, QTableWidget,
        QLabel, QLineEdit, QTextEdit, QPushButton, QDesktopWidget, QHeaderView, QHBoxLayout,
        QGroupBox)
from PyQt5.QtCore import Qt
from customWidgets import customTableWidget

class callLogWidget(QWidget):
    def __init__(self, jobNumber, parent=None):
        super(callLogWidget, self).__init__(parent)
        self.jobNumber = jobNumber
        layout = QVBoxLayout()

        jobNoLabel = QLabel('Job Number:')
        jobNoEdit = QLineEdit(self)
        jobNoEdit.setReadOnly(True)
        jobNoEdit.setPlaceholderText(str(self.jobNumber))

        jobTitleBox = QGroupBox("Job Number")
        jobLayout = QHBoxLayout()
        jobLayout.addWidget(jobNoEdit)
        jobTitleBox.setLayout(jobLayout)
        
        self.callsTable = customTableWidget()
        self.callsTable.setRowCount(1)
        self.callsTable.setColumnCount(4)
        callsHeaders = ["Engineer","Date","Time","Details"]
        self.callsTable.setHorizontalHeaderLabels(callsHeaders)
        self.callsTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        callsBox = QVBoxLayout()
        callsBox.addWidget(self.callsTable)
        callsTitleBox = QGroupBox("Call Log")
        callsTitleBox.setLayout(callsBox)

        layout.addWidget(jobTitleBox)
        layout.addWidget(callsTitleBox)
        self.setLayout(layout)
    def updateTotals(self):
        count = 0
        rount = 0
        totalExVat = 0.00
        print (self.partsTable.rowCount())
        
        for x in range(self.partsTable.rowCount()):
            for i in range(self.partsTable.columnCount()): #go through cells 
                print ('i:', i)
                if i == 1:
                    try:
                        totalExVat = totalExVat + int(self.partsTable.item(x,i).text())
                    except AttributeError:
                        pass
        pound = u'\u00A3'

        self.subTotal.setText(pound+str(totalExVat))
        self.taxAmount.setText(pound+str((totalExVat*0.2)))
        self.totalAmount.setText(pound+str((totalExVat*1.2)))
