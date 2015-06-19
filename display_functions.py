from random import *
import pygame
import sys
import math
from pygame.locals import *
from AsteroidClass import *
from explosionClass import *
from HighScoreControl import *
from PlayerUp import *

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

def highScoreBlit(highScore, index, gameScreen, background):
    scoreList = readHighScoresFromFile()
    highScore = scoreList[index]
    font = pygame.font.Font(None, 33)
    text = font.render(str(highScore[0]) + " " + str(highScore[1]), 1, (255,255,255))#, (0,0,0))
    textPos = text.get_rect()
    textPos.centerx = background.get_rect().centerx
    if index == 0:
        textPos.centery = background.get_rect().centery + 30
        gameScreen.blit(text, textPos)
    elif index == 1:
        textPos.centery = background.get_rect().centery + 55
        gameScreen.blit(text, textPos)
    elif index == 2:
        textPos.centery = background.get_rect().centery + 80
        gameScreen.blit(text, textPos)
    elif index == 3:
        textPos.centery = background.get_rect().centery + 105
        gameScreen.blit(text, textPos)
    elif index == 4:
        textPos.centery = background.get_rect().centery + 130
        gameScreen.blit(text, textPos)
    return

def easterEgg(ship):
    easterEgg = False
    if ship.get_score() > 1000000 and ship.get_score() < 1000000:
        easterEgg = True
        return easterEgg

