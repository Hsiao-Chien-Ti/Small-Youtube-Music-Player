from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
class loopUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        super().__init__()
        Vlayout=QVBoxLayout()
        Hlayout=QHBoxLayout()
        Hlayout.addWidget(QLabel("歌名"))
        self.song=QLineEdit(self)
        Hlayout.addWidget(self.song)
        self.home=QPushButton(self)
        self.home.setText("home")
        self.home.setIcon(QIcon('./img/home.png'))
        self.search=QPushButton(self)
        self.search.setText("Search")
        Hlayout.addWidget(self.search)
        self.songlist=QListWidget(self)
        self.play=QPushButton(self)
        self.pause=QPushButton(self)
        self.play.setText('play')
        self.pause.setIcon(QIcon('./img/pause.png'))

        self.play.setStyleSheet("background-color:	#D7FFEE")
        self.pause.setStyleSheet("background-color:	#D7FFEE")
        self.songlist.setStyleSheet("background-color:	#D7FFEE")
        self.home.setStyleSheet("background-color:	#D7FFEE")
        self.search.setStyleSheet("background-color:	#D7FFEE")
        self.song.setStyleSheet("background-color:	#D7FFEE")
        Vlayout.addLayout(Hlayout)
        Vlayout.addWidget(self.songlist)
        Vlayout.addWidget(self.play)
        Vlayout.addWidget(self.pause)
        Vlayout.addWidget(self.home)
        self.play.setVisible(False)
        self.pause.setVisible(False)
        self.setLayout(Vlayout)