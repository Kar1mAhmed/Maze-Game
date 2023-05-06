import pygame
import main
import sys
from Helpers.button import Button


def options(screen_width, screen_height):
    buttons_posX = screen_width / 2
    y_start = screen_height / 2 - 100
    buttons_posY = [y_start, y_start + 100, y_start + 300]
    
    Music_On = True
    Music_label = "Mute Music"
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        main.SCREEN.fill("white")

        main.SCREEN.blit(main.BG, (0, 0))

        SOUND_BUTTON_MUTE = Button(image=None, pos=(buttons_posX, buttons_posY[0]),
                                   text_input=Music_label, font=main.get_font(60), base_color="White",
                                   hovering_color="#4cc9f0")


        OPTIONS_BACK = Button(image=None, pos=(buttons_posX, buttons_posY[2]),
                              text_input="BACK", font=main.get_font(75), base_color="White",
                              hovering_color="#ff006e")

        for button in [OPTIONS_BACK, SOUND_BUTTON_MUTE]:
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
                    if Music_On:
                        main.mixer.music.stop()
                        Music_label = "UnMute Music"
                        Music_On = False
                    else:
                        main.mixer.music.play()
                        Music_label = "Mute Music"
                        Music_On = True


        pygame.display.update()
