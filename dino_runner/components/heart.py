from dino_runner.utils.constants import HAMMER, FPS, SMALL_HEART
import random
from pygame.sprite import Sprite

class Heart(Sprite):
    def __init__(self):
        self.image = SMALL_HEART
        self.y_velocity = FPS / (3/2)     
        self.rect = self.image.get_rect()
        self.rect_x = 10000
        self.rect_y = 100
        self.random_choise = True

    def update(self):
        self.appear()

    def draw(self, screen):
        screen.blit(self.image, (self.rect_x, self.rect_y))

    def appear(self):
        if self.random_choise:
            self.rect_y = random.choice((190, 140, 210, 240, 280, 310)) 
            self.random_choise = False
        if self.rect_x <= -100:
            self.rect_x = 10000
            self.random_choise = True

        self.rect = self.image.get_rect()
        self.rect_x -= self.y_velocity