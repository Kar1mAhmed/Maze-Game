import pygame
from GameObjects.Agent import Agent
from GameObjects.BlockControl import BlocksControl

import main

FPS = 120

WIDTH, HEIGHT = 1920, 1080
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
MAP_COLOR = "#e2fdff"

Agent = Agent(WIDTH, HEIGHT)

BlockControl = BlocksControl(5, WIDTH, HEIGHT, 'assets/Images/0000.png')
Kids = BlocksControl(1, WIDTH, HEIGHT, 'assets/Images/kid-1.png')


def render(agent, shape):
    WIN.fill(MAP_COLOR)
    WIN.blit(agent.Agent_shapes[shape], (agent.rec.x, agent.rec.y))
    for block in BlockControl.blocks:
        WIN.blit(block.block_shape, (block.x, block.y))
    for kid in Kids.blocks:
        WIN.blit(kid.block_shape, (kid.x, kid.y))
    pygame.display.update()
    pygame.display.flip()



def gameLoop():
    clock = pygame.time.Clock()
    run = True
    shape = 'Right'
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # checking if Exit button pressed
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                    main.main_menu()
        shape = Agent.move(shape)
        render(Agent, shape)


    pygame.quit()


if __name__ == "__main__":
    gameLoop()
