from dino_runner.utils.constants import *
from pygame.sprite import Sprite

class Dinosaur(Sprite):
    def __init__(self):
        self.image = JUMPING
        self.shield = False
        self.hammer = False
        self.dino_rect = self.image.get_rect()
        self.dino_rect_x = 80
        self.dino_rect_y = 310
        self.step = 0

    def update(self, user_input):
        if user_input[pygame.K_DOWN] or user_input[pygame.K_s]:
            self.duck()
        
        elif user_input[pygame.K_UP] or user_input[pygame.K_w]:
            self.jump()

        else:
            self.run()
        self.step += 1
        if self.step == 8:
            self.step = 0

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect_x, self.dino_rect_y))

    def run(self):
        if self.shield == True:
            self.image = RUNNING_SHIELD[0] if self.step < 4 else RUNNING_SHIELD[1]
            self.dino_rect = self.image.get_rect()
            self.dino_rect_x = 80
            self.dino_rect_y = 310
        
        elif self.hammer == True:
            self.image = RUNNING_HAMMER[0] if self.step < 4 else RUNNING_HAMMER[1]
            self.dino_rect = self.image.get_rect()
            self.dino_rect_x = 80
            self.dino_rect_y = 310

        else:
            self.image = RUNNING[0] if self.step < 4 else RUNNING[1]
            self.dino_rect = self.image.get_rect()
            self.dino_rect_x = 80
            self.dino_rect_y = 310

    def jump(self):
        if self.shield == True:
            self.image = JUMPING_SHIELD
            self.dino_rect = self.image.get_rect()
            self.dino_rect_x = 80
            self.dino_rect_y = 90
        
        elif self.hammer == True:
            self.image = JUMPING_HAMMER
            self.dino_rect = self.image.get_rect()
            self.dino_rect_x = 80
            self.dino_rect_y = 90

        else:
            self.image = JUMPING
            self.dino_rect = self.image.get_rect()
            self.dino_rect_x = 80
            self.dino_rect_y = 90

    def duck(self):
        if self.shield == True:
            self.image = DUCKING_SHIELD[0] if self.step < 4 else DUCKING_SHIELD[1]
            self.dino_rect = self.image.get_rect()
            self.dino_rect_x = 80
            self.dino_rect_y = 345
        
        elif self.hammer == True:
            self.image = DUCKING_HAMMER[0] if self.step < 4 else DUCKING_HAMMER[1]
            self.dino_rect = self.image.get_rect()
            self.dino_rect_x = 80
            self.dino_rect_y = 345

        else:
            self.image = DUCKING[0] if self.step < 4 else DUCKING[1]
            self.dino_rect = self.image.get_rect()
            self.dino_rect_x = 80
            self.dino_rect_y = 345
    