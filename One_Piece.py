from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from Menu import *
import time
import sys

class One_Piece ( QMainWindow ) :

    def __init__ ( self ) :
        super().__init__()
        self.video = QVideoWidget()
        self.init_components()
        self.init_layout()
        self.showFullScreen()

    def init_components ( self ) :
        self.setCentralWidget ( QGroupBox() )
        self.push_button1 = QPushButton ( "Access to the game" )
        self.push_button1.clicked.connect ( self.appui_passer )
        self.push_button1.setFont ( QFont ( "ONE PIECE", 50 ) )
        self.push_button1.setStyleSheet ( "QPushButton { background-color: rgb(0, 0, 0); color: white; }" )

        self.player = QMediaPlayer()
        self.player.setVideoOutput ( self.video )
        self.player.setMedia ( QMediaContent ( QUrl.fromLocalFile ( "./Video/debut.mpeg" ) ) )
        self.video.show()

        self.timer = QTimer()
        self.timer.timeout.connect ( self.appui_passer )
        self.timer.start ( 31111 )
        self.player.play()

    def init_layout ( self ):
        self.layout = QVBoxLayout()
        self.centralWidget().setLayout ( self.layout )
        self.layout.addWidget ( self.video )
        self.layout.addWidget ( self.push_button1 )

    def appui_passer ( self ) :
        self.timer.stop()
        self.player.stop()
        self.close()
        self.menu = Menu()

if __name__ == '__main__':
    app = QApplication ( sys.argv )
    OP = One_Piece()
    sys.exit ( app.exec_() )
