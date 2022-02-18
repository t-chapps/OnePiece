from Joueur import *
from PyQt5.QtWidgets import ( QGraphicsEllipseItem )

class Personnage :

    def __init__ ( self, j, perso ) :
        self.joueur = j
        self.taille = 50
        self.perso = perso

    def deplace ( self, x ) :
        if x == 1 :
            self.joueur.pousse_monter()
        elif x == 2 :
            self.joueur.pousse_gauche()
        elif x == 3 :
            self.joueur.pousse_descendre()
        elif x == 4 :
            self.joueur.pousse_droite()
        elif x == 5 :
            self.joueur.tire_monter()
        elif x == 6 :
            self.joueur.tire_gauche()
        elif x == 7 :
            self.joueur.tire_descendre()
        elif x == 8 :
            self.joueur.tire_droite()
        else :
            None

    def get_visual_representation ( self, position ) :
        x = self.joueur.posJ*100
        y = self.joueur.posI*100
        fichier_perso = csv.reader ( open ( r"./Csv/Perso_{}.csv".format ( self.perso ) ) )
        for image in fichier_perso :
            if self.joueur.deplacement == 0 :
                if position == 1 :
                    if image[0] == "{}_pousser_dos".format ( self.perso ) :
                        perso =  QGraphicsPixmapItem ( QPixmap ( image[1] ) )
                        perso.moveBy ( x, y )
                        return perso
                elif position == 2 :
                    if image[0] == "{}_pousser_gauche".format ( self.perso ) :
                        perso =  QGraphicsPixmapItem ( QPixmap ( image[1] ) )
                        perso.moveBy ( x, y )
                        return perso
                elif position == 3 :
                    if image[0] == "{}_pousser_face".format ( self.perso ) :
                        perso =  QGraphicsPixmapItem ( QPixmap ( image[1] ) )
                        perso.moveBy ( x, y )
                        return perso
                elif position == 4 :
                    if image[0] == "{}_pousser_droite".format ( self.perso ) :
                        perso =  QGraphicsPixmapItem ( QPixmap ( image[1] ) )
                        perso.moveBy ( x, y )
                        return perso
                elif position == 5 :
                    if image[0] == "{}_tirer_face".format ( self.perso ) :
                        perso =  QGraphicsPixmapItem ( QPixmap ( image[1] ) )
                        perso.moveBy ( x, y )
                        return perso
                elif position == 6 :
                    if image[0] == "{}_tirer_gauche".format ( self.perso ) :
                        perso =  QGraphicsPixmapItem ( QPixmap ( image[1] ) )
                        perso.moveBy ( x, y )
                        return perso
                elif position == 7 :
                    if image[0] == "{}_tirer_dos".format ( self.perso ) :
                        perso =  QGraphicsPixmapItem ( QPixmap ( image[1] ) )
                        perso.moveBy ( x, y )
                        return perso
                elif position == 8 :
                    if image[0] == "{}_tirer_droite".format ( self.perso ) :
                        perso =  QGraphicsPixmapItem ( QPixmap ( image[1] ) )
                        perso.moveBy ( x, y )
                        return perso
                else :
                    if image[0] == "{}_arret".format ( self.perso ) :
                        perso =  QGraphicsPixmapItem ( QPixmap ( image[1] ) )
                        perso.moveBy ( x, y )
                        return perso

            elif self.joueur.deplacement == 1 :
                if position == 1 :
                    if image[0] == "{}_dos".format ( self.perso ) :
                        perso =  QGraphicsPixmapItem ( QPixmap ( image[1] ) )
                        perso.moveBy ( x, y )
                        return perso
                elif position == 2 :
                    if image[0] == "{}_gauche".format ( self.perso ) :
                        perso =  QGraphicsPixmapItem ( QPixmap ( image[1] ) )
                        perso.moveBy ( x, y )
                        return perso
                elif position == 3 :
                    if image[0] == "{}_face".format ( self.perso ) :
                        perso =  QGraphicsPixmapItem ( QPixmap ( image[1] ) )
                        perso.moveBy ( x, y )
                        return perso
                elif position == 4 :
                    if image[0] == "{}_droite".format ( self.perso ) :
                        perso =  QGraphicsPixmapItem ( QPixmap ( image[1] ) )
                        perso.moveBy ( x, y )
                        return perso
                else :
                    if image[0] == "{}_arret".format ( self.perso ) :
                        perso =  QGraphicsPixmapItem ( QPixmap ( image[1] ) )
                        perso.moveBy ( x, y )
                        return perso
