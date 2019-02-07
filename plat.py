import pygame
from constantes import *

class Plat(pygame.sprite.Sprite):
    def __init__(self,game,x,y,cd=1):
        self._layer = 1
        self.groups = game.les_sprites,game.plateformes
        pygame.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        if cd == 1 :
            self.image = pygame.image.load("images/plateform/test_platform_1.png").convert_alpha()
        elif cd == 2 :
            self.image = pygame.image.load("images/plateform/test_platform_1droite.png").convert_alpha()
        elif cd == 3 :
            self.image = pygame.image.load("images/plateform/test_platform_1enBas.png").convert_alpha()
        elif cd == 4 :
            self.image = pygame.image.load("images/plateform/test_platform_2droite.png").convert_alpha()
        elif cd == 5 :
            self.image = pygame.image.load("images/plateform/test_platform_2enBas.png").convert_alpha()
        elif cd == 6 :
            self.image = pygame.image.load("images/plateform/test_platform_2.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
