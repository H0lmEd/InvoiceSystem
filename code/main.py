# ah BUGS:
# Pressing Enter in "Fault: fucks shit up"
import sys
import os
import sip

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from findJob import findJobWidget
from buttons import buttonsWidget
from jobDisplay import jobDisplayWidget
from jobProgress import jobProgressWidget
from personalDetails import custDetailForm
#from PyKde4.kdeui import KIcon


class mainInterface(QWidget):
    def __init__(self):
        super().__init__()
        mainLayout = QVBoxLayout()
        self.centralWidget = QStackedWidget()

        self.buttons = buttonsWidget(self)
        self.buttons.newJobButton.clicked.connect(self.newJob)
        self.buttons.editJobButton.clicked.connect(lambda: self.getJobNumber(1))
        self.buttons.addToJobButton.clicked.connect(lambda: self.getJobNumber(2))
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
        #self.setGeometry(790, 365, 390, 365)
        self.resize(600, 600)
    #def hzLine(self):
        #line = QFrame()
        #lane.setFrame
    def newJob(self):
        def writeToFile():
            staff = jobForm.staffEdit.text()
            custItems = jobForm.itemEdit.text()
            if jobForm.psuButtonGroup.checkedId == -2:
                custPsu = "Yes"
            elif jobForm.psuButtonGroup.checkedId == -3:
                custPsu = "No"
            else:
                custPsu = "N/A"
            itemCondition = jobForm.condition.text()
            custProblem = jobForm.problemEdit.toPlainText()
            custPasswordField = ""
            print("Passwords",jobForm.passButtonGrp.checkedId())
            if jobForm.passButtonGrp.checkedId() == -2:
                print("Password Detected")
                custPasswords =  "Yes"
                custPasswordField = jobForm.passwords.toPlainText()
            else:
                print("No Password")
                custPasswords = "No"
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
            fileSaveTo.write("\n"+staff)
            fileSaveTo.write("\n"+custItems)
            fileSaveTo.write("\n"+custPsu)
            fileSaveTo.write("\n"+itemCondition)
            fileSaveTo.write("\n"+custProblem)
            fileSaveTo.write("\n"+custPasswordField)
            fileSaveTo.write("\n"+custData)
            fileSaveTo.write("\n"+custDataField) #if data in there, write, if not line is empty
            fileSaveTo.write("\n"+custBackup)
            self.statusBar.showMessage("job Details saved")
            self.personalDeets(jobForm.jobNumber)
            statusText = "No Eeorrs"
        def staffEditCheck():
           if jobForm.staffEdit.text() == "":
                jobForm.staffVal.error()
                
                self.errorsDetected = True
           else:
                jobForm.staffVal.tick()
        def itemEditCheck():
            if jobForm.itemEdit.text() == "":
                jobForm.itemVal.error()
                self.errorsDetected = True
            else:
                jobForm.itemVal.tick()
        def psuButtonCheck():
            if jobForm.psuButtonGroup.checkedId() == -1:
                jobForm.psuVal.error()
                self.errorsDetected = True
            else:
                jobForm.psuVal.tick()

        def conditionCheck():
            if jobForm.condition.text() == "":
                jobForm.conditionVal.error()
                self.errorsDetected = True
            else:
                jobForm.conditionVal.tick()
        def problemEditCheck():
            self.errorsDetected = False
            if jobForm.problemEdit.toPlainText() == "":
                jobForm.problemVal.error()
                self.errorsDetected = True
            else:
                jobForm.problemVal.tick()
        def passwordsBoxCheck():
            if jobForm.passButtonGrp.checkedId() == -1:
                jobForm.passwordCheckVal.error()
                self.errorsDetected = True
            else:
                jobForm.passwordCheckVal.tick()
        def passwordsCheck():
            if jobForm.passwords.toPlainText() == "":
                jobForm.passwordsVal.error()
                self.errorsDetected = True
            else:
                jobForm.passwordCheckVal.tick()
        def importantDataBoxCheck():
            if jobForm.importantDataGrp.checkedId() == -1:
                jobForm.importantDataCheckVal.error()
                self.errorsDetected = True
            else:
                jobForm.importantDataCheckVal.tick()
        def importantDataFieldCheck():
            if jobForm.importantData.text() == "":
                jobForm.importantDataVal.error()
                self.errorsDetected = True
            else:
                jobForm.importantDataVal.tick()
        def dataBackupCheck():
            self.errorsDetected = False
            if jobForm.dataBackupGrp.checkedId() == -1:
                jobForm.dataBackupCheckVal.error()
                self.errorsDetected = True
            else:
                jobForm.dataBackupCheckVal.tick()
            
        def errorChecking():    
            errorFunctions = [staffEditCheck, itemEditCheck, psuButtonCheck, 
                                conditionCheck,problemEditCheck, passwordsBoxCheck,
                                passwordsCheck, importantDataBoxCheck, 
                                importantDataFieldCheck, dataBackupCheck]
            self.errorsDetected = False
            x=0
            for i in errorFunctions:
                print(i,x)
                if x == 8 and jobForm.importantDataGrp.checkedId() != -2:
                    print ("Passing")
                    jobForm.importantDataCheckVal.tick()
                    pass
                else:
                    i()
                if self.errorsDetected == True:
                    self.statusBar.showMessage("Fix Errors")
                    break
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
    def addToJob(self, jobNo):
        jobProgress = jobProgressWidget(jobNo)
        self.centralWidget.addWidget(jobProgress)
        self.centralWidget.setCurrentWidget(jobProgress)
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
        def writeToFile():
            custName = detailsForm.nameEdit.text()
            custAddrOne = detailsForm.addrLineOne.text()
            custAddrTwo = detailsForm.addrLineTwo.text()
            custPC = detailsForm.pcLineEdit.text()

            fileSaveTo = open("."+str(jobNum), "a")
            fileSaveTo.write("\nPERSONALDETAILS\n"+custName)
            fileSaveTo.write('\n'+custPC)
            fileSaveTo.write('\n'+custAddrOne)
            fileSaveTo.write('\n'+custAddrTwo)
            fileSaveTo.close()
            self.statusBar.showMessage("Job Details Saved")
                
        def nameEditCheck():
            if detailsForm.nameEdit.text() == "":
                detailsForm.nameVal.error()
                self.errorsDetected = True
            else:
                detailsForm.nameVal.tick()
        def emailCheck():
            if detailsForm.emailAddr.text() == "":
                pass
            elif "@" in detailsForm.emailAddr.text() and "." in detailsForm.emailAddr.text():
                detailsForm.emailVal.tick()
            else:
                detailsForm.emailVal.error()
                self.errorsDetected = True
        def phoneCheck():
            if detailsForm.phoneNo.text() == "":
                pass
            else:
                phoneFull = detailsForm.phoneNo.text().replace(" ","")
                if phoneFull.isdigit() and phoneFull[0] == 0 and phoneFull.len() == 11:
                    detailsForm.phoneVal.tick()
                else:
                    detailsForm.phoneVal.error()
        def pcEditCheck():
            if detailsForm.pcLineEdit.text() == "":
                self.errorsDetected = True                
                detailsForm.pcVal.error()
            else:
                detailsForm.pcVal.tick()

            if detailsForm.addrLineOne.text() == "" or detailsForm.addrLineTwo.text() == "":
                self.errorsDetected = True
                detailsForm.addrLineOneVal.error()
        def errorChecking():
            errorFunctions = [nameEditCheck, emailCheck, phoneCheck, pcEditCheck]
            self.errorsDetected = False
            x = 0
            for i in errorFunctions:
                print(i,x)
                i()
                if self.errorsDetected == True:
                    self.statusBar.showMessage("Fix Errors")
                    print("ERRORS")
                    break
        detailsForm = custDetailForm(True)
        detailsForm.nextButton.clicked.connect(errorChecking)
        self.centralWidget.addWidget(detailsForm)
        self.centralWidget.setCurrentWidget(detailsForm)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = mainInterface()
    ex.show()
    sys.exit(app.exec_())

# ah BUGS:
# Pressing Enter in "Fault: fucks shit up"
