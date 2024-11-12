import pygame
import pytmx

class Level(object):
    def __init__(self, fileName):
        self.mapObject = pytmx.load_pygame(fileName) #create map object from pyTMX
        self.layers = [] #list of layers for map
        self.levelShift = 0 #amount of level shift left/right
        for layer in range(len(self.mapObject.layers)): #create layers for each layer in the tilemap
            self.layers.append(Layer(index = layer, mapObject = self.mapObject))

    def shiftLevel(self, shiftX): #move layer left/right
        self.levelShift += shiftX
        for layer in self.layers:
            for tile in layer.tiles:
                tile.rect.x += shiftX

    def draw(self, screen): #update layer
        for layer in self.layers:
            layer.draw(screen)

class Layer(object):
    def __init__(self, index, mapObject):
        self.index = index #layer index from tiled map
        self.tiles = pygame.sprite.Group() #create group of tiles for this layer
        self.mapObject = mapObject #reference map object

        for x in range(self.mapObject.width):
            for y in range(self.mapObject.height):
                img = self.mapObject.get_tile_image(x, y, self.index)
                if img:
                    self.tiles.add(Tile(image = img, x = (x * self.mapObject.tilewidth), y = (y * self.mapObject.tileheight)))

    def draw(self, screen):
        self.tiles.draw(screen)

class Tile(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y