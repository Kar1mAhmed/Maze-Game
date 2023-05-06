import pygame
import main
import sys
from Helpers.button import Button

import settings


def options(screen_width, screen_height):
    buttons_posX = screen_width / 2
    y_start = screen_height / 2 
    buttons_posY = [y_start - 300 ,y_start - 200, y_start - 100, y_start , y_start + 150 ,y_start + 300]
    
    Music_On = True
    Music_label = "Mute Music"
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        main.SCREEN.fill("white")

        main.SCREEN.blit(main.BG, (0, 0))

        info = Button(image=None, pos=(buttons_posX, 50),
                            text_input="Left Click to increase - Right Click to decrease",
                            font=main.get_font(20), base_color="White", hovering_color="White")

        Maze_rows = Button(image=None, pos=(buttons_posX, buttons_posY[0]),
                            text_input=f"Number of Maze Rows\t {settings.Number_of_rows}",
                            font=main.get_font(40), base_color="White", hovering_color="#7400b8")
        
        Maze_Cols = Button(image=None, pos=(buttons_posX, buttons_posY[1]),
                            text_input=f"Number of Maze Columns\t {settings.Number_of_cols}",
                            font=main.get_font(40), base_color="White", hovering_color="#6930c3")
        
        Kids = Button(image=None, pos=(buttons_posX, buttons_posY[2]),
                        text_input=f"Number of Kids\t {settings.Num_of_kids}",
                        font=main.get_font(40), base_color="White", hovering_color="#5e60ce")
        
        Time = Button(image=None, pos=(buttons_posX, buttons_posY[3]),
                        text_input=f"Bomb Time :\t {settings.Level_time}",
                        font=main.get_font(40), base_color="White", hovering_color="#5390d9")

        SOUND_BUTTON_MUTE = Button(image=None, pos=(buttons_posX, buttons_posY[4]),
                                   text_input=Music_label, font=main.get_font(60), base_color="White",
                                   hovering_color="#4cc9f0")


        OPTIONS_BACK = Button(image=None, pos=(buttons_posX, buttons_posY[5]),
                              text_input="BACK", font=main.get_font(75), base_color="White",
                              hovering_color="#ff006e")

        for button in [OPTIONS_BACK, SOUND_BUTTON_MUTE, Kids, Maze_rows, Maze_Cols, Time, info]:
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
                        
                if Time.checkForInput(OPTIONS_MOUSE_POS):
                    if event.button == 1:
                        if settings.Level_time == "default":
                            settings.Level_time = 10
                        else:
                            settings.Level_time += 5
                    elif event.button == 3:
                        if settings.Level_time != "default":
                            settings.Level_time -=5
                        if settings.Level_time == 'default' or settings.Level_time <= 0:
                            settings.Level_time = "default"
                            
                if Kids.checkForInput(OPTIONS_MOUSE_POS):
                    if event.button == 1:
                        if settings.Num_of_kids < 100:
                            settings.Num_of_kids +=1
                    elif event.button == 3:
                        if settings.Num_of_kids > 1:
                            settings.Num_of_kids -= 1
                            
                if Maze_Cols.checkForInput(OPTIONS_MOUSE_POS):
                    if event.button == 1:
                        if settings.Number_of_cols < 100:
                            settings.Number_of_cols += 5
                    elif event.button == 3:
                        if settings.Number_of_cols > 5:
                            settings.Number_of_cols -= 5

                if Maze_rows.checkForInput(OPTIONS_MOUSE_POS):
                    if event.button == 1:
                        if settings.Number_of_rows < 100:
                            settings.Number_of_rows += 5
                    elif event.button == 3:
                        if settings.Number_of_rows > 5:
                            settings.Number_of_rows -= 5


        pygame.display.update()
