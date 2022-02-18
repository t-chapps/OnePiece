from Plateau import *
from Joueur import *

class Jeu :

    def __init__ ( self, rows, cols ) :
        self.plateau = Plateau ( rows, cols )
        self.joueur = Joueur ( self.plateau )
        self.nb_lignes = rows
        self.nb_colonnes = cols
        self.niveau = 1

    def jouer ( self, niveau ) :
        self.plateau.debut_partie ( niveau )

    def niveau_suivant ( self ) :
        self.niveau += 1
        self.joueur.case_courante = self.plateau.case_entree
        self.jouer ( self.niveau )
