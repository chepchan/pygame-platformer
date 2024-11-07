import pygame, sys
from pygame.locals import *

# THIS FILE IS FULL OF IDEAS THAT HEVE YET TO BE IMPLEMENTED

# jumping animation (change to another image of the player when jumping)

STANDING_SURFACE = pygame.transform.scale(pygame.image.load("image path"),(48, 64))
JUMPING_SURFACE = pygame.transform.scale(pygame.image.load("image path"),(48, 64))

# implement jumping

# Y_GRAVITY = 1
# JUMP_HEIGHT = 20
# Y_VELOCITY = JUMP_HEIGHT
# jumping = False  # i thing this is only used for the animation?

# def gravity(player):
#     keys = pygame.key.get_pressed() #returns a dictionary of all the keys and whether or not theyre being pressed
#     if keys[pygame.K_UP]:
#         jumping = True
#         player.rect.y -= Y_VELOCITY #subtracting moves it up the screen
#         Y_VELOCITY -= Y_GRAVITY
#         if Y_VELOCITY < -JUMP_HEIGHT:
#             jumping = False
#             Y_VELOCITY = JUMP_HEIGHT
    

# LITERALLY THIRD ATTEMPT AT GRAVITY

def gravity(player, grav=1, y_vel=0):
    player.y_vel