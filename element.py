import pygame
import functions
from random import randint

class Enemy:
    def __init__(self, col, image, speed = 0.01):
        self.rect = self.image.get_rect()
        self.COL = col
        self.rect.x, self.rect.y = col * 98 + 143, 10
        self.life = 1

    def update(self, speed):
        pass


class Box(Enemy):
    def __init__(self, col, speed = 0.01, screen = None):
        self.image = pygame.image.load("caisse.png").convert_alpha()
        # Enemy.__init__(col, speed)
        self.rect = self.image.get_rect()
        self.COL = col
        self.rect.x, self.rect.y = col * 98 + 143, 10
        self.life = 1
        self.speed = speed
        self.isattack = False

    def update(self, speed):
        self.speed = speed
        self.rect.x, self.rect.y = self.rect.x, self.rect.y + self.speed

class Shooter(Enemy):
    def __init__(self, col, speed = 0.01, game = None):
        self.image = pygame.image.load("shooter.png").convert_alpha()
        # Enemy.__init__(col, speed)
        self.rect = self.image.get_rect()
        self.COL = col
        self.life = 1
        self.rect.x, self.rect.y = self.COL * 98 + 143, 10
        self.delay = 1/speed * 2000
        self.timeSpawn = pygame.time.get_ticks()
        self.speed = speed
        self.game = game
        self.isattack = False
        self.x = self.COL * 98 + 143
        self.pos_depart = [10]
        self.pos_objectif = [100]
        self.alpha = 0
        self.direction_alpha = 1
        self.alr_attack = False
        self.alpha_shoot = 0
        self.alpha_shoot_direction = 1

    def attack(self):
        #if self
        self.isattack = True
        self.game.is_player_touched(self)

    def update(self, speed):
        if self.direction_alpha == 1:
            if self.alpha >= 1:
                self.alpha = 1
            else:
                self.alpha += 0.1
        else:
            if self.alpha <= 0:
                self.alpha = 0
            else:
                self.alpha -= 0.1
        self.rect.x, self.rect.y = self.x, functions.lerp(self.pos_depart, self.alpha, self.pos_objectif)[0]
        if pygame.time.get_ticks()-self.timeSpawn>self.delay:
            if self.alpha_shoot_direction == 1:
                if self.alpha_shoot >= 1:
                    self.alpha_shoot = 1
                else:
                    self.alpha_shoot += 0.1
            else:
                if self.alpha_shoot <= 0:
                    self.alpha_shoot = 0
                else:
                    self.alpha_shoot -= 0.1
            if not self.alr_attack:
                self.attack()
                self.alr_attack = True
            if pygame.time.get_ticks()-self.timeSpawn>self.delay + 300:
                self.alpha_shoot_direction = 0
            if pygame.time.get_ticks()-self.timeSpawn>self.delay + 500:
                self.isattack = False
                self.direction_alpha = 0
            if pygame.time.get_ticks()-self.timeSpawn>self.delay + 750:
                self.isattack = False
                self.life = 0
        self.speed = speed


class Spawner:

    def __init__(self, speed = 0.01, game = None):
        self.speed = speed
        self.elements = []
        self.game = game

    def spawnBox(self):
        rand_col = functions.get_random_col()
        if len(self.elements) > 0:
            while rand_col == self.elements[-1].COL:
                rand_col = functions.get_random_col()
        type_enemy = randint(0, 5)
        if type_enemy in range(5):
            self.elements.append(Box(rand_col, self.speed))
        else:
            self.elements.append(Shooter(rand_col, self.speed, self.game))

    def draw(self, screen, elementD = False):
        for element in self.elements:
            if element.isattack:
                pygame.draw.rect(screen, (255, 100, 100), (element.rect.x+16, element.rect.y+64, 32, functions.lerp([0], element.alpha_shoot, [500])[0]), border_radius = 16)
            screen.blit(element.image, element.rect)


    def update(self, speed = 2):
        i = 0
        while i < len(self.elements):
            if self.elements[i].life <= 0:
                del(self.elements[i])
            elif self.elements[i].rect[1] > 480:
                del(self.elements[i])
                game.score_up(1)
            else:
                self.elements[i].update(speed)
            i+=1