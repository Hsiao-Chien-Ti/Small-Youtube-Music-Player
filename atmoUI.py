from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
class atmoUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        super().__init__()
        layout=QHBoxLayout()
        layout.addWidget(QLabel("Search"))
        layout.addWidget(QLineEdit())
        self.home=QPushButton(self)
        self.home.setText("home")
        self.home.setIcon(QIcon('./img/home.png'))
        layout.addWidget(self.home)
        self.setLayout(layout)