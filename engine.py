# Michael Kohlmann
# devCodeCamp - Team Helium
# Asteroids Clone
# 6/15/2015

# This is the main game engine loop for our asteroids clone.

# Main Loop consists of Reading User inputs from the Ship class.
# Iterating through each game object for the time increment (ie, movement, shooting, whatever might happen in one game cyle)
# Iterating through each game object for collision detection
# Iterating through each game object and displaying it to the screen.


import datetime
import time
import pygame
import os
from random import *
import math


from ship import *              # Ryan
from AsteroidClass import *     # Rob
from display_functions import * # Matt
from bulletClass import *       # Mike

pygame.init()



def debug(message):
    DEBUG = True
    if DEBUG:
        print("DEBUG: " + str(message))
    return
    

        
# class Asteroid(pygame.sprite.Sprite):
    # def __init__(self):
        # pygame.sprite.Sprite.__init__(self, self.groups)
        # self.x = 1
        # self.y = 1
        # self.angle = randint(0,360)
        # self.speed = 1
        # return
        
    # def update(self, size):
        # self.x += self.speed * math.cos(math.radians(self.angle))
        # self.y -= self.speed * math.sin(math.radians(self.angle))
        # if self.x > 800:
            # self.x -= 800
        # if self.x < 0:
            # self.x += 800
        # if self.y > 800:
            # self.y -= 800
        # if self.y < 0:
            # self.y += 800
        # return
        
    # def get_location(self):
        # return (self.x, self.y)
        
    # def getSize(self):
        # pass
        # return


# Single Round of the main game loop    
def main(ship, asteroidGroup, screen, lives, size):
    endOfRound = False
    clock = pygame.time.Clock()


    while not endOfRound:
        # 60 Framse per second
        os.system('cls')
        clock.tick(60) # Game will render at 60 frames per second
    
        # Process User Inputs
        isShoot = False
        for event in pygame.event.get():#user does something
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                isShoot = ship.keydown(event)
            elif event.type == pygame.KEYUP:
                isShoot = ship.keyup(event)

        if isShoot:
            Bullet(ship.get_position(), ship.get_angle())
                
        # Process Time Increment
        debug("STARTING PROCESS TIME INCREMENT")
        #for each in objectList:
        ship.update(size)
        for each in asteroidGroup:
            each.update(size)
            print "Ast", each.get_location()
        for each in bulletGroup:
            each.update(size)
            print "Bul", each.get_location()

        # Process Collision Detect
        debug("STARTING COLLISION DETECT")
        ###### Add Collision detect here.

        # Process Graphics
        debug("STARTING GRAPHICS ENGINE")
        displayGameScreen(ship, asteroidGroup, bulletGroup, screen, size)
        if lives == 0:
            return True
    
    pygame.quit()   
    return False # Change this to a gameOver test (No more lives, not more, whatever)


# Game Starting point
if __name__ == "__main__":
    bulletGroup = pygame.sprite.Group()
    Bullet.groups = bulletGroup
    asteroidGroup = pygame.sprite.Group()
    Asteroid.groups = asteroidGroup
    # Clear Console Screen
    os.system("cls")
    
    # Display Startup Screen, and return menu selection (Start Game = 1, Options = 2)
    menuSelection = displayStartupScreen()
    
    # Start Game Menu Option Selected
    if menuSelection == 1:
        lives = 3
        gameOver = False
        while not gameOver:
            # Hard coded number of asteroids. May change later depending on difficulty/level/rounds.
            numberOfAsteroids = 2
        
            # Initialize our Object list
            objectList = []

            
            # Create the ship object
            size = setScreenSize(800, 800) #redefined size variable as call of setScreenSize function
            initial_pos_ship = [size[0]/2,size[1]/2]
            initial_vel = [0,0]
            initial_angle = 0
            ship = Ship(initial_pos_ship,initial_vel,initial_angle)
            objectList.append(ship)
            
            # Create the asteroids
            #asteroidImage = pygame.image.load("sgilogo2.gif").convert() #set player image
            for i in range(0, numberOfAsteroids):
                Asteroid() # Creates an Asteroid Object. Automatically dumps it into the asteroid list.


            # Start the main game loop      
            screen = createScreen(size)
            gameOver = main(ship, asteroidGroup, screen, lives,size)
    
    # Options Menu Selected
    if menuSelection == 2:
        pass
     
        
        
        
        
        
        
        
        