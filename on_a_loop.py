from PyQt6.QtWidgets import *
class on_a_loop(QWidget):  
    self.widget=QWidget()
    self.layout=QFormLayout()
    self.layout.addRow("Search",QLineEdit())
    self.widget.setLayout(self.layout)

