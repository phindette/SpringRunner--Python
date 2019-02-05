import pygame
import personnage
import controleur
import point
import gravity
from constantes import *
from plateform import *

gravity = gravity.Gravity()
contro = controleur.Controleur()
listePixelSolide = contro.getListePixel()
x = 20
y = 50
position = (x,y)

perso = personnage.Personnage(x,y)
perso.getposition()
print("salut")
perso.deplacer(GAUCHE,listePixelSolide,listePixelSolide,listePixelSolide)
perso.getposition()
print("fin du game")


pygame.init()

#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((LARGEURFENETRE, HAUTEURFENETRE))

#Chargement et collage du fond
fond = pygame.image.load("background.jpg").convert()
fenetre.blit(fond, (0,0))

#Chargement et collage du personnage
imagePerso = pygame.image.load("chara.png").convert_alpha()
fenetre.blit(imagePerso, (perso.getpositionx(),perso.getpositiony()))

#Chargement et collage des plateformes
#liste_posit = ((190,464),(415,360),(650,464),(190,264),(650,264))
#plateforme = pygame.image.load("bloc.png").convert()
#plateforme.set_colorkey((255,255,255))
obstacles = []
plateformes = []
p1 = Plateform(500, 10,0,0)
p2 = Plateform(0,100,0,0)
print("connard :",p1.rect)
print("connard2 :",p1.rect.y)
print("connard3 :",p1.rect.w)
print("connard4 :",p1.rect.h)
#p1.image = pygame.image.load("bloc.png").convert_alpha()
obstacles.append(p1)
plateformes.append(p2)


#Rafraîchissement de l'écran
pygame.display.flip()

#BOUCLE INFINIE
continuer = True
pygame.key.set_repeat(1,20)
x = 0
while continuer:
    pygame.time.Clock().tick(60)

    if perso.hitbox.collidelist(plateformes) != -1:
        x =0
    else:
        x +=0.1
    gravity.graviteBase(perso,x)
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                perso.deplacer(DROITE,listePixelSolide,obstacles,plateformes)
            elif event.key == pygame.K_q:
                perso.deplacer(GAUCHE,listePixelSolide,obstacles,plateformes)
        if event.type == pygame.QUIT:
            continuer = False
    #Re-collage
    fenetre.blit(fond, (0,0))
    fenetre.blit(fond, (0,0))
    #for i in range(5):
    #    fenetre.blit(plateforme ,liste_posit[i])
    fenetre.blit(p1.image, (p1.rect.x, p1.rect.y))
    fenetre.blit(p2.image,(p2.rect.x,p2.rect.y))
    fenetre.blit(imagePerso, (perso.getpositionx(),perso.getpositiony()))
    #Rafraichissement
    pygame.display.flip()

pygame.quit()
