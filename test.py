import pygame
import personnage
import controleur
import point
from constantes import *
from plateform import *


contro = controleur.Controleur()
listePixelSolide = contro.getListePixel()
x = 20
y = 50
position = (x,y)

perso = personnage.Personnage(x,y)
perso.getposition()
print("salut")
perso.deplacer(GAUCHE,listePixelSolide,listePixelSolide)
perso.getposition()
print("fin du game")


pygame.init()

#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((LARGEURFENETRE, HAUTEURFENETRE))

#Chargement et collage du fond
fond = pygame.image.load("background.JPG").convert()
fenetre.blit(fond, (0,0))

#Chargement et collage du personnage
imagePerso = pygame.image.load("chara.png").convert_alpha()
fenetre.blit(imagePerso, (perso.getpositionx(),perso.getpositiony()))

#Chargement et collage des plateformes
#liste_posit = ((190,464),(415,360),(650,464),(190,264),(650,264))
#plateforme = pygame.image.load("bloc.png").convert()
#plateforme.set_colorkey((255,255,255))
plateformes = []
p1 = Plateform(500, 10,0,0)
print("connard :",p1.rect)
print("connard2 :",p1.rect.y)
print("connard3 :",p1.rect.w)
print("connard4 :",p1.rect.h)
#p1.image = pygame.image.load("bloc.png").convert_alpha()
plateformes.append(p1)


#Rafraîchissement de l'écran
pygame.display.flip()

#BOUCLE INFINIE
continuer = True
pygame.key.set_repeat(1,20)
while continuer:
    pygame.time.Clock().tick(60)
    perso.setpositiony (perso.getpositiony() +1)
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                perso.deplacer(DROITE,listePixelSolide,plateformes)
            elif event.key == pygame.K_q:
                perso.deplacer(GAUCHE,listePixelSolide,plateformes)
        if event.type == pygame.QUIT:
            continuer = False
    #Re-collage
    fenetre.blit(fond, (0,0))
    fenetre.blit(fond, (0,0))
    #for i in range(5):
    #    fenetre.blit(plateforme ,liste_posit[i])
    fenetre.blit(p1.image, (p1.rect.x, p1.rect.y))
    fenetre.blit(imagePerso, (perso.getpositionx(),perso.getpositiony()))
    #Rafraichissement
    pygame.display.flip()

pygame.quit()
