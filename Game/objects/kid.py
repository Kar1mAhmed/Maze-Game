import pygame
import random
import os

class Kid(pygame.sprite.Sprite):
    def __init__(self, pos, groups, character_size=30):
        super().__init__(groups)
        
        # Getting random kid photo
        kid_photo = str(random.randint(0,3))
        self.image =pygame.image.load(os.path.join("assets\Images", f"kid-{kid_photo}.png")).convert_alpha()
        
        self.Width = character_size
        self.Height = character_size
        
        self.image = pygame.transform.scale(self.image, (self.Width, self.Height))

        self.rect = self.image.get_rect(topleft = pos)
        self.hit_box = self.rect.inflate(0, 0) # change the size of rect
        
        
        self.sound = pygame.mixer.Sound('assets/Sounds/kid_sound.wav')
        self.sound.set_volume(0.8)
        
    def yay(self):
        self.sound.play()
        