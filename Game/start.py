import pygame, sys
from Game.level import Level
import Game.maze_creator


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
            
            self.screen.fill('white')
            self.level.run()
            pygame.display.update()
            self.clock.tick(120)

if __name__ == "__main__":
    game = Game()
    game.run()