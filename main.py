import pygame, pytmx
from game import Game
from config import SCREEN_WIDTH, SCREEN_HEIGHT

def main():
    pygame.init()
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    pygame.display.set_caption("sc platformer")
    clock = pygame.time.Clock()

    done = False
    game = Game()

    while not done:
        done = game.processEvents()
        game.runLogic()
        game.draw(screen)
        clock.tick(30)
    
    pygame.quit()

main()

            
            

        


