from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QToolButton, QSizePolicy
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, Qt
import os


class buttonsWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        iconFolder = os.path.join(os.path.dirname(__file__), os.pardir, "icons/")

        topLayout = QHBoxLayout()
        botLayout = QHBoxLayout()
        vLayout = QVBoxLayout()

        self.newJobButton = QToolButton(self)
        self.newJobButton.setToolButtonStyle(3) #text below icon
        self.newJobButton.setText("New Job")
        self.newJobButton.setIcon(QIcon(iconFolder+'new.png'))
        self.newJobButton.setAutoRaise(True)
        self.newJobButton.setIconSize(QSize(64, 64))
        print("PAth", iconFolder)

        self.editJobButton = QToolButton(self)
        self.editJobButton.setToolButtonStyle(3) #text below icon
        self.editJobButton.setText("View/Edit a Job")
        self.editJobButton.setIcon(QIcon(iconFolder+'find.png'))
        self.editJobButton.setAutoRaise(True)
        self.editJobButton.setIconSize(QSize(64, 64))

        self.addToJobButton = QToolButton(self)
        self.addToJobButton.setToolButtonStyle(3)
        self.addToJobButton.setAutoRaise(True)
        self.addToJobButton.setText("Add Job Progress")
        self.addToJobButton.setIcon(QIcon(iconFolder+'find.png'))
        self.addToJobButton.setIconSize(QSize(64, 64))

        self.callLogButton = QToolButton(self)
        self.callLogButton.setToolButtonStyle(3)
        self.callLogButton.setAutoRaise(True)
        self.callLogButton.setText("Create Invoice")
        self.callLogButton.setIcon(QIcon(iconFolder+'find.png'))
        self.callLogButton.setIconSize(QSize(64, 64))

        topLayout.addWidget(self.newJobButton)
        topLayout.addWidget(self.editJobButton)
        botLayout.addWidget(self.addToJobButton)
        botLayout.addWidget(self.callLogButton)

        vLayout.addLayout(topLayout)
        vLayout.addLayout(botLayout)
        self.setLayout(vLayout)
