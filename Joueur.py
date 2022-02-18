from Plateau import *

class Joueur :

    def __init__ ( self, plat ) :
        self.plateau = plat
        self.case_courante = self.plateau.case_entree
        self.posI = self.case_courante.posI
        self.posJ = self.case_courante.posJ
        self.deplacement = 1

#FONCTION QUI PERMET DE VERIFIER LES POSSIBILITES DE DEPLACEMENT DU JOUEUR

    def peut_deplacer_mur ( self, i, j ) :
        for k in range ( len ( self.plateau.inventaire_mur ) ) :
            x,y = self.plateau.inventaire_mur[k]
            if i == x and j == y :
                return False
                break
            else :
                k += 1

    def peut_deplacer_box ( self, i, j ) :
        for k in range ( len ( self.plateau.inventaire_box ) ) :
            x,y = self.plateau.inventaire_box[k]
            if i == x and j == y :
                return False
                break
            else :
                k += 1

    def peut_deplacer_item ( self, i, j ) :
        for k in range ( len ( self.plateau.inventaire_item ) ) :
            x,y = self.plateau.inventaire_item[k]
            if i == x and j == y :
                return False
                break
            else :
                k += 1

#FONCTION QUI PERMET AU JOUEUR DE DEPLACER DES BLOCS

    def deplace_box ( self, a, b, c, d, k ) :
        self.plateau.plateau[a][b].box = False
        self.plateau.inventaire_box.remove ( k )
        self.plateau.plateau[c][d].box = True
        self.plateau.inventaire_box.append ( ( c, d ) )

    def deplace_item ( self, a, b, c, d, k ) :
        self.plateau.plateau[a][b].item = False
        self.plateau.inventaire_item.remove ( k )
        self.plateau.plateau[c][d].item = True
        self.plateau.inventaire_item.append ( ( c, d ) )
        if self.plateau.plateau[c][d] == self.plateau.case_sortie :
            self.plateau.inventaire_item.remove ( ( c, d ) )

