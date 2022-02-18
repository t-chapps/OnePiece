from Scene import *
from Jeu import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PIL import Image

class GraphicsScene ( QGraphicsScene ) :

    def __init__ ( self, niveau, mainwindow, perso ) :
        QGraphicsScene.__init__ ( self )
        self.mainwindow = mainwindow
        self.position = 0
        self.niveau = niveau
        self.perso = perso
        rows = 8
        cols = 14
        self.jeu = Jeu ( rows, cols )
        self.plateau = self.jeu.plateau
        self.scene = Scene ( self.jeu, self.niveau, self.perso )
        self.init_static_elements()
        self.init_dynamic_elements()
        self.init_timer()

    def init_timer ( self ) :
        self.timer = QTimer()
        self.timer.setInterval ( int ( 1000 / 60 ) )
        self.timer.timeout.connect ( self.reset_dynamic_elements )
        self.timer.start()

    def init_static_elements ( self ) :
        fichier_niveau = csv.reader ( open ( r"./Csv/niveau_{}.csv".format ( self.niveau ) ) )
        for image in fichier_niveau :
            if image[0] == "Background" :
                self.background = QGraphicsPixmapItem ( QPixmap ( image[1] ) )
        for i in range ( len ( self.scene.les_murs ) ) :
            self.addItem ( self.scene.les_murs[i].get_visual_representation ( self.niveau ) )
        self.addItem ( self.background )

    def init_dynamic_elements ( self ) :
        self.list_fourre_tout = []

        for i in range ( len ( self.scene.les_box ) ) :
            self.list_fourre_tout.append ( ( self.scene.inventaire_box[i], "Box", self.scene.les_box[i].get_visual_representation ( self.niveau ) ) )
        for i in range ( len ( self.scene.les_items ) ) :
            self.list_fourre_tout.append ( ( self.scene.inventaire_item[i], "Item", self.scene.les_items[i].get_visual_representation ( self.niveau )) )
        self.list_fourre_tout.append ( ( ( self.jeu.joueur.posI, self.jeu.joueur.posJ ), "Perso", self.scene.personnage.get_visual_representation ( self.position ) ) )

        self.fichier_niveau = csv.reader ( open ( r"./Csv/niveau_{}.csv".format ( self.niveau ) ) )
        for image in self.fichier_niveau :
            if image[0] == "Element_1" :
                element_1 = Image.open ( image[1] )
                x,y = element_1.size
                self.element_1 = QGraphicsPixmapItem ( QPixmap ( image[1] ) )
                self.element_1.setPos ( int ( image[2] ), int ( image[3] ) )
                self.list_fourre_tout.append ( ( ( ( int ( image[3] ) + y ) / 100 - 1, int ( image[2] ) / 100 ), "Element_1", self.element_1 ) )
            elif image[0] == "Element_2" :
                element_2 = Image.open ( image[1] )
                x,y = element_2.size
                self.element_2 = QGraphicsPixmapItem ( QPixmap ( image[1] ) )
                self.element_2.setPos ( int ( image[2] ), int ( image[3] ) )
                self.list_fourre_tout.append ( ( ( ( int ( image[3] ) + y ) / 100 - 1, int ( image[2] ) / 100 ), "Element_2", self.element_2 ) )
            elif image[0] == "Element_3" :
                element_3 = Image.open ( image[1] )
                x,y = element_3.size
                self.element_3 = QGraphicsPixmapItem ( QPixmap ( image[1] ) )
                self.element_3.setPos ( int ( image[2] ), int ( image[3] ) )
                self.list_fourre_tout.append ( ( ( ( int ( image[3] ) + y ) / 100 - 1, int ( image[2] ) / 100 ), "Element_3", self.element_3 ) )
            elif image[0] == "Element_4" :
                element_4 = Image.open ( image[1] )
                x,y = element_4.size
                self.element_4 = QGraphicsPixmapItem ( QPixmap ( image[1] ) )
                self.element_4.setPos ( int ( image[2] ), int ( image[3] ) )
                self.list_fourre_tout.append ( ( ( ( int ( image[3] ) + y ) / 100 - 1, int ( image[2] ) / 100 ), "Element_4", self.element_4 ) )
            elif image[0] == "Element_5" :
                element_5 = Image.open ( image[1] )
                x,y = element_5.size
                self.element_5 = QGraphicsPixmapItem ( QPixmap ( image[1] ) )
                self.element_5.setPos ( int ( image[2] ), int ( image[3] ) )
                self.list_fourre_tout.append ( ( ( ( int ( image[3] ) + y ) / 100 - 1, int ( image[2] ) / 100 ), "Element_5", self.element_5 ) )
            elif image[0] == "Element_6" :
                element_6 = Image.open ( image[1] )
                x,y = element_6.size
                self.element_6 = QGraphicsPixmapItem ( QPixmap ( image[1] ) )
                self.element_6.setPos ( int ( image[2] ), int ( image[3] ) )
                self.list_fourre_tout.append ( ( ( ( int ( image[3] ) + y ) / 100 - 1, int ( image[2] ) / 100 ), "Element_6", self.element_6 ) )
            elif image[0] == "Element_7" :
                element_7 = Image.open ( image[1] )
                x,y = element_7.size
                self.element_7 = QGraphicsPixmapItem ( QPixmap ( image[1] ) )
                self.element_7.setPos ( int ( image[2] ), int ( image[3] ) )
                self.list_fourre_tout.append ( ( ( ( int ( image[3] ) + y ) / 100 - 1, int ( image[2] ) / 100 ), "Element_7", self.element_7 ) )
            elif image[0] == "Element_8" :
                element_8 = Image.open ( image[1] )
                x,y = element_8.size
                self.element_8 = QGraphicsPixmapItem ( QPixmap ( image[1] ) )
                self.element_8.setPos ( int ( image[2] ), int ( image[3] ) )
                self.list_fourre_tout.append ( ( ( ( int ( image[3] ) + y ) / 100 - 1, int ( image[2] ) / 100 ), "Element_8", self.element_8 ) )
            elif image[0] == "Element_9" :
                element_9 = Image.open ( image[1] )
                x,y = element_9.size
                self.element_9 = QGraphicsPixmapItem ( QPixmap ( image[1] ) )
                self.element_9.setPos ( int ( image[2] ), int ( image[3] ) )
                self.list_fourre_tout.append ( ( ( ( int ( image[3] ) + y ) / 100 - 1, int ( image[2] ) / 100 ), "Element_9", self.element_9 ) )
            elif image[0] == "Element_10" :
                element_10 = Image.open ( image[1] )
                x,y = element_10.size
                self.element_10 = QGraphicsPixmapItem ( QPixmap ( image[1] ) )
                self.element_10.setPos ( int ( image[2] ), int ( image[3] ) )
                self.list_fourre_tout.append ( ( ( ( int ( image[3] ) + y ) / 100 - 1, int ( image[2] ) / 100 ), "Element_10", self.element_10 ) )
            elif image[0] == "Element_11" :
                element_11 = Image.open ( image[1] )
                x,y = element_11.size
                self.element_11 = QGraphicsPixmapItem ( QPixmap ( image[1] ) )
                self.element_11.setPos ( int ( image[2] ), int ( image[3] ) )
                self.list_fourre_tout.append ( ( ( ( int ( image[3] ) + y ) / 100 - 1, int ( image[2] ) / 100 ), "Element_11", self.element_11 ) )
            elif image[0] == "Bateau" :
                sortie = Image.open ( image[1] )
                x,y = sortie.size
                self.sortie = QGraphicsPixmapItem ( QPixmap ( image[1] ) )
                self.sortie.setPos ( int ( image[2] ), int ( image[3] ) )
                self.list_fourre_tout.append ( ( ( ( int ( image[3] ) + y ) / 100 - 1, int ( image[2] ) / 100 ), "Bateau", self.sortie ) )

        self.list_elements = sorted ( self.list_fourre_tout )

        self.list_image = []
        for i in range ( len ( self.list_elements ) ) :
            self.list_image.append ( self.list_elements[i][2] )
            self.addItem ( self.list_image[i] )

    def reset_dynamic_elements ( self ) :
        for i in range ( len ( self.list_image ) ) :
            self.removeItem ( self.list_image[i] )
        self.list_image.clear()
        self.scene.init_dynamic_elements()
        self.init_dynamic_elements()
        self.update()

    def change_niveau ( self ) :
        if self.mainwindow.count > 0 :
            if len ( self.scene.plateau.inventaire_item ) <= 0 :
                if self.niveau < 9 :
                    self.niveau += 1
                    self.scene.jeu.jouer ( self.niveau )
                    self.scene.init_static_elements()
                    self.init_static_elements()
                    self.scene.jeu.joueur.posI = 1
                    self.scene.jeu.joueur.posJ = 1
                else :
                    self.mainwindow.fin ( 2 )
        else :
            self.mainwindow.fin ( 1 )

    def keyPressEvent ( self, event ) :
        dx = 0
        dy = 0
        if ( event.key() == Qt.Key_Z ) :
            dy -= 1
            if ( event.modifiers() == Qt.ShiftModifier ) :
                self.position = 5
            else :
                self.position = 1
        elif ( event.key() == Qt.Key_Q ) :
            dx -= 1
            if ( event.modifiers() == Qt.ShiftModifier ) :
                self.position = 6
            else :
                self.position = 2
        elif ( event.key() == Qt.Key_S ) :
            dy += 1
            if ( event.modifiers() == Qt.ShiftModifier ) :
                self.position = 7
            else :
                self.position = 3
        elif ( event.key() == Qt.Key_D ) :
            dx += 1
            if ( event.modifiers() == Qt.ShiftModifier ) :
                self.position = 8
            else :
                self.position = 4
        elif ( event.key() == Qt.Key_Enter ) :
            self.plateau.inventaire_mur.clear()
            self.plateau.inventaire_box.clear()
            self.plateau.inventaire_item.clear()
            self.position = 4
        else :
            self.position = 0

        self.scene.deplace_perso( self.position )
        self.change_niveau()
