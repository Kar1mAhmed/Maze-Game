import pygame
import main
import sys
from Helpers.button import Button


class OptionsClass:
    # def __init__(self, screen_width, screen_height):
    #     self.screen_width = screen_width
    #     self.screen_height = screen_height
    #     self.buttons_posX = screen_width / 2
    #     self.y_start = screen_height / 2 - 100
    #     self.start_menu_buttons_posY = [self.y_start, self.y_start + 150, self.y_start + 300]

    def options(screen_width, screen_height):
        buttons_posX = screen_width / 2
        y_start = screen_height / 2 - 100
        buttons_posY = [y_start, y_start + 100, y_start + 300]
        while True:
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

            main.SCREEN.fill("white")

            main.SCREEN.blit(main.BG, (0, 0))

            SOUND_BUTTON_MUTE = Button(image=None, pos=(buttons_posX, buttons_posY[0]),
                                       text_input="Mute music", font=main.get_font(60), base_color="White",
                                       hovering_color="#4cc9f0")

            SOUND_BUTTON_UnMUTE = Button(image=None, pos=(buttons_posX, buttons_posY[1]),
                                         text_input="Unmute music", font=main.get_font(60), base_color="White",
                                         hovering_color="#4361ee")

            OPTIONS_BACK = Button(image=None, pos=(buttons_posX, buttons_posY[2]),
                                  text_input="BACK", font=main.get_font(75), base_color="White",
                                  hovering_color="#ff006e")

            for button in [OPTIONS_BACK, SOUND_BUTTON_MUTE, SOUND_BUTTON_UnMUTE]:
                button.changeColor(OPTIONS_MOUSE_POS)
                button.update(main.SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                        main.main_menu()
                    if SOUND_BUTTON_MUTE.checkForInput(OPTIONS_MOUSE_POS):
                        main.mixer.music.set_volume(0)
                    if SOUND_BUTTON_UnMUTE.checkForInput(OPTIONS_MOUSE_POS):
                        main.mixer.music.set_volume(0.5)


            pygame.display.update()
