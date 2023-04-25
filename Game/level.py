import pygame
from Setting import *
from tile import Tile
from player import Player

class Level:
    def __init__(self):
        
        # get the display surface
        self.display = pygame.display.get_surface()
        
        # Sprit Group setup
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()
        
        #sprite setup   
        self.create_map()
        
    def create_map(self):
        for row_index, row in enumerate(MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'W':
                    Tile((x,y), [self.visible_sprites])
                if col == 'P':
                    Player((x,y), [self.visible_sprites])

            
    def run(self):
        self.visible_sprites.draw(self.display)