def displayGameScreen(ship, asteroidGroup, bulletGroup, explosionGroup, playerUpGroup, gameScreen, size):
    #pygame.display.set_caption(str(clock.get_fps()))

    #SET BACKGROUND
    if easterEgg(ship) == True:
        bgImage = pygame.image.load("Graphics_Assets\grass_field.png")
    else:
        bgImage = pygame.image.load("Graphics_Assets\star_ground_2.png")
    background = pygame.transform.scale(bgImage, (size))
    gameScreen.blit(background, (0,0))
    
    #SHIP BLIT
    #Standard ship/thrust
    if easterEgg(ship) == True:
        shipImg = pygame.image.load("Graphics_Assets\hand_gun.png")
    elif ship.get_invincible() == False:
        if ship.get_thrust() == True:
            shipImg = pygame.image.load("Graphics_Assets\ship_1_thrust.png")
        else:
            shipImg = pygame.image.load("Graphics_Assets\ship_1.png")
    
    #Standard ship/shield/thrust
    elif ship.get_shield() == True:
        if ship.get_thrust() == True:
            shipImg = pygame.image.load("Graphics_Assets\ship_1_shield_thrust.png")
        else:
            shipImg = pygame.image.load("Graphics_Assets\ship_1_shield.png")        

    #Ghost ship/thrust
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
        if easterEgg(ship) == True:
            if rad == 15:
                aImg = pygame.image.load("Graphics_Assets\\buffalo_small.png")
            elif rad == 30:
                aImg = pygame.image.load("Graphics_Assets\\buffalo.png")

        else:
            if rad == 15:
                aImg = pygame.image.load("Graphics_Assets\meteor_retro_3.png")
            elif rad == 30:
                aImg = pygame.image.load("Graphics_Assets\meteor_retro_2.png")
        aLoc = each.get_location()
        aAngle = each.get_angle()
        rotAstr = rot_center(aImg, aAngle)

        gameScreen.blit(rotAstr, (aLoc))


    #POWERUP BLIT
    for each in playerUpGroup:
        powerUpImg = pygame.image.load("Graphics_Assets\power_up.bmp")
        powerUpLoc = each.get_location()
        gameScreen.blit(powerUpImg, powerUpLoc)
        


    #BULLET BLIT
    for each in bulletGroup:
        if each.get_large() == False:
            bImg = pygame.image.load("Graphics_Assets\laser.png")
        else:
            bImg = pygame.image.load("Graphics_Assets\laser_shield.png")
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
        #Asteroid
        if each.get_name() == "asteroid":
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
        else:
            #Ship: layer 1
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

    #Ship: layer 2
    for each in explosionGroup:
        if each.get_name() == "ship":
            shipExpNum = each.get_image_number()
            if shipExpNum >= 4:
                shipExpImg = pygame.image.load("Graphics_Assets\ship_exp_1.png")
            if shipExpNum == 3:
                shipExpImg = pygame.image.load("Graphics_Assets\ship_exp_2.png")
            if shipExpNum == 2:
                shipExpImg = pygame.image.load("Graphics_Assets\ship_exp_3.png")
            if shipExpNum == 1:
                shipExpImg = pygame.image.load("Graphics_Assets\ship_exp_4.png")

            gameScreen.blit(shipExpImg, each.get_location())
    

    #COLLISION CHECK
    #Asteroid v Ship
    if ship.get_invincible() == False:
        for asteroid in asteroidGroup:
            c = collision(ship.get_position(), asteroid.get_location(), ship.get_radius(), asteroid.get_radius())
            if c == True:
                
                Explosion("ship", ship.get_position(), 4, 0.5, 60)

                ship.death()
               

    #Bullet v Asteroid
    for asteroid in asteroidGroup:
        for bullet in bulletGroup:
            c = collision(asteroid.get_location(), bullet.get_location(), asteroid.get_radius(), bullet.get_radius())
            if c == True:
                bulletGroup.remove(bullet)
                asteroid.make_small_asteroids()
                Explosion("asteroid", asteroid.get_location(), 4, 0.5, 60)
                ship.update_score()

                if ship.get_score() % 1000 == 0:
                    Player_up(asteroid.get_location())

                asteroidGroup.remove(asteroid)

    #Ship v Power Up
    for each in playerUpGroup:
        c = collision(ship.get_position(), each.get_location(), ship.get_radius(), each.get_radius())
        if c == True:
            powerUpType = random.randint(1,3)
            if powerUpType == 1:
                ship.add_life()
            elif powerUpType == 2:
                ship.activate_shield()
            elif powerUpType == 3:
                ship.activate_bulletPowerUp()
        
            playerUpGroup.remove(each)        
    
    


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

    
    #GAME OVER
    if ship.get_lives() <= 0:
        #Game Over Text
        font = pygame.font.Font(None, 100)
        gameOverText = font.render("GAME OVER", 1, (255,255,255))#, (0,0,0))
        gameOverTextPos = gameOverText.get_rect()
        gameOverTextPos.centerx = background.get_rect().centerx
        gameOverTextPos.centery = background.get_rect().centery - 130
    
        # Blit Screen
        gameScreen.blit(gameOverText, gameOverTextPos)


        #Press Key to Continue
        font = pygame.font.Font(None, 33)
        contText = font.render("press any key to continue", 1, (255,255,255))#, (0,0,0))
        contTextPos = contText.get_rect()
        contTextPos.centerx = background.get_rect().centerx
        contTextPos.centery = background.get_rect().centery - 80

        #Blit Screen
        gameScreen.blit(contText, contTextPos)

        #Call High Score File
        scoreList = readHighScoresFromFile()
        player = ship.get_name()
        if ship.get_score_recorded() == False:
            finalScore = ship.get_score()
            insertHighScore(scoreList, player, finalScore)
            saveHighScoresToFile(scoreList)
            ship.set_score_recorded(True)
        else:
            pass


        #HIGH SCORES
        font = pygame.font.Font(None, 50)
        HStext = font.render("HIGH SCORES", 1, (255,255,255))#, (0,0,0))
        HStextPos = HStext.get_rect()
        HStextPos.centerx = background.get_rect().centerx
        HStextPos.centery = background.get_rect().centery - 5

        #Blit Screen
        gameScreen.blit(HStext, HStextPos)
        
        #Individual Scores
        highScore1 = scoreList[0]
        highScore2 = scoreList[1]
        highScore3 = scoreList[2]
        highScore4 = scoreList[3]
        highScore5 = scoreList[4]

        highScoreBlit(highScore1, 0, gameScreen, background)
        highScoreBlit(highScore2, 1, gameScreen, background)
        highScoreBlit(highScore3, 2, gameScreen, background)
        highScoreBlit(highScore4, 3, gameScreen, background)
        highScoreBlit(highScore5, 4, gameScreen, background)



    #DISPLAY UPDATE
    pygame.display.update()




