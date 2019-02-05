#Cette class est un test de jéjé

import pygame
from constantes import *
import personnage
import perso
import plat

class Game:
    def __init__(self):
        #Initialisation de la fenettre de jeu etc...
        pygame.init()
        self.screen = pygame.display.set_mode((LARGEURFENETRE,HAUTEURFENETRE))
        pygame.display.set_caption("JEU DE FOU")
        self.clock = pygame.time.Clock() #je ne sais pas encore en quoi ça consiste vraiment.
        self.enCours = True;

    def nouvellePartie(self):
        #Débute une nouvelle nouvellePartie
        self.les_sprites = pygame.sprite.LayeredUpdates()
        self.plateformes = pygame.sprite.Group()
        self.joueur = perso.Perso(self)
        for plate in [(0, HAUTEURFENETRE - 60),(LARGEURFENETRE / 2 - 50, HAUTEURFENETRE * 3 / 4 - 50),(125, HAUTEURFENETRE - 350),(350, 200),(175, 100)]:
            plat.Plat(self,*plate)
        self.start()

    def start(self):
        #Boucle du jeu
        self.en_jeu = True
        fps = 60
        while self.en_jeu:
            self.clock.tick(fps)
            self.events()
            self.update()
            self.draw()

    def update(self):
        #Mise à jour de la boucle du jeu
        self.les_sprites.update()

        if self.joueur.vel.y > 0:
            hits = pygame.sprite.spritecollide(self.joueur,self.plateformes,False)
            if hits:
                lowest = hits[0]
                for hit in hits:
                    if hit.rect.bottom > lowest.rect.bottom:
                        lowest = hit
                if self.joueur.pos.x < lowest.rect.right + 10 and self.joueur.pos.x>lowest.rect.left -10:
                    if self.joueur.pos.y < lowest.rect.centery :
                        self.joueur.pos.y = lowest.rect.top
                        self.joueur.vel.y = 0
                        self.joueur.sauter = False

    def events(self):
        #évennements de la boucle du jeu
        for event in pygame.event.get():
            #fermeture de la fenettre du jeu :
            if event.type == pygame.QUIT:
                if self.en_jeu:
                    self.en_jeu = False
                self.enCours = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.joueur.jump()
                '''if event.key == pygame.K_d:
                    self.joueur.deplacer(DROITE)
                if event.key == pygame.K_q:
                    self.joueur.deplacer(GAUCHE)'''

    def draw(self):
        #Déssin du jeu dans la boucle
        self.screen.fill((255,255,255))
        self.les_sprites.draw(self.screen)
        pygame.display.flip()

g = Game()
while g.enCours:
    g.nouvellePartie()
pygame.quit()
