import pafy,vlc
import youtube_dl
import keyboard
import load_data
import time
class play_song():
    def __init__(self):
        self.Instance = vlc.Instance()
        self.player = self.Instance.media_player_new()
    def search(self,song):
        data=load_data.load_data()
        self.url=data.search(song)
        self.video=pafy.new(self.url)
        self.best = self.video.getbestaudio()
        self.playurl = self.best.url
        self.Instance = vlc.Instance()
        self.player = self.Instance.media_player_new()
        self.Media = self.Instance.media_new(self.playurl)
        self.Media.get_mrl()
        self.player.set_media(self.Media)
    def end(self):
        if self.player.is_playing():
            self.stop()
    def play(self):
        self.player.play()
    def pause(self):
        self.player.pause()
    def stop(self):
        self.player.stop()
if __name__ == '__main__':
    player=play_song()
    player.play()
    while True:
         pass
    