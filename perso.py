import pygame
from constantes import *
vec = pygame.math.Vector2

class Perso(pygame.sprite.Sprite):
    def __init__(self,game):
        self.groupes = game.les_sprites
        pygame.sprite.Sprite.__init__(self,game.les_sprites)
        self.game = game
        self.marcher = False
        self.sauter = False
        self.charger_images()
        self.image =self.debout
        self.rect = self.image.get_rect()
        self.rect.center = (0, HAUTEURFENETRE - 60)
        self.pos = vec(0, HAUTEURFENETRE - 60)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.check = None
    def charger_images(self):
        #charger les images (pour l'instant que l'image de base)
        self.debout = pygame.image.load("chara.png").convert_alpha()

    def jump(self):
        self.rect.y +=2
        hits = pygame.sprite.spritecollide(self,self.game.plateformes,False)
        self.rect.y -=2
        if hits and not self.sauter:
            self.sauter = True
            self.vel.y =-20

    def respawn(self,c):
        self.pos.x = c.rect.x
        self.pos.y = c.rect.y

    '''def deplacer(self, dir):
        if dir == DROITE:
            for i in range(1,VITESSE):
                self.rect.x +=1
        if dir == GAUCHE:
            for i in range(1,VITESSE):
                self.rect.x -=1'''

    def update(self):
        self.acc = vec(0,0.8)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            self.acc.x = -1
        if keys[pygame.K_d]:
            self.acc.x = 1
        # apply friction
        self.acc.x += self.vel.x * -0.12
        # equations of motion
        self.vel += self.acc
        if abs(self.vel.x) < 0.1:
            self.vel.x = 0
        self.pos += self.vel + 0.5 * self.acc
        # wrap around the sides of the screen
        if self.pos.x > LARGEURFENETRE + self.rect.width / 2:
            self.pos.x = 0 - self.rect.width / 2
        if self.pos.x < 0 - self.rect.width / 2:
            self.pos.x = LARGEURFENETRE + self.rect.width / 2

        self.rect.midbottom = self.pos
