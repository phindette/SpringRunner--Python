import pygame
import animation
from constantes import *
from animation import *

class Goal(pygame.sprite.Sprite):
    def __init__(self,game,x,y):
        self._layer = 1
        self.groups = game.les_sprites,game.goals
        pygame.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        self.index = 0
        self.spritesCollection = initTabSprites(1)
        self.spritesAuto = SpriteSheet("images/goal/goal.png")
        self.charger_image()
        self.image = self.spritesCollection[0][0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def charger_image(self):
        loadSprites(self.spritesCollection[0],self.spritesAuto,3,35,60)

    def update(self):
        self.index+=1
        if self.index >= len(self.spritesCollection[0]):
            self.index=0
        self.image = self.spritesCollection[0][self.index]
