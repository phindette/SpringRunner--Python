import pygame
from constantes import *

class SpriteSheet(object):

    def __init__(self, file_name):
        self.sprite_sheet = pygame.image.load(file_name).convert()

    def get_image(self, x, y, width, height):
        image = pygame.Surface([width, height]).convert()
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(WHITE)
        return image

def loadSprites(list,sprites,nbimage,largeur,hauteur):
    for i in range(0,nbimage):
        image = sprites.get_image(largeur*i,0,largeur,hauteur)
        for j in range(0,3):
            list.append(image)

def loadSpritesInverted(list,sprites,nbimage,largeur,hauteur):
    for i in range(0,nbimage):
        image = sprites.get_image(largeur*i,0,largeur,hauteur)
        image = pygame.transform.flip(image, True, False)
        for j in range(0,3):
            list.append(image)

def initTabSprites(nbAnimations):
    spritesCollection = {}
    for i in range(0,nbAnimations):
        spritesCollection[i] = []
    return spritesCollection
