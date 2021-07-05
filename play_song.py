import pafy,vlc
import youtube_dl
import keyboard
class play_song():
    def __init__(self):
        self.url="https://www.youtube.com/watch?v=6Duo89XuYIM&list=RDMMIoCoIxkGkVw&index=20"
        self.video=pafy.new(self.url)
        self.best = self.video.getbestaudio()
        self.playurl = self.best.url
        self.Instance = vlc.Instance()
        self.player = self.Instance.media_player_new()
        self.Media = self.Instance.media_new(self.playurl)
        self.Media.get_mrl()
        self.Media.add_option('start-time=120.0')
        self.Media.add_option('stop-time=130.0')
        self.player.set_media(self.Media)
    def play(self):
        self.player.play()
    def pause(self):
        self.player.pause()
    def stop(self):
        self.player.stop()
    