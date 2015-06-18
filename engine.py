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
from bulletClass import *       # Michael
from explosionClass import *    # Michael
from display_functions import * # Matt

pygame.init()



def debug(message):
    DEBUG = False
    if DEBUG:
        print("DEBUG: " + str(message))
    return DEBUG
    



# Single Round of the main game loop    
def main(ship, asteroidGroup, explosionGroup, screen, lives, size):
    endOfRound = False
    clock = pygame.time.Clock()
    endOfGamePause = 0


    while not endOfRound:
        # 60 Framse per second
        if debug(""): os.system('cls')
        clock.tick(60) # Game will render at 60 frames per second
    
        # Process User Inputs
        if ship.get_lives() > 0:
            # Player is still alive, Pass inputs to Ship class
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
        else:
            debug("END OF GAME DAMNIT!")
            endOfGamePause += 1
            if endOfGamePause > 180:
                for event in pygame.event.get():#user does something
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        return True
            
        
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
            debug(("Ast" +str(each.get_location())))
        for each in bulletGroup:
            each.update(size)
            debug(("Bul" + str(each.get_location())))
        for each in explosionGroup:
            each.update(size)
            debug(("Exp" + str(each.get_location())))# + str(each.get_counter()))))
            if each.get_counter() <= 0:
                explosionGroup.remove(each)

            
           
        # Process Collision Detect
        debug("STARTING COLLISION DETECT")
        ###### Add Collision detect here.

        # Process Graphics
        debug("STARTING GRAPHICS ENGINE")
        displayGameScreen(ship, asteroidGroup, bulletGroup, explosionGroup, screen, size)

        if len(asteroidGroup) == 0:
            endOfRound = True
            debug("Next Round")
            return False

    return False # Change this to a gameOver test (No more lives, not more, whatever)


# Game Starting point
if __name__ == "__main__":
    # Create Sprite Groups
    shipGroup = pygame.sprite.Group()
    Ship.groups = shipGroup
    bulletGroup = pygame.sprite.Group()
    Bullet.groups = bulletGroup
    asteroidGroup = pygame.sprite.Group()
    Asteroid.groups = asteroidGroup
    explosionGroup = pygame.sprite.Group()
    Explosion.groups = explosionGroup
    
    # Clear Console Screen
    os.system("cls")
    
    while True:
        # Display Startup Screen, and return menu selection (Start Game = 1, Options = 2)
        menuSelection = displayStartupScreen()
        
        # Start Game Menu Option Selected
        if menuSelection == 1:
            lives = 3
            gameOver = False
            numberOfAsteroids = 0
            asteroidGroup.empty()
            # Create the ship object
            size = setScreenSize(800, 800) #redefined size variable as call of setScreenSize function
            initial_pos_ship = [size[0]/2,size[1]/2]
            initial_vel = [0,0]
            initial_angle = 0
            ship = Ship(initial_pos_ship,initial_vel,initial_angle)
            
            while not gameOver:
                # Hard coded number of asteroids. May change later depending on difficulty/level/rounds.
                numberOfAsteroids += 2
                
                # Create the asteroids
                #asteroidImage = pygame.image.load("sgilogo2.gif").convert() #set player image
                for i in range(0, numberOfAsteroids):
                    Asteroid() # Creates an Asteroid Object. Automatically dumps it into the asteroid list.


                # Start the main game loop      
                screen = createScreen(size)
                gameOver = main(ship, asteroidGroup, explosionGroup, screen, lives,size)
        
        # Options Menu Selected
        if menuSelection == 2:
            pass
         
        
        
        
        
        
        
        
        