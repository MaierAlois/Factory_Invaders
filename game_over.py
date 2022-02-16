import pygame
import functions

class GameOver:
    
    def __init__(self, screen, font, score):
        self.score = score
        self.running = True
        self.screen = screen
        self.last_click = "nothing"
        self.image_menu = pygame.image.load("game over.png").convert()
        self.button_play = pygame.image.load("retry_idle.png").convert_alpha()
        self.font = font
        self.score_image = self.font.render(str(self.score), True, (255, 255, 255))
        self.mouse_pos = [0, 0]
       
        
    def get_button(self):
        return self.last_click
    
    
    def handling_event(self):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 164 < self.mouse_pos[0] < 164+312 and 304 < self.mouse_pos[1] < 304+104:
                    self.last_click = "play"
    
    
    def update(self):
        
        self.mouse_pos = pygame.mouse.get_pos()
        
        if 164 < self.mouse_pos[0] < 164+312 and 304 < self.mouse_pos[1] < 304+104:
            self.button_play = pygame.image.load("retry_hover.png").convert_alpha()
        else:
            self.button_play = pygame.image.load("retry_idle.png").convert_alpha()
            
        if self.last_click == "play":
            self.running = False
        
        
    def display(self):
        self.screen.blit(self.image_menu, (0, 0))
        self.screen.blit(self.button_play, (0, 0))
        self.screen.blit(self.score_image, (275, 240))
        pygame.display.flip()
    
    
    def loop(self):
        while self.running:
            self.handling_event()
            self.update()
            self.display()