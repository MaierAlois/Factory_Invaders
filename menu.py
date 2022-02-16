import pygame
import functions

class Menu:
    def __init__(self, screen):
        self.running = True
        self.screen = screen
        self.last_click = "nothing"
        self.image_menu = pygame.image.load("menu.png").convert()
        self.button_play = pygame.image.load("play_idle.png").convert_alpha()
        self.mouse_pos = [0, 0]
        
    def reset(self):
        self.running = True
        self.last_click = "nothing"
        self.image_menu = pygame.image.load("menu.png").convert()
        self.button_play = pygame.image.load("play_idle.png").convert_alpha()
        self.mouse_pos = [0, 0]
        
    def get_button(self):
        return self.last_click
    
    def handling_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 164 < self.mouse_pos[0] < 164+312 and 276 < self.mouse_pos[1] < 276+104:
                    self.last_click = "play"
    
    def update(self):
        self.mouse_pos = pygame.mouse.get_pos()
        if 164 < self.mouse_pos[0] < 164+312 and 276 < self.mouse_pos[1] < 276+104:
            self.button_play = pygame.image.load("play_over.png").convert_alpha()
        else:
            self.button_play = pygame.image.load("play_idle.png").convert_alpha()
            
        if self.last_click == "play":
            self.running = False
        
    def display(self):
        self.screen.blit(self.image_menu, (0, 0))
        self.screen.blit(self.button_play, (0, 0))
        pygame.display.flip()
    
    def loop(self):
        while self.running:
            self.handling_event()
            self.update()
            self.display()