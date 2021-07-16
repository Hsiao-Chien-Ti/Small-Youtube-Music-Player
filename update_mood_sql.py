import csv
import mysql.connector
cnx = mysql.connector.connect(user='Adi', password='Adicoco0410',database='song_data')
cursor=cnx.cursor()
query=("SELECT * FROM songlist")
cursor.execute(query)
data=[]
i=0
with open('output.csv', newline='') as csvfile:
    rows = csv.reader(csvfile)
    row=list(rows)
for (song,singer,CD,moods,link) in cursor:
    data.append([row[i],song])
    i+=1
for d in data:
    print(d[0],d[1])
    if(len(d[0])!=0):
        query="""UPDATE songlist SET moods=%s WHERE song=%s"""
        cursor.execute(query, (d[0][0],d[1]))   
        cnx.commit() 
    else:
        query="""UPDATE songlist SET moods=%s WHERE song=%s"""
        cursor.execute(query, (None,d[1]))   
        cnx.commit() 
cursor.close()
cnx.close()
        