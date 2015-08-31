#******** TODO ********
#- Add Navigation buttons
#    - Tool bar? home But?
#- jOB fORM
#- Job Search
#- Title out of stack?
#- Nav out of stack?
#- Stack in Stack in stack?


import sys
import sip
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
#from PyKde4.kdeui import KIcon


class mainInterface(QWidget):
    def __init__(self):
        super().__init__()
        mainLayout = QVBoxLayout()
        self.centralWidget = QStackedWidget()

        self.buttons = buttonsWidget(self)
        self.buttons.newJobButton.clicked.connect(self.newJob)
        self.buttons.findJobButton.clicked.connect(self.findJob)
        self.centralWidget.addWidget(self.buttons)
        
        #self.progressWidget = progressWidget()

        self.titleLayout = QHBoxLayout()
        horizLine = QFrame()
        horizLine.setFrameShape(QFrame.HLine)
        horizLine.setFrameShadow(QFrame.Sunken)
        homeButton = QToolButton(self)
        homeButton.setToolButtonStyle(2) #Text beside icon
        homeButton.setText("Back")
        homeButton.setIcon(QIcon('back.png'))
        homeButton.setIconSize(QSize(12, 12))
        homeButton.clicked.connect(self.goHome)

        mainLayout.addLayout(self.titleLayout)
        mainLayout.addWidget(horizLine)
        mainLayout.addWidget(self.centralWidget)
        mainLayout.addWidget(homeButton)
        self.setLayout(mainLayout)
        self.setGeometry(390, 365, 390, 365)
    #def hzLine(self):
        #line = QFrame()
        #lane.setFrame
    def newJob(self):
        global progressWidget
        progressWidget = customProgressWidget()
        self.titleLayout.addWidget(progressWidget)
        jobForm = newJobForm()
        self.centralWidget.addWidget(jobForm)
        self.centralWidget.setCurrentWidget(jobForm)
    def findJob(self):
        searchWidget = findJobWidget()
        self.jobSearchTitle = QLabel("Find a Job")
        self.titleLayout.addWidget(self.jobSearchTitle)
        self.centralWidget.addWidget(searchWidget)
        self.centralWidget.setCurrentWidget(searchWidget)
    def goHome(self):
        titleWidget = self.centralWidget.currentWidget()
        if "findJob" in str(titleWidget):
            self.titleLayout.removeWidget(self.jobSearchTitle)
            self.jobSearchTitle.deleteLater()
            self.jobSearchTitle = None
        elif "newJob" in str(titleWidget):
            self.titleLayout.removeWidget(self.progressWidget)
            sip.delete(self.progressWidget) #Steals C++ delete function
            self.progressWidget = None
        self.centralWidget.setCurrentWidget(self.buttons)

#class homeScreen(QWidget):
#    def __init__(self, parent=None):
#        super().__init__()
#        layout(
class customProgressWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()
        self.stageOne = progressButton("Job Info")
        self.stageTwo = progressButton("PersonalInfo")
        layout.addStretch(1)
        layout.addWidget(self.stageOne)
        layout.addWidget(self.stageTwo)
        layout.addStretch(1)
        self.setLayout(layout)
    def changeValue(self, val):
        self.stageOne.setButtonDone()
class progressButton(QWidget):
    def __init__(self, labelText):
        super().__init__()
        layout = QVBoxLayout()
        buttonLayout = QHBoxLayout()
        self.button = QRadioButton()
        self.button.setCheckable(False)
        label = QLabel(labelText)
        buttonLayout.addStretch(1)
        buttonLayout.addWidget(self.button)
        buttonLayout.addStretch(1)
        layout.addLayout(buttonLayout)
        layout.addWidget(label)
        self.setLayout(layout)
    def setButtonDone(self):
        self.button.setCheckable(True)
        self.button.setChecked(True)
        self.button.setEnabled(False)
class buttonsWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        layout = QHBoxLayout()
        self.newJobButton = QToolButton(self)
        self.newJobButton.setToolButtonStyle(3) #text below icon
        self.newJobButton.setText("New Job")
        self.newJobButton.setIcon(QIcon('new.png'))
        self.newJobButton.setIconSize(QSize(64, 64))


        self.findJobButton = QToolButton(self)
        self.findJobButton.setToolButtonStyle(3) #text below icon
        self.findJobButton.setText("Find a Job")
        self.findJobButton.setIcon(QIcon('find.png'))
        self.findJobButton.setIconSize(QSize(64, 64))

        layout.addWidget(self.newJobButton)
        layout.addWidget(self.findJobButton)
        self.setLayout(layout)

class newJobForm(QWidget):
    def __init__(self, parent=None):
        super(newJobForm, self).__init__(parent)
        olayout = QFormLayout()
        #Widgets 
	
	#jobTitle = QLabel("<u>Job Details</u>")
        itemLabel = QLabel('Items:')
        self.itemEdit = QLineEdit(self)
        
        psuLabel = QLabel('Power Supply?') 
        self.psuButtonGroup = QButtonGroup(self)
        psuBox = QHBoxLayout()
        psuY = QCheckBox('Yes', self)
        psuN = QCheckBox('No', self)
        psuNA = QCheckBox('N/A', self)
        psuBox.addWidget(psuY)
        psuBox.addWidget(psuN)
        psuBox.addWidget(psuNA)
        
        problemLabel = QLabel('Job Description:')
        problemEdit = QTextEdit()
        #problemEdit.setFixedHeight(100)
        
        importantDataLabel = QLabel('Any important data on the system?')
        importantDataCheckYes = QCheckBox('Yes', self)
        importantDataCheckNo = QCheckBox('No', self)
        importantDataBox = QHBoxLayout()
        importantDataBox.addWidget(importantDataCheckYes)
        importantDataBox.addWidget(importantDataCheckNo)
        
        dataBackupLabel = QLabel('Data backed up?')
        dataBackupCheckYes = QCheckBox('Yes', self)
        dataBackupCheckNo = QCheckBox('Yes', self)
        dataBackupBox = QHBoxLayout()
        dataBackupBox.addWidget(dataBackupCheckYes)
        dataBackupBox.addWidget(dataBackupCheckNo)
        
        # Back up check boxes set up
        dataBackupGrp = QButtonGroup(self)
        dataBackupGrp.addButton(dataBackupCheckYes)
        dataBackupGrp.addButton(dataBackupCheckNo)
        
        # Important Data check Boxes Set Up
        importantDataGrp = QButtonGroup(self)
        importantDataGrp.addButton(importantDataCheckYes)
        importantDataGrp.addButton(importantDataCheckNo)
#        importantDataGrp.buttonClicked.connect(dataClicked)

        # PSU check Boxes set up
        self.psuButtonGroup.addButton(psuY)
        self.psuButtonGroup.addButton(psuN)
        self.psuButtonGroup.addButton(psuNA)
        # if psuButtonGroup.checkedButton == 0, none clicked
        nextButton = QPushButton("Next", self)
        #nextButton.clicked.connect(lambda: progressWidget.changeValue(1))
        nextButton.clicked.connect(self.errorChecking)
        olayout.addRow(itemLabel, self.itemEdit)
        olayout.addRow(psuLabel, psuBox)
        olayout.addRow(problemLabel, problemEdit)
        olayout.addRow(importantDataLabel, importantDataBox)
        olayout.addRow(dataBackupLabel, dataBackupBox)
        olayout.addRow(nextButton)
        self.setLayout(olayout)
    def errorChecking(self):
        if self.itemEdit.text() == "":
            statusText = "Error: Enter items"
            pass
        elif self.psuButtonGroup.checkedButton == 0:
            statusText = "Error: PSU??"

        print ("Items:", self.itemEdit.text())
        
class findJobWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.layout = QVBoxLayout()
        label = QLabel("Find Job")
        searchLabel = QLabel("Job No:")
        searchField = QLineEdit(self)
        self.searchLayout = QHBoxLayout()
        self.searchLayout.addWidget(searchLabel)
        self.searchLayout.addWidget(searchField)
        
        self.layout.addLayout(self.searchLayout)
        
        self.setLayout(self.layout)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = mainInterface()
    ex.show()
    sys.exit(app.exec_())
    
