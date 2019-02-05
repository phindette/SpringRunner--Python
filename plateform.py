import pygame

class Plateform(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((w, h))
        self.image.fill((250,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
