import pygame
import character
import element
import functions

class Game:

    def __init__(self, screen, font):
        self.screen = screen                                                            # on stocke la fenetre dans une instance de classe
        self.running = True                                                             # variable qui permet la verification du fonctionnement du jeu
        self.clock = pygame.time.Clock()                                                # permet par la suite de fixer un framerate
        self.background = pygame.image.load("fond.png").convert()                       # on stocke l'image de fond
        self.score_bar = pygame.image.load("scoreBar.png")                              # on stocke l'image du bandeau
        self.player = character.Player(143, 360)                                        # initialisation du joueur
        self.spawner = element.Spawner(2)                                               # initialisation du spawner de boite
        self.last_spawn = 0                                                             # permet de trouver le delta spawn
        self.delay_spawn = 1000                                                         # initialisation du delai entre chaque spawn de boite
        self.speed_tapis = 2                                                            # initialisation de la vitesse du tapis
        self.last_upgrade_difficulty = 0                                                # permet de trouver le delta entre chaque augmentation de difficulté
        self.delay_upgrade_difficulty = 2000                                            # initialisation du delai entre chaque augmentation de difficulté
        self.ouch = False                                                               # le joueur a-t-il touché une boite ?
        self.score = 0                                                                  # son nom dit tout
        self.font = font                                                                # récupération de la police d'affichage
        self.score_image = self.font.render(str(self.score), True, (155, 213, 169))     # premier rendu du score pour score = 0
        self.quit_condition = "nothing"

    def get_quit_condition(self):
        return self.quit_condition

    def handling_event(self):
        # Une fonction qui gère les différentes intéraction entre la fenêtre et l'utilisateur

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.move(self.player.power_slide * (-1))
                if event.key == pygame.K_RIGHT:
                    self.player.move(self.player.power_slide)
                if event.key == pygame.K_SPACE:
                    score = self.player.boom(self.spawner)
                    if score > 0:
                        self.score_up(score)


    def is_player_touched(self, enemy):
        if enemy.COL == self.player.col_position_target:
            self.player.loss_life(1)

    def isColliding(self, rect1, rect2) -> bool:
        # juste une fonction qui return un boolean selon si il y a une collision ou non
        return rect1.colliderect(rect2)


    def show_life(self, player):
        i = 0
        while i < player.life:
            pygame.draw.rect(self.screen, (155, 213, 169), (i*((490-140)/9)+140, 26, 10.2, 30))
            i+=1


    def show_score(self):
        self.screen.blit(self.score_image, (555, 433))


    def update(self):

        # mise a jour de la position du drone avec animation grace au alpha_player et la fonction lerp (functions.py)
        if self.player.alpha_player >= 1:
            self.player.alpha_player = 1
        else:
            self.player.alpha_player += 0.2
        self.player.rect.x, self.player.rect.y = functions.lerp(self.player.last_pos, self.player.alpha_player, [self.player.col_position_target * 98 + 143, 360])

        if pygame.time.get_ticks() - self.last_spawn > self.delay_spawn:
            self.spawner.spawnBox()
            self.last_spawn = pygame.time.get_ticks()

        if pygame.time.get_ticks() - self.last_upgrade_difficulty > self.delay_upgrade_difficulty:
            self.last_upgrade_difficulty = pygame.time.get_ticks()
            self.speed_tapis += 0.1
            self.delay_spawn = 3000/self.speed_tapis
            self.player.delay = 1500/self.speed_tapis
        self.spawner.update(self, self.speed_tapis)

        for element in self.spawner.elements:
            if self.isColliding(self.player.rect, element.rect):
                del(self.spawner.elements[self.spawner.elements.index(element)])
                self.player.loss_life(1)
                
        if not self.player.is_alive():
            print("je suis là")
            self.quit_condition = "player_dead"
            self.game_over()


    def score_up(self, nb_point):
        self.score += nb_point
        self.player.charge_boom(2)
        self.score_image = self.font.render(str(self.score), True, (155, 213, 169))


    def display(self):
        self.screen.blit(self.background, (0, 0))
        self.spawner.draw(self.screen)
        self.screen.blit(self.score_bar, (0, 0))
        self.show_life(self.player)
        self.show_score()
        self.player.draw(self.screen)
        pygame.display.flip()


    def game_over(self):
        self.running = False


    def run(self):
        while self.running:
            self.handling_event()
            self.update()
            self.display()
            self.clock.tick(60)