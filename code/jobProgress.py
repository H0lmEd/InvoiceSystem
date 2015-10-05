from PyQt5.QtWidgets import (QWidget, QFormLayout, QVBoxLayout, QTableWidget,
        QLabel, QLineEdit, QTextEdit, QPushButton, QDesktopWidget, QHeaderView, QHBoxLayout)
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
        layout = QFormLayout(self)
        jobNoLabel = QLabel('Job Number:')
        jobNoEdit = QLineEdit(self)
        jobNoEdit.setReadOnly(True)
        jobNoEdit.setPlaceholderText(str(self.jobNumber))

        jobNotesLabel = QLabel('General Job\nNotes:')
        self.jobNotesEdit = QTextEdit()

        partsLabel = QLabel('Parts Used/\nWork Done:')
        self.partsTable = customTableWidget()
        self.partsTable.setRowCount(1)
        self.partsTable.setColumnCount(3)
        tableHeaders = ["Item","Cost ExVat", "Total"]
        self.partsTable.setHorizontalHeaderLabels(tableHeaders)
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
        layout.addRow(jobNoLabel, jobNoEdit)
        layout.addRow(jobNotesLabel, self.jobNotesEdit)
        layout.addRow(partsLabel, tableBox)

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
        
        self.subTotal.setText(str(totalExVat))
        self.taxAmount.setText(str((totalExVat*0.2)))
        self.totalAmount.setText(str((totalExVat*1.2)))
