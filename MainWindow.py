from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from GraphicsScene import *
from Fin import *
import sys

class MainWindow ( QMainWindow ) :

    def __init__ ( self, niveau, perso ) :
        QWidget.__init__ ( self )
        self.niveau = niveau
        self.perso = perso
        self.sound = QSound ( r"./Musique/niveaux.wav" )
        self.sound.setLoops ( -1 )
        self.sound.play()
        self.setWindowTitle ( "Item Blockade" )
        self.setStyleSheet ( "background : url(./Image/Menu/fond_jeu.png);background-repeat: no-repeat;background-position: center;" )
        self.init_components()
        self.init_scene()
        self.init_layout()
        self.Start()
        self.showFullScreen()

    def init_scene ( self ) :
        self.gscene = GraphicsScene ( self.niveau, self, self.perso )
        self.vue = QGraphicsView ( self.gscene )

    def init_components ( self ) :
        self.setCentralWidget ( QGroupBox() )
        self.count = 540
        self.flag = False
        self.label = QLabel ( self )
        self.label.setGeometry ( 200, 100, 200, 75 )
        self.label.setStyleSheet ( "border : 4px solid black; color : red ;" )
        self.label.setText ( str ( self.count ) )
        self.label.setFont ( QFont ( "ONE PIECE", 50 ) )
        self.label.setAlignment ( Qt.AlignCenter )
        timer = QTimer ( self )
        timer.timeout.connect ( self.showTime )
        timer.start ( 1000 )

    def init_layout ( self ) :
        self.layout = QVBoxLayout()
        self.centralWidget().setLayout ( self.layout )
        self.layout.addWidget ( self.vue )

    def showTime ( self ) :
        if self.flag :
            self.count-= 1
        time = str ( self.count )
        self.label.setText ( time )

    def Start ( self ) :
        self.flag = True

    def fin ( self, dlt ) :
        self.sound.stop()
        self.close()
        if dlt == 1 :
            self.fin = Fin ( dlt )
        else :
            self.fin = Fin ( dlt )
