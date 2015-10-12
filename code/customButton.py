from PyQt5.QtWidgets import (QLineEdit, QToolButton, QStyle)
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
import os


class ButtonLineEdit(QLineEdit):

    def __init__(self, parent=None):
        super(ButtonLineEdit, self).__init__(parent)
        self.errorIconFile = os.path.join(os.path.dirname(__file__), os.pardir, "icons/error.png")
        self.tickIconFile = os.path.join(os.path.dirname(__file__), os.pardir, "icons/correct.png")
        self.button = QToolButton(self)
    def showError(self):
        self.button.setIcon(QIcon(self.errorIconFile))
        self.button.setStyleSheet('border: 0px; padding: 0px;') #No Padding
        #self.button.setCursor(ArrowCursor)

        frameWidth = self.style().pixelMetric(QStyle.PM_DefaultFrameWidth)# Set to label length
        buttonSize = self.button.sizeHint()

        self.setStyleSheet('QLineEdit {padding-right: %dpx; }' % (buttonSize.width() + frameWidth + 1))
        self.setMinimumSize(max(self.minimumSizeHint().width(), buttonSize.width() + frameWidth*2 + 2),
                            max(self.minimumSizeHint().height(), buttonSize.height() + frameWidth*2 + 2))

    def showTick(self):
        print("Ticking")
        self.button.setIcon(QIcon(self.tickIconFile))
        self.button.setStyleSheet('border: 0px; padding: 0px;') #No Padding
        #self.button.setCursor(ArrowCursor)

        frameWidth = self.style().pixelMetric(QStyle.PM_DefaultFrameWidth)# Set to label length
        buttonSize = self.button.sizeHint()

        self.setStyleSheet('QLineEdit {padding-right: %dpx; }' % (buttonSize.width() + frameWidth + 1))
        self.setMinimumSize(max(self.minimumSizeHint().width(), buttonSize.width() + frameWidth*2 + 2),
                            max(self.minimumSizeHint().height(), buttonSize.height() + frameWidth*2 + 2))

       
    def resizeEvent(self, event):
        buttonSize = self.button.sizeHint()
        frameWidth = self.style().pixelMetric(QStyle.PM_DefaultFrameWidth)
        self.button.move(self.rect().right() - frameWidth - buttonSize.width(),
                         (self.rect().bottom() - buttonSize.height() + 1)/2)
        super(ButtonLineEdit, self).resizeEvent(event)
