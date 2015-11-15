from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QTableWidget
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QSize, Qt, pyqtSignal
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
        entered = pyqtSignal()
    
    def keyPressEvent(self, event):
        print(event.key())
        if event.key() == 16777220:
            print("ENTER PRESSED")
            newRow = int(super().currentRow()) + 1
            super().insertRow(newRow)
            super().setCurrentCell((super().currentRow()+1), 0)
            print('Signal soon to be Emitted')
            #super.entered = pyqtSignal()
            self.entered.emit()
            #jobProgressWidget.rowNumber = jobProgressWidget.rowNumber+1
            #jobProgressWidget.cellWatcher


