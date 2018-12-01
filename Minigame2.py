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
x = 750
icony = 300
iconx = 400
s = randint(0,500)
font = pygame.font.SysFont("Comic Sans",72)
ingamefont = pygame.font.SysFont("Comic Sans" ,45)
inPlay = True
points = 0
timepassed = 0
deathcounter = 0
ingamedeathtext = ingamefont.render('Deaths: ', 3, GREEN)
passed = False
miliseconds = 0
seconds = 0
timeremaining = 30
ingametimetext = ingamefont.render('Time remaining: ', 3, GREEN)
direction= randint(0,1)
def update(x):
    pygame.event.clear()
    gamewindow.fill(BLACK)
    block1 = pygame.display.get_surface()
    gamewindow.fill(BLACK)
    gamewindow.blit(pygame.transform.scale(icon, (40, 40)), (iconx, icony))
    rectangle1 = pygame.Rect(x,0,50,s)
    block1.fill(Color("WHITE"), rectangle1)
    block2 = pygame.display.get_surface()
    rectangle2= pygame.Rect(x,s+70,50,530-s)
    block2.fill(Color("WHITE"), rectangle2)
    gamewindow.blit(deathtext, (125, 0))
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
    if(x == 0 or x == 752):
        direction= randint(0,1)
        print(direction)
        if(direction == 0):
            s = randint(0,500)
            x = 750
        elif(direction==1):
            s = randint(0,500)
            x = 2
        passed = False
    else:
        if(direction == 0):
            x = x-2
        elif(direction == 1):
            x = x+2
    if(x >= iconx and x<= iconx+50 and passed == False):
        if(icony <= s or icony >= s+30):
            deathcounter = deathcounter+1
            passed = True
        else:
            points = points+1
            passed = True
            
    if(timepassed >= 30):
        inPlay = False
    deaths=str(deathcounter)
    deathtext = ingamefont.render(deaths, 3, GREEN)
    if(miliseconds >= 1):
        seconds = seconds+1
        timeremaining = 30-seconds
        miliseconds = 0
    timedisplay = str(timeremaining)
    timetext = ingamefont.render(timedisplay, 3, GREEN)
    update(x)
    timepassed = timepassed+0.005
    miliseconds = miliseconds + 0.005
    
    
    
gamewindow.fill(BLACK)
pointsscored = str(points)
pointtext = font.render(pointsscored, 3, WHITE)
deathtextfinal = font.render(deaths, 3, WHITE)
text = font.render('Points: ', 3, WHITE)
text2 = font.render('Deaths: ', 3, WHITE)
gameover = font.render('Game Over!', 3, WHITE)
gamewindow.blit(gameover, (275, 200))
gamewindow.blit(text, (300,300))
gamewindow.blit(pointtext, (500,300))
gamewindow.blit(text2, (300,400))
gamewindow.blit(deathtextfinal, (500, 400))
pygame.display.update()
time.sleep(3)
pygame.quit()
