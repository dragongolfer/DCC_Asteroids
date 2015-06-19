import pygame
import math
pygame.init()

# "numberOfImages" is the number of images used in the animation
# "timeForAnimation" is the time for the entire sequence to play

class Explosion(pygame.sprite.Sprite):
    def __init__(self, name, loc, numberOfImages, timeForAnimation, frameRate):
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = int(loc[0])
        self.y = int(loc[1])
        self.startTime = timeForAnimation * frameRate
        self.counter = self.startTime
        self.image_increment = self.startTime / numberOfImages
        self.name = name
        return
        
    def update(self, size): # Size is only used for the function call similarity with the ship and asteroid class
        self.counter -= 1
        return
        
    def get_location(self):
        return (int(self.x), int(self.y))

    def get_image_number(self):
        return int(self.counter / self.image_increment) + 1
        
    def get_counter(self):
        return self.counter
        
    def get_name(self):
        return self.name