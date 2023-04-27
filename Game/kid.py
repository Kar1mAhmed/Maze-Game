import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self,pos, groups, obstacle_sprites) -> None:
        super().__init__(groups)        
        self.image = pygame.image.load('Game/imgs/hero.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hit_box = self.rect.inflate(0, 0)
        
        self.obstacle_sprites = obstacle_sprites
        
        self.direction = pygame.math.Vector2()
        self.speed = 10
