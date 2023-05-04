import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self,pos, groups, img) -> None:
        super().__init__(groups)
        
        self.image = pygame.image.load('assets/Images/'+ img).convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hit_box = self.rect.inflate(0, 0) # change the size of rect