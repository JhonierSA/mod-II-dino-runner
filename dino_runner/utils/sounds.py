import os
from pygame import mixer
import pygame

from dino_runner.utils.constants import IMG_DIR
pygame.init()
DEAD_SOUND = pygame.mixer.Sound(os.path.join(IMG_DIR, 'Sounds/Die.mp3'))

SCORE_SOUND = pygame.mixer.Sound(os.path.join(IMG_DIR, 'Sounds/Points.mp3'))

JUMP_SOUND = pygame.mixer.Sound(os.path.join(IMG_DIR, 'Sounds/Jump.mp3')).play()
