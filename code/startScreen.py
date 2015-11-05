from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QTextEdit, QPushButton, QLineEdit, QLabel, QToolButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, Qt

class startScreenForm(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        titleLabel = QLabel('JOB TRACKING SYSTEM')
        newJob = QToolButton(self)
        newJob.setToolButtonStyle(2)
        newJob.setText('create newJob')
        #newJob.setPixmap(QPixmap('arrow.jpg'))
        newJob.setIcon(QIcon.fromTheme("arrow-left"))
        newJob.setIconSize(QSize(64, 64))
        newJobLayout = QHBoxLayout()
        newJobLayout.addWidget(newJob)
        newJobLayout.addStretch(1)

        editJob = QToolButton(self)
        editJob.setToolButtonStyle(2)
        editJob.setText('Use this function to view or edit a job')
        editJob.setIcon(QIcon.fromTheme("arrow-left"))
        editJob.setIconSize(QSize(64, 64))
        editJobLayout = QHBoxLayout()
        editJobLayout.addWidget(editJob)
        editJobLayout.addStretch(1)

        addToJob = QToolButton(self)
        addToJob.setToolButtonStyle(2)
        addToJob.setText('Use this function to add progress to jobs')
        addToJob.setIcon(QIcon.fromTheme('arrow-left'))
        addToJob.setIconSize(QSize(64, 64))
        addToJobLayout = QHBoxLayout()
        addToJobLayout.addWidget(addToJob)
        addToJobLayout.addStretch(1)

        callLog = QToolButton(self)
        callLog.setToolButtonStyle(2)
        callLog.setText('Add call information here')
        callLog.setIcon(QIcon.fromTheme('arrow-left'))
        callLog.setIconSize(QSize(64, 64))
        callLogLayout = QHBoxLayout()
        callLogLayout.addWidget(callLog)
        callLogLayout.addStretch(1)

        vLayout = QVBoxLayout()
        vLayout.addStretch(1)
        vLayout.addWidget(titleLabel)
        vLayout.addLayout(newJobLayout)
        vLayout.addLayout(editJobLayout)
        vLayout.addLayout(addToJobLayout)
        vLayout.addLayout(callLogLayout)
        vLayout.addStretch(1)
        self.setLayout(vLayout)
