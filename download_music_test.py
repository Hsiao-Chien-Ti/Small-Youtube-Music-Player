import pafy 
url = "https://www.youtube.com/watch?v=nNEw8BtKU-E"
video = pafy.new(url)
  
bestaudio = video.getbestaudio()
bestaudio.download()