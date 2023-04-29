import pygame
import time

class Bomb(pygame.sprite.Sprite):
    def __init__(self,pos, groups) -> None:
        super().__init__(groups)
        
        self.image = pygame.image.load('assets/Images/time-bomb.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hit_box = self.rect.inflate(0, 0) # change the size of rect
        
        
        self.end_beb = pygame.mixer.Sound('assets/Sounds/last_beb.wav')
        self.end_beb.set_volume(0.02)
        
        
        
    def last_beb(self):
        self.end_beb.play()
    
    def stop_last_beb(self):
        self.end_beb.stop()