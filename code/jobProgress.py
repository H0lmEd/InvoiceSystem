from PyQt5.QtWidgets import (QWidget, QFormLayout, QHBoxLayout, QTableWidget,
        QLabel, QLineEdit, QTextEdit, QPushButton, QDesktopWidget, QHeaderView)
from PyQt5.QtCore import Qt

class customTableWidget(QTableWidget):
    def __init__(self):
        QTableWidget.__init__(self)

    def keyPressEvent(QKeyEvent, event):
        print(event.key())
        if event.key() == 16777220:
            print("ENTER PRESSED")
            super().insertRow(1)


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
        addRowButton = QPushButton('+')
        self.partsTable = customTableWidget()
        self.partsTable.setRowCount(1)
        self.partsTable.setColumnCount(3)
        tableBox = QHBoxLayout()
        tableBox.addWidget(self.partsTable)
        tableBox.addWidget(addRowButton)
        tableHeaders = ["Item","Cost", "Total"]
        self.partsTable.setHorizontalHeaderLabels(tableHeaders)
        self.partsTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        addRowButton.clicked.connect(self.partsTable.insertRow)

        layout.addRow(jobNoLabel, jobNoEdit)
        layout.addRow(jobNotesLabel, self.jobNotesEdit)
        layout.addRow(partsLabel, tableBox)

        self.setLayout(layout)

