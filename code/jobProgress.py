from PyQt5.QtWidgets import (QWidget, QFormLayout, QVBoxLayout, QHBoxLayout, QTableWidget,
        QLabel, QLineEdit, QTextEdit, QPushButton, QDesktopWidget, QHeaderView, QHBoxLayout,
        QGroupBox)
from PyQt5.QtCore import Qt

class customTableWidget(QTableWidget):
    def __init__(self):
        QTableWidget.__init__(self)

    def keyPressEvent(QKeyEvent, event):
        print(event.key())
        if event.key() == 16777220:
            print("ENTER PRESSED")
            super().insertRow(1)
            super().setCurrentCell((super().currentRow()+1), 0)
            #jobProgressWidget.rowNumber = jobProgressWidget.rowNumber+1
            #jobProgressWidget.cellWatcher

class jobProgressWidget(QWidget):
    def __init__(self, jobNumber, parent=None):
        super(jobProgressWidget, self).__init__(parent)
        self.jobNumber = jobNumber
        layout = QHBoxLayout()

        jobNoLabel = QLabel('Job Number:')
        jobNoEdit = QLineEdit(self)
        jobNoEdit.setReadOnly(True)
        jobNoEdit.setPlaceholderText(str(self.jobNumber))

        jobNotesLabel = QLabel('General Job\nNotes:')
        self.jobNotesEdit = QTextEdit()
        jobTitleBox = QGroupBox("Job Number")
        jobLayout = QHBoxLayout()
        jobLayout.addWidget(jobNoEdit)
        jobTitleBox.setLayout(jobLayout)
        

        partsLabel = QLabel('Parts Used/\nWork Done:')
        self.partsTable = customTableWidget()
        self.partsTable.setRowCount(1)
        self.partsTable.setColumnCount(3)
        partsHeaders = ["Item","Cost ExVat", "Total"]
        self.partsTable.setHorizontalHeaderLabels(partsHeaders)
        self.partsTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.partsTable.cellChanged.connect(self.updateTotals)
    
        
        self.subTotal = QLabel("$Money")
        self.taxAmount = QLabel("$Less Mpney")
        self.totalAmount = QLabel("$More Money")
        updateButton = QPushButton("Update Total")
        updateButton.clicked.connect(self.updateTotals)

        totalLayout = QVBoxLayout()
        totalLayout.addWidget(self.subTotal)
        totalLayout.addWidget(self.taxAmount)
        totalLayout.addWidget(self.totalAmount)

        totalSpace = QVBoxLayout()
        totalSpace.addWidget(updateButton)
        totalSpace.addStretch(1)
        totalAndSpace = QHBoxLayout()
        totalAndSpace.addLayout(totalSpace)
        totalAndSpace.addLayout(totalLayout)

        tableBox = QVBoxLayout()
        tableBox.addWidget(self.partsTable)
        tableBox.addLayout(totalAndSpace)
        tableTitleBox = QGroupBox("Parts Used/Work Done")
        tableTitleBox.setLayout(tableBox)

        leftLayout = QVBoxLayout()
        leftLayout.addWidget(jobTitleBox)
        leftLayout.addWidget(tableTitleBox)

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

        layout.addLayout(leftLayout)
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
