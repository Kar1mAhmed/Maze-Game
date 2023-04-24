import Main
import pygame
from Helpers.Button import Button
import sys
from MenuScreens import Play


def ChooseYourAlgo(screen_width, screen_height):
    buttons_posX = screen_width / 2
    y_start = screen_height / 2 - 100
    buttons_posY = [y_start - 100, y_start, y_start + 100, y_start + 200, y_start + 350]
    while True:
        Main.SCREEN.blit(Main.BG, (0, 0))

        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        BFS = Button(image=None, pos=(buttons_posX, buttons_posY[0]),
                     text_input="BFS", font=Main.get_font(40), base_color="White", hovering_color="#06d6a0")
        DFS = Button(image=None, pos=(buttons_posX, buttons_posY[1]),
                     text_input="DFS", font=Main.get_font(40), base_color="White", hovering_color="#06d6a0")
        Aastrec = Button(image=None, pos=(buttons_posX, buttons_posY[2]),
                         text_input="A*", font=Main.get_font(40), base_color="White", hovering_color="#06d6a0")
        START_NEW_GAME = Button(image=None, pos=(buttons_posX, buttons_posY[3]),
                                text_input="start new game", font=Main.get_font(40), base_color="White",
                                hovering_color="Green")
        Menu_BACK = Button(image=None, pos=(buttons_posX, buttons_posY[4]),
                           text_input="BACK", font=Main.get_font(50), base_color="White", hovering_color="#ff006e")

        for button in [BFS, DFS, Aastrec, START_NEW_GAME, Menu_BACK]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(Main.SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if START_NEW_GAME.checkForInput(PLAY_MOUSE_POS):
                    Main.mixer.music.set_volume(0.15)
                    Play.gameLoop()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Menu_BACK.checkForInput(PLAY_MOUSE_POS):
                    Main.main_menu()

        pygame.display.update()
