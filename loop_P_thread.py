from PyQt6.QtCore import *
import play_song
import time
class loop_P_thread(QObject):
    show_pause=pyqtSignal(int)
    switch_pause=pyqtSignal()
    def __init__(self):
        super().__init__()
        self.player=play_song.play_song() 
    def play(self,url):
        self.player.end()
        self.player.url=url
        self.player.create()
        self.show_pause.emit(1)
        self.player.play()
    def pause(self):
        self.player.pause()
        self.switch_pause.emit()
    def stop(self):
        self.player.end()