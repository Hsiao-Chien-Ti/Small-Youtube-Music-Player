import json
import mysql.connector

cnx = mysql.connector.connect(user='Adi', password='Adicoco0410',database='song_data')
cursor=cnx.cursor()
query=("SELECT * FROM songlist")
cursor.execute(query)
data = []

for (song,singer,CD,moods,link) in cursor:
    data.append({
        'song':song,
        'link':link
    })
with open('data.json','w',encoding='utf-8') as outfile:
    json.dump(data, outfile,ensure_ascii=False)