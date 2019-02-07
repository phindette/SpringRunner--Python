import pygame
from constantes import *

class Background(pygame.sprite.Sprite):
    def __init__(self,game,nom):
        self._layer = 0
        self.groups = game.les_sprites
        pygame.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        self.image = pygame.image.load(nom).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
