import pygame
import random
from Game.tile import Tile
from Game.player import Player
from Game.maze_creator import maze
from Game.kid import Kid
from Helpers.Debug import debug

class Level:
    def __init__(self, rows=20, cols=20, num_of_kids=3):
        
        # get the display surface
        self.display = pygame.display.get_surface()
        self.rows = rows
        self.cols = cols
        
        my_maze = maze(rows=rows, cols=cols)
        my_maze.CreateMaze()
        self.Map = my_maze.maze_map
        
        # Sprit Group setup
        self.visible_sprites = YSortCameraGroup()
        self.obstacles_sprites = pygame.sprite.Group()
        self.kids = pygame.sprite.Group()
        
        self.num_of_kids = num_of_kids
        self.block_size = 64

        #sprite setup   
        self.create_map()
        
    def create_map(self):
        for key, values in self.Map.items():
            col_index, row_index = key
            col_index-=1
            row_index-=1
            if values['N'] == 0:
                Tile((row_index * self.block_size, col_index * self.block_size), [self.visible_sprites, self.obstacles_sprites], 'horz.png')
            if values['S'] == 0:
                 Tile((row_index * self.block_size, (col_index + 1) * self.block_size), [self.visible_sprites, self.obstacles_sprites], 'horz.png')
            if values['W'] == 0:
                Tile((row_index * self.block_size, col_index * self.block_size), [self.visible_sprites, self.obstacles_sprites], 'vert.png')
            if values['E'] == 0:
                Tile(((row_index + 1) * self.block_size, col_index * self.block_size), [self.visible_sprites, self.obstacles_sprites], 'vert.png')
                
            
            
        for _ in range(self.num_of_kids):   
            
            kid_x = random.randint(self.cols / 4, self.cols - 1) * self.block_size + 10
            kid_y = random.randint(self.rows / 4, self.rows - 1)* self.block_size + 10

            self.kid = Kid((kid_x , kid_y ), [self.visible_sprites, self.kids])
            
        self.player = Player((self.block_size / 3, self.block_size / 3), [self.visible_sprites], self.obstacles_sprites, self.kids, self.visible_sprites)

            
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