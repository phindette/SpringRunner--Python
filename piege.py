import pygame
from constantes import *

class Piege(pygame.sprite.Sprite):
    def __init__(self,game,x,y,cf=1):
        self._layer = 1
        self.groups = game.les_sprites,game.pieges
        pygame.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        # 1 = piques orientés vers le nord
        # 2 = piques orientés vers l'ouest
        # 3 = piques orientés vers l'est
        # 4 = piques orientés vers le sud
        if cf == 1 :
            self.image = pygame.image.load("images/piege/spikes1.png").convert_alpha()
        elif cf == 2 :
            self.image = pygame.image.load("images/piege/spikes2.png").convert_alpha()
        elif cf == 3 :
            self.image = pygame.image.load("images/piege/spikes3.png").convert_alpha()
        elif cf == 4 :
            self.image = pygame.image.load("images/piege/spikes4.png").convert_alpha()

        self.image = pygame.transform.flip(self.image, False, True)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
