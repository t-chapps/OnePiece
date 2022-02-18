from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtCore import *
from Menu import *
import sys


class Fin ( QMainWindow ) :
    # Opening Window
    def __init__ ( self, dlt ) :
        super().__init__()
        self.dlt = dlt
        self.setWindowTitle ( "Fin" )
        self.setObjectName ( "Fin" )
        self.sound = QSound ( r"./Musique/fin.wav" )
        self.sound.setLoops ( -1 )
        self.sound.play()
        image = '''
        #Fin {
        background-image: url(./Image/Menu/Fin.png);
        background-repeat: no-repeat;
        background-position: center;
        }
        '''
        self.init_components()
        self.init_layout()
        self.setStyleSheet ( image )
        self.showFullScreen()


    def init_components ( self ) :
        # Create widget
        self.setCentralWidget ( QGroupBox() )

        self.label_1 = QLabel ( "Copyrights" )
        self.label_1.setStyleSheet ( "QLabel {  background-color: rgba(30, 144, 255, 0); color: white; }" )
        self.label_1.setAlignment ( Qt.AlignCenter )
        self.label_1.setFont ( QFont ( "ONE PIECE", 100 ) )

        self.label_2 = QLabel ( "Game Developer :  Thomas" )
        self.label_2.setStyleSheet ( "QLabel { background-color: rgba(30, 144, 255, 0); color: white; }" )
        self.label_2.setAlignment ( Qt.AlignCenter )
        self.label_2.setFont ( QFont ( "ONE PIECE", 35 ) )

        self.label_3 = QLabel ( "Graphics & Sound : Baptiste" )
        self.label_3.setStyleSheet ( "QLabel { background-color: rgba(30, 144, 255, 0); color: white; }" )
        self.label_3.setAlignment ( Qt.AlignCenter )
        self.label_3.setFont ( QFont ( "ONE PIECE", 35 ) )

        self.label_4 = QLabel ( "Level Architect : Annis" )
        self.label_4.setStyleSheet ( "QLabel { background-color: rgba(30, 144, 255, 0); color: white; }" )
        self.label_4.setAlignment ( Qt.AlignCenter )
        self.label_4.setFont ( QFont ( "ONE PIECE", 35 ) )

        self.label_5 = QLabel ( " " )
        self.label_5.setStyleSheet ( "QLabel { background-color: rgba(30, 144, 255, 0); color: white; }" )
        self.label_5.setAlignment ( Qt.AlignCenter )
        self.label_5.setFont ( QFont ( "ONE PIECE", 35 ) )

        self.push_button1 = QPushButton ( "" )
        self.push_button1.clicked.connect ( self.appui_quitter )
        self.push_button1.setStyleSheet ( "QPushButton { background-color: rgba(0, 0, 0, 0); color: white; }" )
        self.push_button1.setIcon ( QIcon ( "./Image/Menu/Leave.png" ) )
        self.push_button1.setIconSize ( QSize ( 1000, 100 ) )

        self.label_defaite = QLabel ( "You loose, you can't be the king of pirates !" )
        self.label_defaite.setStyleSheet ( "QLabel { background-color: rgba(30, 144, 255, 0); color: white; }" )
        self.label_defaite.setAlignment ( Qt.AlignCenter )
        self.label_defaite.setFont ( QFont ( "ONE PIECE", 50 ) )

        self.label_victoire = QLabel ( "You win, you are ready to find the One Piece !" )
        self.label_victoire.setStyleSheet ( "QLabel { background-color: rgba(30, 144, 255, 0); color: white; }" )
        self.label_victoire.setAlignment ( Qt.AlignCenter )
        self.label_victoire.setFont ( QFont ( "ONE PIECE", 50 ) )

    def init_layout ( self ):
        self.layout = QVBoxLayout()
        self.centralWidget().setLayout ( self.layout )
        self.layout.addWidget ( self.label_1 )
        if self.dlt == 1 :
            self.layout.addWidget ( self.label_defaite )
        else :
            self.layout.addWidget ( self.label_victoire )
        self.layout.addWidget ( self.label_2 )
        self.layout.addWidget ( self.label_3 )
        self.layout.addWidget ( self.label_4 )
        self.layout.addWidget ( self.label_5 )
        self.layout.addWidget ( self.push_button1 )

    def appui_quitter ( self ) :
        self.close()
