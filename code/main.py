import sys
import os
import sip
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from findJob import findJobWidget
from jobForm import newJobForm
from buttons import buttonsWidget
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
        #global progressWidget
        #progressWidget = customProgressWidget()
        #self.titleLayout.addWidget(progressWidget)
        jobForm = newJobForm(self)
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
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = mainInterface()
    ex.show()
    sys.exit(app.exec_())
    
