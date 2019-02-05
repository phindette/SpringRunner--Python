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
