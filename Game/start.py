import pygame, sys
from Game.level import Level
import Game.maze_creator
import main


class Game:
    def __init__(self, WIDTH=1920, HEIGHT=1080):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.display = pygame.display.get_surface()

        pygame.display.set_caption("Fire Fighter")
        self.clock = pygame.time.Clock()
        
        self.level = Level()
    
    def run(self):
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
            self.screen.fill('white')
            self.level.run()
            pygame.display.update()
            self.clock.tick(60)

if __name__ == "__main__":
    game = Game()
    game.run()