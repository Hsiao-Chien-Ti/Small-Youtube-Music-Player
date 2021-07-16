from PyQt6.QtCore import *
import play_song
import time
import random
class singer_P_thread(QObject):
    show_pause=pyqtSignal(int)
    switch_pause=pyqtSignal()
    def __init__(self):
        super().__init__()
        self.player=play_song.play_song() 
        self.play_flag=True
    def play(self,i,link):
        self.player.end()         
        self.show_pause.emit(2)
        self.play_flag=True
        self.player.url=link[i]
        self.player.create()
        self.player.play()
        time.sleep(1)
        duration=self.player.duration()
        timer=time.time()
        while self.play_flag==True:
            if(time.time()-timer>=duration):
                i=random.randint(0,len(link)+1)
                self.player.url=link[i]
                self.player.create()
                self.player.play()
                time.sleep(1)
                duration=self.player.duration()            
    def pause(self):
        self.player.pause()
        self.play_flag=False
        self.switch_pause.emit()
    def stop(self):
        self.play_flag=False
        self.player.end()
        