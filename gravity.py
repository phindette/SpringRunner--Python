import pygame
import personnage

class Gravity:

    def __init__(self):
        self

    def graviteBase(self,personnage,x):
        if x<=4:
            personnage.setpositiony (personnage.getpositiony() +x*1.5)
        else:
            personnage.setpositiony (personnage.getpositiony() +4*1.8)


self.acc = vec(0,-0.8)# gravité haut
self.acc = vec(0.8,0) # gravité droite
self.acc = vec(-0.8,0)# gravité gauche
        if keys[pygame.K_a]:
            self.acc = vec(0,-0.8)
        # else:
        #     self.acc = vec(0,0.8)
