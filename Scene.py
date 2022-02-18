from PyQt5.QtCore import ( QLineF, QPointF, QRectF, Qt, QTimer )
from Personnage import *
from Obstacle import *
from Box import *
from Item import *
from Plateau import *
import time

class Scene :

    def __init__ ( self, jeu, niveau, perso ) :
        self.jeu = jeu
        self.perso = perso
        self.plateau = self.jeu.plateau
        self.plateau.debut_partie ( niveau )
        self.init_static_elements()
        self.init_dynamic_elements()

    def init_static_elements ( self ) :
        self.les_murs = []
        for i in range ( len ( self.plateau.inventaire_mur ) ) :
            x,y = self.plateau.inventaire_mur[i]
            self.les_murs.append ( Obstacle ( y*100, x*100 ) )

    def init_dynamic_elements ( self ) :
        self.les_box = []
        self.les_items = []
        self.personnage = Personnage ( self.jeu.joueur, self.perso )
        for i in range ( len ( self.plateau.inventaire_box ) ) :
            self.inventaire_box = sorted ( self.plateau.inventaire_box )
            x,y = self.inventaire_box[i]
            self.les_box.append ( Box ( y*100, x*100 ) )
        for i in range ( len ( self.plateau.inventaire_item ) ) :
            self.inventaire_item = sorted ( self.plateau.inventaire_item )
            x,y = self.inventaire_item[i]
            self.les_items.append ( Item ( y*100, x*100 ) )

    def deplace_perso ( self, x ) :
        self.personnage.deplace ( x )
