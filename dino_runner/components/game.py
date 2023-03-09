import os
import random
import pygame
from dino_runner.components.cloud import Clouds
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.bird import Birds
from dino_runner.components.hammer import Hammer
from dino_runner.components.heart import Heart
from dino_runner.components.shield import Shield
from dino_runner.components.cactus import Cactus

from dino_runner.utils.constants import BG, GAME_OVER, ICON, IMG_DIR, RESTART, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.player_died = False
        self.died_count = 0
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
        self.heart = Heart()
        self.upgrading = random.choice((self.hammer, self.shield, self.heart))
        self.obsta = random.choice((self.cactus, self.bird))
        self.text = 0
        self.obj_points = 0
        self.points_Sound = pygame.mixer.Sound(os.path.join(IMG_DIR, 'Sounds/Points.mp3'))
        self.obsta_rect = pygame.Rect(self.obstacle().rect_x, self.obstacle().rect_y, self.obstacle().image.get_width(), self.obstacle().image.get_height())
        self.player_rect = pygame.Rect(self.player.dino_rect_x, self.player.dino_rect_y, self.player.image.get_width(), self.player.image.get_height())
        self.upgrade_rect = pygame.Rect(self.upgrade().rect_x, self.upgrade().rect_y, self.upgrade().image.get_width(), self.upgrade().image.get_height())

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
        self.player_rect = pygame.Rect(self.player.dino_rect_x, self.player.dino_rect_y, self.player.image.get_width(), self.player.image.get_height())
        self.obsta_rect = pygame.Rect(self.obstacle().rect_x, self.obstacle().rect_y, self.obstacle().image.get_width(), self.obstacle().image.get_height())
        self.upgrade_rect = pygame.Rect(self.upgrade().rect_x, self.upgrade().rect_y, self.upgrade().image.get_width(), self.upgrade().image.get_height())
        
    def draw(self):
        self.dead()
        if self.player_rect.colliderect(self.upgrade_rect):
            self.upgrade().rect_x = -100
            self.power_up()
            self.player.draw(self.screen)
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
        if self.obsta.rect_x <= -100:
                self.obsta = random.choice((self.cactus, self.bird))
                return self.obsta
        else:
            return self.obsta
    
    def upgrade(self):
        if self.upgrading.rect_x <= -100:
            self.upgrading = random.choice((self.hammer, self.shield, self.heart))
            return self.upgrading
        else: 
            return self.upgrading

    def power_up(self):
        if self.upgrade() == self.hammer:
            self.player.shield = False
            self.player.hammer = True
        elif self.upgrade() == self.shield:
            self.player.hammer = False
            self.player.shield = True
        elif self.upgrade() == self.heart:
            self.player.lifes += 1
    
    def dead(self):
        if self.player_rect.colliderect(self.obsta_rect):
            if self.player.shield == True:
                print("Te has protegido")
                self.player.shield = False
            else:
                self.player.dead()
                self.player_died = True
                self.died_count += 1
    