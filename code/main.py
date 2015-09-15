import sys
import os
import sip
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from findJob import findJobWidget
from jobForm import newJobForm
from buttons import buttonsWidget
from personalDetails import custDetailForm
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
        iconFolder = os.path.join(os.path.dirname(__file__), os.pardir, "icons/")

        self.titleLayout = QHBoxLayout()
        horizLine = QFrame()
        horizLine.setFrameShape(QFrame.HLine)
        horizLine.setFrameShadow(QFrame.Sunken)
        homeButton = QToolButton(self)
        homeButton.setToolButtonStyle(2) #Text beside icon
        homeButton.setText("Back")
        homeButton.setIcon(QIcon(iconFolder + 'back.png'))
        homeButton.setIconSize(QSize(12, 12))
        homeButton.clicked.connect(self.goHome)
        self.statusBar = QStatusBar(self)
        self.statusBar.showMessage("Stat")
        jobButton = QPushButton("POST")
        jobButton.clicked.connect(self.personalDeets)
        mainLayout.addLayout(self.titleLayout)
        mainLayout.addWidget(horizLine)
        mainLayout.addWidget(self.centralWidget)
        mainLayout.addWidget(self.statusBar)
        mainLayout.addWidget(jobButton)
        mainLayout.addWidget(homeButton)
        self.setLayout(mainLayout)
        self.setGeometry(390, 365, 390, 365)
    #def hzLine(self):
        #line = QFrame()
        #lane.setFrame
    def newJob(self):
        def errorChecking():
            def writeToFile():
                custItems = jobForm.itemEdit.text()
                if jobForm.psuButtonGroup.checkedId == -2:
                    custPsu = "Yes"
                elif jobForm.psuButtonGroup.checkedId == -3:
                    custPsu = "No"
                else:
                    custPsu = "N/A"
                custProblem = jobForm.problemEdit.toPlainText()
                if jobForm.importantDataGrp.checkedId() == -1:
                    custData = "Yes"
                else:
                    custData = "No"
                if jobForm.dataBackupGrp.checkedId() == -1:
                    custBackup = "Yes"
                else:
                    custBackup = "No"
                fileSaveTo = open("."+str(jobForm.jobNum), "w")
                fileSaveTo.write("Items: "+custItems)
                fileSaveTo.write("\nPSU: "+custPsu)
                fileSaveTo.write("\nProblem: "+custProblem)
                fileSaveTo.write("\nData: "+custData)
                fileSaveTo.write("\nBackup: "+custBackup)
                self.statusBar.showMessage("job Details saved")
                self.personalDeets()
            statusText = "No Eeorrs"

            if jobForm.itemEdit.text() == "":
                statusText = "Error: Enter Items"
                pass
            elif jobForm.psuButtonGroup.checkedId() == -1:
                statusText = "Error: PSU>?"
                pass
            elif jobForm.problemEdit.toPlainText() == "":
                statusText = "Error: no prob?"
                pass
            elif jobForm.importantDataGrp.checkedId() == -1:
                statusText = "Error: DAta?!"
                pass
            elif jobForm.dataBackupGrp.checkedId() == -1:
                statusText = "Error: Backup?"
                pass
            else:
                writeToFile()

            self.statusBar.showMessage(statusText)
        #global progressWidget
        #progressWidget = customProgressWidget()
        #self.titleLayout.addWidget(progressWidget)
        jobForm = newJobForm(self)
        jobForm.nextButton.clicked.connect(errorChecking)
        
        self.centralWidget.addWidget(jobForm)
        self.centralWidget.setCurrentWidget(jobForm)
    def findJob(self):
        searchWidget = findJobWidget(self)
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
    def personalDeets(self):
        def errorChecking():
            def writeToFile():
                pass
            if detailsForm.nameEdit.text() == "":
                statusText = "Error: No name"
                pass
            elif detailsForm.addrEdit.text() == "":
                statusText = "Error: No Address"
                pass
            elif detailsForm.pcEdit.text() == "":
                statusText = "Error: No Postcode"
                pass
            else:
                writeToFile()
        detailsForm = custDetailForm(self)
        detailsForm.nextButton.clicked.connect(errorChecking)
        
        self.centralWidget.addWidget(detailsForm)
        self.centralWidget.setCurrentWidget(detailsForm)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = mainInterface()
    ex.show()
    sys.exit(app.exec_())
    
