from PyQt5.QtWidgets import (QWidget, QFormLayout, QVBoxLayout, QHBoxLayout, QTableWidget,
        QLabel, QLineEdit, QTextEdit, QPushButton, QDesktopWidget, QHeaderView, QHBoxLayout,
        QGroupBox)
from PyQt5.QtCore import Qt
from customWidgets import customTableWidget

class jobProgressWidget(QWidget):
    def __init__(self, jobNumber, parent=None):
        super(jobProgressWidget, self).__init__(parent)
        self.jobNumber = jobNumber
        layout = QHBoxLayout()

        jobNoLabel = QLabel('Job Number:')
        jobNoEdit = QLineEdit(self)
        jobNoEdit.setReadOnly(True)
        jobNoEdit.setPlaceholderText(str(self.jobNumber))
        
        notesTitleBox = QGroupBox("General Job Notes")
        self.jobNotesEdit = QTextEdit()
        notesLayout = QHBoxLayout()
        notesLayout.addWidget(self.jobNotesEdit)
        notesTitleBox.setLayout(notesLayout)

        jobTitleBox = QGroupBox("Job Number")
        jobLayout = QHBoxLayout()
        jobLayout.addWidget(jobNoEdit)
        jobTitleBox.setLayout(jobLayout)
        

        partsLabel = QLabel('Parts Used/\nWork Done:')
        self.partsTable = customTableWidget()
        self.partsTable.setRowCount(1)
        self.partsTable.setColumnCount(2)
        partsHeaders = ["Item","Cost ExVat"]
        self.partsTable.setHorizontalHeaderLabels(partsHeaders)
        self.partsTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.partsTable.cellChanged.connect(self.updateTotals)
    
        
        self.subTotal = QLabel("$Money")
        self.taxAmount = QLabel("$Less Mpney")
        self.totalAmount = QLabel("$More Money")

        totalLayout = QVBoxLayout()
        totalLayout.addWidget(self.subTotal)
        totalLayout.addWidget(self.taxAmount)
        totalLayout.addWidget(self.totalAmount)

        tableBox = QVBoxLayout()
        tableBox.addWidget(self.partsTable)
        tableBox.addLayout(totalLayout)
        tableTitleBox = QGroupBox("Parts Used/Work Done")
        tableTitleBox.setLayout(tableBox)

        leftLayout = QVBoxLayout()
        leftLayout.addWidget(jobTitleBox)
        leftLayout.addWidget(notesTitleBox)

        layout.addLayout(leftLayout)
        layout.addWidget(tableTitleBox)
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
