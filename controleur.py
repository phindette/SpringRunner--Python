from constantes import *
import point
import pygame

class Controleur:

    def __init__(self):
        #listePixel c'est le dico contenant les pixel solide des bordures.
        self.listePixelBordure = []
        self.initBordures()
        #
        persohitbox = pygame.Rect(20,50,PERSOLARGEUR,PERSOHAUTEUR)


    def initBordures(self):
        self.listePixelBordure.append(pygame.Rect(0,0,1,HAUTEURFENETRE))
        self.listePixelBordure.append(pygame.Rect(900,0,1,HAUTEURFENETRE))
        self.listePixelBordure.append(pygame.Rect(0,0,LARGEURFENETRE,1))
        self.listePixelBordure.append(pygame.Rect(0,900,LARGEURFENETRE,1))

        '''for i in range (0,HAUTEURFENETRE):
            self.listePixelBordure[(0,i)]= point.Point(0,i,SOLIDE)
            self.listePixelBordure[(LARGEURFENETRE,i)]= point.Point(LARGEURFENETRE,i,SOLIDE)
        for i in range (0,LARGEURFENETRE):
            self.listePixelBordure[(i,0)] = point.Point(i,0,SOLIDE)
            self.listePixelBordure[(i,HAUTEURFENETRE)] = point.Point(i,HAUTEURFENETRE,SOLIDE)'''

    def getListePixel(self):
        return self.listePixelBordure
