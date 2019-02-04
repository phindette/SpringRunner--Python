import pygame
import personnage
from constantes import *

x = 20
y = 50
position = (x,y)

perso = personnage.Personnage(x,y)
perso.getposition()
print("salut")
perso.deplacer(GAUCHE)
perso.getposition()
print("fin du game")
