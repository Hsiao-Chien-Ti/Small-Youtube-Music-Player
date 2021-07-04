import pafy,vlc
import keyboard
class play_song():
    def __init__(self):
        self.url="https://www.youtube.com/watch?v=6Duo89XuYIM&list=RDMMIoCoIxkGkVw&index=20"
        self.video=pafy.new(url)
        self.best = video.getbestaudio()
        self.playurl = best.url
        self.Instance = vlc.Instance()
        self.player = Instance.media_player_new()
        self.Media = Instance.media_new(playurl)
        Media.get_mrl()
        Media.add_option('start-time=120.0')
        Media.add_option('stop-time=130.0')
        player.set_media(Media)
    def play_song(self):
        self.player.play()
    def pause(self):
        self.player.pause()
    def stop(self):
        self.player.stop()
    