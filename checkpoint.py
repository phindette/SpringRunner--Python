import pygame
from constantes import *

class Check(pygame.sprite.Sprite):
    def __init__(self,game,x,y):
        self._layer = 1
        self.groups = game.les_sprites,game.check
        pygame.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        self.image = pygame.image.load("images/checkpoint/checkpoint_0.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
