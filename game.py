#Cette class est un test de jéjé

import pygame
from constantes import *
import personnage
import perso
import plat
import piege
import checkpoint

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
        self.pieges = pygame.sprite.Group()
        self.check = pygame.sprite.Group()
        self.joueur = perso.Perso(self)

        for plate in [(0, HAUTEURFENETRE - 60),(LARGEURFENETRE / 2 , HAUTEURFENETRE * 2 / 4 ),(125, HAUTEURFENETRE - 150),(350, 200),(175, 100)]:
            plat.Plat(self,*plate)

        for piegee in [(0, HAUTEURFENETRE - 300)]:
            piege.Piege(self,*piegee)

        for checkk in [(200, HAUTEURFENETRE - 300),(50, HAUTEURFENETRE - 150)]:
            checkpoint.Check(self,*checkk)

        liste = self.check.sprites()
        self.checkpointCourant = liste[0]

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

        #Vérifie que le joueur est sur une plateforme (quand il tombe)
        if self.joueur.vel.y > 0:
            hits = pygame.sprite.spritecollide(self.joueur,self.plateformes,False)

            if hits:
                lowest = hits[0]
                for hit in hits:
                    if hit.rect.left > lowest.rect.left:
                        lowest = hit
                    if hit.rect.bottom > lowest.rect.bottom:
                        lowest = hit
                if self.joueur.pos.x < lowest.rect.right + 10 and self.joueur.pos.x>lowest.rect.left -10:
                    if self.joueur.pos.y < lowest.rect.top +10 :
                        self.joueur.pos.y = lowest.rect.top
                        self.joueur.vel.y = 0
                        self.joueur.sauter = False
                    if self.joueur.pos.x > lowest.rect.left - 10 and self.joueur.pos.y > lowest.rect.top +10:
                        self.joueur.pos.x = lowest.rect.left-10
                        self.joueur.pos.y = self.joueur.pos.y -10
                        self.joueur.acc.x = 0
                        self.joueur.vel.y = 0
                        self.joueur.vel.x = 0
                        self.joueur.acc.y = 0
                        self.joueur.sauter = False
                        self.update()
                        print("collision")

        #test:
        if self.joueur.rect.right >= LARGEURFENETRE /2:
            for plat in self.plateformes:
                plat.rect.x -= max(abs(self.joueur.vel.x), 2)
                if plat.rect.right >= LARGEURFENETRE:
                    plat.kill()

        #Verif que le joueur est sur un pic
        hitMortel = pygame.sprite.spritecollide(self.joueur,self.pieges,False)
        if hitMortel:
            self.joueur.respawn(self.checkpointCourant)

        #Verif que le joueur a activé un checkpoint
        hitCheck = pygame.sprite.spritecollide(self.joueur,self.check,False)
        if hitCheck:
            self.checkpointCourant = pygame.sprite.spritecollideany(self.joueur,self.check)


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
