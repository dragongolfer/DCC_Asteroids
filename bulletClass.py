import pygame
import math
pygame.init()


class Bullet(pygame.sprite.Sprite):
    def __init__(self, loc, angle):
        pygame.sprite.Sprite.__init__(self)
        self.x = loc[0]
        self.y = loc[1]
        self.angle = angle
        self.speed = 15
        self.radius = 10
        return
        
    def update(self):
        self.x += self.speed * math.cos(math.radians(self.angle))
        self.y -= self.speed * math.sin(math.radians(self.angle))

        return
        
    def get_location(self):
        return (self.x, self.y)
        
    def get_angle(self):
        return self.angle
        
    def getSize(self):
        return self.radius