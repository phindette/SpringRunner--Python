from constantes import *
import point

class Controleur:

    def __init__(self):
        self.listePixel = {}
        self.initBordures()

    def initBordures(self):
        for i in range (0,HAUTEURFENETRE):
            self.listePixel[(0,i)]= point.Point(0,i,SOLIDE)
            self.listePixel[(LARGEURFENETRE,i)]= point.Point(LARGEURFENETRE,i,SOLIDE)

            #self.listePixel.append(point.Point(0,i,SOLIDE))
            #self.listePixel.append(point.Point(LARGEURFENETRE,i,SOLIDE))
        for i in range (0,LARGEURFENETRE):
            self.listePixel[(i,0)] = point.Point(i,0,SOLIDE)
            self.listePixel[(i,HAUTEURFENETRE)] = point.Point(i,HAUTEURFENETRE,SOLIDE)

            #self.listePixel.append(point.Point(i,0,SOLIDE))
            #self.listePixel.append(point.Point(i,HAUTEURFENETRE,SOLIDE))

    def getListePixel(self):
        return self.listePixel

    def printPixel(self):
        for cle in self.listePixel.keys():
            print(cle)
