import mysql.connector
class load_data():
    def __init__(self):
        self.cnx = mysql.connector.connect(user='Adi', password='Adicoco0410',database='song_data')
        self.cursor=self.cnx.cursor()
    def search(self,song):
        query=("SELECT * FROM songlist WHERE song like ")
        query=query+'\'%'+song+'%\''
        print(query)
        self.cursor.execute(query)
        for (song,singer,CD,link) in self.cursor:
            self.Link=link
        return self.Link
if __name__ == '__main__':
    ld=load_data()
    # ld.output_link