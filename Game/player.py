import pygame
from Setting import *


class Player(pygame.sprite.Sprite):
    def __init__(self,pos, groups) -> None:
        super().__init__(groups)
        
        self.image = pygame.image.load('Game/imgs/hero.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        