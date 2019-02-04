import pygame

class Plateform:

    def __init__(self,positionx,positiony):
        self.positionx = positionx
        self.positiony = positiony
        self.position = (positionx,positiony)

    def setEtat(self):
        self.Etat="neutre"
        self.Etat="bonus"
        self.Etat="gravite"

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
