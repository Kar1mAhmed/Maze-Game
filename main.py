import pygame
import sys
from pygame import mixer

from MenuScreens import OptionsFile
from MenuScreens.StartGame import ChooseYourAlgo

from Helpers.button import Button
from Helpers.Debug import debug


from settings import *

pygame.init()

##### Global Variables #####

screenXsize =  SCREEN_WIDTH
screenYsize = SCREEN_HEIGHT

fontSize = 50

buttons_posX = screenXsize / 2
y_start = screenYsize / 2 - 100 
start_menu_buttons_posY = [y_start, y_start + 150, y_start + 300]

SCREEN = pygame.display.set_mode((screenXsize, screenYsize))
BG = pygame.image.load("assets/Images/Background3.png")
pygame.display.set_caption("Fire Fighter")


mixer.music.load('assets/Sounds/StrangerThings.wav')
mixer.music.play(-1)


def get_font(size):  # Returns font sized
    return pygame.font.Font("assets/Font/Righteous-Regular.ttf", size)


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(110).render("Fire Fighter", True, "White")

        MENU_RECT = MENU_TEXT.get_rect(center=(buttons_posX, 80))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Images/PlayRect.png"),
                            pos=(buttons_posX, start_menu_buttons_posY[0]),
                            text_input="PLAY", font=get_font(55), base_color="White", hovering_color="#3a86ff")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Images/OptionsRect.png"),
                                pos=(buttons_posX, start_menu_buttons_posY[1]),
                                text_input="OPTIONS", font=get_font(55), base_color="White", hovering_color="#8338ec")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Images/QuitRect.png"),
                            pos=(buttons_posX, start_menu_buttons_posY[2]),
                            text_input="QUIT", font=get_font(55), base_color="White", hovering_color="#ff006e")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    ChooseYourAlgo(screenXsize, screenYsize)
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    OptionsFile.options(screenXsize, screenYsize)
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()


if __name__ == '__main__':
    main_menu()
