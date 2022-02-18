from PyQt5.QtWidgets import ( QGraphicsPixmapItem )
from PyQt5.QtGui import QPixmap
import csv

class Item :

    def __init__ ( self, x, y ) :
        self.posX = x
        self.posY = y

    def afficher ( self ) :
        print ( "I", end = "" )

    def get_visual_representation ( self, niveau ) :
        if niveau <= 9 :
            fichier_niveau = csv.reader ( open ( r"./Csv/niveau_{}.csv".format ( niveau ) ) )
            for obstacle in fichier_niveau :
                if obstacle[0] == "Coffre" :
                    item = QPixmap ( obstacle[1] )
                    item = QGraphicsPixmapItem ( item )
                    item.moveBy ( self.posX, self.posY )
                    return item
