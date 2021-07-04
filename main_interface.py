import sys
import play_song
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('This is a <b>QWidget</b> widget')
        nameLabel = QLabel('&Name',self)
        nameLineEdit = QLineEdit(self)
        mainLayout = QGridLayout(self)
        mainLayout.addWidget(nameLabel,0,0)
        mainLayout.addWidget(nameLineEdit,0,1,1,2)
        nameLabel.setBuddy(nameLineEdit)
        # text=QTextEdit(self)
        play = QPushButton('play', self)
        play.setToolTip('This is a <b>QPushButton</b> widget')
        play.resize(play.sizeHint())
        play.clicked.connect(play_song.play_song)
        play.move(50, 50)

        pause = QPushButton('pause', self)
        pause.setToolTip('This is a <b>QPushButton</b> widget')
        pause.resize(pause.sizeHint())
        pause.clicked.connect(play_song.pause())
        pause.move(100, 50)
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')
        self.show()


def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()