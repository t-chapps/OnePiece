char_mur = u'\u2588'

from Box import *
from Item import *

class Case :

    def __init__ ( self, i, j ) :
        self.posI = i
        self.posJ = j
        self.mur = False
        self.box = False
        self.item = False

    def afficher_mur ( self ) :
        if self.mur == True :
            print ( char_mur, end = "")

    def afficher_box ( self, i, j ) :
        Box ( i, j ).afficher()

    def afficher_item ( self, i, j ) :
        Item ( i, j ).afficher()
