from PyQt5.QtGui import *
from PyQt5.QtMultimedia import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Commandes import *
from Regles import *
from Player import *
import sys


class Regles ( QMainWindow ) :
    # Opening Window
    def __init__ ( self ) :
        super().__init__()
        self.setWindowTitle ( "One Piece Treasure" )
        self.setObjectName ( "Regles" )

        image = '''
        #Regles {
        background-image: url(./Image/Menu/Regles.png);
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

        self.label_1 = QLabel ( "Rules" )
        self.label_1.setStyleSheet ( "color : white ;" )
        self.label_1.setAlignment ( Qt.AlignCenter )
        self.label_1.setFont ( QFont ( "ONE PIECE ", 100 ) )


        self.label_2 = QLabel ( "My treasure? " )
        self.label_2.setStyleSheet ( "color : white ;" )
        self.label_2.setAlignment ( Qt.AlignCenter )
        self.label_2.setFont ( QFont ( "ONE PIECE", 50 ) )
        self.label_2.setStyleSheet ( "background-color: rgba(0, 0, 0, 0); color: white" )

        self.label_3 = QLabel ( "it is there.... somewhere in this world" )
        self.label_3.setStyleSheet ( "color : white ;" )
        self.label_3.setAlignment ( Qt.AlignCenter )
        self.label_3.setFont ( QFont ( "ONE PIECE ", 50 ) )
        self.label_3.setStyleSheet ( "background-color: rgba(0, 0, 0, 0); color: white" )

        self.label_4 = QLabel ( " Find it!" )
        self.label_4.setStyleSheet ( "color : white ;" )
        self.label_4.setAlignment ( Qt.AlignCenter )
        self.label_4.setFont ( QFont ( "ONE PIECE ", 50 ) )
        self.label_4.setStyleSheet ( "background-color: rgba(0, 0, 0, 0); color: white" )

        self.label_5 = QLabel ( "The Last Words of Gol D Rodger King of the Pirates" )
        self.label_5.setStyleSheet ( "color : white ;" )
        self.label_5.setAlignment ( Qt.AlignCenter )
        self.label_5.setFont ( QFont ( "ONE PIECE ", 40 ) )
        self.label_5.setStyleSheet ( "background-color: rgba(0, 0, 0, 0); color: white" )

        self.label_6 = QLabel ( "launched a wave of piracy across the world" )
        self.label_6.setStyleSheet ( "color : white ;" )
        self.label_6.setAlignment ( Qt.AlignCenter )
        self.label_6.setFont ( QFont ( "ONE PIECE ", 40 ) )
        self.label_6.setStyleSheet ( "background-color: rgba(0, 0, 0, 0); color: white" )

        self.label_7 = QLabel ( "Go on an adventure and sail the world's seas" )
        self.label_7.setStyleSheet ( "color : white ;" )
        self.label_7.setAlignment ( Qt.AlignCenter )
        self.label_7.setFont ( QFont ( "ONE PIECE ", 40 ) )
        self.label_7.setStyleSheet ( "background-color: rgba(0, 0, 0, 0); color: white" )

        self.label_8 = QLabel ( "Search for the One Piece and become the King of the Pirates!" )
        self.label_8.setStyleSheet ( "color : white ;" )
        self.label_8.setAlignment ( Qt.AlignCenter )
        self.label_8.setFont ( QFont ( "ONE PIECE ", 40 ) )
        self.label_8.setStyleSheet ( "background-color: rgba(0, 0, 0, 0); color: white" )

        self.label_9 = QLabel ( "A pirate never leaves an island without treasure" )
        self.label_9.setStyleSheet ( "color : white ;" )
        self.label_9.setAlignment ( Qt.AlignCenter )
        self.label_9.setFont ( QFont ( "ONE PIECE ", 40 ) )
        self.label_9.setStyleSheet ( "background-color: rgba(0, 0, 0, 0); color: white" )

        self.label_10 = QLabel ( "The rules are simple:" )
        self.label_10.setStyleSheet ( "color : white ;" )
        self.label_10.setAlignment ( Qt.AlignCenter )
        self.label_10.setFont ( QFont ( "ONE PIECE ", 40 ) )
        self.label_10.setStyleSheet ( "background-color: rgba(0, 0, 0, 0); color: white" )

        self.label_11 = QLabel ( "take the treasures to the boat avoiding obstacles" )
        self.label_11.setStyleSheet ( "color : white ;" )
        self.label_11.setAlignment ( Qt.AlignCenter )
        self.label_11.setFont ( QFont ( "ONE PIECE ", 40 ) )
        self.label_11.setStyleSheet ( "background-color: rgba(0, 0, 0, 0); color: white" )


        self.label_12 = QLabel ( "be smart and strategic." )
        self.label_12.setStyleSheet ( "color : white ;" )
        self.label_12.setAlignment ( Qt.AlignCenter )
        self.label_12.setFont ( QFont ( "ONE PIECE ", 40 ) )
        self.label_12.setStyleSheet ( "background-color: rgba(0, 0, 0, 0); color: white" )


        self.push_button = QPushButton ( "" )
        self.push_button.clicked.connect ( self.appui_retour )
        self.push_button.setStyleSheet ( "QPushButton { background-color: rgba(0, 0, 0, 0); color: white; }" )
        self.push_button.setIcon ( QIcon ( "./Image/Menu/Back.png" ) )
        self.push_button.setIconSize ( QSize ( 1000, 100 ) )

    def init_layout ( self ):
        self.layout = QVBoxLayout()
        self.centralWidget().setLayout ( self.layout )
        self.layout.addWidget ( self.label_1 )
        self.layout.addWidget ( self.label_2 )
        self.layout.addWidget ( self.label_3 )
        self.layout.addWidget ( self.label_4 )
        self.layout.addWidget ( self.label_5 )
        self.layout.addWidget ( self.label_5 )
        self.layout.addWidget ( self.label_6 )
        self.layout.addWidget ( self.label_7 )
        self.layout.addWidget ( self.label_8 )
        self.layout.addWidget ( self.label_9 )
        self.layout.addWidget ( self.label_10 )
        self.layout.addWidget ( self.label_11 )
        self.layout.addWidget ( self.label_12 )
        self.layout.addWidget ( self.push_button )

    def appui_retour ( self ) :
        self.close()
