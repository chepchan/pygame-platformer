import pygame, sys
from pygame.locals import *
import sprites, utils

pygame.init()
FPS = 30
fpsClock = 30
fpsClock = pygame.time.Clock()

#game variables
GRAVITY = 1

DISPLAYSURF = pygame.display.set_mode((800, 600), 0, 32)
pygame.display.set_caption('game')
pygame.key.set_repeat(30,30)
running = True

def create_sprites(ground_rect):
    player = sprites.Player('kitty.png')
    player.rect.x = 400
    player.rect.y = ground_rect.y - player.rect.height
    # player.rect.y = 100

    coin = sprites.Sprite('coin.png')
    coin.rect.x = 200
    coin.rect.y = ground_rect.y - coin.rect.height - 5

    allsprites = pygame.sprite.Group(player, coin)
    return player, allsprites #returns the player-controlled sprite and the group


ground = pygame.image.load('ground.png')
ground_rect = ground.get_rect()
ground_rect.x = 0
ground_rect.y = 600 - ground_rect.height

player, allsprites = create_sprites(ground_rect)


while True:
    DISPLAYSURF.fill((130, 209, 255))
    DISPLAYSURF.blit(ground, ground_rect)
    
    allsprites.update()
    allsprites.draw(DISPLAYSURF)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame(quit)
            sys.exit()

    utils.arrows_control(player, ground_rect, GRAVITY)
    utils.handle_collision(player, allsprites)
    
    pygame.display.update()
    fpsClock.tick(FPS)

