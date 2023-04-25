import pygame
from Setting import *


class Player(pygame.sprite.Sprite):
    def __init__(self,pos, groups, obstacle_sprites) -> None:
        super().__init__(groups)
        
        self.image = pygame.image.load('Game/imgs/hero.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hit_box = self.rect.inflate(0, -5)
        
        self.obstacle_sprites = obstacle_sprites
        
        self.direction = pygame.math.Vector2()
        self.speed = 2
    
    
    def input(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0
        
        if keys[pygame.K_a]:
            self.direction.x = -1
        elif keys[pygame.K_d]:
            self.direction.x = 1
        else:
            self.direction.x = 0
    
    def move(self, speed):
        
        if self.direction.magnitude() != 0: # to avoid division by zero
            self.direction = self.direction.normalize()
        
        self.hit_box.x += self.direction.x * speed
        self.collision('horizontal')
        
        self.hit_box.y += self.direction.y * speed
        self.collision('vertical')
        
        self.rect.center = self.hit_box.center


    def collision(self, direction):
        
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hit_box.colliderect(self.hit_box):
                    if self.direction.x > 0: # moving right
                        self.hit_box.right = sprite.hit_box.left
                    if self.direction.x < 0: # moving left
                        self.hit_box.left = sprite.hit_box.right
                    
                    
        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hit_box.colliderect(self.hit_box):
                    if self.direction.y > 0: # moving down
                        self.hit_box.bottom = sprite.hit_box.top
                    if self.direction.y < 0: # moving up
                        self.hit_box.top = sprite.hit_box.bottom
                    
    def update(self):
        self.input()
        self.move(self.speed)
        