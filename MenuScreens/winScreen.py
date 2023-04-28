import pygame, sys
import main
from Helpers.button import Button



def Win(screen_width, screen_height, time_to_finish, number_of_kids, maze_size):
    buttons_posX = screen_width / 2
    y_start = screen_height / 2 - 100
    buttons_posY = [y_start, y_start + 100, y_start + 200, y_start + 350]
    
   
    
    score = number_of_kids * (maze_size[0] ** maze_size[1])  / time_to_finish

    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        
    
        main.SCREEN.fill("white")
        main.SCREEN.blit(main.BG, (0, 0))
        
        MENU_TEXT = main.get_font(110).render("Winner :)", True, "White")
        MENU_RECT = MENU_TEXT.get_rect(center=(buttons_posX, 80))
        main.SCREEN.blit(MENU_TEXT, MENU_RECT)

        Time = Button(image=None, pos=(buttons_posX, buttons_posY[0]),
                                   text_input=f"Time To Rescue The Kids : {time_to_finish:.2f}", font=main.get_font(50), base_color="White",
                                   hovering_color="White")

        Kids = Button(image=None, pos=(buttons_posX, buttons_posY[1]),
                                     text_input=f"Number of Kids Rescued : {number_of_kids}", font=main.get_font(50), base_color="White",
                                     hovering_color="White")

        Score = Button(image=None, pos=(buttons_posX, buttons_posY[2]),
                              text_input=f"Total Score : {score:.2f}", font=main.get_font(50), base_color="White",
                              hovering_color="White")
        
        OPTIONS_BACK = Button(image=None, pos=(buttons_posX, buttons_posY[3]),
                              text_input="BACK", font=main.get_font(75), base_color="White",
                              hovering_color="#ff006e")

        for button in [Time, Kids, Score, OPTIONS_BACK]:
            button.changeColor(OPTIONS_MOUSE_POS)
            button.update(main.SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        main.mixer.music.set_volume(0.5)
                        main.main_menu()
                        break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main.main_menu()


        pygame.display.update()
