import pygame
from constantes import *

class Personnage:

    def __init__(self,positionx,positiony):
        self.positionx = positionx
        self.positiony = positiony
        self.position = (positionx,positiony)

    def setpositionx(self,positionx):
        self.positionx = positionx
        self.position = (self.positionx,self.positiony)

    def setpositiony(self,positiony):
        self.positiony = positiony
        self.position(self.positionx,self.positiony)

    def setposition(self,position):
        self.position = position

    def getpositionx(self):
        return self.positionx

    def getpositiony(self):
        return self.positiony

    def getposition(self):
        print("je suis en x :",self.positionx,"et je suis en y :",self.positiony)

    def deplacer(self, dir):
        if dir == DROITE:
            self.setpositionx(self.positionx + VITESSE)
        if dir == GAUCHE:
            self.setpositionx(self.positionx - VITESSE)
