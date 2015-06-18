from random import *
import pygame
import sys
import math
from pygame.locals import *
from AsteroidClass import *
from explosionClass import *
from HighScoreControl import *

pygame.init()


def setScreenSize(x, y):
    size = x, y
    return size

def createScreen(size):
    screen = pygame.display.set_mode(size)
    return screen

def displayStartupScreen():
    # Set Screen parameters
    size = setScreenSize(800, 800)
    screen = createScreen(size)

    pygame.display.set_caption('Asteroids For The Win!')
    selection = 1    
    while True:
        # Process Menu Selection Inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selection += 1
                if event.key == pygame.K_UP:
                    selection -= 1
                if event.key == pygame.K_RETURN:
                    return selection
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
            
            if selection > 2:
                selection = 1
            if selection < 1:
                selection = 2
        
        # Setup Background
        backgroundimage = pygame.image.load("StarField_2.png")
        background = pygame.transform.scale(backgroundimage,(size))
        
        # Setup "ASTEROIDS" Title
        font = pygame.font.Font(None, 100)
        asteroidText = font.render("ASTEROIDS", 1, (255,255,255), (0,0,0))
        asteroidTextPos = asteroidText.get_rect()
        asteroidTextPos.centerx = background.get_rect().centerx
        asteroidTextPos.centery = (background.get_rect().centery - 50)
        
        # Setup "START" Menu button
        font = pygame.font.Font(None, 36)
        if selection == 1: 
            startText = font.render("START GAME", 1, (255,255,255), (100,100,100))
        else:
            startText = font.render("START GAME", 1, (255,255,255), (0,0,0))
        startTextPos = startText.get_rect()
        startTextPos.centerx = background.get_rect().centerx
        startTextPos.centery = (background.get_rect().centery + 20)
            
        # Setup "OPTIONS" Menu button
        if selection == 2: 
            optionsText = font.render("OPTIONS", 1, (255,255,255), (100,100,100))
        else:
            optionsText = font.render("OPTIONS", 1, (255,255,255), (0,0,0))
        optionsTextPos = optionsText.get_rect()
        optionsTextPos.centerx = background.get_rect().centerx
        optionsTextPos.centery = (background.get_rect().centery + 50) 
        
        # Blit Screen
        screen.blit(background, (0,0))
        screen.blit(asteroidText, asteroidTextPos)
        screen.blit(startText, startTextPos)
        screen.blit(optionsText, optionsTextPos)
        pygame.display.flip()
    
    #raw_input("Press Enter to continue")
    return screen

def rot_center(image, angle):
    '''rotate an image while keeping its center and size'''
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, float(angle))
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image

def collision(obj_1_Loc, obj_2_Loc, obj_1_Rad, obj_2_Rad):
    collision = False
    if math.sqrt((obj_1_Loc[0] - obj_2_Loc[0])**2 + (obj_1_Loc[1] - obj_2_Loc[1])**2) < (obj_1_Rad + obj_2_Rad):
        collision = True
    return collision

