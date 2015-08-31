#   ----    TODO    ----    #
#    - FIX DAT FADE BRO     #
#    - user details/client  #
#    - slim down imports    #
#    - run on Mac           #
#    - run on Windows       #
#    - make standalone      #
#    - fix vim              #
#    - comment code         #
#    - add invoicing        #
#    -                      #    
#    -                      #
#   --------------------    #








import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimeLine
from PyQt5.QtGui import *







class mainInterface(QWidget):
    def __init__(self):
        super().__init__()
        tabw = QTabWidget()
        
        newJobTab = QWidget()
        findJobTab = QWidget()
        
        title = QLabel("Use the tabs to choose a task to perform. Hover over each tab for extra information")

        tabw.addTab(newJobTab, "New Job")
        tabw.addTab(findJobTab, "Find/Edit a Job")
        tabw.setTabToolTip(0, "Add a new Job")
        tabw.setTabToolTip(1, "Find and Edit an Exisiting Job")
        
        self.newJobLayout = QFormLayout()
        self.findJobLayout = QGridLayout(findJobTab)
        self.splitJobLayout = QHBoxLayout(newJobTab)
        #   TIGHT FADE BRO
        self.newJob()
        self.findJob()
        
#        tabw.tabBarClicked.connect(tabw.setCurrentIndex(index))
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(title)
        mainLayout.addWidget(tabw)
        self.setLayout(mainLayout)
        self.setGeometry(300, 300, 305, 305)
        self.setWindowTitle("File Dialog")
        self.show()




        #   New Job
       
    def newJob(self):
      #  def dataClicked():
      #      checkBoxState = importantDataCheckYes.checkState()
      #      importantData = QLabel('Important Data:')
      #      importantDataDocs = QCheckBox('Documents', self)
      #      importantDataPhoto = QCheckBox('Photos', self)
      #      importantDataOther = QCheckBox('Other', self)
      #      def otherClicked():
      #          otherCheckState = importantDataOther.checkState()
      #          importantDataEdit = QLineEdit(self)
      #          if otherCheckState == 2:
      #              self.newJobLayout.addWidget(importantDataEdit, 8, 1, 8, 3)
      #          elif otherCheckState == 0:
      #              otherItem = self.newJobLayout.itemAtPosition(9, 1)
      #              
      #              otherItem.widget().deleteLater()
      #              self.newJobLayout.removeItem(otherItem)
#
#            if checkBoxState == 2:
#            #    self.newJobLayout.addWidget(importantData, 8, 0)
#            #    self.newJobLayout.addWidget(importantDataDocs, 8, 1)
#            #    self.newJobLayout.addWidget(importantDataPhoto, 8, 2)
#            #    self.newJobLayout.addWidget(importantDataOther, 8, 3)
#                
#            #    importantDataLocationsGrp = QButtonGroup(self)
#            #    importantDataLocationsGrp.addButton(importantDataDocs)
#            #    importantDataLocationsGrp.addButton(importantDataPhoto)
#            #    importantDataLocationsGrp.addButton(importantDataOther)
#             
#                importantDataLocationsGrp.buttonClicked.connect(otherClicked)
#            elif checkBoxState == 0:
#                dataItem = self.newJobLayout.itemAtPosition(8, 0)
          #      docsDataItem = self.newJobLayout.itemAtPosition(8, 1)
          #      photoDataItem = self.newJobLayout.itemAtPosition(8, 2)
          #      otherDataItem = self.newJobLayout.itemAtPosition(8, 3)
#
#
#                dataItem.widget().deleteLater()
#                docsDataItem.widget().deleteLater()
#                photoDataItem.widget().deleteLater()
#                otherDataItem.widget().deleteLater()
#
#                self.newJobLayout.removeItem(dataItem)
#                self.newJobLayout.removeItem(docsDataItem)
#                self.newJobLayout.removeItem(photoDataItem)
#                self.newJobLayout.removeItem(otherDataItem)
#       
        
        leftPanel = QFrame(self)
        rightPanel = QFrame(self)
        
        # Widgets Defined
        jobTitle = QLabel("<u>Job Details</u>")
        itemLabel = QLabel('Items:')
        itemEdit = QLineEdit(self)
        
        psuLabel = QLabel('Power Supply?') 
        psuButtonGroup = QButtonGroup(self)
        psuBox = QHBoxLayout(self)
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
        importantDataBox = QHBoxLayout(self)
        importantDataBox.addWidget(importantDataCheckYes)
        importantDataBox.addWidget(importantDataCheckNo)


        dataBackupLabel = QLabel('Data backed up?')
        dataBackupCheckYes = QCheckBox('Yes', self)
        dataBackupCheckNo = QCheckBox('Yes', self)
        dataBackupBox = QHBoxLayout(self)
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
        psuButtonGroup.addButton(psuY)
        psuButtonGroup.addButton(psuN)
        psuButtonGroup.addButton(psuNA)
        # if psuButtonGroup.checkedButton == 0, none clicked
        
        
        # Layout set up
        self.newJobLayout.setSpacing(10)
        
        #self.newJobLayout.addWidget(jobTitle, 1, 1)
        self.newJobLayout.addRow(itemLabel, itemEdit)
        self.newJobLayout.addRow(psuLabel, psuBox)
        self.newJobLayout.addRow(problemLabel, problemEdit)
        self.newJobLayout.addRow(importantDataLabel, importantDataBox)
        self.newJobLayout.addRow(dataBackupLabel, dataBackupBox)

        leftPanel.setLayout(self.newJobLayout)
        self.splitJobLayout.addWidget(leftPanel)
        
        
    
    def findJob(self):
        #   Find Job
        findJobTitle = QLabel('Enter Job Number')
        findJobEdit = QLineEdit(self)

        self.findJobLayout.setSpacing(10)
        self.findJobLayout.addWidget(findJobTitle, 1, 0)
        self.findJobLayout.addWidget(findJobEdit, 1, 1)

        
        
if __name__ == '__main__':
    app  = QApplication(sys.argv)
    ex = mainInterface()
    sys.exit(app.exec_())
