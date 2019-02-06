import pygame
import animation
from animation import *
from constantes import *
vec = pygame.math.Vector2

class Perso(pygame.sprite.Sprite):
    def __init__(self,game):
        self.groupes = game.les_sprites
        pygame.sprite.Sprite.__init__(self,game.les_sprites)
        self.game = game
        self.marcher = False
        self.sauter = False
        self.animation = "SR"
        self.index = 0
        self.spritesCollection = initTabSprites(4).copy()
        self.spritesDebout = SpriteSheet("chara0.png")
        self.spritesMarche = SpriteSheet("chara_walking_right_spritesheet.png")
        self.charger_images()
        self.image = self.spritesCollection[0][0]
        self.rect = self.image.get_rect()
        self.rect.center = (0, HAUTEURFENETRE - 60)
        self.pos = vec(0, HAUTEURFENETRE - 60)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.check = None
        self.gravite = False
        self.changeM = False

    def charger_images(self):
        #charger les images (pour l'instant que l'image de base)
        loadSprites(self.spritesCollection[0],self.spritesDebout,1,35,60)
        loadSpritesInverted(self.spritesCollection[1],self.spritesDebout,1,35,60)
        loadSprites(self.spritesCollection[2],self.spritesMarche,8,35,60)
        loadSpritesInverted(self.spritesCollection[3],self.spritesMarche,8,35,60)

    def jump(self):
        self.rect.y +=2
        hits = pygame.sprite.spritecollide(self,self.game.plateformes,False)
        self.rect.y -=1
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
        # self.acc = vec(0,0.8)
        # self.acc = vec(0,0.80)
        self.index += 1
        if self.animation == "SR":
            if self.index >= len(self.spritesCollection[0]):
                self.index=0
            self.image = self.spritesCollection[0][self.index]
        elif self.animation == "SL":
            if self.index >= len(self.spritesCollection[1]):
                self.index=0
            self.image = self.spritesCollection[1][self.index]
        elif self.animation == "R":
            if self.index >= len(self.spritesCollection[2]):
                self.index=0
            self.image = self.spritesCollection[2][self.index]
        elif self.animation == "L":
            if self.index >= len(self.spritesCollection[3]):
                self.index=0
            self.image = self.spritesCollection[3][self.index]


        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            if self.gravite == False:
                self.acc = vec(0,-0.80)
                self.gravite = True
            else:
                self.gravite = False
                # self.changeM = False
        else :
            self.acc = vec(0,0.80)
        if self.changeM:
            if keys[pygame.K_z]:
                self.acc.y = -1
            if keys[pygame.K_s]:
                self.acc.y = 1
        else:
            if keys[pygame.K_q]:
                self.acc.x = -1
                self.animation = "L"
            elif keys[pygame.K_d]:
                self.acc.x = 1
                self.animation = "R"
            else:
                if self.animation == "R":
                    self.animation = "SR"
                elif self.animation == "L":
                    self.animation = "SL"

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
