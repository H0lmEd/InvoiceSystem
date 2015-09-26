import sys
import os
import sip
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from findJob import findJobWidget
from buttons import buttonsWidget
from jobDisplay import jobDisplayWidget

from personalDetails import custDetailForm
#from PyKde4.kdeui import KIcon


class mainInterface(QWidget):
    def __init__(self):
        super().__init__()
        mainLayout = QVBoxLayout()
        self.centralWidget = QStackedWidget()

        self.buttons = buttonsWidget(self)
        self.buttons.newJobButton.clicked.connect(self.newJob)
        self.buttons.editJobButton.clicked.connect(self.editJob)
        self.buttons.addToJobButton.clicked.connect(self.addToJob)
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
                print ("impdata", jobForm.importantDataGrp.checkedId())
                custDataField = ""
                if jobForm.importantDataGrp.checkedId() == -2:
                    custData = "Yes"
                    custDataField = jobForm.importantData.text()
                else:
                    custData = "No"
                if jobForm.dataBackupGrp.checkedId() == -1:
                    custBackup = "Yes"
                else:
                    custBackup = "No"
                fileSaveTo = open("."+str(jobForm.jobNumber), "a")
                fileSaveTo.write("JOBDETAILS")
                fileSaveTo.write("\n"+custItems)
                fileSaveTo.write("\n"+custPsu)
                fileSaveTo.write("\n"+custProblem)
                fileSaveTo.write("\n"+custData)
                fileSaveTo.write("\n"+custDataField) #if data in there, write, if not line is empty
                fileSaveTo.write("\n"+custBackup)
                self.statusBar.showMessage("job Details saved")
                self.personalDeets(jobForm.jobNumber)
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
        def jobNumberGenerator():
            jobNoFile = open('.jobNum', 'r+')
            self.jobNum = int(jobNoFile.read())
            newJobNum = self.jobNum + 1
            jobNoFile.seek(0)
            jobNoFile.truncate()
            jobNoFile.write(str(newJobNum))
            return self.jobNum

        jobForm = jobDisplayWidget(jobNumberGenerator())
        jobForm.nextButton.clicked.connect(errorChecking)
        jobForm.importantDataGrp.buttonClicked.connect(jobForm.importantDataChecked)
        
        self.centralWidget.addWidget(jobForm)
        self.centralWidget.setCurrentWidget(jobForm)
    def editJob(self):
        def editJobDetails(jobNo):
            jobForm = jobDisplayWidget(int(jobNo))
            #popul8
            origFile = open('.'+jobNo)
            readFile = origFile.readlines() #load file into list
            custItems = readFile[1]
            if 'N/A' in readFile[2]:
                jobForm.psuNA.setChecked(1)
            elif 'No' in readFile[2]:
                jobForm.psuNo.setChecked(1)
            else:
                jobForm.psuYes.setChecked(1)
            custProblem = readFile[3]
            print ("Important Info?:", readFile[4])
            print(origFile.read())
            if 'No' in readFile[4]:
                jobForm.importantDataCheckNo.setChecked(1)
            else:
                jobForm.importantDataCheckYes.setChecked(1)
                jobForm.importantData.setReadOnly(False)
                jobForm.importantData.setText(readFile[5])
            if 'No' in readFile[6]:
                jobForm.dataBackupCheckNo.setChecked(1)
            else:
                custBackup = -1

            jobForm.itemEdit.setText(custItems)
            jobForm.itemEdit.setCursorPosition(0)
            #jobForm.psuButtonGroup.setcheckedId(custPsu)
            jobForm.problemEdit.setText(custProblem)
            
            self.centralWidget.addWidget(jobForm)
            print("Editing Job",int(jobNo))
            self.centralWidget.setCurrentWidget(jobForm)
            jobForm.nextButton.connect(self.editPersonalDeets)

        searchWidget = findJobWidget(self)
        self.jobSearchTitle = QLabel("Find a Job")
        self.titleLayout.addWidget(self.jobSearchTitle)
        self.centralWidget.addWidget(searchWidget)
        self.centralWidget.setCurrentWidget(searchWidget)
        def errorChecking():
            print (len(searchWidget.searchField.text()))
            if len(searchWidget.searchField.text()) == 6:
                print("success")
                editJobDetails(searchWidget.searchField.text())
        searchWidget.searchBtn.clicked.connect(errorChecking)

    def editPersonalDeets(self):
        pas
    def addToJob(self):
        pass
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
    def personalDeets(self, jobNum):
        print("Job No:",jobNum)
        def errorChecking():
            def writeToFile():
                custName = detailsForm.nameEdit.text()
                custAddrOne = detailsForm.addrLineOne.text()
                custAddrTwo = detailsForm.addrLineTwo.text()
                custPC = detailsForm.pcLineEdit.text()

                fileSaveTo = open("."+str(jobNum), "a")
                fileSaveTo.write("\nPERSONALDETAILS\n"+custName)
                fileSaveTo.write('\n'+custAddrOne)
                fileSaveTo.write('\n'+custAddrTwo)
                fileSaveTo.write('\n'+custPC)
                fileSaveTo.close()
                self.statusBar.showMessage("Job Details Saved")
                
            statusText = "NO Errors"
            if detailsForm.nameEdit.text() == "":
                statusText = "Error: No name"
                pass
            elif detailsForm.addrLineOne.text() == "":
                statusText = "Error: No Address"
                pass
            elif detailsForm.addrLineTwo.text() == "":
                statusText = "Error: No Address"
                pass
            elif detailsForm.pcLineEdit.text() == "":
                statusText = "Error: No Postcode"
                pass
            else:
                writeToFile()
            
            self.statusBar.showMessage(statusText)
        detailsForm = custDetailForm(True)
        detailsForm.nextButton.clicked.connect(errorChecking)
        
        self.centralWidget.addWidget(detailsForm)
        self.centralWidget.setCurrentWidget(detailsForm)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = mainInterface()
    ex.show()
    sys.exit(app.exec_())
    
