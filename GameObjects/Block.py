import random
import pygame
import os


class Block:
    def __init__(self, mapW, mapH, path):
        self.x = random.randint(10, mapW * 0.9)
        self.y = random.randint(10, mapH * 0.9)

        self.Width = mapH * mapW * 0.00004
        self.Height = mapH * mapW * 0.00004

        block_img = pygame.image.load(os.path.join('', path))
        self.block_shape = pygame.transform.scale(block_img, (self.Width, self.Height))
