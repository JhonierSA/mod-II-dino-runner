from dino_runner.utils.constants import CLOUD
import random
from pygame.sprite import Sprite

class Clouds(Sprite):
    def __init__(self):
        self.image = CLOUD    
        self.y_velocity = 3     
        self.cloud_rect = self.image.get_rect()
        self.cloud_rect_x = 1100
        self.cloud_rect_y = 100
        self.random_choise = True
        
    def update(self):
        self.appear()

    def draw(self, screen):
        screen.blit(self.image, (self.cloud_rect_x, self.cloud_rect_y))

    def appear(self):
        if self.random_choise:
            self.cloud_rect_y = random.choice((170, 180, 190, 150, 160, 130, 100, 80)) 
            self.random_choise = False
        if self.cloud_rect_x <= -100:
            self.cloud_rect_x = 1100
            self.random_choise = True

        self.image = CLOUD
        self.cloud_rect = self.image.get_rect()
        self.cloud_rect_x -= self.y_velocity
        