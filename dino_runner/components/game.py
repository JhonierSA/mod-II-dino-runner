import os
import random
import pygame
from dino_runner.components.cloud import Clouds
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.bird import Birds
from dino_runner.components.hammer import Hammer
from dino_runner.components.shield import Shield
from dino_runner.components.cactus import Cactus

from dino_runner.utils.constants import BG, ICON, IMG_DIR, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.points = 0
        self.fps = 0
        self.player = Dinosaur()
        self.bird = Birds()
        self.cloud = Clouds()
        self.shield = Shield()
        self.hammer = Hammer()
        self.cactus = Cactus()
        self.upgrading = random.choice((self.hammer, self.shield))
        self.obsta = random.choice((self.cactus, self.bird))
        self.text = 0
        self.obj_points = 0
        self.points_Sound = pygame.mixer.Sound(os.path.join(IMG_DIR, 'Sounds/Points.mp3'))

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
            self.score()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.cloud.update()
        self.obstacle().update()
        self.upgrade().update()
        self.player.update(user_input)

    def draw(self):
        self.clock.tick(FPS + self.fps)
        self.screen.fill((255, 255, 255))
        self.cloud.draw(self.screen)
        self.obstacle().draw(self.screen)
        self.draw_background()
        self.upgrade().draw(self.screen)
        self.player.draw(self.screen)
        self.score()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
    
    def score(self):
        self.obj_points += 1
        if self.obj_points % 10 == 0:   
            self.points += 1
        if self.obj_points % 1000 == 0 and self.points > 0:
            self.points_Sound.play()
            self.fps += 1
        font = pygame.font.Font('FreeSansBold.ttf', 20)
        self.text = font.render(f'Points:  {str(self.points)}', True, (0, 0, 0))
        self.screen.blit(self.text, (960, 10))
    
    def obstacle(self):
        if self.obsta == self.cactus:
            if self.obsta.cactus_rect_x <= -100:
                self.obsta = random.choice((self.cactus, self.bird))
            return self.obsta
        elif self.obsta == self.bird:
            if self.obsta.bird_rect_x <= -100:
                self.obsta = random.choice((self.cactus, self.bird))
            return self.obsta
        else:
            return self.obsta
    
    def upgrade(self):
        if self.upgrading == self.hammer:
            if self.upgrading.hammer_rect_x <= -100:
                self.upgrading = random.choice((self.hammer, self.shield))
            return self.upgrading
        elif self.upgrading == self.shield:
            if self.upgrading.shield_rect_x <= -100:
                self.upgrading = random.choice((self.hammer, self.shield))
            return self.upgrading
        else:
            return self.upgrading
    
    def dead(self):
        if self.player.rect.colliderect(self.obstacle()):
            self.player.dead()