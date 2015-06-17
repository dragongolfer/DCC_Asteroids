from random import *
import pygame
import sys
from pygame.locals import *

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
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image


def displayGameScreen(objectList, gameScreen, size):
    #SET BACKGROUND
    bgImage = pygame.image.load("Graphics_Assets\star_ground_2.png")
    backGround = pygame.transform.scale(bgImage, (size))
    gameScreen.blit(backGround, (0,0))
    
    #SET SHIP
    ship = objectList[0]
    shipImg = pygame.image.load("Graphics_Assets\ship_1.png")
    shipLoc = ship.get_position()
    shipAngle = ship.get_angle()
    rotShip = rot_center(shipImg, shipAngle)

    shipImg.set_colorkey((0,0,0))
    gameScreen.blit(rotShip, (shipLoc))
    
    #SET ASTEROIDS or BULLET
    '''
    for index, each in enumerate(objectList)
        if isininstance(each, Asteroid):
            aImg = pygame.image.load("Graphics_Assets\meteor_retro_3.png")
            aLoc = a.get_location()
            gameScreen.blit(aImg, (aLoc))
        
        elif isininstance(each, Bullet):
            bImg = pygame.image.load("Graphics_Assets\##########")
            bLoc = each.get_position()
            bAngle = each.get_angle()
            rotBullet = rot_center(bImg, (bLoc))

            bImg.set_colorkey((0,0,0))
            gameScreen.blit(rotBullet, (bLoc))
            pygame.display.update()
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


    #QUIT OPERATION
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

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