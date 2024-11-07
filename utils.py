import pygame
from pygame.locals import *

def arrows_control(sprite, ground_rect, GRAVITY, JUMP_STRENGTH=-10, MOVE_SPEED=5):
    keys = pygame.key.get_pressed()
    if keys[K_RIGHT]:
        sprite.rect.x += MOVE_SPEED
    elif keys[K_LEFT]:
        sprite.rect.x -= MOVE_SPEED

    #jumping
    if keys[K_UP] and not sprite.is_jumping: #cant jump if already jumping
        sprite.velocity_y = JUMP_STRENGTH
        sprite.is_jumping = True

    sprite.velocity_y += GRAVITY 
    sprite.rect.y += sprite.velocity_y

    if sprite.rect.y >= ground_rect.y - sprite.rect.height:
        sprite.rect.y = ground_rect.y - sprite.rect.height
        sprite.velocity_y = 0 #reset vel when on the ground
        sprite.is_jumping = False

    # note: whats up with python, it allowed me to just attach the 
    # is_jumping attribute to the sprite object even though it
    # literally doesnt exist in the class definition or outside of
    # this function at all
    # my c++ mind cannot comprehend
    

def handle_collision(player, allsprites):
    collided_sprites = pygame.sprite.spritecollide(player, allsprites, dokill=False)
    for sprite in collided_sprites:
        if sprite != player:
            allsprites.remove(sprite)


