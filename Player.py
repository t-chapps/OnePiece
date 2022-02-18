from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtCore import *
from MainWindow import *
import sys


class Player ( QMainWindow ) :
    # Opening Window
    def __init__ ( self ) :
        super().__init__()
        self.setWindowTitle ( "Player" )
        self.setObjectName ( "Player" )
        self.perso = "Luffy"
        self.sound = QSound ( r"./Musique/Player.wav" )
        self.sound.setLoops ( -1 )
        self.sound.play()
        image = '''
        #Player {
        background-image: url(./Image/Menu/Player.png);
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

        self.haut = QGroupBox ( "" )
        self.haut.setStyleSheet ( "QGroupBox { background-color: rgba ( 0, 0, 0, 0) ;  }")
        self.milieu = QGroupBox ( "" )
        self.milieu.setStyleSheet ( "QGroupBox { background-color: rgba ( 0, 0, 0, 0) ;  }" )
        self.bas = QGroupBox ( "" )
        self.bas.setStyleSheet ( "QGroupBox { background-color: rgba ( 0, 0, 0, 0) ;  }" )

        self.label_1 = QLabel ( "Choose your player" )
        self.label_1.setStyleSheet ( "QLabel {  background-color: rgba(30, 144, 255, 0); color: white; }" )
        self.label_1.setAlignment ( Qt.AlignCenter )
        self.label_1.setFont ( QFont ( "ONE PIECE", 100 ) )

        self.label_2 = QLabel ( "" )
        self.label_2.setStyleSheet ( "QLabel { background-color: rgba(0, 0, 0, 0); color: rgb(0, 0, 0); }" )
        self.label_2.setAlignment ( Qt.AlignCenter )
        self.label_2.setFont ( QFont ( "Algerian ", 50 ) )

        self.label_3 = QLabel ( "" )
        self.label_3.setStyleSheet ( "QLabel { background-color: rgba(0, 0, 0, 0); color: rgb(0, 0, 0); }" )
        self.label_3.setAlignment ( Qt.AlignCenter )
        self.label_3.setFont ( QFont ( "Algerian ", 50 ) )

        self.label_4 = QLabel ( "" )
        self.label_4.setStyleSheet ( "QLabel { background-color: rgba(0, 0, 0, 0); color: rgb(0, 0, 0); }" )
        self.label_4.setAlignment ( Qt.AlignCenter )
        self.label_4.setFont ( QFont ( "Algerian ", 50 ) )

        self.label_5 = QLabel ( "" )
        self.label_5.setStyleSheet ( "QLabel { background-color: rgba(0, 0, 0, 0); color: rgb(0, 0, 0); }" )
        self.label_5.setAlignment ( Qt.AlignCenter )
        self.label_5.setFont ( QFont ( "Algerian ", 50 ) )

        self.push_button_luffy = QPushButton ( "" )
        self.push_button_luffy.clicked.connect ( self.select_perso_luffy )
        self.push_button_luffy.setStyleSheet ( "QPushButton { background-color: rgb(255, 255, 255); color: white; }" )
        self.push_button_luffy.setIcon ( QIcon ( "./Image/Personnage/Luffy/Luffy.png" ) )
        self.push_button_luffy.setIconSize ( QSize ( 1000, 1000 ) )

        self.push_button_zoro = QPushButton ( "" )
        self.push_button_zoro.clicked.connect ( self.select_perso_zoro )
        self.push_button_zoro.setStyleSheet ( "QPushButton { background-color: rgb(255, 255, 255); color: white; }" )
        self.push_button_zoro.setIcon ( QIcon ( "./Image/Personnage/Zoro/Zoro.png" ) )
        self.push_button_zoro.setIconSize ( QSize ( 1000, 1000 ) )

        self.push_button_sanji = QPushButton ( "" )
        self.push_button_sanji.clicked.connect ( self.select_perso_sanji )
        self.push_button_sanji.setStyleSheet ( "QPushButton { background-color: rgb(255, 255, 255); color: white; }" )
        self.push_button_sanji.setIcon ( QIcon ( "./Image/Personnage/Sanji/Sanji.png" ) )
        self.push_button_sanji.setIconSize ( QSize ( 1000, 1000 ) )

        self.push_button_nami = QPushButton ( "" )
        self.push_button_nami.clicked.connect ( self.select_perso_nami )
        self.push_button_nami.setStyleSheet ( "QPushButton { background-color: rgb(255, 255, 255); color: white; }" )
        self.push_button_nami.setIcon ( QIcon ( "./Image/Personnage/Nami/Nami.png" ) )
        self.push_button_nami.setIconSize ( QSize ( 1000, 1000 ) )

        self.push_button_usopp = QPushButton ( "" )
        self.push_button_usopp.clicked.connect ( self.select_perso_usopp )
        self.push_button_usopp.setStyleSheet ( "QPushButton { background-color: rgb(255, 255, 255); color: white; }" )
        self.push_button_usopp.setIcon ( QIcon ( "./Image/Personnage/Usopp/Ussop.png" ) )
        self.push_button_usopp.setIconSize ( QSize ( 1000, 1000 ) )

        self.push_button_robin = QPushButton ( "" )
        self.push_button_robin.clicked.connect ( self.select_perso_robin )
        self.push_button_robin.setStyleSheet ( "QPushButton { background-color: rgb(255, 255, 255); color: white; }" )
        self.push_button_robin.setIcon ( QIcon ( "./Image/Personnage/Robin/Robin.png" ) )
        self.push_button_robin.setIconSize ( QSize ( 1000, 1000 ) )

        self.push_button_chopper = QPushButton ( "" )
        self.push_button_chopper.clicked.connect ( self.select_perso_chopper )
        self.push_button_chopper.setStyleSheet ( "QPushButton { background-color: rgb(255, 255, 255); color: white; }" )
        self.push_button_chopper.setIcon ( QIcon ( "./Image/Personnage/Chopper/Chopper.png" ) )
        self.push_button_chopper.setIconSize ( QSize ( 1000, 1000 ) )

        self.push_button_franky = QPushButton ( "" )
        self.push_button_franky.clicked.connect ( self.select_perso_franky )
        self.push_button_franky.setStyleSheet ( "QPushButton { background-color: rgb(255, 255, 255); color: white; }" )
        self.push_button_franky.setIcon ( QIcon ( "./Image/Personnage/Franky/Franky.png" ) )
        self.push_button_franky.setIconSize ( QSize ( 1000, 1000 ) )

        self.push_button_brook = QPushButton ( "" )
        self.push_button_brook.clicked.connect ( self.select_perso_brook )
        self.push_button_brook.setStyleSheet ( "QPushButton { background-color: rgb(255, 255, 255); color: white; }" )
        self.push_button_brook.setIcon ( QIcon ( "./Image/Personnage/Brook/Brook.png" ) )
        self.push_button_brook.setIconSize ( QSize ( 1000, 1000 ) )

        self.push_button_law = QPushButton ( "" )
        self.push_button_law.clicked.connect ( self.select_perso_law )
        self.push_button_law.setStyleSheet ( "QPushButton { background-color: rgb(255, 255, 255); color: white; }" )
        self.push_button_law.setIcon ( QIcon ( "./Image/Personnage/Law/Law.png" ) )
        self.push_button_law.setIconSize ( QSize ( 1000, 1000 ) )

        self.push_button_ace = QPushButton ( "" )
        self.push_button_ace.clicked.connect ( self.select_perso_ace )
        self.push_button_ace.setStyleSheet ( "QPushButton { background-color: rgb(255, 255, 255); color: white; }" )
        self.push_button_ace.setIcon ( QIcon ( "./Image/Personnage/Ace/Ace.png" ) )
        self.push_button_ace.setIconSize ( QSize ( 1000, 1000 ) )

        self.push_button_doflamingo = QPushButton ( "" )
        self.push_button_doflamingo.clicked.connect ( self.select_perso_doflamingo )
        self.push_button_doflamingo.setStyleSheet ( "QPushButton { background-color: rgb(255, 255, 255); color: white; }" )
        self.push_button_doflamingo.setIcon ( QIcon ( "./Image/Personnage/Doflamingo/Doflamingo.png" ) )
        self.push_button_doflamingo.setIconSize ( QSize ( 1000, 1000 ) )

        self.push_button_boa = QPushButton ( "" )
        self.push_button_boa.clicked.connect ( self.select_perso_boa )
        self.push_button_boa.setStyleSheet ( "QPushButton { background-color: rgb(255, 255, 255); color: white; }" )
        self.push_button_boa.setIcon ( QIcon ( "./Image/Personnage/Boa/Boa.png" ) )
        self.push_button_boa.setIconSize ( QSize ( 1000, 1000 ) )

        self.push_button_sabo = QPushButton ( "" )
        self.push_button_sabo.clicked.connect ( self.select_perso_sabo )
        self.push_button_sabo.setStyleSheet ( "QPushButton { background-color: rgb(255, 255, 255); color: white; }" )
        self.push_button_sabo.setIcon ( QIcon ( "./Image/Personnage/Sabo/Sabo.png" ) )
        self.push_button_sabo.setIconSize ( QSize ( 1000, 1000 ) )

        self.push_button_play = QPushButton ( "Play" )
        self.push_button_play.setFont ( QFont ( "ONE PIECE", 100 ) )
        self.push_button_play.clicked.connect ( self.appui_jouer )
        self.push_button_play.setStyleSheet ( "QPushButton { background-color: rgba(0, 0, 0, 0); color: white; }" )

    def init_layout ( self ):
        self.layout = QVBoxLayout()
        self.centralWidget().setLayout ( self.layout )

        self.layout.addWidget ( self.haut )
        self.layout.addWidget ( self.milieu )
        self.layout.addWidget ( self.bas )

        self.layout_haut = QVBoxLayout()
        self.haut.setLayout ( self.layout_haut )

        self.layout_haut.addWidget ( self.label_2 )
        self.layout_haut.addWidget ( self.label_1 )
        self.layout_haut.addWidget ( self.label_3 )

        self.layout_milieu = QHBoxLayout()
        self.milieu.setLayout ( self.layout_milieu )

        self.layout_milieu.addWidget ( self.push_button_luffy )
        self.layout_milieu.addWidget ( self.push_button_zoro )
        self.layout_milieu.addWidget ( self.push_button_sanji )
        self.layout_milieu.addWidget ( self.push_button_nami )
        self.layout_milieu.addWidget ( self.push_button_usopp )
        self.layout_milieu.addWidget ( self.push_button_robin )
        self.layout_milieu.addWidget ( self.push_button_chopper )
        self.layout_milieu.addWidget ( self.push_button_franky )
        self.layout_milieu.addWidget ( self.push_button_brook )
        self.layout_milieu.addWidget ( self.push_button_law )
        self.layout_milieu.addWidget ( self.push_button_ace )
        self.layout_milieu.addWidget ( self.push_button_doflamingo )
        self.layout_milieu.addWidget ( self.push_button_boa )
        self.layout_milieu.addWidget ( self.push_button_sabo )

        self.layout_bas = QVBoxLayout()
        self.bas.setLayout ( self.layout_bas )

        self.layout_bas.addWidget ( self.label_4 )
        self.layout_bas.addWidget ( self.push_button_play )
        self.layout_bas.addWidget ( self.label_5 )

    def appui_jouer ( self ) :
        self.sound.stop()
        self.close()
        self.main_window = MainWindow ( 1, self.perso )

    def select_perso_luffy ( self ) :
        self.perso = "Luffy"
        return self.perso

    def select_perso_zoro ( self ) :
        self.perso = "Zoro"
        return self.perso

    def select_perso_sanji ( self ) :
        self.perso = "Sanji"
        return self.perso

    def select_perso_nami ( self ) :
        self.perso = "Nami"
        return self.perso

    def select_perso_usopp ( self ) :
        self.perso = "Usopp"
        return self.perso

    def select_perso_robin ( self ) :
        self.perso = "Robin"
        return self.perso

    def select_perso_chopper ( self ) :
        self.perso = "Chopper"
        return self.perso

    def select_perso_franky ( self ) :
        self.perso = "Franky"
        return self.perso

    def select_perso_brook ( self ) :
        self.perso = "Brook"
        return self.perso

    def select_perso_law ( self ) :
        self.perso = "Law"
        return self.perso

    def select_perso_ace ( self ) :
        self.perso = "Ace"
        return self.perso

    def select_perso_doflamingo ( self ) :
        self.perso = "Doflamingo"
        return self.perso

    def select_perso_boa ( self ) :
        self.perso = "Boa"
        return self.perso

    def select_perso_sabo ( self ) :
        self.perso = "Sabo"
        return self.perso
