import pygame, sys, time
from Game.level import Level
import Game.maze_creator
import main

from MenuScreens.winScreen import Win

from Helpers.Debug import debug

class Game:
    def __init__(self, WIDTH=1920, HEIGHT=1080):
        self.Width = WIDTH
        self.Height = HEIGHT
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.display = pygame.display.get_surface()

        pygame.display.set_caption("Fire Fighter")
        self.clock = pygame.time.Clock()
        
        self.level = Level()
    
    def run(self):
        pygame.mixer.init()
        game_sound = pygame.mixer.Sound("assets/Sounds/background.wav")
        game_sound.set_volume(0.01)
        game_sound.play()
        start_time = time.time()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        main.mixer.music.set_volume(0.5)
                        main.main_menu()
                        break
            self.screen.fill('#2b2d42')
            self.level.run()
            
            debug(f"Collected {self.level.player.collected_kids} of {self.level.num_of_kids}")
            if self.level.player.collected_kids == self.level.num_of_kids:
                finish_time = time.time() - start_time
                self.level = Level()
                game_sound.set_volume(0.0)
                main.mixer.music.unpause()
                Win(self.Width, self.Height, finish_time, self.level.num_of_kids, (self.level.rows, self.level.cols))
                break
                
            pygame.display.update()
            self.clock.tick(60)

if __name__ == "__main__":
    game = Game()
    game.run()