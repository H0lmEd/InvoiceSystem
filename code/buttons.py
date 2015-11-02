from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QToolButton, QSizePolicy, QActionGroup, QAction, QToolBar
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

        self.newJobButton = QAction(self)
        self.newJobButton.setText("New Job")
        self.newJobButton.setIcon(QIcon(iconFolder+'new.png'))
        self.newJobButton.setCheckable(True)
        print("PAth", iconFolder)

        self.editJobButton = QAction(self)
        self.editJobButton.setText("View/Edit a Job")
        self.editJobButton.setIcon(QIcon(iconFolder+'find.png'))
        self.editJobButton.setCheckable(True)

        self.addToJobButton = QAction(self)
        self.addToJobButton.setText("Add Job Progress")
        self.addToJobButton.setIcon(QIcon(iconFolder+'find.png'))
        self.addToJobButton.setCheckable(True)

        self.callLogButton = QAction(self)
        self.callLogButton.setText("Create Invoice")
        self.callLogButton.setIcon(QIcon(iconFolder+'find.png'))
        self.callLogButton.setCheckable(True)
        
        self.toolBar = QToolBar()
        self.toolBar.setMovable(False)
        self.toolBar.setIconSize(QSize(64, 64))
        self.toolBar.setToolButtonStyle(3)
        self.toolBar.setOrientation(0x2)
        #addToolBar(toolBar)
        self.toolBar.addAction(self.newJobButton)
        self.toolBar.addAction(self.editJobButton)
        self.toolBar.addAction(self.addToJobButton)
        self.toolBar.addAction(self.callLogButton)
        
        bGroup = QActionGroup(self)
        bGroup.addAction(self.newJobButton)
        bGroup.addAction(self.editJobButton)
        bGroup.addAction(self.addToJobButton)
        bGroup.addAction(self.callLogButton)
        vLayout.addWidget(self.toolBar)

        self.setLayout(vLayout)
