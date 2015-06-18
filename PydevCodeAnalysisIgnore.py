#@PydevCodeAnalysisIgnore
#@UndefinedVariable
import pygame as p, sys, random as r, math as m
from pygame.locals import *


p.init()

w,h=300,300
display = p.display.set_mode([w,h])
p.display.set_caption("Collision Test")
font = p.font.SysFont("calibri", 12)

x,y=150,150
radius=50
cursorRadius=20
count=0
hit=False
white = (255,255,255)
blue =(144,144,144)
while(True):
    display.fill([0,0,0])
    mx,my=p.mouse.get_pos()
    for event in p.event.get():
        if(event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE)):
            p.quit()

    ### MAIN TEST FOR COLLISION ###
    if(mx in range(x-radius,x+radius) and my in range(y-radius,y+radius)):
        hit=True
    else:
        hit=False

    p.draw.circle(display,blue,[x,y],radius,0)
    p.draw.circle(display,white,p.mouse.get_pos(),cursorRadius,0)

    xy=font.render(str(p.mouse.get_pos()),True, white)
    hitTxt=font.render(str(hit),True, blue)
    display.blit(xy,[5,285])
    display.blit(hitTxt,[270,285])

    p.display.update()

    #http://stackoverflow.com/questions/22135712/pygame-collision-detection-with-two-circles