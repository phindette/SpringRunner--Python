import pygame
from constantes import *
import point

class Personnage(pygame.sprite.Sprite):

    def __init__(self,positionx,positiony):
        self.positionx = positionx
        self.positiony = positiony
        self.hitbox = pygame.Rect(positionx,positiony,PERSOLARGEUR,PERSOHAUTEUR)

    def setpositionx(self,positionx):
        self.positionx = positionx

    def setpositiony(self,positiony):
        self.positiony = positiony

    def getpositionx(self):
        return self.positionx

    def getpositiony(self):
        return self.positiony

    def getposition(self):
        print("je suis en x :",self.positionx,"et je suis en y :",self.positiony)


    def deplacer(self, dir,listePixelSolide,obstacles,plateformes):


        if self.hitbox.collidelist(listePixelSolide) == -1 and self.hitbox.collidelist(obstacles) == -1:
            if dir == DROITE:
                for i in range(1,VITESSE):
                    if self.hitbox.collidelist(listePixelSolide) == -1 and self.hitbox.collidelist(obstacles) == -1:
                        # if self.hitbox.collidelist(plateformes) != -1:
                        #     self.hitbox = pygame.Rect(self.positionx +1,self.positiony,PERSOLARGEUR,PERSOHAUTEUR)
                        #     self.positionx +=1
                        # else:
                        #     #IL TOMBE
                            self.hitbox = pygame.Rect(self.positionx +1,self.positiony,PERSOLARGEUR,PERSOHAUTEUR)
                            self.positionx +=1
                    else:
                        self.hitbox = pygame.Rect(self.positionx -1,self.positiony,PERSOLARGEUR,PERSOHAUTEUR)
                        self.positionx = self.positionx -1

            if dir == GAUCHE:
                for i in range(1,VITESSE):
                    if self.hitbox.collidelist(listePixelSolide) == -1 and self.hitbox.collidelist(obstacles) == -1:
                        # if self.hitbox.collidelist(plateformes) != -1:
                            self.hitbox = pygame.Rect(self.positionx -1,self.positiony,PERSOLARGEUR,PERSOHAUTEUR)
                            self.positionx -=1
                        # else:
                        #     #IL TOMBE
                        #     self.hitbox = pygame.Rect(self.positionx,self.positiony + 1,PERSOLARGEUR,PERSOHAUTEUR)
                        #     self.positiony +=1
                    else:
                        self.hitbox = pygame.Rect(self.positionx +1,self.positiony,PERSOLARGEUR,PERSOHAUTEUR)
                        self.positionx +=1
        else:
            if(self.positionx == 0):
                self.hitbox = pygame.Rect(self.positionx +1,self.positiony,PERSOLARGEUR,PERSOHAUTEUR)
                self.positionx +=1
            else:
                self.hitbox = pygame.Rect(self.positionx -1,self.positiony,PERSOLARGEUR,PERSOHAUTEUR)
                self.positionx = self.positionx -1



        # def mourirEtRespawn(self,listePiege,checkpointCourant):
        #     if self.hitbox.collidelist(listePiege) != -1:
        #         print("issou")
        #         self.hitbox = pygame.Rect(checkpointCourant.rect.x,checkpointCourant.rect.y,PERSOLARGEUR,PERSOHAUTEUR)
        #         self.positonx = checkpointCourant.rect.x;
        #         self.positiony = checkpointCourant.rect.y;
