import pygame
from constantes import *

class Goal(pygame.sprite.Sprite):
    def __init__(self,game,x,y):
        self._layer = 1
        self.groups = game.les_sprites,game.goals
        pygame.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        self.image = pygame.image.load("chara_walking_anim_2.gif").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
