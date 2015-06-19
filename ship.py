import pygame
import random
import math

#constant colors to use for screen display
BLACK = (0,0,0)
WHITE = (255,255,255)
#SIZE = (800,800)

#initialize pygame to use sounds for ship class
pygame.init()
ship_thrust_sound = pygame.mixer.Sound("Graphics_Assets\go_thrust.ogg")
ship_missile_sound = pygame.mixer.Sound("Graphics_Assets\missile.wav")

#used for calculating forward direction based on angle(in radians) provided
def angle_to_vector(ang):
    return [math.cos(ang), -math.sin(ang)]
 
#uses pythagorean theorem to calculate differences in distance between two points.
def dist(p,q):
    return math.sqrt((p[0]-q[0])**2+(p[1]-q[1])**2)
 
 #pygame function used to take in image and angle and rotate it
 #image must be a square to work.
def rot_center(image, angle):
    '''rotate an image while keeping its center and size'''
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image
 
# Ship class - child class of pygame sprite class
# currently image here is not used
# initialize variables used for ship on creation.
class Ship(pygame.sprite.Sprite):
    def __init__(self, pos, vel, angle):
        pygame.sprite.Sprite.__init__(self,self.groups)#groups used in case multiple ships are added
        self.name = "Player"
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = angle
        self.thrust = False
        self.angle_vel = 0
        self.image = pygame.image.load("Graphics_Assets\ship_1.png")#not used, just in case sprite groups are used
        self.rect = self.image.get_rect()
        #x,y coordinates used for determing what the forward direction is
        self.forward = [0,0]
        #radius used for collision detection
        self.radius = 22.5
        self.score = 0
        self.lives = 3
        #invincible used for initial spawn
        self.invincible = False
        #counter used to know how long ship is invincible
        self.time_counter = 0
        self.shield_counter = 0
        self.shield = False
        #counter used to knof how long the ship is in bullet powerup
        self.bulletPowerup = False
        self.bullet_counter = 0
        
        self.score_recorded = False
        
    
    def get_position(self):
        return (self.pos[0],self.pos[1])

    def get_angle(self):
        return self.angle

    #sets thrust to true if up arrow is pressed and plays sound.
    def set_thrust(self, thrust):
        self.thrust = thrust
        if self.thrust == True:
            ship_thrust_sound.play()
        else:
            ship_thrust_sound.stop()

    #returns true for bullet creation and plays sound.
    def shoot(self):
        ship_missile_sound.set_volume(.5)
        ship_missile_sound.play()
        return True

    #draw not used. Here just in case display function wanted to reference this.
    #color value is used to set the background color of the image to black so the background image is transparent.
    def draw(self,screen):
        self.image.set_colorkey(BLACK)
        screen.blit(rot_center(self.image, self.angle),self.pos)
 
    #on screen refresh, ship position is updated.
    def update(self,size):
        #added a friction element so ship will stop moving if key is not pressed.
        #larger acceleration, faster the ship will move
        acc = 0.2
        fric = acc / 18
        
        #ship rotation angle for forward direction
        self.angle += self.angle_vel
        
        #calculates direction ship should be facing
        self.forward = angle_to_vector(math.radians(self.angle))
 
        #accelerates ship in the forward direction
        if self.thrust:
            self.vel[0] += self.forward[0] * acc
            self.vel[1] += self.forward[1] * acc
 
        #applies friction to velocity of ship to slow down ship when thrust isn't applied.
        self.vel[0] *= (1 - fric)
        self.vel[1] *= (1 - fric)
 
        # update positions for each update. self.rect.x & y used in case sprite collision detection is used.
        self.pos[0] = (self.pos[0] + self.vel[0]) % (size[0])
        self.pos[1] = (self.pos[1] + self.vel[1]) % (size[1])
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]

        #counter value decremented and when it hits zero invincible is set to False.
        if self.time_counter > 0:
            self.time_counter -= 1
        else:
            self.invincible = False

        if self.shield_counter > 0:
            self.shield_counter -= 1
        else:
            self.shield = False

        # counter value decrement for bullet powerup
        if self.bullet_counter > 0:
            self.bullet_counter -= 1
        else:
            self.bulletPowerup = False
            
            
            
    def set_angle_vel(self, vel):
        self.angle_vel = vel

    #used for collision detection
    def get_radius(self):
        return self.radius

    def get_score(self):
        return self.score

    def get_lives(self):
        return self.lives

    # removes life and sets invincible to True. Sets counter to 300.
    def death(self):
        self.lives -= 1
        self.invincible = True
        if self.lives <= 0:
            self.lives = 0
            return True
        else:
            self.time_counter = 300
            return False

    def toggle_invincible(self):
        if self.invincible == True:
            self.invincible = False
        else:
            self.invincible = True

    def get_invincible(self):
        return self.invincible

    def activate_shield(self):
        self.shield = True
        self.shield_counter = 600
        self.invincible = True
        self.time_counter = 600

    def deactivate_shield(self):
        self.shield = False
        self.shield_counter = 0

    def get_shield(self):
        return self.shield

    #not used now, can be used in future version.
    def checkCollision(self,asteroid_center, asteroid_location):
        pass

    def keydown(self,event):
#     ang_vel is how fast the ship will rotate
        ang_vel = 4.5
        if event.key == pygame.K_ESCAPE:
            pygame.quit()
        if event.key == pygame.K_LEFT:
            self.set_angle_vel(ang_vel)
        if event.key == pygame.K_RIGHT:
            self.set_angle_vel(-ang_vel)
        if event.key == pygame.K_UP:
            self.set_thrust(True)
        if event.key == pygame.K_SPACE:
            return self.shoot()

    def keyup(self,event):
        if event.key in (pygame.K_LEFT,pygame.K_RIGHT):
            self.set_angle_vel(0)
        if event.key == pygame.K_UP:
            self.set_thrust(False)

    def update_score(self):
        self.score += 100

    def get_score(self):
        return self.score

    def get_thrust(self):
        return self.thrust

    def get_score_recorded(self):
        return self.score_recorded

    def set_score_recorded(self,value):
        self.score_recorded = value

    def set_name(self,name):
        self.name = name

    def get_name(self):
        return self.name
        
    def add_life(self):
        self.lives += 1

    def activate_bulletPowerUp(self):
        self.bulletPowerup = True
        self.bullet_counter = 600
        
    def get_bulletPowerUp(self):
        return self.bulletPowerup