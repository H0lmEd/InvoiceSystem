from PyQt5.QtWidgets import (QWidget, QFormLayout, QVBoxLayout, QHBoxLayout, QTableWidget,
        QLabel, QLineEdit, QTextEdit, QPushButton, QDesktopWidget, QHeaderView, QHBoxLayout,
        QGroupBox)
from PyQt5.QtCore import Qt, pyqtSlot
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
        #self.partsTable.entered.connect(self.updateTotals)
    
        
        self.subTotal = QLabel("$Money")
        self.taxAmount = QLabel("$Less Mpney")
        self.totalAmount = QLabel("$More Money")
        
        subTotalTitle = QLabel("Sub Total:")
        taxTotalTitle = QLabel("Tax:")
        totalTitle = QLabel("Total:")
        totalTitleLayout = QVBoxLayout()
        totalTitleLayout.addWidget(subTotalTitle)
        totalTitleLayout.addWidget(taxTotalTitle)
        totalTitleLayout.addWidget(totalTitle)

        totalLayout = QVBoxLayout()
        totalLayout.addWidget(self.subTotal)
        totalLayout.addWidget(self.taxAmount)
        totalLayout.addWidget(self.totalAmount)

        totalAndTitleLayout = QHBoxLayout()
        totalAndTitleLayout.addLayout(totalTitleLayout)
        totalAndTitleLayout.addLayout(totalLayout)
        totalAndTitleLayout.addStretch(1)
        
        tableBox = QVBoxLayout()
        tableBox.addWidget(self.partsTable)
        tableBox.addLayout(totalAndTitleLayout)
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
        totalExVat = float(0.00)
        taxTotal = float(0.00)
        total = float(0.00)
        print (self.partsTable.rowCount())
        
        for x in range(self.partsTable.rowCount()):
            
            for i in range(self.partsTable.columnCount()): #go through cells 
                print ('Cell Number:', i, 'Row Number:',x)
                if i == 1:
                    try:
                        totalExVat = float(totalExVat) + float(self.partsTable.item(x,i).text())
                        totalExVat = float(format(totalExVat, '.2f'))
                        taxTotal = float(format((totalExVat*0.2), '0.2f'))
                        total = float(format((totalExVat*1.2), '0.2f'))
                    except AttributeError:
                        print("Attrubute ERror")
                    except ValueError:
                        print("Value Error")
        pound = u'\u00A3'
        self.subTotal.setText(pound+str(totalExVat))
        self.taxAmount.setText(pound+str(taxTotal))
        self.totalAmount.setText(pound+str(total))
