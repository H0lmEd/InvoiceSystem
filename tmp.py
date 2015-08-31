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


class jobPage(QWidget):
    def __init__(self):
        super().__init__()
        title = QLabel("Item")
        titleText = QLineEdit(self)

        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(title, 1, 0)
        grid.addWidget(titleText, 1, 1)

        self.setLayout(grid)
class StackedWidget(QStackedWidget):

    def __init__(self, parent = None):
        QStackedWidget.__init__(self, parent)
    
    def setCurrentIndex(self, index):
        self.fader_widget = FaderWidget(self.currentWidget(), 
self.widget(index))
        QStackedWidget.setCurrentIndex(self, index)
 
    def setPage1(self):
        print("hello")
        self.setCurrentIndex(0)
    
    def setPage2(self):
        print("Hello")
        self.setCurrentIndex(1)

class mainPage(QWidget):
    def __init__(self):
        super().__init__()
        title = QLabel("Choose a task to perform")
        newJobButton = QPushButton("New Job", self)
        findJobButton = QPushButton("Find job", self)
        invoiceButton = QPushButton("Create Invoice", self)
        hbox1 = QHBoxLayout()
        hbox1.addWidget(title)
        hbox2 = QHBoxLayout()
        hbox2.addWidget(newJobButton)
        hbox2.addWidget(findJobButton)
        hbox3 = QHBoxLayout()
        hbox3.addWidget(invoiceButton)

        stack = StackedWidget()
        
        newJobButton.clicked.connect(stack.setPage1)
        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)


        self. setLayout(vbox)
        
if __name__ == "__main__":

    app = QApplication(sys.argv)
    
    window = QWidget()
    
    stack = StackedWidget()
    stack.addWidget(mainPage())
    stack.addWidget(jobPage())
    
    page1Button = QPushButton("Page 1")
    page2Button = QPushButton("Page 2")
    page1Button.clicked.connect(stack.setPage1)
    page2Button.clicked.connect(stack.setPage2)
    
    layout = QGridLayout(window)
    layout.addWidget(stack, 0, 0, 1, 2)
    layout.addWidget(page1Button, 1, 0)
    layout.addWidget(page2Button, 1, 1)
    
    window.show()
    
    sys.exit(app.exec_())
