import sys
import play_song
import load_data
import loopUI
import singerUI
import atmoUI
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

class main_interface(QWidget):
    def __init__(self):
        super().__init__()
        self.sql=load_data.load_data()
        self.initUI()        
        self.setGeometry(400, 200, 300, 400)
        self.setWindowTitle('Concentrate Youtube')
        self.show()
    def initUI(self):
        self.stack=QStackedWidget(self)
        main=mainUI()
        self.loop=loopUI.loopUI()
        singer=singerUI.singerUI()
        atmo=atmoUI.atmoUI()
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
        self.loop.play.clicked.connect(lambda:self.play())
        self.loop.pause.clicked.connect(lambda:self.pause())
        self.setLayout=self.stack
        self.GoHome()
    def GoHome(self):
        self.stack.setCurrentIndex(3)
    def search(self):
        song=self.loop.song.text()
        songlist,self.link=self.sql.search(song)
        self.loop.songlist.clear()
        for s in songlist:
            self.loop.songlist.addItem(s)
        print(self.loop.songlist.count())
        self.loop.songlist.setVisible(True)
        self.loop.play.setVisible(True)
    def play(self):
        self.player.end()
        i=self.loop.songlist.currentIndex().row()
        print(i)
        self.player.url=self.link[i]
        self.player.play()
        self.loop.pause.setVisible(True)
    def pause(self):
        self.player.pause()
        p=QIcon('./img/pause.png')
        q=QIcon('./img/play.png')
        if self.loop.pause.icon==p:
            self.loop.pause.setIcon(q)
    

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