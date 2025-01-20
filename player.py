import pygame
from config import SCREEN_WIDTH, MAP_COLLISION_LAYER


class SpriteSheet(object):
    def __init__(self, fileName):
        self.sheet = pygame.image.load(fileName)

    def image_at(self, rectangle):
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size, pygame.SRCALPHA, 32).convert_alpha()
        image.blit(self.sheet, (0, 0), rect)
        return image
    
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        
        #load spritesheet of frames for this player
        self.sprites = SpriteSheet("assets/bunnyPlayer.png")
        self.stillRight = self.sprites.image_at((128, 32, 32, 32))
        self.stillLeft = self.sprites.image_at((128, 64, 32, 32))

        #list of frames for each animation
        self.runningRight = (self.sprites.image_at((0, 32, 32, 32)),
                             self.sprites.image_at((32, 32, 32, 32)),
                             self.sprites.image_at((64, 32, 32, 32)),
                             self.sprites.image_at((128, 32, 32, 32)),
                             self.sprites.image_at((160, 32, 32, 32)),
                             self.sprites.image_at((192, 32, 32, 32)),
                             self.sprites.image_at((224, 32, 32, 32)))
        
        self.runningLeft = (self.sprites.image_at((0, 64, 32, 32)),
                             self.sprites.image_at((32, 64, 32, 32)),
                             self.sprites.image_at((64, 64, 32, 32)),
                             self.sprites.image_at((128, 64, 32, 32)),
                             self.sprites.image_at((160, 64, 32, 32)),
                             self.sprites.image_at((192, 64, 32, 32)),
                             self.sprites.image_at((224, 64, 32, 32)))
        
        self.jumpingRight = (self.sprites.image_at((128, 32, 32, 32)),
                             self.sprites.image_at((96, 32, 32, 32)))
        
        self.jumpingLeft = (self.sprites.image_at((128, 64, 32, 32)),
                             self.sprites.image_at((96, 64, 32, 32)))
        
        self.image = self.stillRight

        #set player position
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        #set speed and direction
        self.changeX = 0
        self.changeY = 0
        self.direction = "right"

        #bool to check if player is running, current running frame, and time since last frame change
        self.running = False
        self.runningFrame = 0
        self.runningTime = pygame.time.get_ticks()

        #player current level, set after object initialized in game constructor
        self.currentLevel = None

    def update(self):
        #update player position by change
        self.rect.x += self.changeX

        #get tiles in collision layer that player is currently touching
        tileHitList = pygame.sprite.spritecollide(self, self.currentLevel.layers[MAP_COLLISION_LAYER].tiles, False)

        #move player to correct side of that block
        for tile in tileHitList:
            if self.changeX > 0:
                self.rect.right = tile.rect.left
            else:
                self.rect.left = tile.rect.right

        #move screen if player reaches screen bounds
        if self.rect.right >= SCREEN_WIDTH - 200:
            difference = self.rect.right - (SCREEN_WIDTH - 200)
            self.rect.right = SCREEN_WIDTH - 200
            self.currentLevel.shiftLevel(-difference)

        if self.rect.left <= 200:
            difference = 200 - self.rect.left
            self.rect.left = 200
            self.currentLevel.shiftLevel(difference)

        #update player position by change
        self.rect.y += self.changeY

        #get tiles in collision layer that player is currently touching
        tileHitList = pygame.sprite.spritecollide(self, self.currentLevel.layers[MAP_COLLISION_LAYER].tiles, False)

        if len(tileHitList) > 0: #if there are tiles in the list
            #move player to correct side of the tile, update player frame ??????????????????
            for tile in tileHitList:
                if self.changeY > 0:
                    self.rect.bottom = tile.rect.top
                    self.changeY = 1
                    if self.direction == "right":
                        self.image = self.stillRight
                    else:
                        self.image = self.stillLeft
                else:
                    self.rect.top = tile.rect.bottom
                    self.changeY = 0
    
        else: #if there are no tiles in the list
            #update player change for jumping/falling and player frame
            self.changeY += 0.3 # gravity i think
            if self.changeY > 0:
                if self.direction == "right":
                    self.image = self.jumpingRight[1]
                else:
                    self.image = self.jumpingLeft[1]
        #if player is on ground and running, update running animation
        if self.running and self.changeY == 1:
            if self.direction == "right":
                self.image = self.runningRight[self.runningFrame]
            else:
                self.image = self.runningLeft[self.runningFrame]
        
        #when correct amount of time has passed, go to next frame
        if pygame.time.get_ticks() - self.runningTime > 50:
            self.runningTime = pygame.time.get_ticks()
            if self.runningFrame == 6:
                self.runningFrame = 0
            else:
                self.runningFrame += 1

    #make player jump
    def jump(self):
        #check if player is on ground
        self.rect.y += 2
        tileHitList = pygame.sprite.spritecollide(self, self.currentLevel.layers[MAP_COLLISION_LAYER].tiles, False)
        self.rect.y -= 2
        if len(tileHitList) > 0:
            if self.direction == "right":
                self.image = self.jumpingRight[0]
            else:
                self.image = self.jumpingLeft[0]
            self.changeY = -6

    #move right
    def goRight(self):
        self.direction = "right"
        self.running = True
        self.changeX = 3

    #move left
    def goLeft(self):
        self.direction = "left"
        self.running = True
        self.changeX = -3

    #stop moving
    def stop(self):
        self.running = False
        self.changeX = 0
        
    #draw player
    def draw(self, screen):
        screen.blit(self.image, self.rect)


