from pytube import Playlist,YouTube
import re
import mysql.connector

playlist = Playlist("https://www.youtube.com/watch?v=gd38-X3HpbM&list=PLj6NQzHFCvkGOAwI_ofdmAmWiEO2QhVp2")
cnx = mysql.connector.connect(user='Adi', password='Adicoco0410',database='song_data')
cursor=cnx.cursor()

playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
print(len(playlist.video_urls))
for url in playlist.video_urls:
    yt=YouTube(url)
    print(yt.title)
    # title=re.split('周杰倫 ',yt.title)
    # print(title)
    # # title=re.split('Official',title[1])
    # title=re.split(' ',title[1])
    # title=re.split('- ',yt.title)
    # print(url)
    query=("INSERT ignore INTO `songlist` VALUES(%s,%s,%s,%s)")
    data=(yt.title,'林俊傑',None,url)
    cursor.execute(query,data)
# url='https://www.youtube.com/watch?v=ChXiROKng30'
# query=("INSERT ignore INTO `songlist` VALUES(%s,%s,%s,%s)")
# data=('Jay Chou 周杰倫【手語 Sign Language】-Official Music Video','周杰倫',None,url)
# cursor.execute(query,data)
cnx.commit()
# for (song,singer,link) in cursor:
#     print(song)