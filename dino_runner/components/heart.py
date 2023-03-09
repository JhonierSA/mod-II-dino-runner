from dino_runner.utils.constants import HAMMER, FPS, SMALL_HEART
import random
from pygame.sprite import Sprite

class Heart(Sprite):
    def __init__(self):
        self.image = SMALL_HEART
        self.y_velocity = FPS / (3/2)     
        self.heart_rect = self.image.get_rect()
        self.heart_rect_x = 10000
        self.heart_rect_y = 100
        self.random_choise = True

    def update(self):
        self.appear()

    def draw(self, screen):
        screen.blit(self.image, (self.heart_rect_x, self.heart_rect_y))

    def appear(self):
        if self.random_choise:
            self.heart_rect_y = random.choice((190, 140, 210, 240, 280, 310)) 
            self.random_choise = False
        if self.heart_rect_x <= -100:
            self.heart_rect_x = 10000
            self.random_choise = True

        self.heart_rect = self.image.get_rect()
        self.heart_rect_x -= self.y_velocity