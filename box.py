import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimeLine
from PyQt5.QtGui import *

class TabWidget(QTabWidget):
    def __init__(self):
        QTabWidget.__init__(self, parent = None)

    def setCurrentIndex(self, index):
        self.faderWidget = FaderWidget(self.currentWidget(), self.widget(index))
        QTabWidget.setCurrentIndex(self, index)

#    def tabBarClicked(self, index):
#        self.setCurrentIndex(index)

    def setTab1(self):
        self.setCurrentIndex(0)
    def setTab2(self):
        self.setCurrentIndex(1)

class mainInterface(QWidget):
    def __init__(self):
        super().__init__()
        tabw = TabWidget()
        
        newJobTab = QWidget()
        findJobTab = QWidget()
        title = QLabel("Use the tabs to choose a task to perform. Hover over each tab for extra information")
        
        tabw.addTab(newJobTab, "New Job")
        tabw.addTab(findJobTab, "Find/Edit a Job")
        tabw.setTabToolTip(0, "Add a new Job")
        tabw.setTabToolTip(1, "Find and Edit an Exisiting Job")
        
        self.findJobLayout = QGridLayout(findJobTab)
        self.splitJobLayout = QHBoxLayout(newJobTab)
        
        self.newJob()
        self.findJob()
        
        

        
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(title)
        mainLayout.addWidget(tabw)
        self.setLayout(mainLayout)
        self.setGeometry(300, 300, 305, 305)
        self.setWindowTitle("Alpha Testing")
        self.show()

    def newJob(self):
        
        
        self.leftPanel = QFrame(self)
        self.rightPanel = QFrame(self)
        
        #LEFT PANEL
        def jobDetails(self):
            
            # WIDGET DEFINITION
            jobTitle = QLabel("<u>Job Details</u>")
            itemLabel = QLabel('Items:')
            itemEdit = QLineEdit(self)
            
            psuLabel = QLabel('Power Supply?') 
            psuButtonGroup = QButtonGroup(self)
            psuY = QCheckBox('Yes', self)
            psuN = QCheckBox('No', self)
            psuNA = QCheckBox('N/A', self)
            
            problemLabel = QLabel('Job Description:')
            problemEdit = QTextEdit()
            
            importantDataLabel = QLabel('Any important data on the system?')
            importantDataCheckYes = QCheckBox('Yes', self)
            importantDataCheckNo = QCheckBox('No', self)

            dataBackupLabel = QLabel('Data backed up?')
            dataBackupCheckYes = QCheckBox('Yes', self)
            dataBackupCheckNo = QCheckBox('Yes', self)
            
            dataBackupGrp = QButtonGroup(self)
            dataBackupGrp.addButton(dataBackupCheckYes)
            dataBackupGrp.addButton(dataBackupCheckNo)
            
            #importantDataGrp.buttonClicked.connect(dataClicked)
            
            # PSU check Boxes set up
            psuButtonGroup.addButton(psuY)
            psuButtonGroup.addButton(psuN)
            psuButtonGroup.addButton(psuNA)
            
            itemBox = QHBoxLayout()
            itemBox.addWidget(itemLabel)
            itemBox.addWidget(itemEdit)
            itemBox.setSpacing(10)
            
            psuBox = QHBoxLayout()
            psuBox.addWidget(psuLabel)
            psuBox.addWidget(psuY)
            psuBox.addWidget(psuN)
            psuBox.addWidget(psuNA)
            psuBox.setSpacing(10)
            
            problemBox = QHBoxLayout()
            problemBox.addWidget(problemLabel)
            problemBox.addWidget(problemEdit)
            problemBox.setSpacing(10)
            
            importantDataBox = QHBoxLayout()
            importantDataBox.addWidget(importantDataLabel)
            importantDataBox.addWidget(importantDataCheckYes)
            importantDataBox.addWidget(importantDataCheckNo)
            importantDataBox.setSpacing(10)
            
            dataBackupBox = QHBoxLayout()
            dataBackupBox.addWidget(dataBackupLabel)
            dataBackupBox.addWidget(dataBackupCheckYes)
            dataBackupBox.addWidget(dataBackupCheckNo)
            dataBackupBox.setSpacing(10)
            
            newJobLayout = QVBoxLayout()
            newJobLayout.setSpacing(10)
            newJobLayout.addWidget(jobTitle)
            newJobLayout.addLayout(itemBox)
            newJobLayout.addLayout(psuBox)
            newJobLayout.addLayout(problemBox)
            newJobLayout.addLayout(importantDataBox)
            newJobLayout.addLayout(dataBackupBox)
            
            self.leftPanel.setLayout(newJobLayout)
            self.splitJobLayout.addWidget(self.leftPanel)
            
        def personalDetails(self):
            detailsTitle = QLabel("<b><u>Customer's Personal Details</u></b>")
            nameLabel = QLabel("Name")
            nameEdit = QLineEdit(self)
            addressLabel = QLabel("Address")
            addressEdit = QLineEdit(self)
            phoneLabel = QLabel("Phone Number")
            phoneEdit = QLineEdit(self)
            mobileLabel = QLabel("Mobile Number")
            mobileEdit = QLineEdit(self)
            emailLabel = QLabel("Email")
            emailEdit = QLineEdit(self)
            
            nameBox = QHBoxLayout()
            nameBox.addWidget(nameLabel)
            nameBox.addWidget(nameEdit)
            nameBox.setSpacing(10)
            
            addressBox = QHBoxLayout()
            addressBox.addWidget(addressLabel)
            addressBox.addWidget(addressEdit)
            addressBox.setSpacing(10)
            
            phoneBox = QHBoxLayout()
            phoneBox.addWidget(phoneLabel)
            phoneBox.addWidget(phoneEdit)
            phoneBox.setSpacing(10)
            
            mobileBox = QHBoxLayout()
            mobileBox.addWidget(mobileLabel)
            mobileBox.addWidget(mobileEdit)
            mobileBox.setSpacing(10)
            
            emailBox = QHBoxLayout()
            emailBox.addWidget(emailLabel)
            emailBox.addWidget(emailEdit)
            emailBox.setSpacing(10)
            
            pDetailsLayout = QVBoxLayout()
            pDetailsLayout.addWidget(detailsTitle)
            pDetailsLayout.addLayout(nameBox)
            pDetailsLayout.addLayout(addressBox)
            pDetailsLayout.addLayout(phoneBox)
            pDetailsLayout.addLayout(mobileBox)
            pDetailsLayout.addLayout(emailBox)
            
            self.rightPanel.setLayout(pDetailsLayout)
            self.splitJobLayout.addWidget(self.rightPanel)
   
        jobDetails(self)
        personalDetails(self)
    def findJob(self):
        #   Find Job
        findJobTitle = QLabel('Enter Job Number')
        findJobEdit = QLineEdit(self)
        findJobLayout = QGridLayout()
        findJobLayout.setSpacing(10)
        findJobLayout.addWidget(findJobTitle, 1, 0)
        findJobLayout.addWidget(findJobEdit, 1, 1)
        
        
        
if __name__ == '__main__':
    app  = QApplication(sys.argv)
    ex = mainInterface()
    sys.exit(app.exec_())
