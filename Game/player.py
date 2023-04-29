import pygame
import os




class Player(pygame.sprite.Sprite):
    def __init__(self,pos, groups, obstacle_sprites, kids, visible_sprites, character_size = 40) -> None:
        super().__init__(groups)        
        
        self.obstacle_sprites = obstacle_sprites # Wall places 
        self.visible_sprites = visible_sprites
        self.kids = kids
        
        self.collected_kids = 0
        
        self.direction = pygame.math.Vector2()
        self.speed = 5
        
        self.Width = character_size
        self.Height = character_size
        
        # THE IMAGE OF AGENT WHEN MOVE Right
        AGENT_RIGHT_IMG = pygame.image.load(os.path.join("assets/Images", "heroE.png")).convert_alpha()
        AGENT_RIGHT = pygame.transform.scale(AGENT_RIGHT_IMG, (self.Width, self.Height))

        # THE IMAGE OF AGENT WHEN MOVE LEFT
        AGENT_LEFT_IMG = pygame.image.load(os.path.join("assets/Images", "heroW.png")).convert_alpha()
        AGENT_LEFT = pygame.transform.scale(AGENT_LEFT_IMG, (self.Width, self.Height))

        # THE IMAGE OF AGENT WHEN MOVE UP
        AGENT_UP_IMG = pygame.image.load(os.path.join("assets/Images", "heroN.png")).convert_alpha()
        AGENT_UP = pygame.transform.scale(AGENT_UP_IMG, (self.Width, self.Height))

        # THE IMAGE OF AGENT WHEN MOVE Down
        AGENT_DOWN_IMG= pygame.image.load(os.path.join("assets/Images", "hero.png")).convert_alpha()
        AGENT_DOWN = pygame.transform.scale(AGENT_DOWN_IMG, (self.Width, self.Height))

        self.Agent_shapes = {
            'Right': AGENT_RIGHT,
            'Left': AGENT_LEFT,
            'Up': AGENT_UP,
            'Down': AGENT_DOWN
        }
        
        self.image = self.Agent_shapes["Down"]
        
        self.rect = self.image.get_rect(topleft = pos)
        self.hit_box = self.rect.inflate(0, 0)



    
    def input(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_w]:
            self.direction.y = -1
            self.image = self.Agent_shapes['Up']
        elif keys[pygame.K_s]:
            self.direction.y = 1
            self.image = self.Agent_shapes['Down']
        else:
            self.direction.y = 0
            
        if keys[pygame.K_a]:
            self.direction.x = -1
            self.image = self.Agent_shapes['Left']
        elif keys[pygame.K_d]:
            self.direction.x = 1
            self.image = self.Agent_shapes['Right']
        else:
            self.direction.x = 0
    
    def move(self, speed):
        
        self.collision_with_kid()
        
        if self.direction.magnitude() != 0  : # to avoid division by zero
            self.direction = self.direction.normalize()
        
        self.hit_box.x += self.direction.x * speed
        
        if self.direction.x != 0 :
            self.collision('horizontal')
        
        self.hit_box.y += self.direction.y * speed
        
        if self.direction.y !=0 :
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
    
    
    def collision_with_kid(self):
        
        for kid in self.kids:
            if kid.hit_box.colliderect(self.hit_box):
                kid.yay()
                self.kids.remove(kid)
                self.visible_sprites.remove(kid)
                self.collected_kids+=1  
                    
    def update(self):
        self.input()
        self.move(self.speed)