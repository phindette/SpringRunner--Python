import pygame
from constantes import *

class Plat(pygame.sprite.Sprite):
    def __init__(self,game,x,y):
        self._layer = 1
        #self.groups = game.les_spritesniv1,game.plateformes
        pygame.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        self.image = pygame.image.load("bloc.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
