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
import plateformeAntiGrav
vec = pygame.math.Vector2
#

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

    def nouvellePartie(self):
        #Débute une nouvelle nouvellePartie
        self.les_sprites = pygame.sprite.LayeredUpdates()
        self.plateformes = pygame.sprite.Group()
        self.textes = pygame.sprite.Group()
        self.pieges = pygame.sprite.Group()
        self.check = pygame.sprite.Group()
        self.goals = pygame.sprite.Group()
        self.plateformegGravite = pygame.sprite.Group()


        #MISE EN PLACE DES SPRITE POUR LE NIVEAU 1
        self.niveau = 1
        self.initNiveau(self.niveau)
        self.c = False


        self.start()




    def start(self):
        #Boucle du jeu
        self.en_jeu = True
        fps = 60
        self.minutes = 0
        self.seconds = 0
        self.milliseconds = 0
        while self.en_jeu:
            self.clock.tick(fps)
            self.milliseconds += 1
            self.events()
            self.update()
            self.draw()

    def update(self):
        #Mise à jour de la boucle du jeu
        self.les_sprites.update()

        #MISE EN PLACE DU TIMER 1
        if self.milliseconds > 60:
            if self.c:
                self.timer.clear()
            self.seconds += 1
            self.milliseconds -= 60
            self.c = True
            self.timer = texte.Texte(self,str(self.minutes)+":"+str(self.seconds),LARGEURFENETRE-200)
        if self.seconds > 60:
            self.minutes += 1
            self.seconds -= 60
            pygame.mixer.music.rewind()


        #VERIF DE LA FIN DU JEU
        if(self.minutes >=3):
            self.en_jeu = False
            self.fin = fin.Application()
            self.fin.startFin(self.niveau)


        #Vérifie que le joueur est sur une plateforme (quand il tombe)
        hits = pygame.sprite.spritecollide(self.joueur,self.plateformes,False)
        if hits:
            platBas = hits[0]
            platDroit = hits[0]
            platGauche = hits[0]
            platHaut = hits[0]
            for hit in hits:
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
                    if self.joueur.pos.y > plat.rect.bottom +10:
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
                        if self.joueur.pos.x > platDroit.rect.right -20 and self.joueur.pos.y > platDroit.rect.top:
                            self.joueur.pos.x = platDroit.rect.right +22 #positionne le joueur contre la partie droite
                            self.joueur.acc.x = 0
                            self.joueur.sauter = False
                    #colision a gauche:
                    if platBas != platGauche:
                        if self.joueur.pos.y < platBas.rect.top +25 :
                            self.joueur.pos.y = platBas.rect.top #positionne le joueur sur la plateforme
                            self.joueur.vel.y = 0 #supprime la vélocité du saut du joueur
                            self.joueur.sauter = False #le joueur n'est plus en train de sauter
                        if self.joueur.pos.x < platGauche.rect.left +20 and self.joueur.pos.y > platGauche.rect.top:
                            self.joueur.pos.x = platGauche.rect.left -22 #positionne le joueur contre la partie gauche
                            self.joueur.acc.x = 0
                            self.joueur.sauter = False
        '''    else :
                self.seconds = '0' + str(minutes) + ':'  +  str(ingametimer)
            print(self.seconds)
            if self.timer != 0:
                print("ta petite maman")
                self.timer.clear()
            self.timer = texte.Texte(self,self.seconds,LARGEURFENETRE-250)
            ur.pos.x - 20 #positionne le joueur contre la partie gauche de la plateforme
                            self.joueur.acc.x = 0
                            self.joueur.vel.x = 0
                            self.joueur.sauter = False""



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

        #VERIF POUR LA GRAVITE
        hitGrav = pygame.sprite.spritecollide(self.joueur,self.plateformegGravite,False)
        if hitGrav:
            self.joueur.zeroGrav = True
        else :
            self.joueur.zeroGrav = False


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
        #self.screen.surface.fill()
        self.les_sprites.draw(self.screen)
        pygame.display.flip()

    def initNiveau(self,niveau):
        self.les_sprites.empty()
        self.plateformes.empty()
        self.pieges.empty()
        self.check.empty()
        self.goals = pygame.sprite.Group()
        self.plateformegGravite = pygame.sprite.Group()



        #MISE EN PLACE DU NOMBRE DE POINTS
        pts = self.niveau
        stringpts = "Points : " + str(self.niveau)
        self.pts = texte.Texte(self,stringpts,LARGEURFENETRE-150,0,150)


        if niveau == 1: #VRAI NIVEAU 1
            background.Background(self,"images/backgrounds/background_1.png")
            for plate in [(0, 728),(150,650),(700,300),(900,300)]:
                plat.Plat(self,*plate)

            for piegee in []:
                piege.Piege(self,*piegee)

            for gravv in [(300,500),(300,400),(300,300),(400,500),(400,400),(400,300)] :
                plateformeAntiGrav.PlateformeAntiGrav(self,*gravv)

            self.checkpointCourant = checkpoint.Check(self,80, 618)
            for checkk in []:
                checkpoint.Check(self,*checkk)

            for finniv in[(950,250)]:
                goal.Goal(self,*finniv)
            self.joueur = perso.Perso(self)
            self.joueur.pos = vec(40,20)

        elif niveau == 2: #VRAI NIVEAU 2
            background.Background(self,"images/backgrounds/background_1.png")
            for plate in [(0, 150)]:
                plat.Plat(self,*plate)

            for piegee in [(0,600)]:
                piege.Piege(self,*piegee)

            for gravv in [(300,500),(300,400),(300,300),(400,500),(400,400),(400,300)] :
                plateformeAntiGrav.PlateformeAntiGrav(self,*gravv)

            self.checkpointCourant = checkpoint.Check(self,0, 40)
            for checkk in []:
                checkpoint.Check(self,*checkk)

            for finniv in[(600,718)]:
                goal.Goal(self,*finniv)
            self.joueur = perso.Perso(self)
            self.joueur.pos = vec(40,150)

        elif niveau == 3: #VRAI LEVEL 3
            background.Background(self,"images/backgrounds/background_2.jpg")

            for plate in [(5,700),(388,700),(650,580),(520,450),(5,100),(120,450)]:
                plat.Plat(self,*plate)

            for piegee in []:
                piege.Piege(self,*piegee)

            for gravv in [(220,350),(120,250)] :
                plateformeAntiGrav.PlateformeAntiGrav(self,*gravv)

            self.checkpointCourant = checkpoint.Check(self,50, 590)
            for checkk in []:
                checkpoint.Check(self,*checkk)

            for finniv in[(0,0)]:
                goal.Goal(self,*finniv)
            self.joueur = perso.Perso(self)
            self.joueur.pos = vec(20,620)

        elif niveau == 4: #VRAI NIVEAU 4
            background.Background(self,"images/backgrounds/background_2.jpg")

            for plate in [(900,80),(725,600),(240,600),(946,600,6),
            (805,0,4),(805,100,4),(805,200,4),(805,300,4),(805,364,4),(805,600,4)]:
                plat.Plat(self,*plate)

            for piegee in [(835,0,3),(835,100,3),(835,200,3),(835,300,3),(835,364,3),(835,600,3),(946,630),
            (0,-60,4),(100,-60,4),(200,-60,4),(300,-60,4),(400,-60,4),(500,-60,4),(600,-60,4),(700,-60,4),(800,-60,4),(900,-60,4)]:
                piege.Piege(self,*piegee)

            for gravv in [(850,500),(850,600),(850,250),(560,500),
            (120,500),(120,600),(120,400),(120,300)] :
                plateformeAntiGrav.PlateformeAntiGrav(self,*gravv)

            self.checkpointCourant = checkpoint.Check(self,940, -35)
            for checkk in [(760,490)]:
                checkpoint.Check(self,*checkk)

            for finniv in[(155,0)]:
                goal.Goal(self,*finniv)
            self.joueur = perso.Perso(self)
            self.joueur.pos = vec(950,50)

        elif niveau == 5: #VRAI NIVEAU 5

            background.Background(self,"images/backgrounds/background_1.png")

            for plate in [(0, 728),(310, 550,2),(460, 450,2),(610, 350,2),(760,250,2)]:
                plat.Plat(self,*plate)

            for piegee in [(300,550,2),(450,450,2),(600,350,2),(750,250,2)]:
                piege.Piege(self,*piegee)

            for gravv in [(200,550),(350,450),(500,350),(650,250)] :
                plateformeAntiGrav.PlateformeAntiGrav(self,*gravv)

            self.checkpointCourant = checkpoint.Check(self,10, 620)
            for checkk in []:
                checkpoint.Check(self,*checkk)

            for finniv in[(800,250)]:
                goal.Goal(self,*finniv)
            self.joueur = perso.Perso(self)
            self.joueur.pos = vec(40,700)

        elif niveau == 6: # VRAI LEVEL 6
            background.Background(self,"images/backgrounds/background_1.png")


            for plate in [(20,120,6),(455,680,6),
                    (490,0,4),(490,100,4),(490,200,4),(490,300,4),(490,400,4),(490,455,4)]:
                plat.Plat(self,*plate)

            for piegee in [  (0,-60,4),(100,-60,4),(200,-60,4),(300,-60,4),(400,-60,4),(500,-60,4),(600,-60,4),(700,-60,4),(800,-60,4),(900,-60,4),
                      (480,0,2),(480,100,2),(480,200,2),(480,300,2),(480,400,2),(480,455,2),
                      (520,0,3),(520,100,3),(520,200,3),(520,300,3),(520,400,3),(520,455,3)]:
                piege.Piege(self,*piegee)

            for gravv in [(210,200),(210,300),(210,400),(210,500),(210,600),(210,100)] :
                plateformeAntiGrav.PlateformeAntiGrav(self,*gravv)

            self.checkpointCourant = checkpoint.Check(self,60,0)
            for checkk in [(530,560)]:
                checkpoint.Check(self,*checkk)

            for finniv in[(950,250)]:
                goal.Goal(self,*finniv)
            self.joueur = perso.Perso(self)
            self.joueur.pos = vec(60,100)

        elif niveau == 7: #VRAI NIVEAU 7
            background.Background(self,"images/backgrounds/background_1.png")
            for plate in [(0, 150),(210,0,2),(210,100,2),(210,200,2),(210,500,2),(210,600,2),(210,700,2) #,(210,300,2)
            ,(450,700,1)]:
                plat.Plat(self,*plate)

            for piegee in [(200,0,2),(200,100,2),(200,200,2),(200,500,2),(200,600,2),(200,700,2)]: #,(200,300,2)
                piege.Piege(self,*piegee)

            for gravv in [(100,150),(100,250),(100,350),(100,450),(100,550),(100,650)] :
                plateformeAntiGrav.PlateformeAntiGrav(self,*gravv)

            self.checkpointCourant = checkpoint.Check(self,10, 40)
            for checkk in []:
                checkpoint.Check(self,*checkk)

            for finniv in[(500,650)]:
                goal.Goal(self,*finniv)
            self.joueur = perso.Perso(self)
            self.joueur.pos = vec(40,20)

        elif niveau == 8: #VRAI NIVEAU 8

            background.Background(self,"images/backgrounds/background_1.png")

            for plate in [(0, 150),(0,410),(100,410),(200,410),(300,410),(400,410),(500,410),(600,410)
                  ,(600,600),(0,410),(100,410),(200,410),(300,410),(400,410),(500,410),(600,410),(600,600)
                  ,(0,440,3),(100,440,3),(200,440,3),(300,440,3),(400,440,3),(500,440,3),(600,440,3)]:
                plat.Plat(self,*plate)

            for piegee in [(0,400,4),(100,400,4),(200,400,4),(300,400,4),(400,400,4),(500,400,4),(600,400,4)
                  ,(0,470,1),(100,470,1),(200,470,1),(300,470,1),(400,470,1),(500,470,1),(600,470,1)]:
                piege.Piege(self,*piegee)

            for gravv in [(300,100),(500,200),(700,300),(700,400),(700,500)
                  ,(500,550),(400,550),(300,550),(200,550),(100,550)] :
                plateformeAntiGrav.PlateformeAntiGrav(self,*gravv)

            self.checkpointCourant = checkpoint.Check(self,0, 40)
            for checkk in []:
                checkpoint.Check(self,*checkk)

            for finniv in[(30,700)]:

                goal.Goal(self,*finniv)
            self.joueur = perso.Perso(self)
            self.joueur.pos = vec(40,150)

        elif niveau == 9: #VRAI LEVEL 9
            background.Background(self,"images/backgrounds/background_1.png")


            for plate in [(20,120),(220,0,2),(220,100,2),(220,200,2),(120,300),
            (170,450),(370,320),(478,200,2),(545,0,2),(10,450)]:
                plat.Plat(self,*plate)

            for piegee in [(0,757,4),(100,757,4),(200,757,4),(300,757,4),(400,757,4),(500,757,4),(600,757,4),(700,757,4),(800,757,4),(900,757,4),
            (210,0,2),(210,100,2),(210,200,2),(120,290,4),
            (10,440,4),
            (0,-60,4),(100,-60,4),(200,-60,4),(300,-60,4),(400,-60,4),(500,-60,4),(600,-60,4),(700,-60,4),(800,-60,4),(900,-60,4),
            (535,0,2),(470,200,2)]:
                piege.Piege(self,*piegee)

            for gravv in [(10,180),(10,280),
            (270,65),(300,-35),(400,-35),
            (540,120)] :
                plateformeAntiGrav.PlateformeAntiGrav(self,*gravv)

            self.checkpointCourant = checkpoint.Check(self,60,0)
            for checkk in [(410,205)]:
                checkpoint.Check(self,*checkk)

            for finniv in[(950,250)]:
                goal.Goal(self,*finniv)
            self.joueur = perso.Perso(self)
            self.joueur.pos = vec(60,100)

        elif niveau == 10:
            background.Background(self,"images/backgrounds/background_2.jpg")
            for plate in [(0, 150)]:
                plat.Plat(self,*plate)

            #pieges vers la droite descente
            for piegee in [(100,170,3),(100,270,3),(100,370,3),(100,470,3),(100,570,3),(100,625,3)]:
                piege.Piege(self,*piegee)

            #piege vers la gauche descente
            for piegee in [(185,-30,2),(185,70,2),(185,170,2),(185,270,2),(185,370,2),(185,470,2)]:
                piege.Piege(self,*piegee)

            #piege vers le bas ligne droite
            for piegee in [(190,580,1),(290,580,1),(390,580,1),(490,580,1),(590,580,1),(670,580,1)]:
                piege.Piege(self,*piegee)

            #piege vers le haut ligne droite
            for piegee in [(100,730,4),(200,730,4),(300,730,4),(400,730,4),(500,730,4),(600,730,4),(700,730,4),(770,730,4)]:
                piege.Piege(self,*piegee)

            #piege vers la gauche montée
            for piegee in [(868,630,2),(868,530,2),(868,430,2),(868,330,2),(868,230,2),]:
                piege.Piege(self,*piegee)

            #pieges vers la droite montée
            for piegee in [(770,470,3),(770,400,3),(770,370,3),]:
                piege.Piege(self,*piegee)

            #piege vers le bas petite ligne droite
            for piegee in [(768,230,1),(668,230,1),(568,230,1),]:
                piege.Piege(self,*piegee)

            #piege vers le haut petite ligne droite
            for piegee in [(670,370,4),(570,370,4)]:
                piege.Piege(self,*piegee)

            #plateformes descente gauche
            for plate in [(70,150,2),(70, 250,2),(70, 350,2),(70, 450,2),(70, 550,2),(70, 650,2)]:
                plat.Plat(self,*plate)

            #plateformes descente droite
            for plate in [(195,-30,2),(195,70,2),(195,170,2),(195,270,2),(195,370,2),(195,470,2)]:
                plat.Plat(self,*plate)

            #plateformes ligne droite haut
            for plate in [(200,550,3),(300,550,3),(400,550,3),(500,550,3),(600,550,3),(670,550,3),]:
                plat.Plat(self,*plate)

            #plateformes ligne droite bas
            for plate in [(100,740),(200,740),(300,740),(400,740),(500,740),(600,740),(700,740),(800,740)]:
                plat.Plat(self,*plate)

            #plateformes montée droite
            for plate in [(878,640,2),(878,540,2),(878,440,2),(878,340,2),(878,240,2),(878,220,2)]:
                plat.Plat(self,*plate)

            #plateformes montée gauche
            for plate in [(740,470,2),(740,380,2)]:
                plat.Plat(self,*plate)

            #le reste des plateformes osef de les décrire de toute façon personne lit ça
            for plate in [(670,380),(570,380), (768,200,3),(668,200,3), (568,200,3)]:
                plat.Plat(self,*plate)

            for gravv in [(100,150),(100,246),(100,342),(100,438),(100,534),(100,630),(196,630),(292,630),(388,630),(484,630),(580,630),(676,630),(772,630),(772,534),(772,438),(772,342),(772,246),(676,246),(580,246)] :
                plateformeAntiGrav.PlateformeAntiGrav(self,*gravv)

            self.checkpointCourant = checkpoint.Check(self,0, 40)
            for checkk in []:
                checkpoint.Check(self,*checkk)

            for finniv in[(400,500)]:
                goal.Goal(self,*finniv)

            self.joueur = perso.Perso(self)
            self.joueur.pos = vec(40,20)

        elif niveau == 11:

            background.Background(self,"images/backgrounds/background_1.png")


            for plate in [(0,750),(950,750)]:
                plat.Plat(self,*plate)


            for gravv in [(-46,114), (-46,210), (-46,306), (-46,402), (-46,498), (50,114),(146,114), (50,306),(50,500),(144,500), (288,114),(288,302),(288,396),(288,490),(288,208), (384,208),(432,304),(480,400),(576,496),(576,400),(576,304),(576,208),(576,112),(720,112),(720,208),(720,304),(720,400),(720,496),(816,112),(816,496),(912,208),(912,400),(960,304)] :
                plateformeAntiGrav.PlateformeAntiGrav(self,*gravv)

            self.checkpointCourant = checkpoint.Check(self,0,650)
            for checkk in []:
                checkpoint.Check(self,*checkk)

            for finniv in[(950,700)]:
                goal.Goal(self,*finniv)

            self.joueur = perso.Perso(self)
            self.joueur.pos = vec(40,20)
