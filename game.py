#Cette class est un test de jéjé

import pygame
from constantes import *
import personnage
import perso
import plat
import piege
import checkpoint
import goal
import texte
import background
import fin


class Game:
    def __init__(self):
        #Initialisation de la fenettre de jeu etc...
        pygame.init()
        self.screen = pygame.display.set_mode((LARGEURFENETRE,HAUTEURFENETRE))
        pygame.display.set_caption("Spring Runner")
        self.clock = pygame.time.Clock() #je ne sais pas encore en quoi ça consiste vraiment.
        self.enCours = True;
        pygame.mixer.music.load("soundtrack/Actipognon_test_2.mp3")
        pygame.mixer.music.play()
        self.timer = 0

    def nouvellePartie(self):
        #Débute une nouvelle nouvellePartie
        self.les_sprites = pygame.sprite.LayeredUpdates()
        self.plateformes = pygame.sprite.Group()
        self.textes = pygame.sprite.Group()
        self.pieges = pygame.sprite.Group()
        self.check = pygame.sprite.Group()
        self.goals = pygame.sprite.Group()



        #MISE EN PLACE DES SPRITE POUR LE NIVEAU 1
        self.niveau = 1
        self.initNiveau(self.niveau)


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
        #MISE EN PLACE DU TIMER
        if((pygame.time.get_ticks()-0)/1000)% 1 > 0.94 :
            minutes = 0
            ingametimer = 180 - round(((pygame.time.get_ticks()-0)/1000))
            if ingametimer >= 180 :
                minutes = 3
                ingametimer -= 180
            elif ingametimer >= 120 :
                minutes = 2
                ingametimer -= 120
            elif ingametimer >= 60 :
                minutes = 1
                ingametimer -= 60

            if ingametimer < 10 :
                self.seconds = '0' + str(minutes) + ':' + '0'+ str(ingametimer)
            else :
                self.seconds = '0' + str(minutes) + ':'  +  str(ingametimer)
            print(self.seconds)
            if self.timer != 0:
                print("ta petite maman")
                self.timer.clear()
            self.timer = texte.Texte(self,self.seconds,LARGEURFENETRE-250)

        #VERIF DE LA FIN DU JEU
        if((pygame.time.get_ticks()-0)/1000 >= 180):
            self.en_jeu = False
            self.fin = fin.Application()
            #fin = fin.Application()
            self.fin.startFin()

        #Vérifie que le joueur est sur une plateforme (quand il tombe)
        hits = pygame.sprite.spritecollide(self.joueur,self.plateformes,False)
        if hits:
            platBas = hits[0]
            platDroit = hits[0]
            platGauche = hits[0]
            platHaut = hits[0]
            for hit in hits:
                #print(hit.rect.bottom,"et ",)
                if hit.rect.bottom >= platBas.rect.bottom:
                    platBas = hit
                if hit.rect.left >= platGauche.rect.left:
                    platGauche = hit
                if hit.rect.right >= platDroit.rect.right:
                    platDroit = hit
                if hit.rect.top >= platHaut.rect.top:
                    platHaut = hit
            #Vérification si le joueur est au contacte d'une plateforme
            if self.joueur.pos.x < platBas.rect.right +10 and self.joueur.pos.x > platBas.rect.left -10:
                #Si les 3 plat sont égales (colision avec une seule plateforme)
                if platBas == platDroit and platBas == platGauche and platBas == platHaut:
                    #définition d'une plateforme générale
                    plat = platBas
                    #Si le joueur est au dessus de la plateforme
                    if self.joueur.pos.y < plat.rect.top +25 :
                        self.joueur.pos.y = plat.rect.top #positionne le joueur sur la plateforme
                        self.joueur.vel.y = 0 #supprime la vélocité du saut du joueur
                        self.joueur.sauter = False #le joueur n'est plus en train de sauter

                    #Si le joueur est à gauche de la plateforme
                    if self.joueur.pos.x < plat.rect.left +20 and self.joueur.pos.y > plat.rect.top:
                        self.joueur.pos.x = plat.rect.left -10 #positionne le joueur contre la partie gauche de la plateforme
                        self.joueur.acc.x = 0
                        self.joueur.vel.x = 0
                        self.joueur.sauter = False
                        if self.joueur.gravite:
                            self.joueur.changeM = True
                    #Si le joueur est à droite de la plateforme
                    if self.joueur.pos.x > plat.rect.right -20 and self.joueur.pos.y > plat.rect.top:
                        self.joueur.pos.x = plat.rect.right +10 #positionne le joueur contre la partie droite
                        self.joueur.acc.x = 0
                        self.joueur.vel.x = 0
                        self.joueur.sauter = False
                        if self.joueur.gravite:
                            self.joueur.changeM = True
                    #Si le joueur est en dessous de la plateformes
                    if self.joueur.pos.y > plat.rect.bottom -10:
                        self.joueur.pos.y = plat.rect.bottom +75
                        self.joueur.acc.y = 0
                        self.joueur.vel.y = 0
                        self.joueur.sauter =False

                #Vérification si le joueur est au contacte de deux plateformes
                if platBas != platDroit or platBas != platGauche:
                    #colision a droite :
                    if platBas != platDroit:
                        if self.joueur.pos.y < platBas.rect.top +25 :
                            self.joueur.pos.y = platBas.rect.top #positionne le joueur sur la plateforme
                            self.joueur.vel.y = 0 #supprime la vélocité du saut du joueur
                            self.joueur.sauter = False #le joueur n'est plus en train de sauter
                        if self.joueur.pos.x > platDroit.rect.right -20 and self.joueur.pos.y > plat.rect.top:
                            self.joueur.pos.x = platDroit.rect.right +10 #positionne le joueur contre la partie droite
                            self.joueur.acc.x = 0
                            self.joueur.sauter = False
                    #colision a gauche:
                    if platBas != platGauche:
                        if self.joueur.pos.y < platBas.rect.top +25 :
                            self.joueur.pos.y = platBas.rect.top #positionne le joueur sur la plateforme
                            self.joueur.vel.y = 0 #supprime la vélocité du saut du joueur
                            self.joueur.sauter = False #le joueur n'est plus en train de sauter
                        if self.joueur.pos.x < platGauche.rect.left +20 and self.joueur.pos.y > platGauche.rect.top:
                            self.joueur.pos.x = self.joueur.pos.x - 20 #positionne le joueur contre la partie gauche de la plateforme
                            self.joueur.acc.x = 0
                            self.joueur.vel.x = 0
                            self.joueur.sauter = False



                    '''if hit.rect.left > lowest.rect.left:
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
                        print("collision")'''

        #test:
        '''if self.joueur.rect.right >= LARGEURFENETRE /2:
            for plat in self.plateformes:
                plat.rect.x -= max(abs(self.joueur.vel.x), 2)
                if plat.rect.right >= LARGEURFENETRE:
                    plat.kill()'''

        #Verif que le joueur est sur un pic ou hors écran
        hitMortel = pygame.sprite.spritecollide(self.joueur,self.pieges,False)
        if hitMortel or self.joueur.pos[0] < 0 or self.joueur.pos[0] > 1024 or self.joueur.pos[1] > 768:
            self.joueur.respawn(self.checkpointCourant)

        #Verif que le joueur a activé un checkpoint
        hitCheck = pygame.sprite.spritecollide(self.joueur,self.check,False)
        if hitCheck:
            self.checkpointCourant = pygame.sprite.spritecollideany(self.joueur,self.check)

        #Verif que le joueur a activé une fin de niveau
        hitGoal = pygame.sprite.spritecollide(self.joueur,self.goals,False)
        if hitGoal:
            self.niveau += 1
            self.initNiveau(self.niveau)



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

    def initNiveau(self,niveau):
        self.les_sprites.empty()
        self.plateformes.empty()
        self.pieges.empty()
        self.check.empty()
        self.joueur = perso.Perso(self)

        #MISE EN PLACE DU NOMBRE DE POINTS
        pts = self.niveau
        stringpts = "Points : " + str(self.niveau)
        self.pts = texte.Texte(self,stringpts,LARGEURFENETRE-150,0,150)


        if niveau == 1:
            background.Background(self,"images/backgrounds/background_2.jpg")

            for plate in [(0, 728),(512, 384),(125, 578),(350, 200),(175, 100),(0,438)]:
                plat.Plat(self,*plate)

            for piegee in [(0, 468)]:
                piege.Piege(self,*piegee)

            self.checkpointCourant = checkpoint.Check(self,50, 618)
            for checkk in [(200, 468)]:
                checkpoint.Check(self,*checkk)

            for finniv in[(400,718)]:
                goal.Goal(self,*finniv)



        elif niveau == 2:
            background.Background(self,"images/backgrounds/background_1.png")
            for plate in [(0, 728),(512 , 384 ),(125, 578),(350, 200),(175, 100),(0,438)]:
                plat.Plat(self,*plate)

            for piegee in [(0, 468)]:
                piege.Piege(self,*piegee)

            self.checkpointCourant = checkpoint.Check(self,50, 618)
            for checkk in [(200, 468)]:
                checkpoint.Check(self,*checkk)

            for finniv in[(600,718)]:
                goal.Goal(self,*finniv)
