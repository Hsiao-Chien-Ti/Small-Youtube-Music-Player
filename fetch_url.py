from pytube import Playlist,YouTube
import re
import mysql.connector

playlist = Playlist("https://www.youtube.com/playlist?list=PLDgLLnSBXR_MjEsil58mIOSCOYAsp141E")
cnx = mysql.connector.connect(user='Adi', password='Adicoco0410',database='song_data')
cursor=cnx.cursor()

playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
print(len(playlist.video_urls))
for url in playlist.video_urls:
    yt=YouTube(url)
    title=re.split('【',yt.title)
    title=re.split('】',title[1])
    title=re.split(' ',title[0])
    # print(title)
    # print(url)
    query=("INSERT INTO `songlist` VALUES(%s,%s,%s)")
    data=(title[0],'陳零九',url)
    cursor.execute(query,data)
cnx.commit()
query=("SELECT * FROM songlist")
cursor.execute(query)
for (song,singer,link) in cursor:
    print(song)