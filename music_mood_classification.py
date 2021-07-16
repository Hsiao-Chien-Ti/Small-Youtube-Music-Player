# import tensorflow as tf
# # import pandas as pd
# import librosa.display
# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
# import pafy 
import mysql.connector
# from keras.models import load_model
# from keras.preprocessing import image
# import os
# from PIL import Image
import csv

cnx = mysql.connector.connect(user='Adi', password='Adicoco0410',database='song_data')
cursor=cnx.cursor()
query=("SELECT * FROM songlist")
# model=load_model("./music_mood_20210715_mobilenet(lr0.00001_400epoch).h5")
img_path=['./output1.png','./output2.png','./output3.png']
cursor.execute(query)
mood=['aggressive','happy','romantic','sad']
k=0
for (song,singer,CD,moods,link) in cursor:
    with open('songlist.csv', 'a',encoding="utf-16", newline='') as csvfile:
        row=[]
        row.append(song)
        row.append(link)
        writer = csv.writer(csvfile)
        writer.writerow(row)
    # # if(k<54):
    # #     k+=1
    # #     continue
    # url=link
    # name="./song.m4a"
    # video = pafy.new(url)
    # bestaudio = video.getbestaudio(preftype="m4a")
    # bestaudio.download(name)    

    # y,sr = librosa.load(name,offset=90,duration=5)
    # mels = librosa.feature.melspectrogram(y=y,sr=sr)
    # fig = plt.Figure()
    # p = plt.imshow(librosa.power_to_db(mels,ref=np.max))
    # plt.savefig('./output1.png')

    # y,sr = librosa.load(name,offset=120,duration=5)
    # mels = librosa.feature.melspectrogram(y=y,sr=sr)
    # fig = plt.Figure()
    # p = plt.imshow(librosa.power_to_db(mels,ref=np.max))
    # plt.savefig('./output2.png')

    # y,sr = librosa.load(name,offset=150,duration=5)
    # mels = librosa.feature.melspectrogram(y=y,sr=sr)
    # fig = plt.Figure()
    # p = plt.imshow(librosa.power_to_db(mels,ref=np.max))
    # plt.savefig('./output3.png')
    # avg_pred=np.zeros((1,4),dtype=float)

    # for path in img_path:
    #     img=image.load_img(path)
    #     img=img.resize((432,288))
    #     img_tensor = image.img_to_array(img)                    # (height, width, channels)
    #     img_tensor=img_tensor/255.
    #     img_tensor = np.expand_dims(img_tensor, axis=0)  
    #     pred=model.predict(img_tensor)
    #     print(pred)
    #     avg_pred+=pred
    # print(song+' '+mood[np.argmax(avg_pred)])
    # with open('output.csv', 'a', newline='') as csvfile:
    #     writer = csv.writer(csvfile)
    #     writer.writerow([mood[np.argmax(avg_pred)]])
    # os.remove(name)
    # for path in img_path:
    #     os.remove(path)
    # # query="UPDATE songlist SET `moods`="
    # # query+=mood[np.argmax(pred)]
    # # query+=" where `song`='"
    # # query+=song
    # # query+="';"
    # # cursor.execute(query)


