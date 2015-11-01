from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QTableWidget
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QSize, Qt
import os

class validationImage(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.iconFolder = os.path.join(os.path.dirname(__file__), os.pardir, "icons/")

        self.layout = QVBoxLayout()

        self.label = QLabel(self)
    def tick(self):
        pixmap = QPixmap(self.iconFolder+"correct.png")
        self.label.setPixmap(pixmap)
        
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)
    def error(self):
        pixmap = QPixmap(self.iconFolder+"error.png")
        self.label.setPixmap(pixmap)
        
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)

class customTableWidget(QTableWidget):
    def __init__(self):
        QTableWidget.__init__(self)

    def keyPressEvent(QKeyEvent, event):
        print(event.key())
        if event.key() == 16777220:
            print("ENTER PRESSED")
            super().insertRow(1)
            super().setCurrentCell((super().currentRow()+1), 0)
            #jobProgressWidget.rowNumber = jobProgressWidget.rowNumber+1
            #jobProgressWidget.cellWatcher


