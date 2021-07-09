import sys
import play_song
import load_data
import loopUI
import singerUI
import atmoUI
import time
import loop_P_thread
import singer_P_thread
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

class main_interface(QWidget):
    loop_play_sgn=pyqtSignal(str)
    singer_play_sgn=pyqtSignal(int,list)
    singer_stop_sgn=pyqtSignal()
    def __init__(self):
        super().__init__()
        self.sql=load_data.load_data()
        self.pause_icon=QIcon('./img/pause.png')
        self.play_icon=QIcon('./img/play.png')
        self.link=[]
        self.pause_flag=False
        self.initUI()        
        self.setGeometry(400, 200, 300, 700)
        self.setWindowTitle('Concentrate Youtube')
        self.show()
    def initUI(self):
        self.stack=QStackedWidget(self)
        main=mainUI()
        self.loop=loopUI.loopUI()
        self.singer=singerUI.singerUI()
        atmo=atmoUI.atmoUI()

        self.loop_thread=QThread()
        self.loop_p_thread=loop_P_thread.loop_P_thread() 
        self.loop_p_thread.moveToThread(self.loop_thread) 
        self.loop_p_thread.show_pause.connect(lambda:self.show_pause(1))
        self.loop_p_thread.switch_pause.connect(lambda:self.switch_pause())
        self.loop_play_sgn.connect(self.loop_p_thread.play)

        self.singer_thread=QThread()
        self.singer_p_thread=singer_P_thread.singer_P_thread() 
        self.singer_p_thread.moveToThread(self.singer_thread) 
        self.singer_p_thread.show_pause.connect(lambda:self.show_pause(2))
        self.singer_p_thread.switch_pause.connect(lambda:self.switch_pause())
        self.singer_play_sgn.connect(self.singer_p_thread.play)
        self.singer_stop_sgn.connect(self.singer_p_thread.stop)

        self.stack.addWidget(self.loop)
        self.stack.addWidget(self.singer)
        self.stack.addWidget(atmo)
        self.stack.addWidget(main)
        self.loop.home.clicked.connect(self.GoHome)
        self.singer.home.clicked.connect(self.GoHome)
        atmo.home.clicked.connect(self.GoHome)
        main.btn1.clicked.connect(lambda:self.stack.setCurrentWidget(self.loop))
        main.btn2.clicked.connect(lambda:self.stack.setCurrentWidget(self.singer))
        main.btn3.clicked.connect(lambda:self.stack.setCurrentWidget(atmo))
        self.loop.search.clicked.connect(lambda:self.search(1))
        self.loop.play.clicked.connect(lambda:self.play(1))
        self.singer.mayday.clicked.connect(lambda:self.search(2,'五月天'))
        self.singer.nine.clicked.connect(lambda:self.search(2,'陳零九'))
        self.singer.jay.clicked.connect(lambda:self.search(2,'周杰倫'))
        self.singer.JJ.clicked.connect(lambda:self.search(2,'林俊傑'))
        self.singer.play.clicked.connect(lambda:self.play(2))
        
        self.singer.pause.clicked.connect(lambda:self.singer_p_thread.pause())
        self.loop.pause.clicked.connect(lambda:self.loop_p_thread.pause())
        self.setLayout=self.stack
        self.GoHome()
        self.loop_thread.start()
        self.singer_thread.start()
    def GoHome(self):
        self.stack.setCurrentIndex(3)
    def search(self,mode,singer=''):
        if mode==1:
            song=self.loop.song.text()
            songlist,self.link=self.sql.search_song(song)
            self.loop.songlist.clear()
            for s in songlist:
                self.loop.songlist.addItem(s)
            self.loop.songlist.setVisible(True)
            self.loop.play.setVisible(True)
        elif mode==2:
            songlist,self.link=self.sql.search_singer(singer)
            self.singer.songlist.clear()
            for s in songlist:
                self.singer.songlist.addItem(s)
            self.singer.songlist.setVisible(True)
            self.singer.play.setVisible(True)
    def play(self,mode):
        if mode==1:
            url=self.link[self.loop.songlist.currentIndex().row()]
            self.loop_play_sgn.emit(url)
        elif mode==2:
            i=self.singer.songlist.currentIndex().row()
            self.singer_stop_sgn.emit()
            self.singer_play_sgn.emit(i,self.link)

    def show_pause(self,mode):
        if mode==1:
            self.loop.pause.setVisible(True)
        elif mode==2:
            self.singer.pause.setVisible(True)
    def switch_pause(self):
        if self.pause_flag==False:
            self.loop.pause.setIcon(self.play_icon)
            self.singer.pause.setIcon(self.play_icon)
            self.pause_flag=True
        elif self.pause_flag==True:
            self.loop.pause.setIcon(self.pause_icon)
            self.singer.pause.setIcon(self.play_icon)
            self.pause_flag=False

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