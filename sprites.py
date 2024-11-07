import pygame
from pygame.locals import *    

class Sprite(pygame.sprite.Sprite) :
    def __init__(self, img_path) :
        super().__init__()

        self.image = pygame.image.load(img_path)
        self.rect = self.image.get_rect()

class Player(Sprite):
    def __init__(self, img_path):
        super().__init__(img_path)
        self.velocity_y = 0
        self.on_ground = False