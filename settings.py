import pyautogui

global Num_of_kids, Number_of_rows, Number_of_cols, Level_time

Number_of_rows = 20
Number_of_cols = 20
Num_of_kids = 3
Level_time = 'default'


def get_settings():
    return Number_of_rows, Number_of_cols, Num_of_kids , Level_time



SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()

# SCREEN_WIDTH, SCREEN_HEIGHT = 720, 720

