from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import os


class buttonsWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__()

        layout = QVBoxLayout()

        self.newJobButton = QAction(self)
        self.newJobButton.setText("New Job")
        self.newJobButton.setIcon(QIcon.fromTheme("document-new"))
        self.newJobButton.setCheckable(True)

        self.editJobButton = QAction(self)
        self.editJobButton.setText("View/Edit a Job")
        self.editJobButton.setIcon(QIcon.fromTheme("edit-find-replace"))
        self.editJobButton.setCheckable(True)

        self.addToJobButton = QAction(self)
        self.addToJobButton.setText("Add Job Progress")
        self.addToJobButton.setIcon(QIcon.fromTheme("story-editor"))
        self.addToJobButton.setCheckable(True)

        self.jobsButton = QAction(self)
        self.jobsButton.setText("Existing Jobs")
        self.jobsButton.setIcon(QIcon.fromTheme("project-open")) #view-process-all
        self.jobsButton.setCheckable(True)
 
 
        self.toolBar = QToolBar()
        self.toolBar.setMovable(False)
        self.toolBar.setIconSize(QSize(64, 64))
        self.toolBar.setToolButtonStyle(3)
        self.toolBar.setOrientation(0x2)
        self.toolBar.addAction(self.jobsButton)
        self.toolBar.addAction(self.newJobButton)
        self.toolBar.addAction(self.editJobButton)
        self.toolBar.addAction(self.addToJobButton)
        
        bGroup = QActionGroup(self)
        bGroup.addAction(self.newJobButton)
        bGroup.addAction(self.editJobButton)
        bGroup.addAction(self.addToJobButton)
        bGroup.addAction(self.jobsButton)
        layout.addWidget(self.toolBar)
        layout.setAlignment(Qt.AlignVCenter)
        self.setLayout(layout)
