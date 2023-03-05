import pygame
import random
from dino_runner.components.cloud import Clouds
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.bird import Birds
from dino_runner.components.hammer import Hammer
from dino_runner.components.shield import Shield
from dino_runner.components.cactus import Cactus

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS


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
        self.player = Dinosaur()
        self.bird = Birds()
        self.cloud = Clouds()
        self.shield = Shield()
        self.hammer = Hammer()
        self.cactus = Cactus()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.cactus.update()
        self.bird.update()
        self.cloud.update()
        self.shield.update()
        self.hammer.update()
        self.player.update(user_input)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.cactus.draw(self.screen)
        self.draw_background()
        self.bird.draw(self.screen)
        self.cloud.draw(self.screen)
        self.shield.draw(self.screen)
        self.hammer.draw(self.screen)
        self.player.draw(self.screen)
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
