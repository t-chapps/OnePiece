from PyQt5.QtWidgets import ( QGraphicsPixmapItem )
from PyQt5.QtGui import QPixmap
import csv

class Obstacle :

    def __init__ ( self, x, y ) :
        self.posX = x
        self.posY = y

    def get_visual_representation ( self, niveau ) :
        fichier_niveau = csv.reader ( open ( r"./Csv/niveau_{}.csv".format ( niveau ) ) )
        for obstacle in fichier_niveau :
            if obstacle[0] == "Obstacle" :
                mur = QPixmap ( obstacle[1] )
                mur = QGraphicsPixmapItem ( mur )
                mur.moveBy ( self.posX, self.posY )
                return mur
