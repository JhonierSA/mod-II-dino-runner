from dino_runner.utils.constants import BIRD, FPS
import random
from pygame.sprite import Sprite

class Birds(Sprite):
    def __init__(self):
        self.image = BIRD[1]
        self.step = 0       
        self.y_velocity = FPS / (3/2)   
        self.bird_rect = self.image.get_rect()
        self.bird_rect_x = 1200
        self.bird_rect_y = 100
        self.random_choise = True
        
    def update(self):
        self.fly()
        self.step += 1
        if self.step == 12:
            self.step = 0

    def draw(self, screen):
        screen.blit(self.image, (self.bird_rect_x, self.bird_rect_y))

    def fly(self):
        if self.random_choise:
            self.bird_rect_y = random.choice((170, 180, 190, 200, 240, 260, 310, 320)) 
            self.random_choise = False
        if self.bird_rect_x <= -100:
            self.bird_rect_x = 1200
            self.random_choise = True

        self.image = BIRD[0] if self.step < 6 else BIRD[1]
        self.bird_rect = self.image.get_rect()
        self.bird_rect_x -= self.y_velocity
        