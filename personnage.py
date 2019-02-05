import pygame
from constantes import *
import point

class Personnage:

    def __init__(self,positionx,positiony):
        self.positionx = positionx
        self.positiony = positiony
        self.hitbox = pygame.Rect(positionx,positiony,PERSOLARGEUR,PERSOHAUTEUR)

    def setpositionx(self,positionx):
        self.positionx = positionx

    def setpositiony(self,positiony):
        self.positiony = positiony

    def getpositionx(self):
        return self.positionx

    def getpositiony(self):
        return self.positiony

    def getposition(self):
        print("je suis en x :",self.positionx,"et je suis en y :",self.positiony)

    def deplacer(self, dir,listePixelSolide):
        if dir == DROITE:
            for i in range(1,VITESSE):
                if self.hitbox.collidelist(listePixelSolide) == -1:
                    self.hitbox = pygame.Rect(self.positionx +1,self.positiony,PERSOLARGEUR,PERSOHAUTEUR)
                    self.positionx +=1

        if dir == GAUCHE:
            for i in range(1,VITESSE):
                if self.hitbox.collidelist(listePixelSolide) == -1:
                    self.hitbox = pygame.Rect(self.positionx -1,self.positiony,PERSOLARGEUR,PERSOHAUTEUR)
                    self.positionx -=1
