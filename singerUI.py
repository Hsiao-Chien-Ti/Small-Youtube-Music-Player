from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import*
class singerUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        super().__init__()
        layout=QVBoxLayout(self)
        singer_layout=QGridLayout(self)
        self.mayday=QToolButton(self)
        self.mayday.setFixedSize(100,100)
        self.mayday.setIcon(QIcon('./img/mayday.png'))
        self.mayday.setIconSize(QSize(100,100))
        self.mayday.setToolTip('五月天')
        self.nine=QToolButton(self)
        self.nine.setFixedSize(100,100)
        self.nine.setIcon(QIcon('./img/nine.png'))
        self.nine.setIconSize(QSize(100,100))
        self.nine.setToolTip('陳零九')
        self.jay=QToolButton(self)
        self.jay.setFixedSize(100,100)
        self.jay.setIcon(QIcon('./img/jay.png'))
        self.jay.setIconSize(QSize(100,100))
        self.jay.setToolTip('周杰倫')
        self.JJ=QToolButton(self)
        self.JJ.setFixedSize(100,100)
        self.JJ.setIcon(QIcon('./img/JJ.png'))
        self.JJ.setIconSize(QSize(100,100))
        self.JJ.setToolTip('林俊傑')
        
        singer_layout.addWidget(self.mayday,0,0)
        singer_layout.addWidget(self.nine,0,1)
        singer_layout.addWidget(self.jay,1,0)
        singer_layout.addWidget(self.JJ,1,1)

        self.play=QPushButton(self)
        self.pause=QPushButton(self)
        self.play.setText('play')
        self.pause.setIcon(QIcon('./img/pause.png'))

        self.songlist=QListWidget(self)
        self.songlist.setGeometry(0,250,250,300)
        # self.songlist.setMinimumSize(QSize(300,300))
        self.home=QPushButton(self)
        self.home.setText("home")
        self.home.setIcon(QIcon('./img/home.png'))
        
        layout.addLayout(singer_layout)
        layout.addWidget(self.songlist,alignment=Qt.AlignmentFlag.AlignBaseline)
        layout.addWidget(self.play)
        layout.addWidget(self.pause)
        layout.addWidget(self.home)
        
        self.play.setVisible(False)
        self.pause.setVisible(False)
        self.songlist.setVisible(False)
        self.setLayout(layout)