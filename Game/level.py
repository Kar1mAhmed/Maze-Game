import pygame
from Setting import *
from tile import Tile
from player import Player
from Debug import debug

class Level:
    def __init__(self):
        
        # get the display surface
        self.display = pygame.display.get_surface()
        
        # Sprit Group setup
        self.visible_sprites = YSortCameraGroup()
        self.obstacles_sprites = pygame.sprite.Group()
        
        #sprite setup   
        self.create_map()
        
    def create_map(self):
        for row_index, row in enumerate(MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'W':
                    Tile((x,y), [self.visible_sprites, self.obstacles_sprites])
                if col == 'P':
                    self.player = Player((x,y), [self.visible_sprites], self.obstacles_sprites)

            
    def run(self):
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()



class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self) -> None:
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()
        
    def custom_draw(self, player):
        
        # getting the offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height
        
        
        #for sprite in self.sprites():
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery): # render by z index
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)