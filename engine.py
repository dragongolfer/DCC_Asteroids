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
from OptionsScreen import *     # Michael
from PlayerUp import *          # Rob

pygame.init()



def debug(message):
    DEBUG = False
    if DEBUG:
        print("DEBUG: " + str(message))
    return DEBUG

#add background music
pygame.mixer.music.load('Graphics_Assets/space1.ogg')
pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
pygame.mixer.music.play()


# Single Round of the main game loop    
def main(ship, asteroidGroup, explosionGroup, screen, lives, size):
    endOfRound = False
    clock = pygame.time.Clock()
    endOfGamePause = 0


    while not endOfRound:
        # 60 Framse per second
        if debug(""): os.system('cls')
        #clock.tick(60) 
    
        # Process User Inputs
        if ship.get_lives() > 0:
            clock.tick(60) # Game will render at 60 frames per second
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
                elif event.type == pygame.constants.USEREVENT:
            # This event is triggered when the song stops playing.
            # Next, song then plays
                    pygame.mixer.music.load('Graphics_Assets/fly.ogg')
                    pygame.mixer.music.play()
                if isShoot:
                    if ship.get_bulletPowerUp():
                        Bullet(ship.get_position(), ship.get_angle(), True)
                    else:
                        Bullet(ship.get_position(), ship.get_angle(), False)

        else:
            clock.tick(10) # Game will render at 10 frames per second during death sequence
            debug("END OF GAME DAMNIT!")
            ship_thrust_sound.stop()
            ship_missile_sound.stop()
            endOfGamePause += 1 
            for event in pygame.event.get():#user does something
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if endOfGamePause > 20:
                        return True
            
        
     
        # Process Time Increment
        debug("STARTING PROCESS TIME INCREMENT")
        #for each in objectGroup, update time increment:
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
        for each in playerUpGroup:
            each.update(size)

            
           
        # Process Collision Detect
        debug("STARTING COLLISION DETECT")
        ###### Add Collision detect here.

        # Process Graphics
        debug("STARTING GRAPHICS ENGINE")
        displayGameScreen(ship, asteroidGroup, bulletGroup, explosionGroup, playerUpGroup, screen, size)

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
    playerUpGroup = pygame.sprite.Group()
    Player_up.groups = playerUpGroup
    
    
    #Default Options
    options = ["ACE"]
    
    # Clear Console Screen
    os.system("cls")
    
    while True:
        # Display Startup Screen, and return menu selection (Start Game = 1, Options = 2)
        menuSelection = displayStartupScreen()
        print menuSelection
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
            ship.set_name(options[0])
            
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
            options = displayOptionsScreen(options)
         
        
        
        
        
        
        
        
        