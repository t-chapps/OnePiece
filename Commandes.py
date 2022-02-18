from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import ( QGraphicsPixmapItem )
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QLineEdit, QSlider, QPushButton, QVBoxLayout, QApplication, QWidget)
from PyQt5.QtCore import Qt
from PyQt5.QtMultimedia import *
import sys


class Commandes ( QMainWindow ) :
    # Opening Window
    def __init__ ( self ) :
        super().__init__()
        self.setWindowTitle ( "MainWindow" )
        self.setObjectName ( "Parametres" )
        image = '''
        #Parametres {
        background-image: url(./Image/Menu/Parametres.png);
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

        self.Rectangle_1 = QGroupBox()
        self.Rectangle_1.setStyleSheet ( "QTextEdit { background-color: red; }" )

        self.Rectangle_2 = QGroupBox()
        self.Rectangle_2.setStyleSheet ( "QTextEdit { background-color: Black; }" )

        self.Rectangle_3 = QGroupBox()
        self.Rectangle_3.setStyleSheet ( "QTextEdit { background-color: White; }" )

        self.Rectangle_4 = QGroupBox()
        self.Rectangle_4.setStyleSheet ( "QTextEdit { background-color: White; }" )

        self.label_3 = QLabel ( "Command" )
        self.label_3.setStyleSheet ( "QLabel { background-color: rgba(30, 144, 255, 0); color: rgb(0, 0, 0); }" )
        self.label_3.setAlignment ( Qt.AlignCenter )
        self.label_3.setFont ( QFont ( "Algerian ", 100 ) )

        self.label_4 = QLabel ( "" )
        self.label_4.setStyleSheet ( "QLabel { background-color: rgba(30, 144, 255, 0); color: rgb(0, 0, 0); }" )
        self.label_4.setAlignment ( Qt.AlignCenter )
        self.label_4.setFont ( QFont ( "Algerian ", 50 ) )

        self.push_button = QPushButton ( "" )
        self.push_button.clicked.connect ( self.appui_retour )
        self.push_button.setStyleSheet ( "QPushButton { background-color: rgba(0, 0, 0, 0); color: white; }" )
        self.push_button.setIcon ( QIcon ( "./Image/Menu/Back.png" ) )
        self.push_button.setIconSize ( QSize ( 1000, 100 ) )

        self.label_commandes = QLabel ( "" )
        self.label_commandes.setAlignment ( Qt.AlignCenter )
        self.pixmap = QPixmap ( "./Image/Menu/Commandes_jeu.png" )
        self.label_commandes.setPixmap ( self.pixmap )

    def init_layout ( self ):

        self.layout = QHBoxLayout()
        self.centralWidget().setLayout ( self.layout )

        self.layout.addWidget ( self.Rectangle_1 )
        self.layout.addWidget ( self.Rectangle_2 )

        self.layoutgauche = QVBoxLayout()
        self.Rectangle_1.setLayout ( self.layoutgauche )

        self.layoutgauche.addWidget ( self.Rectangle_3 )
        self.layoutgauche.addWidget ( self.Rectangle_4 )

        self.layouthautgauche = QVBoxLayout()
        self.Rectangle_3.setLayout ( self.layouthautgauche )
        self.layouthautgauche.addWidget ( self.label_3 )
        self.layouthautgauche.addWidget ( self.label_4 )

        self.layoutbasgauche = QHBoxLayout()
        self.Rectangle_4.setLayout ( self.layoutbasgauche )
        self.layoutbasgauche.addWidget ( self.push_button )

        self.layoutdroite = QVBoxLayout()
        self.Rectangle_2.setLayout ( self.layoutdroite )
        self.layoutdroite.addWidget ( self.label_commandes )

    def appui_retour ( self ) :
        self.close()
