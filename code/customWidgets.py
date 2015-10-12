from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel
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
