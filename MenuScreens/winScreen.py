import pygame, sys
import main


def Win(screen_width, screen_height, time_to_finish, number_of_kids, maze_size):
    buttons_posX = screen_width / 2
    y_start = screen_height / 2 - 100
    buttons_posY = [y_start, y_start + 100, y_start + 300]
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        main.SCREEN.fill("white")

        main.SCREEN.blit(main.BG, (0, 0))
        # SOUND_BUTTON_MUTE = Button(image=None, pos=(buttons_posX, buttons_posY[0]),
        #                            text_input="Mute music", font=main.get_font(60), base_color="White",
        #                            hovering_color="#4cc9f0")

        # SOUND_BUTTON_UnMUTE = Button(image=None, pos=(buttons_posX, buttons_posY[1]),
        #                              text_input="Unmute music", font=main.get_font(60), base_color="White",
        #                              hovering_color="#4361ee")

        # OPTIONS_BACK = Button(image=None, pos=(buttons_posX, buttons_posY[2]),
        #                       text_input="BACK", font=main.get_font(75), base_color="White",
        #                       hovering_color="#ff006e")

        # for button in [OPTIONS_BACK, SOUND_BUTTON_MUTE, SOUND_BUTTON_UnMUTE]:
        #     button.changeColor(OPTIONS_MOUSE_POS)
        #     button.update(main.SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        main.mixer.music.set_volume(0.5)
                        main.main_menu()
                        break
        #     if event.type == pygame.MOUSEBUTTONDOWN:
        #         if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
        #             main.main_menu()
        #         if SOUND_BUTTON_MUTE.checkForInput(OPTIONS_MOUSE_POS):
        #             main.mixer.music.pause()
        #         if SOUND_BUTTON_UnMUTE.checkForInput(OPTIONS_MOUSE_POS):
        #             main.mixer.music.unpause()

        pygame.display.update()
