import pygame
import os


class Agent:
    def __init__(self, mapW, mapH):
        self.Width = mapW * mapH * 0.00005
        self.Height = mapW * mapH * 0.00005
        self.speed = 2

        self.mapW = mapW
        self.mapH = mapH

        self.rec = pygame.Rect(100, 300, self.Width, self.Height)


        AGENT_RIGHT_IMG = pygame.image.load(os.path.join("assets/Images", "heroE.png"))
        AGENT_RIGHT = pygame.transform.scale(AGENT_RIGHT_IMG, (self.Width, self.Height))

        # THE IMAGE OF AGENT WHEN MOVE LEFT
        AGENT_LEFT_IMG = pygame.image.load(os.path.join("assets/Images", "heroW.png"))
        AGENT_LEFT = pygame.transform.scale(AGENT_LEFT_IMG, (self.Width, self.Height))

        # THE IMAGE OF AGENT WHEN MOVE UP
        AGENT_UP_IMG = pygame.image.load(os.path.join("assets/Images", "heroN.png"))
        AGENT_UP = pygame.transform.scale(AGENT_UP_IMG, (self.Width, self.Height))

        # THE IMAGE OF AGENT WHEN MOVE Down
        AGENT_Down_IMG = pygame.image.load(os.path.join("assets/Images", "hero.png"))
        AGENT_Down = pygame.transform.scale(AGENT_Down_IMG, (self.Width, self.Height))

        self.Agent_shapes = {
            'Right': AGENT_RIGHT,
            'Left': AGENT_LEFT,
            'Up': AGENT_UP,
            'Down': AGENT_Down
        }

    def move(self, shape):
        key = pygame.key.get_pressed()
        last = shape
        if key[pygame.K_a]:  # LEFT
            newX = self.rec.x - self.speed
            self.rec.x = max(0, newX)
            last = 'Left'

        if key[pygame.K_d]:  # RIGHT
            newX = self.rec.x + self.speed
            self.rec.x = min(self.mapW - (self.Width / 1.3), newX)
            last = 'Right'


        if key[pygame.K_w]:  # Up
            newY = self.rec.y - self.speed
            self.rec.y = max(0, newY)
            last = 'Up'


        if key[pygame.K_s]:  # Down
            newY = self.rec.y + self.speed
            self.rec.y = min(self.mapH - self.Height, newY)
            last = 'Down'

        return last
