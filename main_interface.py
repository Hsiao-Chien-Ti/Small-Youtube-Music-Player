import sys
import play_song
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

class main_interface(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()        
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Concentrate Youtube')
        self.show()
    def initUI(self):
        self.stack=QStackedWidget(self)
        main=mainUI()
        self.loop=loopUI()
        singer=singerUI()
        atmo=atmoUI()
        self.player=play_song.play_song()        
        self.stack.addWidget(self.loop)
        self.stack.addWidget(singer)
        self.stack.addWidget(atmo)
        self.stack.addWidget(main)
        self.loop.home.clicked.connect(self.GoHome)
        singer.home.clicked.connect(self.GoHome)
        atmo.home.clicked.connect(self.GoHome)
        main.btn1.clicked.connect(lambda:self.stack.setCurrentWidget(self.loop))
        main.btn2.clicked.connect(lambda:self.stack.setCurrentWidget(singer))
        main.btn3.clicked.connect(lambda:self.stack.setCurrentWidget(atmo))
        self.loop.search.clicked.connect(lambda:self.search())
        self.setLayout=self.stack
        self.GoHome()
    def GoHome(self):
        self.stack.setCurrentIndex(3)
    def search(self):
        song=self.loop.song.text()
        self.player.end()
        self.player.search(song)
        self.player.play()
        
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
        Vlayout.addLayout(Hlayout)
        Vlayout.addWidget(self.home)
        self.setLayout(Vlayout)
class singerUI(QWidget):
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
class mainUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        layout=QVBoxLayout()
        want=QLabel(self)
        want.setText("What do you want today?")
        want.move(10,10)
        want.resize(170,20)
        self.btn1=QPushButton("單曲循環")
        self.btn2=QPushButton("單一歌手")
        self.btn3=QPushButton("情境")
        layout.addWidget(want)
        layout.addWidget(self.btn1)
        layout.addWidget(self.btn2)
        layout.addWidget(self.btn3)
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = main_interface()
    sys.exit(app.exec())