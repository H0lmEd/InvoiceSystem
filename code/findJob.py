from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit

class findJobWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self)
        self.layout = QVBoxLayout()
        label = QLabel("Find Job")
        searchLabel = QLabel("Job No:")
        searchField = QLineEdit(self)
        self.searchLayout = QHBoxLayout()
        self.searchLayout.addWidget(searchLabel)
        self.searchLayout.addWidget(searchField)
        
        self.layout.addLayout(self.searchLayout)
        
        self.setLayout(self.layout)

