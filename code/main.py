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
from callLog import callLogWidget
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
        self.buttons.callLogButton.clicked.connect(lambda: self.getJobNumber(3))
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
            if jobForm.psuButtonGroup.checkedId() == -2:
                custPsu = "Yes"
            elif jobForm.psuButtonGroup.checkedId() == -3:
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
                custPasswordField = ""
            if jobForm.importantDataGrp.checkedId() == -2:
                custData = "Yes"
                custDataField = jobForm.importantData.text()
            else:
                custData = "No"
                custDataField = ""
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
            fileSaveTo.write("\n"+custPasswords)
            fileSaveTo.write("\n"+custPasswordField)
            fileSaveTo.write("\n"+custData)
            fileSaveTo.write("\n"+custDataField) #if data in there, write, if not line is empty
            fileSaveTo.write("\n"+custBackup)
            self.statusBar.showMessage("job Details saved")
            statusText = "No Eeorrs"
        
        def staffEditCheck():
            print("Staff",jobForm.staffEdit.text())
            if jobForm.staffEdit.text() == "":
                jobForm.staffVal.error()
                
                self.errorsDetected = True
            else:
                jobForm.staffVal.tick()
        def itemEditCheck():
            print("Item Check")
            if jobForm.itemEdit.text() == "":
                jobForm.itemVal.error()
                print("Item Error")
                self.errorsDetected = True
            else:
                jobForm.itemVal.tick()
                print("Item PAss")
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
            print("id", jobForm.psuButtonGroup.checkedId())
            errorFunctions = [staffEditCheck, itemEditCheck, psuButtonCheck, 
                                conditionCheck,problemEditCheck, passwordsBoxCheck,
                                passwordsCheck, importantDataBoxCheck, 
                                importantDataFieldCheck, dataBackupCheck]
            self.errorsDetected = False
            x=0
            for i in errorFunctions:
                print(i,x)
                print("Checking for Errors")
                if (x == 8 and jobForm.importantDataGrp.checkedId() != -2) or (x == 6 and jobForm.passButtonGrp.checkedId() != -2):
                    print ("Passing")
                    x = x+1
                    jobForm.importantDataCheckVal.tick()
                    pass
                else:
                    i()
                    x = x+1
                if self.errorsDetected == True:
                    self.statusBar.showMessage("Fix Errors")
                    break
                elif self.errorsDetected == False and x == 10:
                    print("Writing to File")
                    self.personalDeets(jobForm.jobNoEdit.text())
        
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
   
    def getJobNumber(self, nextFunction):
        searchWidget = findJobWidget(self)
        self.jobSearchTitle = QLabel("Find a Job")
        #self.titleLayout.addWidget(self.jobSearchTitle)
        self.centralWidget.addWidget(searchWidget)
        self.centralWidget.setCurrentWidget(searchWidget)
        def errorChecking():
            print (len(searchWidget.searchField.text()))
            if len(searchWidget.searchField.text()) == 6:
                print("success")
                if nextFunction == 1:
                    self.editJobDetails(int(searchWidget.searchField.text()))
                elif nextFunction == 2:
                    self.addToJob(int(searchWidget.searchField.text()))
                elif nextFunction == 3:
                    self.jobCalls(int(searchWidget.searchField.text()))
        searchWidget.searchBtn.clicked.connect(errorChecking)
    def editPersonalDeets(self):
        detailsForm = custDetailForm(False)
        print(self.readFile)
        detailsForm.nameEdit.setText(self.readFile[12])
        if self.readFile[13] != "":
            detailsForm.emailAddr.setText(self.readFile[13])
        if self.readFile[14] != "":
            detailsForm.phoneNo.setText(self.readFile[14])
        detailsForm.mobileNo.setText(self.readFile[15])
        detailsForm.pcEdit.setText(self.readFile[16])
        detailsForm.addrLineOne.setText(self.readFile[17])
        detailsForm.addrLineTwo.setText(self.readFile[18])
        self.centralWidget.addWidget(detailsForm)
        self.centralWidget.setCurrentWidget(detailsForm)
         
    def editJobDetails(self, jobNo):
        def errorChecking():
            self.staffEdit = jobForm.staffEdit
            if self.jobDisplayErrorChecking(jobNo) == 1:
                print ("No Errors RETURNED")
        jobForm = jobDisplayWidget(int(jobNo))
        #popul8
        origFile = open('.'+str(jobNo))
        self.readFile = origFile.readlines() #load file into list
        print("FIle:",self.readFile)
        staff = self.readFile[1]
        custItems = self.readFile[2]
        if 'N/A' in self.readFile[3]:
            jobForm.psuNA.setChecked(1)
        elif 'No' in self.readFile[3]:
            jobForm.psuNo.setChecked(1)
        else:
            jobForm.psuYes.setChecked(1)
        itemCondition = self.readFile[4]
        custProblem = self.readFile[5]
        if "No" in self.readFile[6]:
            jobForm.passwordCheckNo.setChecked(1)
        elif "Yes" in self.readFile[6]:
            jobForm.passwordCheckYes.setChecked(1)
            jobForm.passwords.setText(self.readFile[7])
        print(origFile.read())
        if 'No' in self.readFile[8]:
            jobForm.importantDataCheckNo.setChecked(1)
        else:
            jobForm.importantDataCheckYes.setChecked(1)
            jobForm.importantData.setReadOnly(False)
            jobForm.importantData.setText(self.readFile[9])
        if 'No' in self.readFile[10]:
            jobForm.dataBackupCheckNo.setChecked(1)
        else:
            jobForm.dataBackupCheckYes.setChecked(1)
        jobForm.itemEdit.setText(custItems)
        jobForm.staffEdit.setText(staff)
        jobForm.itemEdit.setCursorPosition(0)
        #jobForm.psuButtonGroup.setcheckedId(custPsu)
        jobForm.condition.setText(itemCondition)
        jobForm.problemEdit.setText(custProblem)
        
        self.centralWidget.addWidget(jobForm)
        print("Editing Job",int(jobNo))
        self.centralWidget.setCurrentWidget(jobForm)
        jobForm.nextButton.clicked.connect(lambda: errorChecking())

        
    def jobDisplayErrorChecking(self, jobNo):
        jobForm = jobDisplayWidget(int(jobNo))
                 
    
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
        print("Job 1No:",jobNum)
        def writeToFile():
            custName = detailsForm.nameEdit.text()
            if self.emailPresent:
                custEmail = detailsForm.emailAddr.text()
            else:
                custEmail = ""
            if self.phonePresent:
                custPhoneNo = detailsForm.phoneNo.text()
            else:
                custPhoneNo = ""
            custMobileNo = detailsForm.mobileNo.text()
            custPC = detailsForm.pcLineEdit.text()
            custAddrOne = detailsForm.addrLineOne.text()
            custAddrTwo = detailsForm.addrLineTwo.text()
            
            fileSaveTo = open("."+str(jobNum), "a")
            fileSaveTo.write("\nPERSONALDETAILS\n"+custName)
            fileSaveTo.write('\n'+custEmail)
            fileSaveTo.write('\n'+custPhoneNo)
            fileSaveTo.write('\n'+custMobileNo)
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
                self.emailPresent = False
            elif "@" in detailsForm.emailAddr.text() and "." in detailsForm.emailAddr.text():
                detailsForm.emailVal.tick()
                self.emailPresent = True
            else:
                detailsForm.emailVal.error()
                self.errorsDetected = True
        def phoneCheck():
            if detailsForm.phoneNo.text() == "":
                self.phonePresent = False
            else:
                phoneFull = detailsForm.phoneNo.text().replace(" ","")
                print("HomePhone",phoneFull)
                print(phoneFull.isdigit(),phoneFull[0], len(phoneFull))
                if phoneFull.isdigit() and int(phoneFull[0]) == 0 and len(phoneFull) == 11:
                    detailsForm.phoneVal.tick()
                    self.phonePresent = True
                else:
                    detailsForm.phoneVal.error()
        def mobileCheck():
            if detailsForm.mobileNo.text() == "":
                detailsForm.mobileVal.error()
                self.errorsDetected = True
            else:
                detailsForm.mobileVal.tick()
        def pcEditCheck():
            if detailsForm.pcLineEdit.text() == "":
                self.errorsDetected = True                
                detailsForm.pcVal.error()
            else:
                detailsForm.pcVal.tick()
        def addrOneCheck():
            if detailsForm.addrLineOne.text() == "":
                detailsForm.addrLineOneVal.error()
                self.errorsDetected = True
            else:
                detailsForm.addrLineOneVal.tick()
        def addrTwoCheck():
            if detailsForm.addrLineTwoVal.error():
                self.errorsDetected = True
            else:
                detailsForm.addrLineTwoVal.tick()
        def errorChecking():
            errorFunctions = [nameEditCheck, emailCheck, phoneCheck, mobileCheck,
                                pcEditCheck, addrOneCheck, addrTwoCheck]
            self.errorsDetected = False
            x = 0
            for i in errorFunctions:
                print(i,x)
                i()
                x = x+1
                if self.errorsDetected == True:
                    self.statusBar.showMessage("Fix Errors")
                    print("ERRORS")
                    break
                elif self.errorsDetected == False and x == 7:
                    print("WRote")
                    writeToFile()
                    self.goHome()
        detailsForm = custDetailForm(True)
        detailsForm.nextButton.clicked.connect(errorChecking)
        self.centralWidget.addWidget(detailsForm)
        self.centralWidget.setCurrentWidget(detailsForm)

    def jobCalls(self, jobNo):
        callLog = callLogWidget(jobNo)
        self.centralWidget.addWidget(callLog)
        self.centralWidget.setCurrentWidget(callLog)
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = mainInterface()
    ex.show()
    sys.exit(app.exec_())

# ah BUGS:
# Pressing Enter in "Fault: fucks shit up"
