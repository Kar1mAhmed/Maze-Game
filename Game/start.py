import pygame, sys, time
from Game.level import Level
import Game.maze_creator
import main

from MenuScreens.winScreen import Win

from Helpers.Debug import debug

class Game:
    def __init__(self, WIDTH=1920, HEIGHT=1080, end_time =15):
        self.Width = WIDTH
        self.Height = HEIGHT
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.display = pygame.display.get_surface()

        pygame.display.set_caption("Fire Fighter")
        self.clock = pygame.time.Clock()
        
        self.game_sound = pygame.mixer.Sound("assets/Sounds/background.wav")
        self.game_sound.set_volume(0.02)
        
        self.level = Level()
        self.end_time = end_time
    
    def esc(self):
        self.game_sound.stop()
        main.mixer.music.set_volume(0.5)
        main.mixer.music.unpause()
        main.main_menu()
        
    def game_end(self, start_time, collected_kids):
        self.level.Bomb.stop_last_beb()
        finish_time = time.time() - start_time
        self.level = Level()
        self.game_sound.set_volume(0.0)
        main.mixer.music.unpause()
        Win(self.Width, self.Height, finish_time, collected_kids, (self.level.rows, self.level.cols))
        
        
    def handel_bomb_sound(self, current_time):
        if self.end_time - current_time < 7:
            self.level.Bomb.last_beb()

                
    def run(self):       
        start_time = time.time()
        self.game_sound.play()
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
            self.screen.fill('#2b2d42')
            self.level.run()
            
            time_left = self.end_time - current_time
            debug(f'Time Left : {(time_left):.2f}')
            if self.level.player.collected_kids == self.level.num_of_kids or time_left <= 0:
                self.game_end(start_time, self.level.player.collected_kids)
                break
                
            pygame.display.update()
            self.clock.tick(60)

if __name__ == "__main__":
    game = Game()
    game.run()