from PyQt5.QtWidgets import QWidget, QHBoxLayout, QToolButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
import os


class buttonsWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        iconFolder = os.path.join(os.path.dirname(__file__), os.pardir, "icons/")

        layout = QHBoxLayout()
        self.newJobButton = QToolButton(self)
        self.newJobButton.setToolButtonStyle(3) #text below icon
        self.newJobButton.setText("New Job")
        self.newJobButton.setIcon(QIcon(iconFolder+'new.png'))
        
        self.newJobButton.setIconSize(QSize(64, 64))
        print("PAth", iconFolder)

        self.editJobButton = QToolButton(self)
        self.editJobButton.setToolButtonStyle(3) #text below icon
        self.editJobButton.setText("View/Edit a Job")
        self.editJobButton.setIcon(QIcon(iconFolder+'find.png'))
        self.editJobButton.setIconSize(QSize(64, 64))

        self.addToJobButton = QToolButton(self)
        self.addToJobButton.setToolButtonStyle(3)
        self.addToJobButton.setText("Add Job Progress")
        self.addToJobButton.setIcon(QIcon(iconFolder+'find.png'))
        self.addToJobButton.setIconSize(QSize(64, 64))

        layout.addWidget(self.newJobButton)
        layout.addWidget(self.editJobButton)
        layout.addWidget(self.addToJobButton)
        self.setLayout(layout)
