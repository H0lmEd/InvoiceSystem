from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QPushButton

class findJobWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self)
        self.layout = QVBoxLayout()
        label = QLabel("Find Job")
        searchLabel = QLabel("Job No:")
        self.searchField = QLineEdit(self)
        self.searchBtn = QPushButton('Go', self)

        self.searchLayout = QHBoxLayout()
        self.searchLayout.addWidget(searchLabel)
        self.searchLayout.addWidget(self.searchField)
        self.searchLayout.addWidget(self.searchBtn)
        self.layout.addLayout(self.searchLayout)
        self.setLayout(self.layout)
        self.searchField.returnPressed.connect(lambda: self.searchBtn.click())
