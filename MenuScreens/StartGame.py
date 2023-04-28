import main
import pygame
from Helpers.button import Button
import sys
from Game.start import Game

game = Game()

def ChooseYourAlgo(screen_width, screen_height):
    buttons_posX = screen_width / 2
    y_start = screen_height / 2 - 100
    buttons_posY = [y_start - 100, y_start, y_start + 100, y_start + 200, y_start + 350]
    while True:
        main.SCREEN.blit(main.BG, (0, 0))

        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        BFS = Button(image=None, pos=(buttons_posX, buttons_posY[0]),
                     text_input="BFS", font=main.get_font(40), base_color="White", hovering_color="#06d6a0")
        DFS = Button(image=None, pos=(buttons_posX, buttons_posY[1]),
                     text_input="DFS", font=main.get_font(40), base_color="White", hovering_color="#06d6a0")
        Aastrec = Button(image=None, pos=(buttons_posX, buttons_posY[2]),
                         text_input="A*", font=main.get_font(40), base_color="White", hovering_color="#06d6a0")
        START_NEW_GAME = Button(image=None, pos=(buttons_posX, buttons_posY[3]),
                                text_input="Enter The Game", font=main.get_font(40), base_color="White",
                                hovering_color="#758bfd")
        Menu_BACK = Button(image=None, pos=(buttons_posX, buttons_posY[4]),
                           text_input="BACK", font=main.get_font(50), base_color="White", hovering_color="#ff006e")

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
                    game.run()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Menu_BACK.checkForInput(PLAY_MOUSE_POS):
                    main.main_menu()

        pygame.display.update()
