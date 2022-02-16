import pygame
import functions

class Menu:
    def __init__(self, screen):
        self.running = True
        self.screen = screen
        self.last_click = "nothing"
        self.image_menu = pygame.image.load("menu.png").convert()
        self.button_play = pygame.image.load("play_idle.png").convert_alpha()
    
    def handling_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    
    def update(self):
        """oui"""
        
    def display(self):
        self.screen.blit(self.image_menu, (0, 0))
        self.screen.blit(self.button_play, (0, 0))
    
    def loop(self):
        while self.running:
            self.update()
            self.display()