import pygame, time
from random import randint
from pygame.locals import *

pygame.init()

gamewindow = pygame.display.set_mode((800, 600))
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
icon =  pygame.image.load('heart.png')
x = 0
icony = 300
iconx = 400
s = randint(0,500)
font = pygame.font.SysFont("Comic Sans",72)
ingamefont = pygame.font.SysFont("Comic Sans" ,45)
inPlay = True
timepassed = 0
deathcounter = 0
ingamedeathtext = ingamefont.render('Hits: ', 3, GREEN)
passed = False
miliseconds = 0
seconds = 0
timeremaining = 40
ingametimetext = ingamefont.render('Time remaining: ', 3, GREEN)
direction= randint(0,3)
y = 0
s2 = randint(0,700)

def update(x,y):
    pygame.event.clear()
    gamewindow.fill(BLACK)
    gamewindow.fill(BLACK)
    gamewindow.blit(pygame.transform.scale(icon, (40, 40)), (iconx, icony))
    if(direction == 0 or direction == 1):
        block1 = pygame.display.get_surface()
        rectangle1 = pygame.Rect(x,0,50,s)
        block1.fill(Color("WHITE"), rectangle1)
        block2 = pygame.display.get_surface()
        rectangle2= pygame.Rect(x,s+70,50,530-s)
        block2.fill(Color("WHITE"), rectangle2)
    elif(direction == 2 or direction == 3):
        block1= pygame.display.get_surface()
        rectangle1 = pygame.Rect(0,y,s2,50)
        block1.fill(Color("WHITE"), rectangle1)
        block2 = pygame.display.get_surface()
        rectangle2 = pygame.Rect(s2+80, y,720-s2, 50)
        block2.fill(Color("WHITE"), rectangle2)
    gamewindow.blit(deathtext, (90, 2))
    gamewindow.blit(ingamedeathtext, (0, 0))
    gamewindow.blit(timetext, (750,0))
    gamewindow.blit(ingametimetext, (500,0))
    pygame.display.update()
    time.sleep(0.005)
    
while inPlay:
    keys=pygame.key.get_pressed()
    if keys[K_UP]:
        icony-=3
    if keys[K_DOWN]:
        icony+=3
    if keys[K_RIGHT]:
        iconx+=3
    if keys[K_LEFT]:
        iconx-=3
    if(icony > 600):
        icony = 590
    elif(icony < 0):
        icony = 10
    elif(iconx > 800):
        iconx = 790
    elif(iconx < 0):
        iconx = 10
    if(x < 0 or x > 750 or y < 0 or y > 550):
        direction= randint(0,3)
        if(direction == 0):
            s = randint(0,500)
            x = 750
            y = 300
        elif(direction==1):
            s = randint(0,500)
            x = 0
            y = 300
        elif(direction == 2):
            s2 = randint(0,700)
            x = 400
            y = 0
        elif(direction == 3):
            s2 = randint(0,700)
            x = 400
            y = 550
        passed = False
    else:
        if(direction == 0):
            x = x-2
        elif(direction == 1):
            x = x+2
        elif(direction == 2):
            y = y+1.5
        elif(direction == 3):
            y = y-1.5
    if(direction == 0 or direction == 1):
        if(x >= iconx and x<= iconx+50 and passed == False):
            if(icony <= s or icony >= s+30):
                deathcounter = deathcounter+1
                passed = True
            else:
                passed = True
    elif(direction == 2 or direction == 3):
        if(icony >=  y and icony <= y+50 and passed == False):
            if(iconx <= s2+5 or iconx >= s2+40):
                deathcounter = deathcounter+1
                passed = True
            else:
                passed = True
            
    if(timepassed >= 40):
        inPlay = False
    deaths=str(deathcounter)
    deathtext = ingamefont.render(deaths, 3, GREEN)
    if(miliseconds >= 1):
        seconds = seconds+1
        timeremaining = 40-seconds
        miliseconds = 0
    timedisplay = str(timeremaining)
    timetext = ingamefont.render(timedisplay, 3, GREEN)
    update(x,y)
    timepassed = timepassed+0.005
    miliseconds = miliseconds + 0.005
