from PyQt5.QtWidgets import QWidget, QHBoxLayout, QToolButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize

class buttonsWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        layout = QHBoxLayout()
        self.newJobButton = QToolButton(self)
        self.newJobButton.setToolButtonStyle(3) #text below icon
        self.newJobButton.setText("New Job")
        self.newJobButton.setIcon(QIcon(':/icons/new.png'))
        self.newJobButton.setIconSize(QSize(64, 64))


        self.findJobButton = QToolButton(self)
        self.findJobButton.setToolButtonStyle(3) #text below icon
        self.findJobButton.setText("Find a Job")
        self.findJobButton.setIcon(QIcon('find.png'))
        self.findJobButton.setIconSize(QSize(64, 64))

        layout.addWidget(self.newJobButton)
        layout.addWidget(self.findJobButton)
        self.setLayout(layout)