#FONCTION QUI PERMET AU JOUEUR DE SE DEPLACER

    def pousse_monter ( self ) :
        if self.peut_deplacer_mur ( self.posI - 1, self.posJ ) != False and self.peut_deplacer_box ( self.posI - 1, self.posJ ) != False and self.peut_deplacer_item ( self.posI - 1, self.posJ ) != False :
            self.nouvelleCaseCourante ( self.posI - 1, self.posJ )
            self.deplacement = 1
        elif self.peut_deplacer_mur ( self.posI - 1, self.posJ ) != False and self.peut_deplacer_box ( self.posI - 1, self.posJ ) == False :
            if self.peut_deplacer_mur ( self.posI - 2, self.posJ ) != False and self.peut_deplacer_box ( self.posI - 2, self.posJ ) != False and self.peut_deplacer_item ( self.posI - 2, self.posJ ) != False :
                self.deplace_box ( self.posI-1, self.posJ, self.posI - 2, self.posJ, ( self.posI - 1, self.posJ ) )
                self.nouvelleCaseCourante ( self.posI - 1, self.posJ )
                self.deplacement = 0
            else :
                print ( "Impossible !" )
                self.deplacement = 0
        elif self.peut_deplacer_mur ( self.posI - 1, self.posJ ) != False and self.peut_deplacer_item ( self.posI - 1, self.posJ ) == False :
            if self.peut_deplacer_mur ( self.posI - 2, self.posJ ) != False and self.peut_deplacer_box ( self.posI - 2, self.posJ ) != False and self.peut_deplacer_item ( self.posI - 2, self.posJ ) != False :
                self.deplace_item ( self.posI - 1, self.posJ, self.posI - 2, self.posJ, ( self.posI - 1, self.posJ ) )
                self.nouvelleCaseCourante ( self.posI - 1, self.posJ )
                self.deplacement = 0
            else :
                print ( "Impossible !" )
                self.deplacement = 0

    def pousse_descendre(self):
        if self.peut_deplacer_mur(self.posI+1,self.posJ) != False and self.peut_deplacer_box(self.posI+1,self.posJ) != False and self.peut_deplacer_item(self.posI+1,self.posJ) != False :
            self.nouvelleCaseCourante(self.posI+1,self.posJ)
            self.deplacement = 1
        elif self.peut_deplacer_mur(self.posI+1,self.posJ) != False and self.peut_deplacer_box(self.posI+1,self.posJ) == False :
            if self.peut_deplacer_mur(self.posI+2,self.posJ) != False and self.peut_deplacer_box(self.posI+2,self.posJ) != False and self.peut_deplacer_item(self.posI+2,self.posJ) != False :
                self.deplace_box(self.posI+1,self.posJ,self.posI+2,self.posJ,(self.posI+1,self.posJ))
                self.nouvelleCaseCourante(self.posI+1,self.posJ)
                self.deplacement = 0
            else :
                print("Impossible !")
                self.deplacement = 0
        elif self.peut_deplacer_mur(self.posI+1,self.posJ) != False and self.peut_deplacer_item(self.posI+1,self.posJ) == False :
            if self.peut_deplacer_mur(self.posI+2,self.posJ) != False and self.peut_deplacer_box(self.posI+2,self.posJ) != False and self.peut_deplacer_item(self.posI+2,self.posJ) != False :
                self.deplace_item(self.posI+1,self.posJ,self.posI+2,self.posJ,(self.posI+1,self.posJ))
                self.nouvelleCaseCourante(self.posI+1,self.posJ)
                self.deplacement = 0
            else :
                print("Impossible !")
                self.deplacement = 0

    def pousse_gauche(self):
        if self.peut_deplacer_mur(self.posI,self.posJ-1) != False and self.peut_deplacer_box(self.posI,self.posJ-1) != False and self.peut_deplacer_item(self.posI,self.posJ-1) != False :
            self.nouvelleCaseCourante(self.posI,self.posJ-1)
            self.deplacement = 1
        elif self.peut_deplacer_mur(self.posI,self.posJ-1) != False and self.peut_deplacer_box(self.posI,self.posJ-1) == False :
            if self.peut_deplacer_mur(self.posI,self.posJ-2) != False and self.peut_deplacer_box(self.posI,self.posJ-2) != False and self.peut_deplacer_item(self.posI,self.posJ-2) != False :
                self.deplace_box(self.posI,self.posJ-1,self.posI,self.posJ-2,(self.posI,self.posJ-1))
                self.nouvelleCaseCourante(self.posI,self.posJ-1)
                self.deplacement = 0
            else :
                print("Impossible !")
                self.deplacement = 0
        elif self.peut_deplacer_mur(self.posI,self.posJ-1) != False and self.peut_deplacer_item(self.posI,self.posJ-1) == False :
            if self.peut_deplacer_mur(self.posI,self.posJ-2) != False and self.peut_deplacer_box(self.posI,self.posJ-2) != False and self.peut_deplacer_item(self.posI,self.posJ-2) != False :
                self.deplace_item(self.posI,self.posJ-1,self.posI,self.posJ-2,(self.posI,self.posJ-1))
                self.nouvelleCaseCourante(self.posI,self.posJ-1)
                self.deplacement = 0
            else :
                print("Impossible !")
                self.deplacement = 0

    def pousse_droite(self):
        if self.peut_deplacer_mur(self.posI,self.posJ+1) != False and self.peut_deplacer_box(self.posI,self.posJ+1) != False and self.peut_deplacer_item(self.posI,self.posJ+1) != False :
            self.nouvelleCaseCourante(self.posI,self.posJ+1)
            self.deplacement = 1
        elif self.peut_deplacer_mur(self.posI,self.posJ+1) != False and self.peut_deplacer_box(self.posI,self.posJ+1) == False :
            if self.peut_deplacer_mur(self.posI,self.posJ+2) != False and self.peut_deplacer_box(self.posI,self.posJ+2) != False and self.peut_deplacer_item(self.posI,self.posJ+2) != False :
                self.deplace_box(self.posI,self.posJ+1,self.posI,self.posJ+2,(self.posI,self.posJ+1))
                self.nouvelleCaseCourante(self.posI,self.posJ+1)
                self.deplacement = 0
            else :
                print("Impossible !")
                self.deplacement = 0
        elif self.peut_deplacer_mur(self.posI,self.posJ+1) != False and self.peut_deplacer_item(self.posI,self.posJ+1) == False :
            if self.peut_deplacer_mur(self.posI,self.posJ+2) != False and self.peut_deplacer_box(self.posI,self.posJ+2) != False and self.peut_deplacer_item(self.posI,self.posJ+2) != False :
                self.deplace_item(self.posI,self.posJ+1,self.posI,self.posJ+2,(self.posI,self.posJ+1))
                self.nouvelleCaseCourante(self.posI,self.posJ+1)
                self.deplacement = 0
            else :
                print("Impossible !")
                self.deplacement = 0

    def tire_monter(self):
        if self.peut_deplacer_mur(self.posI-1,self.posJ) != False and self.peut_deplacer_box(self.posI-1,self.posJ) != False and self.peut_deplacer_item(self.posI-1,self.posJ) != False :
            if self.peut_deplacer_box(self.posI+1,self.posJ) == False :
                self.deplace_box(self.posI+1,self.posJ,self.posI,self.posJ,(self.posI+1,self.posJ))
                self.nouvelleCaseCourante(self.posI-1,self.posJ)
                self.deplacement = 0
            elif self.peut_deplacer_item(self.posI+1,self.posJ) == False :
                self.deplace_item(self.posI+1,self.posJ,self.posI,self.posJ,(self.posI+1,self.posJ))
                self.nouvelleCaseCourante(self.posI-1,self.posJ)
                self.deplacement = 0
        else :
            print("Impossible !")

    def tire_descendre(self):
        if self.peut_deplacer_mur(self.posI+1,self.posJ) != False and self.peut_deplacer_box(self.posI+1,self.posJ) != False and self.peut_deplacer_item(self.posI+1,self.posJ) != False :
            if self.peut_deplacer_box(self.posI-1,self.posJ) == False :
                self.deplace_box(self.posI-1,self.posJ,self.posI,self.posJ,(self.posI-1,self.posJ))
                self.nouvelleCaseCourante(self.posI+1,self.posJ)
                self.deplacement = 0
            elif self.peut_deplacer_item(self.posI-1,self.posJ) == False :
                self.deplace_item(self.posI-1,self.posJ,self.posI,self.posJ,(self.posI-1,self.posJ))
                self.nouvelleCaseCourante(self.posI+1,self.posJ)
                self.deplacement = 0
        else :
            print("Impossible !")

    def tire_gauche ( self ) :
        if self.peut_deplacer_mur ( self.posI, self.posJ - 1 ) != False and self.peut_deplacer_box ( self.posI, self.posJ - 1 ) != False and self.peut_deplacer_item ( self.posI, self.posJ - 1 ) != False :
            if self.peut_deplacer_box ( self.posI, self.posJ + 1 ) == False :
                self.deplace_box ( self.posI, self.posJ + 1, self.posI, self.posJ, ( self.posI, self.posJ + 1 ) )
                self.nouvelleCaseCourante ( self.posI, self.posJ - 1 )
                self.deplacement = 0
            elif self.peut_deplacer_item ( self.posI, self.posJ + 1 ) == False :
                self.deplace_item ( self.posI, self.posJ + 1, self.posI, self.posJ, ( self.posI, self.posJ + 1 ) )
                self.nouvelleCaseCourante(self.posI,self.posJ-1)
                self.deplacement = 0
        else :
            print("Impossible !")

    def tire_droite ( self ) :
        if self.peut_deplacer_mur(self.posI,self.posJ+1) != False and self.peut_deplacer_box(self.posI,self.posJ+1) != False and self.peut_deplacer_item(self.posI,self.posJ+1) != False :
            if self.peut_deplacer_box(self.posI,self.posJ-1) == False :
                self.deplace_box(self.posI,self.posJ-1,self.posI,self.posJ,(self.posI,self.posJ-1))
                self.nouvelleCaseCourante(self.posI,self.posJ+1)
                self.deplacement = 0
            elif self.peut_deplacer_item(self.posI,self.posJ-1) == False :
                self.deplace_item(self.posI,self.posJ-1,self.posI,self.posJ,(self.posI,self.posJ-1))
                self.nouvelleCaseCourante(self.posI,self.posJ+1)
                self.deplacement = 0
        else :
            print("Impossible !")

    def nouvelleCaseCourante ( self, i, j ) :
        self.case_courante = self.plateau.plateau[i][j]
        self.posI = i
        self.posJ = j
