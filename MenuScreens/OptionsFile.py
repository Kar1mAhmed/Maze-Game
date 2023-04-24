import pygame
import Main
import sys
from Helpers.Button import Button


def options(screen_width, screen_height):
    buttons_posX = screen_width / 2
    y_start = screen_height / 2 - 100
    buttons_posY = [y_start, y_start + 100, y_start + 300]
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        Main.SCREEN.fill("white")

        Main.SCREEN.blit(Main.BG, (0, 0))

        SOUND_BUTTON_MUTE = Button(image=None, pos=(buttons_posX, buttons_posY[0]),
                                   text_input="Mute music", font=Main.get_font(60), base_color="White",
                                   hovering_color="#4cc9f0")

        SOUND_BUTTON_UnMUTE = Button(image=None, pos=(buttons_posX, buttons_posY[1]),
                                     text_input="Unmute music", font=Main.get_font(60), base_color="White",
                                     hovering_color="#4361ee")

        OPTIONS_BACK = Button(image=None, pos=(buttons_posX, buttons_posY[2]),
                              text_input="BACK", font=Main.get_font(75), base_color="White",
                              hovering_color="#ff006e")

        for button in [OPTIONS_BACK, SOUND_BUTTON_MUTE, SOUND_BUTTON_UnMUTE]:
            button.changeColor(OPTIONS_MOUSE_POS)
            button.update(Main.SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    Main.main_menu()
                if SOUND_BUTTON_MUTE.checkForInput(OPTIONS_MOUSE_POS):
                    Main.mixer.music.pause()
                if SOUND_BUTTON_UnMUTE.checkForInput(OPTIONS_MOUSE_POS):
                    Main.mixer.music.unpause()

        pygame.display.update()
