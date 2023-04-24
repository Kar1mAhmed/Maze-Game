import main
import pygame
from Helpers.button import Button
import sys
import Play


class Algorithm(object):
    def ChooseYourAlgo(screen_width, screen_height):
        buttons_posX = screen_width / 2
        y_start = screen_height / 2 - 100
        buttons_posY = [y_start - 100, y_start, y_start + 100, y_start + 200, y_start + 350]
        while True:
            main.SCREEN.blit(main.BG, (0, 0))

            PLAY_MOUSE_POS = pygame.mouse.get_pos()

            BFS = Button(image=None, pos=(buttons_posX, buttons_posY[0]),
                         text_input="BFS", font=main.get_font(40), base_color="White", hovering_color="Green")
            DFS = Button(image=None, pos=(buttons_posX, buttons_posY[1]),
                         text_input="DFS", font=main.get_font(40), base_color="White", hovering_color="Green")
            Aastrec = Button(image=None, pos=(buttons_posX, buttons_posY[2]),
                             text_input="A*", font=main.get_font(40), base_color="White", hovering_color="Green")
            START_NEW_GAME = Button(image=None, pos=(buttons_posX, buttons_posY[3]),
                                    text_input="start new game", font=main.get_font(40), base_color="White",
                                    hovering_color="Green")
            Menu_BACK = Button(image=None, pos=(buttons_posX, buttons_posY[4]),
                               text_input="BACK", font=main.get_font(50), base_color="White", hovering_color="#E90064")

            for button in [BFS, DFS, Aastrec, START_NEW_GAME, Menu_BACK]:
                button.changeColor(PLAY_MOUSE_POS)
                button.update(main.SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if START_NEW_GAME.checkForInput(PLAY_MOUSE_POS):
                        main.mixer.music.set_volume(0.15)
                        Play.gameLoop()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Menu_BACK.checkForInput(PLAY_MOUSE_POS):
                        main.main_menu()

            pygame.display.update()
