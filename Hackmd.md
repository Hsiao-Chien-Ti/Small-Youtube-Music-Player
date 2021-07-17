# Small Youtube Music Player
* 20210703
    * jupyter notebook
    * install modules:
        * pafy
        * python-vlc
            * 要先裝vlc media player https://www.videolan.org/ 
        * youtube_dl
    * 酷斃了，播音樂不會生成新視窗欸
        * 可是要怎麼關掉它XD
        * ```python
            import pafy,vlc
            url="https://www.youtube.com/watch?v=6Duo89XuYIM&list=RDMMIoCoIxkGkVw&index=20"
            video=pafy.new(url)
            best = video.getbestaudio()
            playurl = best.url
            Instance = vlc.Instance()
            player = Instance.media_player_new()
            Media = Instance.media_new(playurl)
            Media.get_mrl()
            player.set_media(Media)
            player.play()
            ```
*  20210704
    *  install modules:
        *  keyboard:用鍵盤按鈕結束撥放
        *  pyside6:用來做GUI
        *  PyQt6:pyside6的教學資源好少，改用pyqt6
        *  PyAudio:voice chat
            *  要用conda install
            *  conda install PyAudio
    *  vlc function:
        *  Media.add_option()可以設定播放時間 
        *  player.pause()可暫停
        *  player.stop()可結束
    *  keyboard:
        *  ```python
            if keyboard.read_key()=='p':
            player.stop()
            ```
    *  voice chat:
        *  https://github.com/TomPrograms/Python-Voice-Chat
    *  PyQt6:
        *  https://zetcode.com/pyqt6/firstprograms/
        *  event processing是signal&slot設計，signal代表event發生，slot是收到signal後要做的事
        *  setToolTip:按鈕提示
        *  QPushButton:按鈕
        *  不知道為甚麼和PyQt合在一起之後，vlc就會報error
            *  https://stackoverflow.com/questions/68245733/mmdevice-audio-output-error-cannot-initialize-com-error-0x80010106
            *  被外國人罵，好氣
    * 改變idea了啦
        * 專心ㄉYoutube播放器
        ![](https://i.imgur.com/CmgT9Wh.png)
    * 目前介面
        ![](https://i.imgur.com/G7iaxYn.png)
        * 好想改中文字體，有夠醜
* 20210705
    * Layout
        * ![](https://i.imgur.com/8xjs5bH.jpg)
        * multi-page:
            * 用QStackedWidget
            * addWidget()新增新的介面
    * 程式架構
        * 每個page寫成一個class，在main_interface裡面宣告class型別的widget，再把宣告好的widget加入stack裡
            ```python
            main=mainUI()
            loop=loopUI()
            singer=singerUI()
            atmo=atmoUI()        
            self.stack.addWidget(loop)
            self.stack.addWidget(singer)
            self.stack.addWidget(atmo)
            self.stack.addWidget(main)
            ```
        * 各個class的button寫self，在main_interface裡面再去定義connect
            ```python
            main.btn1.clicked.connect(lambda:self.stack.setCurrentWidget(loop))
            main.btn2.clicked.connect(lambda:self.stack.setCurrentWidget(singer))
            main.btn3.clicked.connect(lambda:self.stack.setCurrentWidget(atmo))
            ```
            * 用到stack的要寫lambda
    * QListWidget：
        * 不設nothing的時候介面一打開就出現loop介面，可是設了nothing，loop就變成第二的選項了![](https://i.imgur.com/2AoBJB5.png)
        * 發現是因為QListWidget預設會選第一個選項，所以一進入就會直接跳到loop的介面
            * 還是決定改用button好了...
    * Button的Icon設定：
        ```python
        self.home.setIcon(QIcon('./img/home.png'))
        ```
        * 資料夾最前面要記得寫.啦
    * 目前介面
        ![](https://i.imgur.com/j5pz34d.png)
        ![](https://i.imgur.com/IRDfASG.png)
* 20210706
    * database
        * 網址資料存在database中
        * 用mySQL來做database
        * ![](https://i.imgur.com/M4FYbIZ.png)
    * install modules
        * install mySQL
            * 官網下載/32位元沒關係
            * 選full
            * route不要弄
        * mysql connector
            * pip install mysql-connector-python
        * youtube api(用來fetch url)
            * 到google cloud上建立一個專案
            * 在憑證區申請一個youtube v3 api金鑰
            * pip install --upgrade google-api-python-client
            * 好像可以直接用youtube data api module做
            * pip install youtube-data-api
        * 後來發現好像可以用pafy做
            * https://www.geeksforgeeks.org/pafy-getting-end-value-for-each-item-of-playlist/
            * 404 not found![](https://i.imgur.com/0gj6Cct.png)
            * 結果發現pafy的get_playlist()功能好像最近被封了
        * 也可以用pytube3?
            * pip install pytube3
            * 用這個語法感覺可行，可是youtube好像又修正過，所以讀不到東西 https://stackoverflow.com/questions/62661930/pytube3-playlist-returns-empty-list
                ```python
                from pytube import Playlist
                url='https://www.youtube.com/playlist?list=PLDgLLnSBXR_MjEsil58mIOSCOYAsp141E'
                yt=Playlist(url)
                print(len(yt.video_urls))
                for i in yt.video_urls:
                    print(i)         
                ```
    * mySQL
        * 要刪除全部資料要先關掉safe mode
            * edit->preference->sql editor
            * ![](https://i.imgur.com/ojhuIM9.png)
            * 登出再進來一次
    * 目前進度：
        * 單曲播放可以搜尋歌曲
          ![](https://i.imgur.com/cHuqRsv.png)
        * 播放搜尋的下一首前會先關掉目前的歌
        * database建立完陳零九
          ![](https://i.imgur.com/kTVzaZc.png)
        * 重複的歌待移除
        * 搜尋功能現在只能播完全一樣的，待優化
* 20210707
    * 擴充資料庫(目前388首/五月天、陳零九、周杰倫)
      ![](https://i.imgur.com/xRPTD9W.png)
        * 原本打算只取歌名，可是每首歌的命名方式不一(ex'【'和'\[')
            * 命名不統一會沒辦法用re.split處理
            * 決定整個歌名都存 
        * 重複歌名只存一首
            * 用ignore
            ```python
            query=("INSERT ignore INTO `songlist` VALUES(%s,%s,%s,%s)")
            ```
    * 優化搜尋功能
         ```python
         query=("SELECT * FROM songlist WHERE song like ")
         query=query+'\'%'+song+'%\''
         ```
         可以搜到名稱裡含有'%文字%'的
    * 搜尋結果list顯示
        * 不知道怎麼先讓list隱藏起來
        * 先hide再在裡面additem，結果再show出來的時候大小沒有變大，所有選項都被擋住看不到
        * 目前還沒有解決方法 
    * 單曲播放完成
        * 改成用media_list_player
    * 單一歌手圖片按鈕
        * 用QToolButton才可以有超大圖片
    * 目前介面：
      ![](https://i.imgur.com/JpoSLWZ.png)
      ![](https://i.imgur.com/oW5lyyM.png)
      ![](https://i.imgur.com/0L83h1U.png)
      ![](https://i.imgur.com/QjMAQWa.png)
      ![](https://i.imgur.com/tPiofvX.png)
* 20210708
    * 單一歌手當掉
        * 一次把所有歌都放進去要等至少5分鐘(GUI在add media list的時候會當掉)
        * 一次放一首然後用迴圈輪播
        * 在play()裡用for搭配time.sleep()，可是這樣會block住整個程式，GUI完全當掉(會播歌)![](https://i.imgur.com/OFee4I9.png)

        * 應該要建立QThread
        * https://realpython.com/python-pyqt-qthread/
            * ![](https://i.imgur.com/QVnEzCw.png)
    * QThread
        * 創建好Qthread物件
        * 還沒改完(31~34改好)
            ```python
            self.thread=QThread()
            self.p_thread=P_thread.P_thread()
            self.player=play_song.play_song()  
            self.p_thread.moveToThread(self.thread) 
            ```
* 20210709
    * thread大致修改完畢
        * 單一歌手可以連續播歌不會當掉
        * 最後決定loop和singer分兩個thread
        * 待處理的問題：
            * 不能再播到一半切到其他首歌
            * 播singer時若切到loop，singer的播放器不會停止
    * music classification(要用來做情境)
        * google colab
            * 就是google版的jupyter
            * 要適當操控雲端硬碟空間QQ
        * K-nearest neighbors algorithm
            * 監督式學習
            * k值代表要取幾個鄰居
            * 原有的dataset已知針對兩個特徵做座標圖，新放入的資料P定位後，看離他最近的k個點分別歸在哪些類別，哪個類別多就把P歸到那一類去。
            * ![](https://i.imgur.com/9Y72Dkl.png)
            * https://data-flair.training/blogs/python-project-music-genre-classification/
        * CNN
            * 好像比較多人是用CNN欸
            * 原理應該是把librosa visualize出的spectrogram當成圖片丟進去分類(好像跟傷口辨識很像欸酷)
        * GTZAN dataset
        * 用spectrogram來區分類別
          ![](https://i.imgur.com/Rjoxb6b.png)
          用librosa視覺化出來的
        * import os->處理檔案和文件
        * f-string：一種字串形式
        * https://medium.com/@sdoshi579/classification-of-music-into-different-genres-using-keras-82ab5339efe0
        * https://towardsdatascience.com/music-genre-recognition-using-convolutional-neural-networks-cnn-part-1-212c6b93da76
* 20210710
    * dataset前處理
        * dataset從kaggle導入google colab
        * 要把音檔用Librosa轉成圖片
        * ![](https://i.imgur.com/oa05ytV.png)
          這張是classical，還滿可愛ㄉ

        * 轉超級久，跑了4個小時還不到2000，總共有9000張圖片...
        * 轉到一半突然想到，我需要的好像不是要分類blue/classical/jazz ...，應該是要分類happy/sad...
        * GTZAN應該不是我需要的dataset，只好果斷放棄跑了4個小時的東東
        * 改用 https://www.kaggle.com/shanmukh05/music-classification
        * 因為雲端空間不夠，決定捨去dramatic，先載到電腦裡，再把其他類別壓縮起來傳到雲端
        * 因為新的dataset太大了，一個種類有快2000個，跑超級久，只好刪掉一些data不然不知道甚麼時候才能跑完
        * aggressive跑到一半就放著去睡覺了
* 20210711
    * 又花了一整天終於把dataset處理完
        * 早上起床發現，因為我刪掉了後面的data，所以aggresive在我去睡後4分鐘就爆error跑完了(總共跑了4小時52分)...等於整個晚上都沒跑到東西
        * 早上繼續跑
        * 刪掉figurecanvas，剛開始有比較快，可是後來實際上happy也跑了4個半小時
        * 後來發現是剛開始跑的時候速度會超快，後面不知道為甚麼會越跑越慢
        * 決定人為操控看看，每隔半個多小時暫停一次，然後把已經跑過的wav刪掉，再從下一個編號開始跑
        * 這樣可以一直維持剛開始的超快速度
        * 結果romantic和sad都只跑了兩個小時左右而已，超讚
    * 決定拿以前專研的model結構來用用看
        * 20:12終於開始train了，好快樂
          ![](https://i.imgur.com/ypcHMeP.png)
        * 兩年沒看過這個畫面ㄌ
        * 希望結果會好... 
* 20210712
    * 超慢超爛
        * ![](https://i.imgur.com/DhmW06W.png)
        * 這參數絕對有問題
        * 爬文看到先把dataset直接import到google colab裡可以加速
        * ![](https://i.imgur.com/E6OxGRN.png)
        * 傳data就傳了快2個小時，瘋掉
        * 氣到快吐血，我沒開GPU啊啊啊啊啊
        * ![](https://i.imgur.com/mYZtf5S.png)
        * 開GPU之後train一次只要48分鐘==
    * 結果好糟歐
        * 用當年專研的model直接train
        * ![](https://i.imgur.com/Y2gUvD0.png)
        * 這...這比亂猜還慘欸
    * 改了一下model後變成0.5626 val_loss了
        * 5層conv(8/16/32/64/128)
        * 200 epoch
        * 好讚
* 20210713
    * 用昨天的model來實測
        * 好...傻眼
        * ![](https://i.imgur.com/7mjGj4w.png)
        * 到底我不配哪裡happy了
        * 什麼歌哪裡sad了...
        * 重train...
        * 多加一層conv(256)
        * 改成300 epoch
    * 一次predict只能取5秒
        * 因為dataset是5秒，所以只能predict 5秒
        * 決定分別在90/120/150秒時取樣5秒鐘
        * pred相加後再取最大值
    * 重新train
        * ![](https://i.imgur.com/UIAYJfw.png)
* 20210714
    * 更換dataset
        * 因為predict出來的結果一直很奇怪，決定換dataset
        * https://www.kaggle.com/imsparsh/4q-audio-emotion-dataset-russell
        * ![](https://i.imgur.com/whKB19Q.png)
        * 凌晨花了很久才弄好圖片
        * 改成一次取10秒，可是弄出來的圖片有很多白色的地方
        * ![](https://i.imgur.com/RTgzR4M.png)
        * 訓練結果很糟，決定用opencv切割掉白色的部分
        * ```python
            img = cv2.imread(img_path)
            crop_img = img[y:y+h, x:x+w]
            cv2.imwrite(img_path,crop_img)
            ```
        * ![](https://i.imgur.com/QXQOII4.png)
        * 可是換完之後還是很糟欸
    * train了很多個版本
        * 換了dataset之後還是超糟
        * 甚至是train的時候就明顯很糟
        * 不知道為甚麼一開始loss都會先上升然後再下降
        * ![](https://i.imgur.com/9ZBNnXj.png)
        * val_loss最低才大概0.9
        * 甚至有出現val_loss比training loss低的奇怪狀況
        * 改用nasnet也沒有甚麼改善，甚至更慘，val_loss都大於1。而且好像有出現overfitting的問題，training acc都0.9，val_acc只有0.3。
        * ![](https://i.imgur.com/erzCuqc.png)

        * 不知道是甚麼問題
        * 明天來看看這個 https://hackmd.io/@gHqlkOFQSJ2sI2HyZmY99Q/Sy2froHpQ?type=view
        * 希望可以趕快結束這個環節...
* 20210715
    * 放棄新dataset了，真的不知道為甚麼弄不好
    * 用nasnet訓練舊data，一樣出現很明顯的overfit
        * 推測應該是因為nasnet太複雜
    * 改用mobilenetv2訓練舊data
        * ![](https://i.imgur.com/D3hYJjD.png)
        * ![](https://i.imgur.com/xxr9URf.png)
        * ![](https://i.imgur.com/r3a7ii7.png)
    * 把song和link輸出到一個json檔，丟到google colab上面跑
    * 選時改選50/80/130
    * 大部分看起來正常
        * 還是有部分歌結果很怪，但似乎真的是那些歌在那些秒數特別怪
            * 彩虹
            * 時光機(剛好選到抒情part)
            * 藉口
            * 陽光宅男(剛好選到"我決定插手你的人生")
        * 有些歌是在其中一個取樣特怪，可是那個怪值太大，導致最後誤判
            * 例如藉口，其中兩個都是sad，但有一個是happy，而且是超級happy，最後就變成happy
            * 陽光宅男，一個超級sad，一個aggresive和一個happy也打不掉
        * 有些歌太短
            * 前傳199
            * 神的孩子都在跳舞208
            * 為什麼(今日的愛情)255
            * 金多蝦274
* 20210716 
    * 手動更改某些真的太詭異的分類
        * 永不失聯的愛sad->romantic
        * 彩虹happy->sad
        * 時光機sad->happy
        * 藉口happy->romantic
        * 倔強live sad->aggressive
        * 因為你所以我sad->aggressive
        * 私奔到月球live sad->happy
        * 笑忘歌live sad->happy
        * 天使sad->romantic
        * 我又初戀了sad->happy
        * 垃圾車sad->romantic
        * 五月天時光機happy->sad
        * 裂縫中的陽光sad->aggressive
        * 小酒窩sad->romantic
        * 天黑請閉眼sad->aggressive
        * 千年以後sad->romantic
    * GUI的排版很詭異
        * 如果先隱藏list，把list叫出來的時候原本的toolbutton會擠成一團
        * 在stackoverflow上問還是沒有人要理我
        * 最後真的搞不定就決定還是讓List一開始就在了
    * 播音樂的時候會卡在while裡面沒辦法接收其他的signal
        * 後來想到的方法是不要用time.sleep(duration)
        * 用一個flag來看是否要跳出while
        * 每次要emit signal前，就先把flag改成False，就可以跳出while接收到signal了
        * 計時的部分另外計
    * 換顏色！
    * 終於完工了！好讚！




        













 




 

 
