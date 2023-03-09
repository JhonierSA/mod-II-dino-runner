from dino_runner.utils.constants import CLOUD, FPS
import random
from pygame.sprite import Sprite

class Clouds(Sprite):
    def __init__(self):
        self.y_velocity = FPS / 100
        self.clouds = []
        self.num_clouds = 4
        for cloud in range(self.num_clouds):
            cloud = {}
            cloud["image"] = CLOUD      
            cloud["cloud_rect"] = cloud["image"].get_rect()
            cloud["cloud_rect_x"] = 1200
            cloud["cloud_rect_y"] = random.choice((170, 180, 190, 150, 160, 130, 100, 80))
            cloud["distance_rect_x"] = random.choice((200, 300, 400, 500, 600, 700, 800, 900))
            self.clouds.append(cloud)

    def update(self):
        for cloud in self.clouds:    
            self.appear()

    def draw(self, screen):
        for cloud in self.clouds:
            screen.blit(cloud["image"], (cloud["cloud_rect_x"], cloud["cloud_rect_y"]))

    def appear(self):
        if self.clouds[3]["cloud_rect_x"] <= -100:
            self.clouds = []
            for cloud in range(self.num_clouds):
                cloud = {}
                cloud["image"] = CLOUD       
                cloud["cloud_rect"] = cloud["image"].get_rect()
                cloud["cloud_rect_x"] = 1200
                cloud["cloud_rect_y"] = random.choice((170, 180, 190, 150, 160, 130, 100, 80))
                cloud["distance_rect_x"] = random.choice((200, 300, 400, 500, 600, 700, 800, 900))
                self.clouds.append(cloud)
        
        else:
            for x in range(0,4):
                if x >= 1:
                    if self.clouds[x]["cloud_rect_x"] - self.clouds[x-1]["cloud_rect_x"] >= self.clouds[x-1]["distance_rect_x"]:
                        self.clouds[x]["cloud_rect_x"] -= self.y_velocity
                        self.clouds[0]["cloud_rect_x"] -= self.y_velocity
                    else:
                        self.clouds[0]["cloud_rect_x"] -= self.y_velocity
        