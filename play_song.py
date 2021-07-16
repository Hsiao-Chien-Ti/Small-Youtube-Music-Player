import pafy,vlc
import youtube_dl
import keyboard
import load_data
import time
class play_song():
    def __init__(self):
        self.url=''
        self.Instance = vlc.Instance('--loop')
        self.player = self.Instance.media_player_new()
    def end(self):
        if self.player.is_playing():
            self.pause()
    def create(self):        
        self.video=pafy.new(self.url)
        self.best = self.video.getbestaudio()
        self.playurl = self.best.url  
        self.Media = self.Instance.media_new(self.playurl)
        self.Media.get_mrl()
    def play(self):    
        self.player.set_media(self.Media)
        self.player.play()
    def pause(self):
        self.player.pause()
    def stop(self):
        self.player.stop()
    def duration(self):
        return self.player.get_length()/1000
if __name__ == '__main__':
    player=play_song()
    player.play()
    while True:
         pass
    