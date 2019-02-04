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


pygame.init()

#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((900, 900))

#Chargement et collage du fond
fond = pygame.image.load("background.JPG").convert()
fenetre.blit(fond, (0,0))

#Chargement et collage du personnage
imagePerso = pygame.image.load("mon_image.jpg").convert_alpha()
fenetre.blit(imagePerso, (perso.getpositionx(),perso.getpositiony()))

#Rafraîchissement de l'écran
pygame.display.flip()

#BOUCLE INFINIE
continuer = True
pygame.key.set_repeat(1,20)
while continuer:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                perso.deplacer(DROITE)
            elif event.key == pygame.K_q:
                perso.deplacer(GAUCHE)
        if event.type == pygame.QUIT:
            continuer = False
    #Re-collage
    fenetre.blit(fond, (0,0))
    fenetre.blit(imagePerso, (perso.getpositionx(),perso.getpositiony()))
    #Rafraichissement
    pygame.display.flip()

pygame.quit()
