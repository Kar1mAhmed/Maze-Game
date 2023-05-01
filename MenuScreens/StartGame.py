import main
import pygame
from Helpers.button import Button
import sys
from Game.start import Game

import settings

game = Game()

def ChooseYourAlgo(screen_width, screen_height):
    
    buttons_posX = screen_width / 2
    y_start = screen_height / 2 - 100
    buttons_posY = [y_start - 200, y_start - 100, y_start , y_start + 100 ,y_start + 300, y_start + 450]
    while True:
        main.SCREEN.blit(main.BG, (0, 0))

        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        Maze_rows = Button(image=None, pos=(buttons_posX, buttons_posY[0]),
                            text_input=f"Number of Maze Columns\t {settings.Number_of_rows}",
                            font=main.get_font(40), base_color="White", hovering_color="#06d6a0")
        
        Maze_Cols = Button(image=None, pos=(buttons_posX, buttons_posY[1]),
                            text_input=f"Number of Maze Columns\t {settings.Number_of_cols}",
                            font=main.get_font(40), base_color="White", hovering_color="#06d6a0")
        
        Kids = Button(image=None, pos=(buttons_posX, buttons_posY[2]),
                        text_input=f"Number of Kids\t {settings.Num_of_kids}",
                        font=main.get_font(40), base_color="White", hovering_color="#06d6a0")
        
        Time = Button(image=None, pos=(buttons_posX, buttons_posY[3]),
                        text_input=f"Bomb Time :\t {settings.Level_time}",
                        font=main.get_font(40), base_color="White", hovering_color="#06d6a0")
        
        START_NEW_GAME = Button(image=None, pos=(buttons_posX, buttons_posY[4]),
                                text_input="Enter The Game", font=main.get_font(60), base_color="White",
                                hovering_color="#758bfd")
        
        Menu_BACK = Button(image=None, pos=(buttons_posX, buttons_posY[5]),text_input="BACK",
                            font=main.get_font(60), base_color="White", hovering_color="#ff006e")


        for button in [Kids, Maze_rows, Maze_Cols, Time, START_NEW_GAME, Menu_BACK]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(main.SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if START_NEW_GAME.checkForInput(PLAY_MOUSE_POS):
                    main.mixer.music.pause()
                    game.run()
                    
                if Menu_BACK.checkForInput(PLAY_MOUSE_POS):
                    main.main_menu()
                    
                if Time.checkForInput(PLAY_MOUSE_POS):
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
                            
                if Kids.checkForInput(PLAY_MOUSE_POS):
                    if event.button == 1:
                        if settings.Num_of_kids < 100:
                            settings.Num_of_kids +=1
                    elif event.button == 3:
                        if settings.Num_of_kids > 1:
                            settings.Num_of_kids -= 1
                            
                if Maze_Cols.checkForInput(PLAY_MOUSE_POS):
                    if event.button == 1:
                        if settings.Number_of_cols < 100:
                            settings.Number_of_cols += 5
                    elif event.button == 3:
                        if settings.Number_of_cols > 5:
                            settings.Number_of_cols -= 5

                if Maze_rows.checkForInput(PLAY_MOUSE_POS):
                    if event.button == 1:
                        if settings.Number_of_rows < 100:
                            settings.Number_of_rows += 5
                    elif event.button == 3:
                        if settings.Number_of_rows > 5:
                            settings.Number_of_rows -= 5


        pygame.display.update()
