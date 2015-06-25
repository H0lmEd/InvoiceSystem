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


class FaderWidget(QWidget):

    def __init__(self, old_widget, new_widget):
    
        QWidget.__init__(self, new_widget)
        
        self.old_pixmap = QPixmap(new_widget.size())
        old_widget.render(self.old_pixmap)
        self.pixmap_opacity = 1.0
        
        self.timeline = QTimeLine()
        self.timeline.valueChanged.connect(self.animate)
        self.timeline.finished.connect(self.close)
        self.timeline.setDuration(333)
        self.timeline.start()
        
        self.resize(new_widget.size())
        self.show()
    
    def paintEvent(self, event):
    
        painter = QPainter()
        painter.begin(self)
        painter.setOpacity(self.pixmap_opacity)
        painter.drawPixmap(0, 0, self.old_pixmap)
        painter.end()
    
    def animate(self, value):
    
        self.pixmap_opacity = 1.0 - value
        self.repaint()


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
        
        self.newJobLayout = QGridLayout()
        self.pDetailsLayout = QGridLayout()
        self.findJobLayout = QGridLayout(findJobTab)
        self.splitJobLayout = QVBoxLayout(newJobTab)
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
        def dataClicked():
            checkBoxState = importantDataCheckYes.checkState()
            importantData = QLabel('Important Data:')
            importantDataDocs = QCheckBox('Documents', self)
            importantDataPhoto = QCheckBox('Photos', self)
            importantDataOther = QCheckBox('Other', self)
            def otherClicked():
                otherCheckState = importantDataOther.checkState()
                importantDataEdit = QLineEdit(self)
                if otherCheckState == 2:
                    self.newJobLayout.addWidget(importantDataEdit, 8, 1, 8, 3)
                elif otherCheckState == 0:
                    otherItem = self.newJobLayout.itemAtPosition(9, 1)
                    
                    otherItem.widget().deleteLater()
                    self.newJobLayout.removeItem(otherItem)

            if checkBoxState == 2:
                self.newJobLayout.addWidget(importantData, 8, 0)
                self.newJobLayout.addWidget(importantDataDocs, 8, 1)
                self.newJobLayout.addWidget(importantDataPhoto, 8, 2)
                self.newJobLayout.addWidget(importantDataOther, 8, 3)
                
                importantDataLocationsGrp = QButtonGroup(self)
                importantDataLocationsGrp.addButton(importantDataDocs)
                importantDataLocationsGrp.addButton(importantDataPhoto)
                importantDataLocationsGrp.addButton(importantDataOther)
             
                importantDataLocationsGrp.buttonClicked.connect(otherClicked)
            elif checkBoxState == 0:
                dataItem = self.newJobLayout.itemAtPosition(8, 0)
                docsDataItem = self.newJobLayout.itemAtPosition(8, 1)
                photoDataItem = self.newJobLayout.itemAtPosition(8, 2)
                otherDataItem = self.newJobLayout.itemAtPosition(8, 3)


                dataItem.widget().deleteLater()
                docsDataItem.widget().deleteLater()
                photoDataItem.widget().deleteLater()
                otherDataItem.widget().deleteLater()

                self.newJobLayout.removeItem(dataItem)
                self.newJobLayout.removeItem(docsDataItem)
                self.newJobLayout.removeItem(photoDataItem)
                self.newJobLayout.removeItem(otherDataItem)
       
        
        leftPanel = QFrame(self)
        rightPanel = QFrame(self)
        
        # Widgets Defined
        jobTitle = QLabel("<u>Job Details</u>")
        itemLabel = QLabel('Items:')
        itemEdit = QLineEdit(self)
        
        psuLabel = QLabel('Power Supply?') 
        psuButtonGroup = QButtonGroup(self)
        psuY = QCheckBox('Yes', self)
        psuN = QCheckBox('No', self)
        psuNA = QCheckBox('N/A', self)
        
        problemLabel = QLabel('Job Description:')
        problemEdit = QTextEdit(self)
        
        importantDataLabel = QLabel('Any important data on the system?')
        importantDataCheckYes = QCheckBox('Yes', self)
        importantDataCheckNo = QCheckBox('No', self)

        dataBackupLabel = QLabel('Data backed up?')
        dataBackupCheckYes = QCheckBox('Yes', self)
        dataBackupCheckNo = QCheckBox('Yes', self)


        # Back up check boxes set up
        dataBackupGrp = QButtonGroup(self)
        dataBackupGrp.addButton(dataBackupCheckYes)
        dataBackupGrp.addButton(dataBackupCheckNo)

        # Important Data check Boxes Set Up
        importantDataGrp = QButtonGroup(self)
        importantDataGrp.addButton(importantDataCheckYes)
        importantDataGrp.addButton(importantDataCheckNo)

        importantDataGrp.buttonClicked.connect(dataClicked)
        
        # PSU check Boxes set up
        psuButtonGroup.addButton(psuY)
        psuButtonGroup.addButton(psuN)
        psuButtonGroup.addButton(psuNA)
        # if psuButtonGroup.checkedButton == 0, none clicked
        
        
        # Layout set up
        self.newJobLayout.setSpacing(10)
        
        self.newJobLayout.addWidget(jobTitle, 1, 1)
        self.newJobLayout.addWidget(itemLabel, 2, 0)
        self.newJobLayout.addWidget(itemEdit, 2, 1, 2, 3)
        self.newJobLayout.addWidget(psuLabel, 3, 0)
        self.newJobLayout.addWidget(psuY, 3, 1)
        self.newJobLayout.addWidget(psuN, 3, 2)
        self.newJobLayout.addWidget(psuNA, 3, 3)
        self.newJobLayout.addWidget(problemLabel, 4, 0)
        self.newJobLayout.addWidget(problemEdit, 4, 1, 4, 3) # is 2 lines deep test to find best size
        self.newJobLayout.addWidget(importantDataLabel, 7, 0)
        self.newJobLayout.addWidget(importantDataCheckYes, 7, 1)
        self.newJobLayout.addWidget(importantDataCheckNo, 7, 2)
        self.newJobLayout.addWidget(dataBackupLabel, 16, 0)
        self.newJobLayout.addWidget(dataBackupCheckYes, 16, 1)
        self.newJobLayout.addWidget(dataBackupCheckNo, 16, 2)

        leftPanel.setLayout(self.newJobLayout)

        self.splitJobLayout.addWidget(leftPanel)
        
        

        detailsTitle = QLabel("<b><u>Customer's Personal Details</u></b>")



        self.pDetailsLayout.addWidget(detailsTitle)
        self.splitJobLayout.addWidget(rightPanel)


    
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
