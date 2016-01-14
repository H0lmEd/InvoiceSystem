from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QTextEdit, QPushButton, QLineEdit, QLabel, QToolButton, QAction, QToolBar, QActionGroup
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, Qt

class helpScreenForm(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        titleLabel = QLabel('<font size= "5">Job Tracking Syste978234m')
        
        layout = QVBoxLayout()
        
        self.homeButton = QAction(self)
        self.homeButton.setText("View/Edit Existing Jobs")
        self.homeButton.setIcon(QIcon.fromTheme("arrow-left"))

        self.newJobButton = QAction(self)
        self.newJobButton.setText("Create a new Job")
        self.newJobButton.setIcon(QIcon.fromTheme("arrow-left"))
        self.newJobButton.setCheckable(False)

        self.editJobButton = QAction(self)
        self.editJobButton.setText("View/Edit a Job")
        self.editJobButton.setIcon(QIcon.fromTheme("arrow-left"))
        self.editJobButton.setCheckable(False)

        self.addToJobButton = QAction(self)
        self.addToJobButton.setText("Add Job Progress")
        self.addToJobButton.setIcon(QIcon.fromTheme("arrow-left"))
        self.addToJobButton.setCheckable(False)

        self.callLogButton = QAction(self)
        self.callLogButton.setText("Help Screen")
        self.callLogButton.setIcon(QIcon.fromTheme("arrow-left"))
        self.callLogButton.setCheckable(False)
        
        self.toolBar = QToolBar()
        self.toolBar.setMovable(False)
        self.toolBar.setIconSize(QSize(64, 64))
        self.toolBar.setToolButtonStyle(3)
        self.toolBar.setOrientation(0x2)
        #addToolBar(toolBar)
        self.toolBar.addAction(self.homeButton)
        self.toolBar.addAction(self.newJobButton)
        self.toolBar.addAction(self.editJobButton)
        self.toolBar.addAction(self.addToJobButton)
        self.toolBar.addAction(self.callLogButton)
        
        bGroup = QActionGroup(self)
        bGroup.addAction(self.homeButton)
        bGroup.addAction(self.newJobButton)
        bGroup.addAction(self.editJobButton)
        bGroup.addAction(self.addToJobButton)
        bGroup.addAction(self.callLogButton)

        layout.addWidget(titleLabel)
        layout.addWidget(self.toolBar)
        layout.setAlignment(Qt.AlignVCenter)
        self.setLayout(layout)

