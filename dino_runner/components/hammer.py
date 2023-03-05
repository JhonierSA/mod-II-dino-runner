from dino_runner.utils.constants import HAMMER
import random
from pygame.sprite import Sprite

class Hammer(Sprite):
    def __init__(self):
        self.image = HAMMER  
        self.y_velocity = 5     
        self.hammer_rect = self.image.get_rect()
        self.hammer_rect_x = 1100
        self.hammer_rect_y = 100
        self.random_choise = True
        
    def update(self):
        self.appear()

    def draw(self, screen):
        screen.blit(self.image, (self.hammer_rect_x, self.hammer_rect_y))

    def appear(self):
        if self.random_choise:
            self.hammer_rect_y = random.choice((190, 140, 210, 240, 280, 310)) 
            self.random_choise = False
        if self.hammer_rect_x <= -100:
            self.hammer_rect_x = 1100
            self.random_choise = True

        self.image = HAMMER
        self.hammer_rect = self.image.get_rect()
        self.hammer_rect_x -= self.y_velocity