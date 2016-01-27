from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import *
import glob
import pickle

class jobsWidget(QWidget):
    def __init__(self, parent=None):
        super(jobsWidget, self).__init__(parent)
        
        layout = QVBoxLayout()
        self.instructions = QLabel("Choose an existing job below to View/Edit, or Add To, or use the buttons on the left to manually use these functions")
        self.jobTable = QTableWidget()
        self.jobTable.setColumnCount(6)
        self.jobTable.setHorizontalHeaderLabels(["Job Number","Customer","Item", "Status", "Edit", "Add To"])
        self.jobTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        compFileList = glob.glob("Jobs/Complete/.1*")
        incompFileList = glob.glob("Jobs/Incomplete/.1*")

        x = 0
        for i in incompFileList:
            self.jobTable.insertRow(x)
            incompStatus = QTableWidgetItem("Incomplete")
            jobNo = i.replace("Jobs/Incomplete/.", "")
            jobNoWidget = QTableWidgetItem(jobNo)
            custData = pickle.load(open("Customers/."+str(jobNo), "rb"))
            name = QTableWidgetItem(custData['name'])
            itemData = pickle.load(open(str(i), "rb"))
            items = QTableWidgetItem(itemData['items'])
            self.jobTable.setItem(x, 0, jobNoWidget) 
            self.jobTable.setItem(x, 1, name)
            self.jobTable.setItem(x, 2, items)
            self.jobTable.setItem(x, 3, incompStatus)
            x += 1

        for i in compFileList:
            self.jobTable.insertRow(x)
            compStatus = QTableWidgetItem("Complete")
            jobNo = i.replace("Jobs/Complete/.", "")
            jobNoWidget = QTableWidgetItem(jobNo)
            custData = pickle.load(open("Customers/."+str(jobNo), "rb"))
            name = QTableWidgetItem(custData['name'])
            itemData = pickle.load(open(str(i), "rb"))
            items = QTableWidgetItem(itemData['items'])
            self.jobTable.setItem(x, 0, jobNoWidget)
            self.jobTable.setItem(x, 1, name)
            self.jobTable.setItem(x, 2, items)
            self.jobTable.setItem(x, 3, compStatus)
            x += 1



        #self.jobTable.setItem(1, 1, test)
        layout.addWidget(self.instructions)
        layout.addWidget(self.jobTable)
        self.rowCount = x
        self.setLayout(layout)
