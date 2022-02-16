# from classes.character import *
# from classes.element import *
# from classes.gamemode import *
import pygame
from game import Game
from menu import Menu
from game_over import GameOver


# on initialise la fenetre de jeu (taille, nom, icone)
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Factory Invaders")
icon = pygame.image.load("Invaders X.png").convert()
pygame.display.set_icon(icon)

# initialisation pygame
pygame.init()

# police pour affichage du score
font = pygame.font.Font('freesansbold.ttf', 31)


menu = Menu(screen)
# initialisation d'une instance de jeu
game1 = Game(screen, font)

score = 000

running = True
# s'éxécute lorsque main.py se lance
if __name__ == "__main__":
    """while running:
        
        menu.loop()
        
        if menu.get_button() == "play":
            game1.run()
            print("fin")
            if game1.get_quit_condition() == "nothing":
                running = False
            else:
                pass
        elif menu.get_button() == "nothing":
            running = False
        menu = Menu(screen)
        game1 = Game(screen, font)"""
    game_over = GameOver(screen, font, score)
    game_over.loop()
    pygame.quit()