import pygame
from constantes import *

class Texte(pygame.sprite.Sprite):
    def __init__(self,game,texte,x=LARGEURFENETRE -100,y = 0,l=100,h=50):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.texte = texte
        self._layer = 1
        self.groups = game.les_sprites,game.textes
        pygame.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        self.font = pygame.font.SysFont("Arial",20,bold=True)
        self.textSurf = self.font.render(self.texte, 1, (255,255,255))
        #self.image = pygame.Surface((l, h))
        #self.textSurf.fill((pygame.SRCALPHA))
        self.image = pygame.Surface([l,h], pygame.SRCALPHA, 32)
        #self.image.fill((255,255,255))
        #self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        W = self.textSurf.get_width()
        H = self.textSurf.get_height()
        self.image.blit(self.textSurf, [W/2,  H/2])
        self.rect.x = x
        self.rect.y = y
    def clear(self):
        self.image.fill(pygame.SRCALPHA)
