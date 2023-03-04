from dino_runner.utils.constants import *
from pygame.mixer import *
from pygame.sprite import Sprite

class Dinosaur(Sprite):
    def __init__(self):
        self.image = JUMPING
        self.is_jumping = False
        self.jump_speed = 30    # Velocidad inicial de salto
        self.gravity = 2        # Gravedad aplicada.
        self.y_velocity = 0     # Velocidad actual.
        self.shield = False
        self.hammer = False
        self.dino_rect = self.image.get_rect()
        self.dino_rect_x = 80
        self.dino_rect_y = 310
        self.step = 0
        self.die_Sound = pygame.mixer.Sound(os.path.join(IMG_DIR, 'Sounds/Die.mp3'))
        self.points_Sound = pygame.mixer.Sound(os.path.join(IMG_DIR, 'Sounds/Points.mp3'))

    def update(self, user_input):
        if user_input[pygame.K_DOWN] or user_input[pygame.K_s]:
            self.duck()
        
        elif user_input[pygame.K_UP] or user_input[pygame.K_w] or user_input[pygame.K_SPACE]:
            self.jump()
            if self.is_jumping:
                # actualizar velocidad vertical del dinosaurio
                self.y_velocity += self.gravity
                # actualizar posición vertical del dinosaurio
                self.dino_rect_y += self.y_velocity

                # si el dinosaurio llegó al suelo, detener el salto
                if self.dino_rect_y >= 310:
                    self.dino_rect_y = 310
                    self.y_velocity = 0
                    self.is_jumping = False
                    self.run()

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
        
        elif self.hammer == True:
            self.image = RUNNING_HAMMER[0] if self.step < 4 else RUNNING_HAMMER[1]

        else:
            self.image = RUNNING[0] if self.step < 4 else RUNNING[1]

        self.dino_rect = self.image.get_rect()
        self.dino_rect_x = 80
        self.dino_rect_y = 310

    def jump(self):
        if self.shield == True:
            self.image = JUMPING_SHIELD
        
        elif self.hammer == True:
            self.image = JUMPING_HAMMER

        else:
            self.image = JUMPING
        
        if not self.is_jumping:
            pygame.mixer.Sound(os.path.join(IMG_DIR, 'Sounds/Jump.mp3')).play()
            self.is_jumping = True
            self.y_velocity = -self.jump_speed
        

    def duck(self):
        if self.shield == True:
            self.image = DUCKING_SHIELD[0] if self.step < 4 else DUCKING_SHIELD[1]
        
        elif self.hammer == True:
            self.image = DUCKING_HAMMER[0] if self.step < 4 else DUCKING_HAMMER[1]

        else:
            self.image = DUCKING[0] if self.step < 4 else DUCKING[1]

        self.dino_rect = self.image.get_rect()
        self.dino_rect_x = 80
        self.dino_rect_y = 345
    