from PyQt5.QtWidgets import (QWidget, QFormLayout, QVBoxLayout, QHBoxLayout, QTableWidget,
        QLabel, QLineEdit, QTextEdit, QPushButton, QDesktopWidget, QHeaderView, QHBoxLayout,
        QGroupBox, QMessageBox, QToolButton)
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtGui import QIcon
from customWidgets import customTableWidget
import pickle
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
        
        def test():
            print("Ok")
        partsLabel = QLabel('Parts Used/\nWork Done:')
        #self.partsTable = customTableWidget()
        #self.partsTable.setRowCount(1)
        #self.partsTable.setColumnCount(2)
        #partsHeaders = ["Item","Cost ExVat"]
        #self.partsTable.setHorizontalHeaderLabels(partsHeaders)
        #self.partsTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        #self.partsTable.cellChanged.connect(self.updateTotals)
        #self.partsTable.entered.connect(self.updateTotals)
        itemLabel = QLabel("Item")
        priceLabel = QLabel("Price")
        self.items = 0
        self.item = {}
        self.price = {}
        self.item[0] = QLineEdit(self)
        self.price[0] = QLineEdit(self)
        self.addButton = QToolButton(self)
        self.addButton.setIcon(QIcon.fromTheme("list-add"))
        self.addButton.clicked.connect(lambda: self.addItems(self.item[0].text(), self.price[0].text()))
        self.priceLayout = QVBoxLayout()
        self.priceLayout.addWidget(priceLabel)
        self.priceLayout.addWidget(self.price[0])
        self.itemLayout = QVBoxLayout()
        self.itemLayout.addWidget(itemLabel)
        self.itemLayout.addWidget(self.item[0])

        self.removeButton = {}
        self.buttonLayout = {}
        self.buttonColumn = QVBoxLayout()
        self.buttonColumn.addWidget(self.addButton)

        self.tableLayout = QHBoxLayout()
        self.tableLayout.addLayout(self.itemLayout)
        self.tableLayout.addLayout(self.priceLayout)
        self.tableLayout.addLayout(self.buttonColumn)

        self.saveButton = QPushButton("Save") 
        
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
        totalAndTitleLayout.addWidget(self.saveButton)
        
        tableBox = QVBoxLayout()
        tableBox.addLayout(self.tableLayout)
        tableBox.addStretch(1)
        tableBox.addLayout(totalAndTitleLayout)
        tableTitleBox = QGroupBox("Parts Used/Work Done")
        tableTitleBox.setLayout(tableBox)

        leftLayout = QVBoxLayout()
        leftLayout.addWidget(jobTitleBox)
        leftLayout.addWidget(notesTitleBox)

        layout.addLayout(leftLayout)
        layout.addWidget(tableTitleBox)
        self.setLayout(layout)
    def addItems(self, itemContent, priceContent):
        self.items += 1
        x = self.items
        #itemContent = self.item[0].text()
        #priceContent = self.price[0].text()
        self.item[0].setText("")
        self.price[0].setText("")
        self.item[x] = QLineEdit(self)
        self.item[x].setText(itemContent)
        self.itemLayout.addWidget(self.item[x])
        self.price[x] = QLineEdit(self)
        self.price[x].setText(priceContent)
        self.priceLayout.addWidget(self.price[x])
        #self.buttonColumn.removeWidget(self.addButton)
        
        self.removeButton[x] = QToolButton(self)
        self.removeButton[x].setIcon(QIcon.fromTheme("list-remove"))
        self.removeButton[x].setToolButtonStyle(2)
        self.removeButton[x].setText(str(x))
        self.removeButton[x].clicked.connect(lambda: self.removeItems(x)) #Deletes previous line, not current
        
        self.buttonLayout[x] = QHBoxLayout()
        self.buttonLayout[x].addWidget(self.removeButton[x])
        self.buttonColumn.addLayout(self.buttonLayout[x])
        #self.buttonColumn.addWidget(self.addButton)
        self.updateTotals()
    def removeItems(self, x):
        self.removals = []
        self.removals.append(x)
        print("X:",x)
        self.itemLayout.removeWidget(self.item[x])
        self.priceLayout.removeWidget(self.price[x])
        self.buttonLayout[x].removeWidget(self.removeButton[x])

        self.buttonColumn.removeItem(self.buttonLayout[x])
        
        self.item[x].deleteLater()
        del self.item[x]
        self.price[x].deleteLater()
        del self.price[x]
        self.removeButton[x].deleteLater()
        del self.removeButton[x]
        print("Job Number", self.jobNumber)
        self.items -= 1
        
        print("itemLength",len(self.item),"Dict",self.item)
        



    def updateTotals(self):
        count = 0
        rount = 0
        totalExVat = float(0.00)
        taxTotal = float(0.00)
        total = float(0.00)
        for i in range(0, len(self.item)):
            if i == 0:
                pass
            else:
                totalExVat = float(totalExVat)+float((self.price[i].text()))

        totalExVat = float(format(totalExVat, '.2f'))
        taxTotal = float(format((totalExVat*0.2), '0.2f'))
        total = float(format((totalExVat*1.2), '0.2f'))
        
        pound = u'\u00A3'
        self.subTotal.setText(pound+str(totalExVat))
        self.taxAmount.setText(pound+str(taxTotal))
        self.totalAmount.setText(pound+str(total))
