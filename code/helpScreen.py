from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QTextEdit, QPushButton, QLineEdit, QLabel, QToolButton, QAction, QToolBar, QActionGroup
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, Qt

class helpScreenForm(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        #titleLabel = QLabel('<font size= "5">Job Tracking System')
        
        layout = QVBoxLayout()
        
        
        self.homeButton = QAction(self)
        self.homeButton.setEnabled(False)
        self.homeButton.setText("A list of the existing jobs. From here, you can View/Edit the  job details or add details to the job")
        self.homeButton.setIcon(QIcon.fromTheme("arrow-left"))

        self.newJobButton = QAction(self)
        self.newJobButton.setText("Use this form to create a new job")
        self.newJobButton.setIcon(QIcon.fromTheme("arrow-left"))
        self.newJobButton.setCheckable(False)

        self.editJobButton = QAction(self)
        self.editJobButton.setText("Use this form to manually View/Edit a job's details, specifying the job number")
        self.editJobButton.setIcon(QIcon.fromTheme("arrow-left"))
        self.editJobButton.setCheckable(False)

        self.addToJobButton = QAction(self)
        self.addToJobButton.setText("This function is used to add details to a jobm either in general note form, or by logging the work done/parts used as well as their prices")
        self.addToJobButton.setIcon(QIcon.fromTheme("arrow-left"))
        self.addToJobButton.setCheckable(False)

        self.callLogButton = QAction(self)
        self.callLogButton.setText("This function gives you an overview of what each job function does")
        self.callLogButton.setIcon(QIcon.fromTheme("arrow-left"))
        self.callLogButton.setCheckable(False)
        
        actionLayout = QVBoxLayout()
        actionLayout.addWidget(self.homeButton)
        actionLayout.addWidget(self.newJobButton)
        self.toolBar = QToolBar()
        self.toolBar.setMovable(False)
        self.toolBar.setIconSize(QSize(64, 64))
        self.toolBar.setToolButtonStyle(3)
        self.toolBar.setOrientation(0x2)
        self.toolBar.addAction(self.editJobButton)
        self.toolBar.addAction(self.addToJobButton)
        self.toolBar.addAction(self.callLogButton)
        
        bGroup = QActionGroup(self)
        bGroup.addAction(self.homeButton)
        bGroup.addAction(self.newJobButton)
        bGroup.addAction(self.editJobButton)
        bGroup.addAction(self.addToJobButton)
        bGroup.addAction(self.callLogButton)

        #layout.addWidget(titleLabel)
        layout.addLayout(actionLayout)
        layout.addWidget(self.toolBar)
        layout.setAlignment(Qt.AlignVCenter)
        self.setLayout(layout)

