from PyQt6.QtCore import *
import play_song
import time
class atmo_P_thread(QObject):
    show_pause=pyqtSignal(int)
    switch_pause=pyqtSignal()
    def __init__(self):
        super().__init__()
        self.player=play_song.play_song() 
    def play(self,i,link):
        self.player.end()         
        self.show_pause.emit(2)
        while i<=len(link):
            self.player.url=link[i]
            self.player.create()
            self.player.play()
            time.sleep(1)
            duration=self.player.duration()
            time.sleep(duration)
            i+=1
    def pause(self):
        self.player.pause()
        self.switch_pause.emit()
    def stop(self):
        self.player.end()