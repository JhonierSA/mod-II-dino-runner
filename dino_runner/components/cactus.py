from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS
import random
from pygame.sprite import Sprite

class Cactus(Sprite):
    def __init__(self):
        self.image = random.choice((LARGE_CACTUS[0], LARGE_CACTUS[1], LARGE_CACTUS[2], SMALL_CACTUS[0], SMALL_CACTUS[1], SMALL_CACTUS[2]))
        self.y_velocity = 20     
        self.cactus_rect = self.image.get_rect()
        self.cactus_rect_x = 1100
        self.cactus_rect_y = 305 if self.image == LARGE_CACTUS[0] or self.image == LARGE_CACTUS[1] or self.image == LARGE_CACTUS[2] else 330
        self.random_choise = True
        
    def update(self):
        self.appear()

    def draw(self, screen):
        screen.blit(self.image, (self.cactus_rect_x, self.cactus_rect_y))

    def appear(self):
        if self.random_choise:
            self.image = random.choice((LARGE_CACTUS[0], LARGE_CACTUS[1], LARGE_CACTUS[2], SMALL_CACTUS[0], SMALL_CACTUS[1], SMALL_CACTUS[2]))
            self.cactus_rect_y = 305 if self.image == LARGE_CACTUS[0] or self.image == LARGE_CACTUS[1] or self.image == LARGE_CACTUS[2] else 330
            self.random_choise = False
        if self.cactus_rect_x <= -100:
            self.cactus_rect_x = 1100
            self.random_choise = True

        self.image = self.image
        self.cactus_rect = self.image.get_rect()
        self.cactus_rect_x -= self.y_velocity