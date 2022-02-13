# from classes.character import *
# from classes.element import *
# from classes.gamemode import *
import pygame
from game import Game


# on initialise la fenetre de jeu (taille, nom, icone)
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Invaders X")
icon = pygame.image.load("Invaders X.png").convert()
pygame.display.set_icon(icon)

# initialisation pygame
pygame.init()

# police pour affichage du score
font = pygame.font.Font('freesansbold.ttf', 31)

# initialisation d'une instance de jeu
game1 = Game(screen, font)

# s'éxécute lorsque main.py se lance
if __name__ == "__main__":
    game1.run() # lancement du jeu
    pygame.quit()