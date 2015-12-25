# ah BUGS:
#   - Can leave "Add To" Without saving
#   - 
import sys
import os
import sip
import pickle
# PICKLE SHIT UP YO
# - 
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from findJob import findJobWidget
from buttons import buttonsWidget
from startScreen import startScreenForm
from jobDisplay import jobDisplayWidget
from jobProgress import jobProgressWidget
from personalDetails import custDetailForm
from jobs import jobsWidget
#from PyKde4.kdeui import KIcon


class mainInterface(QWidget):
    def __init__(self):
        super().__init__()
        centralLayout = QVBoxLayout()
        mainLayout = QHBoxLayout()
        self.centralWidget = QStackedWidget()
        self.buttons = buttonsWidget(self)
        
        self.buttons.newJobButton.triggered.connect(self.newJob)
        self.buttons.editJobButton.triggered.connect(lambda: self.getJobNumber(1))
        self.buttons.addToJobButton.triggered.connect(lambda: self.getJobNumber(2))
        self.buttons.jobsButton.triggered.connect(self.jobs)
        self.buttons.homeButton.triggered.connect(self.startScreen)        
        vertLine = QFrame()
        vertLine.setFrameShape(QFrame.VLine)
        vertLine.setFrameShadow(QFrame.Sunken)

        self.statusBar = QStatusBar(self)
        self.statusBar.showMessage("Stat")
        
        centralLayout.addWidget(self.centralWidget)
        centralLayout.addWidget(self.statusBar)

        mainLayout.addWidget(self.buttons)
        mainLayout.addWidget(vertLine)
        mainLayout.addLayout(centralLayout)
        self.setLayout(mainLayout)
        self.resize(800, 600)

        self.setWindowTitle("Job Tracker")
        self.setWindowIcon(QIcon.fromTheme("application-rtf"))
        self.startScreen()
        

    def startScreen(self):
        screen = startScreenForm()
        self.centralWidget.addWidget(screen)
        self.centralWidget.setCurrentWidget(screen)
   
       
    def newJob(self):
        def writeToFile():
            itemData = {}
            itemData['staff'] = jobForm.staffEdit.text()
            itemData['items'] = jobForm.itemEdit.text()
            if jobForm.psuButtonGroup.checkedId() == -2:
                custPsu = "Yes"
                itemData['psu'] = "Yes"
            elif jobForm.psuButtonGroup.checkedId() == -3:
                custPsu = "No"
                itemData['psu'] = "No"
            else:
                custPsu = "N/A"
                itemData['psu'] = "N/A"
            itemData['condition'] = jobForm.condition.text()
            itemData['problem'] = jobForm.problemEdit.toPlainText()
            if jobForm.passButtonGrp.checkedId() == -2:
                custPasswords =  "Yes"
                itemData['password'] = jobForm.passwords.toPlainText()
            else:
                custPasswords = "No"
                itemData['password'] = ""

            if jobForm.importantDataGrp.checkedId() == -2:
                custData = "Yes"
                itemData['data'] = jobForm.importantData.text()
            else:
                custData = "No"
                itemData['data'] = ""
                
            if jobForm.dataBackupGrp.checkedId() == -1:
                itemData['backup'] = "Yes"
            else:
                itemData['backup'] = "No"
            pickle.dump(itemData, open("Jobs/Incomplete/."+str(jobForm.jobNumber), "wb"))

        
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
                if (x == 8 and jobForm.importantDataGrp.checkedId() != -2) or (x == 6 and jobForm.passButtonGrp.checkedId() != -2):
                    print ("Passing")
                    x = x+1
                    jobForm.importantDataCheckVal.tick()
                    pass
                else:
                    i()
                    x = x+1
                if self.errorsDetected == True:
                    popup = QMessageBox.critical(self, "Error",
                            "Fix the marked errors in the form and try again", QMessageBox.Ok)
                    break
                elif self.errorsDetected == False and x == 10:
                    writeToFile()
                    self.personalDeets(jobForm.jobNumber)
        
        def jobNumberGenerator():
            jobNoFile = open('.jobNum', 'r+')
            self.jobNum = int(jobNoFile.read())
            newJobNum = self.jobNum + 1
            jobNoFile.seek(0)
            jobNoFile.truncate()
            jobNoFile.write(str(newJobNum))
            return self.jobNum

        self.buttons.newJobButton.setChecked(True)
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
            jobNo = searchWidget.searchField.text()
            if os.path.isfile("Jobs/Complete/."+str(jobNo)):
                jobStatus = "Complete"
            elif os.path.isfile("Jobs/Incomplete/."+str(jobNo)):
                jobStatus = "Incomplete"
            else:
                print("Error")
            if jobStatus != "":
                if nextFunction == 1:
                    self.editJobDetails(jobNo, jobStatus)
                elif nextFunction == 2:
                    self.addToJob(jobNo, jobStatus)
        searchWidget.searchBtn.clicked.connect(errorChecking)
    def editPersonalDeets(self, jobNum):
        def writeToFile():
            custData = {}
            custData['name'] = detailsForm.nameEdit.text()
            if self.emailPresent:
                custData['email'] = detailsForm.emailAddr.text()
            else:
                custData['email'] = ""
            if self.phonePresent:
                custData['phone'] = detailsForm.phoneNo.text()
            else:
                custData['phone'] = ""
            custData['mobile'] = detailsForm.mobileNo.text()
            custData['postcode'] = detailsForm.pcEdit.text()
            custData['addrone'] = detailsForm.addrLineOne.text()
            custData['addrtwo'] = detailsForm.addrLineTwo.text()
            
            self.statusBar.showMessage("Job Details Saved")
            pickle.dump(custData, open("Customers/."+str(jobNum), "wb"))               

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
            if detailsForm.pcEdit.text() == "": #Different for layout 
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
                i()
                x = x+1
                if self.errorsDetected == True:
                    popup = QMessageBox.critical(self, "Error",
                            "Fix the marked errors in the form and try again", QMessageBox.Ok)
                    break
                elif self.errorsDetected == False and x == 7:
                    writeToFile()
         
        detailsForm = custDetailForm(False)
        custData = pickle.load(open('Customers/.'+str(jobNum), 'rb'))
        detailsForm.nameEdit.setText(custData['name'])
        if custData['email'] != "":
            detailsForm.emailAddr.setText(custData['email'])
        if custData['phone'] != "":
            detailsForm.phoneNo.setText(custData['phone'])
        detailsForm.mobileNo.setText(custData['mobile'])
        detailsForm.pcEdit.setText(custData['postcode'])
        detailsForm.addrLineOne.setText(custData['addrone'])
        detailsForm.addrLineTwo.setText(custData['addrtwo'])
        detailsForm.nextButton.clicked.connect(errorChecking)
        detailsForm.addrLineOne.setReadOnly(False)
        detailsForm.addrLineTwo.setReadOnly(False)
        self.centralWidget.addWidget(detailsForm)
        self.centralWidget.setCurrentWidget(detailsForm)
         
    def editJobDetails(self, jobNo, jobStatus):
        def writeToFile():
            itemData = {}
            itemData['staff'] = jobForm.staffEdit.text()
            itemData['items'] = jobForm.itemEdit.text()
            if jobForm.psuButtonGroup.checkedId() == -2:
                custPsu = "Yes"
                itemData['psu'] = "Yes"
            elif jobForm.psuButtonGroup.checkedId() == -3:
                custPsu = "No"
                itemData['psu'] = "No"
            else:
                custPsu = "N/A"
                itemData['psu'] = "N/A"
            itemData['condition'] = jobForm.condition.text()
            itemData['problem'] = jobForm.problemEdit.toPlainText()
            if jobForm.passButtonGrp.checkedId() == -2:
                custPasswords =  "Yes"
                itemData['password'] = jobForm.passwords.toPlainText()
            else:
                custPasswords = "No"
                itemData['password'] = ""

            if jobForm.importantDataGrp.checkedId() == -2:
                custData = "Yes"
                itemData['data'] = jobForm.importantData.text()
            else:
                custData = "No"
                itemData['data'] = ""
                
            if jobForm.dataBackupGrp.checkedId() == -1:
                itemData['backup'] = "Yes"
            else:
                itemData['backup'] = "No"
            pickle.dump(itemData, open("Jobs/"+str(jobStatus)+"/."+str(jobNo), "wb"))
            
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
                    writeToFile()
                    self.editPersonalDeets(jobNo)

        self.buttons.editJobButton.setChecked(True)
        jobForm = jobDisplayWidget(int(jobNo))
        itemData = pickle.load(open('Jobs/'+str(jobStatus)+'/.'+str(jobNo), "rb"))

        #for line in itemData:
        #    itemData[line] = line.replace("\n","")
        if 'N/A' in itemData['psu']:
            jobForm.psuNA.setChecked(1)
        elif 'No' in itemData['psu']:
            jobForm.psuN.setChecked(1)
        else:
            jobForm.psuY.setChecked(1)

        if itemData['password'] == "":
            jobForm.passwordCheckNo.setChecked(1)
        else:
            jobForm.passwordCheckYes.setChecked(1)
            jobForm.passwords.setText(itemData['password'])
        if itemData['data'] == "":
            jobForm.importantDataCheckNo.setChecked(1)
        else:
            jobForm.importantDataCheckYes.setChecked(1)
            jobForm.importantData.setReadOnly(False)
            jobForm.importantData.setText(itemData['data'])
        if 'No' in itemData['backup']:
            jobForm.dataBackupCheckNo.setChecked(1)
        else:
            jobForm.dataBackupCheckYes.setChecked(1)
        jobForm.itemEdit.setText(itemData['items'])
        jobForm.staffEdit.setText(itemData['staff'])
        jobForm.itemEdit.setCursorPosition(0)
        jobForm.condition.setText(itemData['condition'])
        jobForm.problemEdit.setText(itemData['problem'])
        
        jobForm.importantDataChecked()

        self.centralWidget.addWidget(jobForm)
        self.centralWidget.setCurrentWidget(jobForm)
        jobForm.nextButton.clicked.connect(lambda: errorChecking())

        
    def jobDisplayErrorChecking(self, jobNo):
        jobForm = jobDisplayWidget(int(jobNo))
                 
    
    def addToJob(self, jobNo, jobStatus):
        self.jobPath = 'Jobs/'+str(jobStatus)+'/.'+str(jobNo)
        def writeToFile():
            #fileReadFrom = open("."+str(jobNo), "r")
            #oldFile = fileReadFrom.readlines()
            itemData = pickle.load(open(self.jobPath, 'rb'))
            try:
                for i in jobProgress.removals:
                    del itemData['item'+str(i-1)] #arrayu is 1 infront of items
                    del itemData['price'+str(i-1)]
            except AttributeError or KeyError: #Attr (no removal) key (add then del before save)
                pass
            x = 0
            for i in range(1,len(jobProgress.item)):
                itemIndex = 'item'+str(x)
                priceIndex = 'price'+str(x)
                try:
                    itemData[itemIndex] = jobProgress.item[i].text()
                    itemData[priceIndex] = jobProgress.price[i].text()
                except KeyError:
                    pass
                x += 1 
            itemData['jobnotes'] = jobProgress.jobNotesEdit.toPlainText()
            pickle.dump(itemData, open(self.jobPath, "wb"))
        def completeJob():
            if jobProgress.completeBox.isChecked():
                jobFile = pickle.load(open('Jobs/Incomplete/.'+str(jobNo), 'rb'))
                os.remove('Jobs/Incomplete/.'+str(jobNo))
                pickle.dump(itemData, open('Jobs/Complete/.'+str(jobNo), 'wb'))
                self.jobPath = 'Jobs/Complete/.'+str(jobNo)
            else:
                jobFile = pickle.load(open('Jobs/Complete/.'+str(jobNo), 'rb'))
                os.remove('Jobs/Complete/.'+str(jobNo))
                pickle.dump(itemData, open('Jobs/Incomplete/.'+str(jobNo), 'wb'))
                self.jobPath = 'Jobs/Incomplete/.'+str(jobNo)

        self.buttons.addToJobButton.setChecked(True)
        jobProgress = jobProgressWidget(jobNo)
        itemData = pickle.load(open(self.jobPath, 'rb'))
        itemCount = 0
        for i in itemData:
            if 'price' in i: #iteratge price, item is taken
                i=i[5:] #remove price
                jobProgress.addItems(itemData['item'+str(i)], itemData['price'+str(i)])
        try:
            jobProgress.jobNotesEdit.setText(itemData['jobnotes'])
        except KeyError:
            pass
        jobProgress.saveButton.clicked.connect(writeToFile)
        if jobStatus == "Complete":
            jobProgress.completeBox.setChecked(True)
        jobProgress.completeBox.stateChanged.connect(completeJob)

        self.centralWidget.addWidget(jobProgress)
        self.centralWidget.setCurrentWidget(jobProgress)
    
    def personalDeets(self, jobNum):
        def writeToFile():
            custData = {}
            custData['name'] = detailsForm.nameEdit.text()
            if self.emailPresent:
                custData['email'] = detailsForm.emailAddr.text()
            else:
                custData['email'] = ""
            if self.phonePresent:
                custData['phone'] = detailsForm.phoneNo.text()
            else:
                custData['phone'] = ""
            custData['mobile'] = detailsForm.mobileNo.text()
            custData['postcode'] = detailsForm.pcLineEdit.text()
            custData['addrone'] = detailsForm.addrLineOne.text()
            custData['addrtwo'] = detailsForm.addrLineTwo.text()
            
            self.statusBar.showMessage("Job Details Saved")
            pickle.dump(custData, open("Customers/."+str(jobNum), "wb"))               
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
                i()
                x = x+1
                if self.errorsDetected == True:
                    self.statusBar.showMessage("Fix Errors")
                    break
                elif self.errorsDetected == False and x == 7:
                    print("SAVED")
                    writeToFile()
                    #self.goHome()
                    detailsForm.nextButton.setText("Saved")
                    detailsForm.nextButton.setEnabled(False)
                    
        detailsForm = custDetailForm(True)
        detailsForm.nextButton.clicked.connect(errorChecking)
        self.centralWidget.addWidget(detailsForm)
        self.centralWidget.setCurrentWidget(detailsForm)
    
    
    def jobs(self):
        jobWidget = jobsWidget()
        self.centralWidget.addWidget(jobWidget)
        self.centralWidget.setCurrentWidget(jobWidget)
        
        for i in range(0, jobWidget.rowCount):
            editButton = QToolButton(self)
            editButton.setIcon(QIcon.fromTheme("edit-find-replace"))
            editButton.setIconSize(QSize(32, 32))
            addToButton = QToolButton(self)
            addToButton.setIcon(QIcon.fromTheme("story-editor"))
            addToButton.setIconSize(QSize(32, 32))
            
            jobNo = str(jobWidget.jobTable.item(i, 0).text())
            jobStatus = str(jobWidget.jobTable.item(i, 3).text())
            editButton.clicked.connect(lambda sacrafice="", z=jobNo, y=jobStatus: self.editJobDetails(z,y))
            addToButton.clicked.connect(lambda sacrafice="", z=jobNo, y=jobStatus: self.addToJob(z,y))

            #actionWidget = QWidget()
            #actionLayout = QHBoxLayout()
            #actionLayout.addWidget(editButton)
            #actionLayout.addWidget(addToButton)
            #actionWidget.setLayout(actionLayout)
            jobWidget.jobTable.setCellWidget(i, 4, editButton)
            jobWidget.jobTable.setCellWidget(i, 5, addToButton)

    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = mainInterface()

    ex.show()
    sys.exit(app.exec_())
