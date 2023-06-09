import pygame
import random
import copy

from Game.objects.tile import Tile
from Game.objects.player import Player
from Game.objects.kid import Kid
from Game.objects.bomb import Bomb

from Game.maze.maze_solver import MazeSolverDFS
from Game.maze.maze_solver import MazeSolverBFS

from Game.maze.maze_creator import maze

import settings as s


class Level:
    def __init__(self):
        rows, cols, num_of_kids, time = s.get_settings()
        # get the display surface
        self.display = pygame.display.get_surface()
        self.rows = rows
        self.cols = cols
        
        my_maze = maze(rows=rows, cols=cols)
        my_maze.CreateMaze(pattern='h', loopPercent=10)
        self.Map = my_maze.maze_map
        
        map_copy = copy.deepcopy(self.Map)
        self.solver_DFS = MazeSolverDFS(map_copy)        
        self.solver_BFS = MazeSolverBFS(map_copy)
        
        # Sprit Group setup
        self.visible_sprites = YSortCameraGroup()
        self.path_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()
        self.kids = pygame.sprite.Group()
        
        self.kids_positions = []

        self.num_of_kids = num_of_kids
        self.block_size = 64
        
        if isinstance(time, int):
            self.level_time = time
        else:
            self.level_time = num_of_kids * 10 + rows + cols 

        self.visual_path = False
        self.kids_saved = 0
        #sprite setup   
        self.create_map()
        
    def create_map(self):
        for key, values in self.Map.items():
            
            col_index, row_index = key
            col_index-=1
            row_index-=1
            
            if values['N'] == 0:
                Tile((row_index * self.block_size, col_index * self.block_size), [self.visible_sprites, self.obstacles_sprites], 'horzWhite64_5.png')
            if values['S'] == 0:
                 Tile((row_index * self.block_size, (col_index + 1) * self.block_size), [self.visible_sprites, self.obstacles_sprites], 'horzWhite64_5.png')
            if values['W'] == 0:
                Tile((row_index * self.block_size, col_index * self.block_size), [self.visible_sprites, self.obstacles_sprites], 'vertWhite5_64.png')
            if values['E'] == 0:
                Tile(((row_index + 1) * self.block_size, col_index * self.block_size), [self.visible_sprites, self.obstacles_sprites], 'vertWhite5_64.png')
                
        bomb_x = self.block_size * (self.rows / 2)    + 30
        bomb_y = self.block_size * (self.cols / 2)    + 30
    
        self.Bomb = Bomb((bomb_x, bomb_y), [self.visible_sprites])
        
        
        for _ in range(self.num_of_kids):   
            SPAWN_START = 2
            BLOCK_SPAWN_POSITION = random.randint(5, 15)
            
            
            kid_block_x = random.randint(SPAWN_START, self.cols-1)
            kid_block_y = random.randint(SPAWN_START, self.rows-1)
            
            self.kids_positions.append((kid_block_y + 1, kid_block_x + 1))

            kid_x = kid_block_x * self.block_size + BLOCK_SPAWN_POSITION
            kid_y = kid_block_y * self.block_size + BLOCK_SPAWN_POSITION

            Kid((kid_x , kid_y ), [self.visible_sprites, self.kids])
            
        self.player = Player((self.block_size / 3, self.block_size / 3), [self.visible_sprites],
                                self.obstacles_sprites, self.kids, self.visible_sprites)
            
            
    def run(self):
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        
        for kid_pos in self.kids_positions:
            if kid_pos == self.player.block_position() and self.kids_saved != self.player.collected_kids:
                self.kids_positions.remove(kid_pos)
                self.kids_saved = self.player.collected_kids
                
                self.visible_sprites.remove(self.path_sprites)
                self.visual_path = False
    
                
    
    def draw_path(self, Algo='BFS'):
        
        if len(self.kids_positions) < 1:
            return
        
        solver = None
        path_img = None
        
        if Algo == "DFS":
            solver = self.solver_DFS
            path_img = 'path_yellow_20.png'
        elif Algo == "BFS":
            path_img = 'path_Red_20.png'
            solver = self.solver_BFS
        
        map_copy = copy.deepcopy(self.Map)
        solver.reset(map_copy)
        
        
        self.visible_sprites.remove(self.path_sprites)
        self.path_sprites.empty()
            
        paths = solver.get_path(self.kids_positions.copy(), self.player.block_position())
        
        
        start_transparency = 255
        transparency_step = start_transparency  / len(paths[0]) 
        
        for step, block in enumerate(paths[0]):
            current_transparency = start_transparency - step * transparency_step
            
            Tile((block[1] * self.block_size - 40, block[0] * self.block_size - 40),
                    [self.path_sprites], path_img, current_transparency)
        
        # Control the Visualization of path   
        if self.visual_path == False:
            self.visible_sprites.add(self.path_sprites)
            self.visual_path = True
        else:
            self.visible_sprites.remove(self.path_sprites)
            self.visual_path = False
            
            
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