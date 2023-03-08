import pygame
from dino_runner.utils.constants import SHIELD, FPS
import random
from pygame.sprite import Sprite

class Shield(Sprite):
    def __init__(self):
        self.image = SHIELD   
        self.y_velocity = FPS / (3/2)      
        self.shield_rect = self.image.get_rect()
        self.shield_rect_x = 10000
        self.shield_rect_y = 100
        self.random_choise = True
        self.rect = pygame.Rect(self.shield_rect_x, self.shield_rect_y, self.image.get_width(), self.image.get_height())
        
    def update(self):
        self.appear()

    def draw(self, screen):
        screen.blit(self.image, (self.shield_rect_x, self.shield_rect_y))

    def appear(self):
        if self.random_choise:
            self.shield_rect_y = random.choice((190, 140, 210, 240, 280, 310)) 
            self.random_choise = False
        if self.shield_rect_x <= -100:
            self.shield_rect_x = 10000
            self.random_choise = True

        self.image = SHIELD
        self.shield_rect = self.image.get_rect()
        self.shield_rect_x -= self.y_velocity