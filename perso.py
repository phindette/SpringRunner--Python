import pygame
import animation
from animation import *
from constantes import *
vec = pygame.math.Vector2

class Perso(pygame.sprite.Sprite):
    def __init__(self,game):
        self._layer = 1
        self.groupes = game.les_sprites
        pygame.sprite.Sprite.__init__(self,game.les_sprites)
        self.game = game
        self.marcher = False
        self.sauter = False
        self.animation = "SR"
        self.index = 0
        self.spritesCollection = initTabSprites(6).copy()
        self.spritesDebout = SpriteSheet("images/chara/chara_still.png")
        self.spritesMarche = SpriteSheet("images/chara/chara_walking_right_spritesheet.png")
        self.spritesSaut = SpriteSheet("images/chara/chara_jumping.png")
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
        self.zeroGrav = False

    def charger_images(self):
        #charger les images (pour l'instant que l'image de base)
        loadSprites(self.spritesCollection[0],self.spritesDebout,10,35,60)
        loadSpritesInverted(self.spritesCollection[1],self.spritesDebout,10,35,60)
        loadSprites(self.spritesCollection[2],self.spritesMarche,8,35,60)
        loadSpritesInverted(self.spritesCollection[3],self.spritesMarche,8,35,60)
        loadSprites(self.spritesCollection[4],self.spritesSaut,1,35,60)
        loadSpritesInverted(self.spritesCollection[5],self.spritesSaut,1,35,60)

    def jump(self):
        self.rect.y +=2
        hits = pygame.sprite.spritecollide(self,self.game.plateformes,False)
        self.rect.y -=1
        if hits and not self.sauter:
            self.sauter = True
            self.vel.y =-15


    def respawn(self,c):
        self.pos.x = c.rect.x
        self.pos.y = c.rect.bottom

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
        elif self.animation == "JR":
            if self.index >= len(self.spritesCollection[4]):
                self.index=0
            self.image = self.spritesCollection[4][self.index]
        elif self.animation == "JL":
            if self.index >= len(self.spritesCollection[5]):
                self.index=0
            self.image = self.spritesCollection[5][self.index]

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.gravite = True

        else :
            self.gravite = False
            self.changeM = False
            self.acc = vec(0,0.80)
        if keys[pygame.K_e]:
            if self.zeroGrav:
                self.acc = vec(0,-0.8)
        if self.changeM:
            if keys[pygame.K_z]:
                self.pos.y = self.pos.y -2
            if keys[pygame.K_s]:
                self.pos.y = self.pos.y +2
        else:
            if keys[pygame.K_q]:
                if self.vel.y < -0.0:
                    self.acc.x = -1
                    self.animation = "JL"
                else:
                    self.acc.x = -1
                    self.animation = "L"
            elif keys[pygame.K_d]:
                if self.vel.y < -0.0:
                    self.acc.x = 1
                    self.animation = "JR"
                else:
                    self.acc.x = 1
                    self.animation = "R"
            elif self.vel.y < -0.0:
                if self.animation == "R" or self.animation == "SR" or self.animation == "JR":
                    self.animation = "JR"
                elif self.animation == "L" or self.animation == "SL" or self.animation == "JL":
                    self.animation = "JL"

            else:
                if self.animation == "R" or self.animation == "SR" or self.animation == "JR":
                    self.animation = "SR"
                elif self.animation == "L" or self.animation == "SL" or self.animation == "JL":
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
