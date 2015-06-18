from random import *
import pygame
import sys
import math
from pygame.locals import *
from AsteroidClass import *

pygame.init()

'''
#TESTING CLASSES
class Ship():
    def __init__(self):
        self.pos = [100, 100]
        self.angle = 230

    def get_position(self):
        return self.pos

    def get_angle(self):
        return self.angle

class Asteroid():
    def __init__(self, id, locX, locY):
        self.id = id
        self.location = [locX, locY]

    def get_location(self):
        return self.location
'''

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

def displayGameScreen(ship, asteroidGroup, bulletGroup, gameScreen, size):
    #pygame.display.set_caption(str(clock.get_fps()))

    #SET BACKGROUND
    bgImage = pygame.image.load("Graphics_Assets\star_ground_2.png")
    backGround = pygame.transform.scale(bgImage, (size))
    gameScreen.blit(backGround, (0,0))
    
    #SET SHIP
    shipImg = pygame.image.load("Graphics_Assets\ship_1.png")
    shipLoc = ship.get_position()
    shipAngle = ship.get_angle()
    rotShip = rot_center(shipImg, shipAngle)

    shipImg.set_colorkey((0,0,0))
    gameScreen.blit(rotShip, (shipLoc))
    

    for each in asteroidGroup:
        aImg = pygame.image.load("Graphics_Assets\meteor_retro_3.png")
        aLoc = each.get_location()
        gameScreen.blit(aImg, (aLoc))

    for each in bulletGroup:
        bImg = pygame.image.load("Graphics_Assets\laser.png")
        bLoc = each.get_location()
        bAngle = each.get_angle()
        rotBullet = rot_center(bImg, bAngle)

        #REMOVE BULLETS
        if (bLoc[0] < 0) or (bLoc[0] > size[0]):
            bulletGroup.remove(each)

        elif (bLoc[1] < 0) or (bLoc[1] > size[1]):
            bulletGroup.remove(each)

        gameScreen.blit(rotBullet, (bLoc))


    #COLLISION CHECK
    #Asteroid v Ship
    print ship.get_lives()
    
    #if ship.get_invincible() == False:
    for asteroid in asteroidGroup:
        c = collision(ship.get_position(), asteroid.get_location(), ship.get_radius(), asteroid.get_radius())
        if c == True:
            ship.death()
            print ship.get_lives()  


    #Bullet v Asteroid
    for asteroid in asteroidGroup:
        for bullet in bulletGroup:
            c = collision(asteroid.get_location(), bullet.get_location(), asteroid.get_radius(), bullet.get_radius())
            if c == True:
                bulletGroup.remove(bullet)
                asteroidGroup.remove(asteroid)


    #SCORING
    #font = pygame.font.Font(None, 100)
    #asteroidText = font.render("ASTEROIDS", 1, (255,255,255), (0,0,0))
    #asteroidTextPos = asteroidText.get_rect()
    #asteroidTextPos.centerx = background.get_rect().centerx
    #asteroidTextPos.centery = (background.get_rect().centery - 50)

    
    '''
    #COLLISION
    #Set Asteroids
    asteroids = objectList[1:]
    for a in asteroids:
        aImg = pygame.image.load("Graphics_Assets\meteor_retro_3.png")
        aLoc = a.get_location()
        a.rect = aImg.get_rect()
        a.rect.x = a.x
        a.rect.y = a.y
        gameScreen.blit(aImg, (aLoc))

    asteroid_list = list(objectList[1:])
    for asteroid in asteroid_list:
            if pygame.sprite.collide_rect(ship,asteroid):
                objectList.remove(asteroid)
    '''

    #DISPLAY UPDATE
    pygame.display.update() 


'''    
#TESTING PURPOSES
s = Ship()
objectList = [s]


for a in range(10):
    locX = randint(10,290)
    locY = randint(10,290)
    
    asteroid = Asteroid(a, locX, locY)
    objectList.append(asteroid)


gameScreen = pygame.display.set_mode((300, 300))
while True:
    displayGameScreen(objectList, gameScreen)
'''