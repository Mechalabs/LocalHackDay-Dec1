import pygame, time
from random import randint
from pygame.locals import *

pygame.init()

gamewindow = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Game")
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
win = False
count = 0

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
    
def gameover():
    gamewindow.fill(BLACK)
    graphics = font.render("Game Over",1,WHITE)
    gamewindow.blit(graphics,(270,250))
    pygame.display.update()

def wingame():
    gamewindow.fill(BLACK)
    graphics = font.render("Good job you win!",1,WHITE)
    gamewindow.blit(graphics, (200,250))
    pygame.display.update()
    
while inPlay:
    keys=pygame.key.get_pressed()
    if keys[K_UP]:
        icony-=3
    if keys[K_DOWN]:
        icony+=3
    if(x == 0):
        s = randint(0,500)
        x = 750
        count = count+1
    else:
        s == s
        x = x-2
    if(x <= 80):
        if(icony <= s or icony >= s+30):
            inPlay = False
    if(count == 10):
        win = True
        inPlay = False

    update(x)

if(win == False):
    gameover()
else:
    wingame()
time.sleep(5)
pygame.quit()