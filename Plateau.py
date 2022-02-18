# Le caractère pour faire un mur
char_mur = u'\u2588'

from Case import *
from Box import *
from Item import *
import csv

class Plateau :

    def __init__ ( self, rows, cols ) :
        self.nb_lignes = rows
        self.nb_colonnes = cols
        self.inventaire_mur = []
        self.inventaire_box = []
        self.inventaire_item = []

        self.plateau = [0] * self.nb_lignes
        for i in range ( len ( self.plateau ) ) :
            self.plateau[i] = [0] * self.nb_colonnes
        for i in range ( self.nb_lignes ) :
            for j in range ( self.nb_colonnes ) :
                self.plateau[i][j] = Case ( i, j )

        self.case_entree = self.plateau[1][1]
        self.case_sortie = self.plateau[4][12]

    def affiche_plateau ( self, joueur ) :
        for i in range ( self.nb_lignes ) :
            for j in range ( self.nb_colonnes ) :
                if self.plateau[i][j].mur == True :
                    self.plateau[i][j].afficher_mur()
                elif self.plateau[i][j].box == True :
                    self.plateau[i][j].afficher_box ( i, j )
                elif self.plateau[i][j].item == True :
                    self.plateau[i][j].afficher_item ( i, j )
                elif self.plateau[i][j] == self.case_entree :
                    print ( "E", end = "" )
                elif self.plateau[i][j] == self.case_sortie :
                    print ( "S", end = "" )
                elif self.plateau[i][j].posI == joueur.posI and self.plateau[i][j].posJ == joueur.posJ :
                    print ( "P", end = "" )
                else :
                    print ( " ", end = "" )
            print()

    def debut_partie ( self, niveau ) :
        self.definir_niveau ( niveau )
        self.inventaire_mur.clear()
        self.inventaire_box.clear()
        self.inventaire_item.clear()
        for i in range ( self.nb_lignes ) :
            for j in range ( self.nb_colonnes ) :
                if self.plateau[i][j].mur == True :
                    self.inventaire_mur.append ( ( i, j ) )
                elif self.plateau[i][j].box == True :
                    self.inventaire_box.append ( ( i, j ) )
                elif self.plateau[i][j].item == True :
                    self.inventaire_item.append ( ( i, j ) )

    def definir_cadre ( self ) :
        for haut in self.plateau[0] :
            haut.mur = True
        for bas in self.plateau[self.nb_lignes-1] :
            bas.mur = True
        for droite in self.plateau :
            droite[self.nb_colonnes-1].mur = True
        for gauche in self.plateau :
            gauche[0].mur = True

    def clear_plateau ( self ) :
        for i in range ( len ( self.plateau ) ) :
            for j in range ( len ( self.plateau[0] ) ) :
                self.plateau[i][j].mur = False
                self.plateau[i][j].box = False
                self.plateau[i][j].item = False

    def definir_niveau ( self, niveau ) :
        self.clear_plateau()
        self.definir_cadre()
        level = csv.reader ( open ( r"./Csv/niveau_{}.csv".format ( niveau ) ) )
        for obstacle in level :
            if obstacle[0] == "Mur" :
                self.plateau[ int ( obstacle[1] ) ][ int ( obstacle[2] ) ].mur = True
            elif obstacle[0] == "Box" :
                self.plateau[ int ( obstacle[1] ) ][ int ( obstacle[2] ) ].box = True
            elif obstacle[0] == "Item" :
                self.plateau[ int ( obstacle[1] ) ][ int ( obstacle[2] ) ].item = True
