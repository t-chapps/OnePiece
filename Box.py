from PyQt5.QtWidgets import ( QGraphicsPixmapItem )
from PyQt5.QtGui import QPixmap
import csv

class Box :

    def __init__ ( self, x, y ) :
        self.posX = x
        self.posY = y

    def afficher ( self ) :
        print ( "B", end = "" )

    def get_visual_representation ( self, niveau ) :
        if niveau <= 9 :
            fichier_niveau = csv.reader ( open ( r"./Csv/niveau_{}.csv".format ( niveau ) ) )
            for obstacle in fichier_niveau :
                if obstacle[0] == "Caisse" :
                    box = QPixmap ( obstacle[1] )
                    box = QGraphicsPixmapItem ( box )
                    box.moveBy ( self.posX, self.posY )
                    return box
