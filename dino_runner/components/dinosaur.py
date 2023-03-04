from dino_runner.utils.constants import *
from pygame.sprite import Sprite

class Dinosaur(Sprite):
    def __init__(self):
        self.image = JUMPING
        self.dino_rect = self.image.get_rect()
        self.dino_rect_x = 80
        self.dino_rect_y = 310
        self.step = 0

    def update(self, user_input):
        if user_input[pygame.K_DOWN] or user_input[pygame.K_s]:
            self.duck()
        else:
            self.run()
        self.step += 1
        if self.step == 8:
            self.step = 0

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect_x, self.dino_rect_y))

    def run(self):
        self.image = RUNNING[0] if self.step < 4 else RUNNING[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect_x = 80
        self.dino_rect_y = 310

    def jump(self):
        pass

    def duck(self):
        self.image = DUCKING[0] if self.step < 4 else DUCKING[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect_x = 80
        self.dino_rect_y = 345