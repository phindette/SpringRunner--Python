import pygame
import personnage
import controleur
import point
from constantes import *


contro = controleur.Controleur()
listePixelSolide = contro.getListePixel()
contro.printPixel()
x = 20
y = 50
position = (x,y)

perso = personnage.Personnage(x,y)
perso.getposition()
print("salut")
perso.deplacer(GAUCHE,listePixelSolide)
perso.getposition()
print("fin du game")


pygame.init()

#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((LARGEURFENETRE, HAUTEURFENETRE))

#Chargement et collage du fond
fond = pygame.image.load("background.JPG").convert()
fenetre.blit(fond, (0,0))

#Chargement et collage du personnage
imagePerso = pygame.image.load("mon_image.jpg").convert_alpha()
fenetre.blit(imagePerso, (perso.getpositionx(),perso.getpositiony()))

#Chargement et collage des plateformes
liste_posit = ((190,464),(415,360),(650,464),(190,264),(650,264))
plateforme = pygame.image.load("bloc.png").convert()
plateforme.set_colorkey((255,255,255))


#Rafraîchissement de l'écran
pygame.display.flip()

#BOUCLE INFINIE
continuer = True
pygame.key.set_repeat(1,20)
while continuer:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                perso.deplacer(DROITE,listePixelSolide)
            elif event.key == pygame.K_q:
                perso.deplacer(GAUCHE,listePixelSolide)
        if event.type == pygame.QUIT:
            continuer = False
    #Re-collage
    fenetre.blit(fond, (0,0))
    fenetre.blit(fond, (0,0))
    for i in range(5):
        fenetre.blit(plateforme ,liste_posit[i])
    fenetre.blit(imagePerso, (perso.getpositionx(),perso.getpositiony()))
    #Rafraichissement
    pygame.display.flip()

pygame.quit()
