import pygame
import personnage

class Deplacements:

    def __init__(self,positionx,positiony,ecran: pygame.Surface,personnage):
        self.position = position(positionx,positiony)
        self.positionx = positionx
        self.positiony = positiony
        self.ecran = ecran
        self.personnage = personnage

    def deplacer(self, dir: int=RIEN):
        if dir == DROITE:
            positionx = positionx +10
            position = (positionx,positiony)
            personnage.setposition(position)
            personnage.getposition()