def displayGameScreen(ship, asteroidGroup, bulletGroup, explosionGroup, gameScreen, size):
    #pygame.display.set_caption(str(clock.get_fps()))

    #SET BACKGROUND
    bgImage = pygame.image.load("Graphics_Assets\star_ground_2.png")
    background = pygame.transform.scale(bgImage, (size))
    gameScreen.blit(background, (0,0))
    
    #SHIP BLIT
    if ship.get_invincible() == False:
        if ship.get_thrust() == True:
            shipImg = pygame.image.load("Graphics_Assets\ship_1_thrust.png")
        else:
            shipImg = pygame.image.load("Graphics_Assets\ship_1.png")
    else:
        if ship.get_thrust() == True:
            shipImg = pygame.image.load("Graphics_Assets\ship_1_thrust_ghost.png")
        else:
            shipImg = pygame.image.load("Graphics_Assets\ship_1_ghost.png")
    shipLoc = ship.get_position()
    shipAngle = ship.get_angle()
    rotShip = rot_center(shipImg, shipAngle)
    
    if ship.get_lives() > 0:
        gameScreen.blit(rotShip, (shipLoc))
    
    #ASTEROID BLIT
    for each in asteroidGroup:
        rad = each.get_radius()
        if rad == 15:
            aImg = pygame.image.load("Graphics_Assets\meteor_retro_3.png")
        elif rad == 30:
            aImg = pygame.image.load("Graphics_Assets\meteor_retro_2.png")
        aLoc = each.get_location()
        aAngle = each.get_angle()
        rotAstr = rot_center(aImg, aAngle)

        gameScreen.blit(rotAstr, (aLoc))





    #BULLET BLIT
    for each in bulletGroup:
        bImg = pygame.image.load("Graphics_Assets\laser.png")
        bLoc = each.get_location()
        bAngle = each.get_angle()
        rotBullet = rot_center(bImg, bAngle)

        #Remove Bullets
        if (bLoc[0] < 0) or (bLoc[0] > size[0]):
            bulletGroup.remove(each)

        elif (bLoc[1] < 0) or (bLoc[1] > size[1]):
            bulletGroup.remove(each)

        gameScreen.blit(rotBullet, (bLoc))


    #EXPLOSION BLIT
    for each in explosionGroup:
        expImgNum = each.get_image_number()
        if expImgNum == 4:
            expImg = pygame.image.load("Graphics_Assets\exp_1.png")
        if expImgNum == 3:
            expImg = pygame.image.load("Graphics_Assets\exp_2.png")
        if expImgNum == 2:
            expImg = pygame.image.load("Graphics_Assets\exp_3.png")
        if expImgNum == 1:
            expImg = pygame.image.load("Graphics_Assets\exp_4.png")

        
        gameScreen.blit(expImg, each.get_location())


    #COLLISION CHECK
    #Asteroid v Ship
    if ship.get_invincible() == False:
        for asteroid in asteroidGroup:
            c = collision(ship.get_position(), asteroid.get_location(), ship.get_radius(), asteroid.get_radius())
            if c == True:
                ship.death()
               

    #Bullet v Asteroid
    for asteroid in asteroidGroup:
        for bullet in bulletGroup:
            c = collision(asteroid.get_location(), bullet.get_location(), asteroid.get_radius(), bullet.get_radius())
            if c == True:
                bulletGroup.remove(bullet)
                asteroid.make_small_asteroids()
                asteroidGroup.remove(asteroid)

                Explosion(asteroid.get_location(), 4, 0.5, 60)

                ship.update_score()

    


    size = setScreenSize(800, 800)
    #SCORING
    score = ship.get_score()
    font = pygame.font.Font(None, 50)
    scoreText = font.render("Score: " + str(score), 1, (255,255,255), (0,0,0))
    scoreTextPos = (10,10)

    gameScreen.blit(scoreText, scoreTextPos)

    #LIVES
    lives = ship.get_lives()
    font = pygame.font.Font(None, 25)
    livesText = font.render("Lives: " + str(lives), 1, (255,255,255), (0,0,0))
    livesTextPos = ((size[0] - 100), (size[1] - 790))
    
    gameScreen.blit(livesText, livesTextPos)






    if ship.get_lives() <= 0:
        #GAME OVER
        font = pygame.font.Font(None, 100)
        gameOverText = font.render("GAME OVER", 1, (255,255,255))#, (0,0,0))
        gameOverTextPos = gameOverText.get_rect()
        gameOverTextPos.centerx = background.get_rect().centerx
        gameOverTextPos.centery = background.get_rect().centery
    
        # Blit Screen
        gameScreen.blit(gameOverText, gameOverTextPos)


        #PRESS KEY TO CONTINUE
        font = pygame.font.Font(None, 33)
        contText = font.render("press any key to continue", 1, (255,255,255))#, (0,0,0))
        contTextPos = contText.get_rect()
        contTextPos.centerx = background.get_rect().centerx
        contTextPos.centery = background.get_rect().centery + 50

        #Blit Screen
        gameScreen.blit(contText, contTextPos)


        
        #HIGH SCORES
        font = pygame.font.Font(None, 66)
        contText = font.render("High Scores", 1, (255,255,255))#, (0,0,0))
        contTextPos = contText.get_rect()
        contTextPos.centerx = background.get_rect().centerx
        contTextPos.centery = background.get_rect().centery + 100

        #Blit Screen
        gameScreen.blit(contText, contTextPos)
        


    #DISPLAY UPDATE
    pygame.display.update() 




