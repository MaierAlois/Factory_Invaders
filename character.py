import pygame
print("e")

class Player:
    def __init__(self, x, y):
        self.image = pygame.image.load("drone.png").convert_alpha()
        self.rect = self.image.get_rect(x=x, y=y)
        self.life = 10
        self.delay = 300
        self.col_position_target = 0
        self.power_slide = 1
        self.last_player_move = pygame.time.get_ticks()
        self.last_pos = [0, 0]
        self.alpha_player = 1
        self.boom_charge = 0
        
    def charge_boom(self, nb_points):
        self.boom_charge += nb_points

    def boom(self, spawner):
        score = 0
        if self.boom_charge >= 50:
            score = len(spawner.elements)
            spawner.elements = []
            self.boom_charge = 0
            return score
        else:
            print("non")
            return score
        
    def loss_life(self, nb_point):
        self.life -= nb_point
    
    def is_alive(self):
        alive = True
        if self.life <= 0:
            alive = False
        return alive
    
    def move(self, direction):
        fut = self.col_position_target + direction
        if fut > 3:
            fut = 3
        elif fut < 0:
            fut = 0
        else:
            now = pygame.time.get_ticks()
            if now - self.last_player_move >= self.delay:
                self.last_pos = self.rect
                self.col_position_target = fut
                self.last_player_move = pygame.time.get_ticks()
                self.alpha_player = 0
                # self.rect = [self.col_position * 98 + 143, 360]
        

    def draw(self, screen):
        screen.blit(self.image, self.rect)