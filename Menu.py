from PyQt5.QtGui import *
from PyQt5.QtMultimedia import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Commandes import *
from Regles import *
from Player import *
import sys

class Menu ( QMainWindow ) :
    # Opening Window
    def __init__ ( self ) :
        super().__init__()
        self.setWindowTitle ( "One Piece Treasure" )
        self.setObjectName ( "Menu" )
        self.sound = QSound ( r"./Musique/menu.wav" )
        self.sound.setLoops ( -1 )
        self.sound.play ()
        image = '''
        #Menu {
        background-image: url(./Image/Menu/Menu.png);
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

        self.vide = QLabel ( " " )

        self.push_button = QPushButton ( "" )
        self.push_button.clicked.connect ( self.appui_jouer )
        self.push_button1 = QPushButton ( "" )
        self.push_button1.clicked.connect ( self.appui_regles )
        self.push_button2 = QPushButton ( "" )
        self.push_button2.clicked.connect ( self.appui_commandes )
        self.push_button3 = QPushButton ( "" )
        self.push_button3.clicked.connect ( self.appui_quitter )

        self.push_button.setStyleSheet ( "QPushButton { background-color: rgba(0, 0, 0, 0); color: white; }" )
        self.push_button.setIcon ( QIcon ( "./Image/Menu/Play.png" ) )
        self.push_button.setIconSize ( QSize ( 1000, 100 ) )
        self.push_button1.setStyleSheet ( "QPushButton { background-color: rgba(0, 0, 0, 0); color: white; }" )
        self.push_button1.setIcon ( QIcon ( "./Image/Menu/Rules.png" ) )
        self.push_button1.setIconSize ( QSize ( 1000, 100 ) )
        self.push_button2.setStyleSheet ( "QPushButton { background-color: rgba(0, 0, 0, 0); color: white; }" )
        self.push_button2.setIcon ( QIcon ( "./Image/Menu/Commandes.png" ) )
        self.push_button2.setIconSize ( QSize ( 1000, 100 ) )
        self.push_button3.setStyleSheet ( "QPushButton { background-color: rgba(0, 0, 0, 0); color: white; }" )
        self.push_button3.setIcon ( QIcon ( "./Image/Menu/Leave.png" ) )
        self.push_button3.setIconSize ( QSize ( 1000, 100 ) )

    def init_layout ( self ):
        self.layout = QGridLayout()
        self.centralWidget().setLayout ( self.layout )
        self.layout.addWidget ( self.vide )

        self.layout.addWidget ( self.vide, 0, 0 )
        self.layout.addWidget ( self.push_button, 1, 0 )
        self.layout.addWidget ( self.push_button1, 2, 0 )
        self.layout.addWidget ( self.vide, 0, 1 )
        self.layout.addWidget ( self.push_button2, 1, 1 )
        self.layout.addWidget ( self.push_button3, 2, 1 )

    def appui_jouer ( self ) :
        self.sound.stop()
        self.close()
        self.player = Player()

    def appui_regles ( self ) :
        self.regles = Regles()

    def appui_commandes ( self ) :
        self.commandes = Commandes()

    def appui_quitter ( self ) :
        self.close()
