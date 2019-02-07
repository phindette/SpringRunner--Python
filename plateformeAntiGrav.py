import pygame
from constantes import *

class PlateformeAntiGrav(pygame.sprite.Sprite):
    def __init__(self,game,x,y):
        self._layer = 1
        self.groups = game.les_sprites,game.plateformegGravite
        pygame.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        self.image = pygame.image.load("images/plateform/antiGrav.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
