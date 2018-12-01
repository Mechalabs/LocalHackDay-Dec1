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
icony = 300
x = 750
s = randint(0,500)
font = pygame.font.SysFont("Comic Sans",72)
inPlay = True
points = 0
timepassed = 0
def update(x):
    pygame.event.clear()
    gamewindow.fill(BLACK)
    block1 = pygame.display.get_surface()
    gamewindow.fill(BLACK)
    gamewindow.blit(pygame.transform.scale(icon, (40, 40)), (50, icony))
    rectangle1 = pygame.Rect(x,0,50,s)
    block1.fill(Color("WHITE"), rectangle1)
    block2 = pygame.display.get_surface()
    rectangle2= pygame.Rect(x,s+70,50,530-s)
    block2.fill(Color("WHITE"), rectangle2)
    pygame.display.update()
    time.sleep(0.005)
    
while inPlay:
    keys=pygame.key.get_pressed()
    if keys[K_UP]:
        icony-=3
    if keys[K_DOWN]:
        icony+=3
    if(x == 0):
        s = randint(0,500)
        x = 750
    else:
        s == s
        x = x-2
    if(x == 80):
        if(icony <= s or icony >= s+30):
            icony = 300
        else:
            points = points+1
    if(timepassed >= 30):
        inPlay = False
    update(x)
    timepassed = timepassed+0.005

gamewindow.fill(BLACK)
pointsscored = str(points)
pointtext = font.render(pointsscored, 3, WHITE)
text = font.render('points: ', 3, WHITE)
gamewindow.blit(text, (250,300))
gamewindow.blit(pointtext, (450,300))
pygame.display.update()
time.sleep(3)
pygame.quit()
