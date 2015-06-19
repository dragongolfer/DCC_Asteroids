import pygame
import math
pygame.init()


class Bullet(pygame.sprite.Sprite):
    def __init__(self, loc, angle, size):
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = float(loc[0])
        self.y = float(loc[1])
        self.angle = float(angle)
        self.speed = 15
        self.radius = 10
        self.large = size
        if self.large == True:
            self.radius = 45
        return
        
    def update(self, size): # Size is only used for the function call similarity with the ship and asteroid class
        self.x += self.speed * math.cos(math.radians(self.angle))
        self.y -= self.speed * math.sin(math.radians(self.angle))
        return
        
    def get_location(self):
        return (int(self.x), int(self.y))
        
    def get_angle(self):
        return int(self.angle)
        
    def get_radius(self):
        return self.radius

    def get_large(self):
        return self.large

    def set_large(self,value):
        self.large = value


