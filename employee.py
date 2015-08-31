import sys
from PyQt5.QtWidgets import (QWidget, QDesktopWidget, QLabel, QLineEdit, QTextEdit, QVBoxLayout, QHBoxLayout, QApplication, QPushButton, QStackedWidget, QGridLayout)
from PyQt5.QtGui import *



class mainPage(QWidget):
    def __init__(self):
        super().__init__()
        title = QLabel('Choose a task to perform')
        newJobButton = QPushButton('New Job', self)
        findJobButton = QPushButton('Find Job', self)
        invoiceButton = QPushButton('Create Invoice', self)
        hbox1 = QHBoxLayout()
        hbox1.addWidget(title)
        hbox2 = QHBoxLayout()
        hbox2.addWidget(newJobButton)
        hbox2.addWidget(findJobButton)
        hbox3 = QHBoxLayout()
        hbox3.addWidget(invoiceButton)
       


        stack = StackedWidget()

        newJobButton.clicked.connect(StackedWidget.setNewJob)
        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)


        self.setLayout(vbox)


class jobPage(QWidget):
    def __init__(self):
        super().__init__()
        title = QLabel("Items")
        titleText = QLineEdit(self)
        
        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(title, 1, 0)
        grid.addWidget(titleText, 1, 1)
class StackedWidget(QStackedWidget):
    def __init__(self, parent = None):
        QStackedWidget.__init__(self, parent)

    def setCurrentIndex(self, index):
        QStackedWidget.setCurrentIndex(self, index)

    def newJobPage(self):
        pass
    def setNewJob(self):
        print("hello")
        StackedWidget.setCurrentIndex(self, 1)
        print("bo")
    
    def setPage2(self):
        self.setCurrentIndex(1)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()
    stack = StackedWidget()
    stack.addWidget(mainPage())
    stack.addWidget(jobPage())
    btn = QPushButton("Next")
    btn.clicked.connect(stack.setNewJob)
    layout = QGridLayout(window)
    layout.addWidget(stack, 0, 0, 1, 2)
    layout.addWidget(btn, 1, 2)
    
    window.show()

    sys.exit(app.exec_())

    
