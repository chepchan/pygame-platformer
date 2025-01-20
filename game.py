import pygame
from player import Player
from level import Level
from config import BACKGROUND

class Game(object):
    def __init__(self):
        #level setup
        self.currentLevelNumber = 0
        self.levels = []
        self.levels.append(Level(fileName = "tiled/map.tmx")) #rename file to level1.tmx
        self.currentLevel = self.levels[self.currentLevelNumber]

        #creating a player object and set the level its in
        self.player = Player(x = 200, y = 100)
        self.player.currentLevel = self.currentLevel

    def processEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            
            # keyboard input and player movement
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.goLeft()
                elif event.key == pygame.K_RIGHT:
                    self.player.goRight()
                elif event.key == pygame.K_UP:
                    self.player.jump()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and self.player.changeX < 0:
                    self.player.stop()
                elif event.key == pygame.K_RIGHT and self.player.changeX > 0:
                    self.player.stop()
        return False
    
    def runLogic(self):
        #update player movement and collision logic
        self.player.update()

    #draw level, player
    def draw(self, screen):
        screen.fill(BACKGROUND)
        self.currentLevel.draw(screen)
        self.player.draw(screen)
        pygame.display.flip()
