import pygame

class Plateform(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((w, h))
        #pygame.image.load("bloc.png").convert()
        self.image = pygame.image.load("images/plateform/test_platform_1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
