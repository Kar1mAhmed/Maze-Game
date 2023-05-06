import pygame, sys, time
from Game.level import Level
import Game.maze.maze_creator
import main

from MenuScreens.winScreen import Win

from Helpers.Debug import debug
from settings import *



class Game:
    def __init__(self, WIDTH=SCREEN_WIDTH, HEIGHT=SCREEN_HEIGHT):
        self.Width = WIDTH
        self.Height = HEIGHT
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.display = pygame.display.get_surface()

        pygame.display.set_caption("Fire Fighter")
        self.clock = pygame.time.Clock()
        
        self.game_sound = pygame.mixer.Sound("assets/Sounds/background.wav")
        self.game_sound.set_volume(0.0)
        self.game_sound.play(-1)

        self.level = None
        self.end_time = None
        
        self.win = True
    

                
    def run(self):   
            
        self.level = Level()
        self.end_time = self.level.level_time

        start_time = time.time()
        
        while True:
            self.game_sound.set_volume(0.02)
            current_time = time.time() - start_time
            self.handel_bomb_sound(current_time)
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.esc()
                        break
                    if event.key == pygame.K_e:
                        self.level.draw_path(Algo='DFS')
                    if event.key == pygame.K_q:
                        self.level.draw_path(Algo='BFS')
            self.screen.fill('#2b2d42')
            self.level.run()
            
            time_left = self.end_time - current_time
            debug("Press E to use DFS ability", y=50)
            debug("Press ESC to end the game")
            debug(f'Time Left : {(time_left):.2f}',x=SCREEN_WIDTH / 2)
            debug(f'Rescued {self.level.player.collected_kids} of {self.level.num_of_kids}',x=SCREEN_WIDTH/2, y=40)
            if self.level.player.collected_kids == self.level.num_of_kids or time_left <= 0:
                if time_left < 0:
                    self.win = False
                self.game_end(start_time, self.level.player.collected_kids)
                break
                
            pygame.display.update()
            self.clock.tick(60)

    def esc(self):
        self.game_sound.stop()
        main.mixer.music.set_volume(0.2)
        main.main_menu()
        
    def game_end(self, start_time, collected_kids):
        self.level.Bomb.stop_last_beb()
        finish_time = time.time() - start_time
        self.level = Level()
        self.game_sound.set_volume(0.0)
        main.mixer.music.set_volume(0.2)
        Win(self.Width, self.Height, finish_time, collected_kids, (self.level.rows, self.level.cols), self.win)
        
        
    def handel_bomb_sound(self, current_time):
        if self.end_time - current_time < 7:
            self.level.Bomb.last_beb()
            
            
            
if __name__ == "__main__":
    game = Game()
    game.run()