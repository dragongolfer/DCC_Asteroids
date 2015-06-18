import os, sys, random, math
import pygame

pygame.init()

height = 800
width = 800
size = (width, height) #here I am setting the size of the window

black = (0, 0, 0)
white = (255, 255, 255)
#create a clock and a gameover variable
clock = pygame.time.Clock()
game_over = False #conditional that determines if game is playing

asteroid_list = [] #list where my astroid objects are stored
screen = pygame.display.set_mode(size)#this creates the window with the size specified
pygame.display.set_caption("Asteroids Errywhere")#sets the display to show the string
background = pygame.image.load("StarField.gif").convert() #sets background
collision = False
##Use Trigonometry to make this easier
class Asteroid(pygame.sprite.Sprite):
    def __init__(self, location):
        pygame.sprite.Sprite.__init__(self)
        self.x_axis = location[0] #cosine runs paralell to the x-axis
        self.y_axis = location[1] #sine runs paralell to the y-axis
        self.angle = random.randint(0, 360) #angle of rotation randomly selected 
        self.angle_of_rotation = random.randint(0,360)
        self.angluar_momentum = 10 #amount of energy the asteroid has
        self.angular_velocity = 10 #one degree of rotation per clock tick, based on frame rate
        self.image = pygame.image.load("Asteroid.gif").convert() #just the image of the asteroids
        #self.num_of_asteroids = 0
        self.rect = self.image.get_rect()#forms a rectangle for collision detection, if boxes touch they collide
        self.radius = 10
        return

    def get_location(self):
        return (self.x_axis, self.y_axis)

    def get_angle(self):
        return self.angle_of_rotation

    def movement(self):
        self.x_axis += self.angluar_momentum * math.cos(math.radians(self.angle))#uses trig functions to derive the proper
        self.y_axis -= self.angluar_momentum * math.sin(math.radians(self.angle))#movement along a 2D plane for the asteroid
        self.angle_of_rotation += self.angular_velocity
        if self.x_axis > 800: #if x axis is greater than screen size then adjust the x axis
            self.x_axis = self.x_axis - 800
        if self.x_axis < 0:
            self.x_axis = self.x_axis + 800
        if self.y_axis > 800: #if y axis is greater than screen size then adjust the y axis
            self.y_axis = self.y_axis - 800
        if self.y_axis < 0:
            self.y_axis = self.y_axis + 800
        return

    def make_small_asteroids(self):
        smallAsteroid = Asteroid()
        smallAsteroid.radius = 5
        smallAsteroid.x_axis = self.x_axis
        smallAsteroid.y_axis = self.y_axis
        smallAsteroid2 = Asteroid()
        smallAsteroid2.radius = 5
        smallAsteroid2.x_axis = self.x_axis
        smallAsteroid2.y_axis = self.y_axis
        return



def rot_center(image, angle):
    '''rotate an image while keeping its center and size'''
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image


def spawn_asteroids():
    screen.blit(background, (0,0))
    #coll_x, coll_y = Asteroid.get_location()
    #for lone_asteroid in range(10):
    #   lone_asteroid = Asteroid()
    #   asteroid_list.append(lone_asteroid)

    lone_asteroid1 = Asteroid((1,100))
    lone_asteroid2 = Asteroid((1,150))
    asteroid_list.append(lone_asteroid1)
    asteroid_list.append(lone_asteroid2)

    while game_over == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(white) #has to be outside the foor loop or only one asteroid will appear!       
        for lone_asteroid in asteroid_list:
            asteroid_position = lone_asteroid.get_location()
            rot_image = rot_center(lone_asteroid.image, lone_asteroid.get_angle())
            screen.blit(rot_image, asteroid_position)
            lone_asteroid.movement()
            #screen.blit(lone_asteroid.image, asteroid_position)
            if math.sqrt((lone_asteroid1.x_axis - lone_asteroid2.x_axis)**2 + (lone_asteroid1.y_axis - lone_asteroid2.y_axis)**2) < 20:#pygame.sprite.collide_circle(lone_asteroid1, lone_asteroid2):#this is for collision detection
                #asteroid_list.remove(lone_asteroid1)
                #print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
                print "You had an accident"
            else:
                print "Things are fine"
            #print "Radii", lone_asteroid1.radius, lone_asteroid2.radius
            #print "Locale:", lone_asteroid1.get_location(), lone_asteroid2.get_location()
            #print "Distance:", math.sqrt((lone_asteroid1.x_axis - lone_asteroid2.x_axis)**2 + (lone_asteroid1.y_axis - lone_asteroid2.y_axis)**2)
            
            #continue
        #if (coll_x in range(lone_asteroid.x_axis - lone_asteroid.angle, lone_asteroid.x_axis + lone_asteroid.angle) and coll_y in range(lone_asteroid.y_axis - lone_asteroid.angle, lone_asteroid.y_axis + lone_asteroid.angle)):
        #    collision = True
        #else:
        #    collision = False
        #pygame.draw.circle(screen, colour("white"),[lone_asteroid.x_axis, lone_asteroid.y_axis], lone_asteroid.angle)

        pygame.display.update()
        pygame.time.delay(100)

spawn_asteroids()
# http://stackoverflow.com/questions/8195649/python-pygame-collision-detection-with-rects?rq=1