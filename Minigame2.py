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

def update(x):
    pygame.event.clear()
    gamewindow.fill(BLACK)
    block1 = pygame.display.get_surface()
    gamewindow.fill(BLACK)
    gamewindow.blit(pygame.transform.scale(icon, (40, 40)), (50, icony))
    rectangle1 = pygame.Rect(x,0,50,s)
    block1.fill(Color("WHITE"), rectangle1)
    block2 = pygame.display.get_surface()
    rectangle2= pygame.Rect(x,s+60,50,540-s)
    block2.fill(Color("WHITE"), rectangle2)
    pygame.display.update()
    time.sleep(0.005)

while True:
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
    update(x)

