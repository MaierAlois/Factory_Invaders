import pygame
import functions

class Menu:
    def __init__(self):
        self.last_click = "nothing"
        self.image_menu = pygame.image.load("menu.png").convert()
        self.button_play = pygame.image.load("play_idle.png").convert_alpha()