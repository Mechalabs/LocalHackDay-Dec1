import pygame
import time
from random import randint
pygame.init()
pygame.font.init()
pygame.mixer.init()
WIDTH = 800
HEIGHT = 800
gameWindow = pygame.display.set_mode((WIDTH, HEIGHT))

# Variables
font = pygame.font.SysFont("Comic Sans MS", 32)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
oppHP = 100
playHP = 100
Narwhal = pygame.image.load("Evil Narwhal.png")
fightNarwhal = pygame.image.load("Evil Narwhal - FIGHT.png")

# Functions
def startingPage():
    gameWindow.fill(BLACK)
    pygame.draw.rect(gameWindow, WHITE, (50, 600, 300, 100), 1)
    pygame.draw.rect(gameWindow, WHITE, (450, 600, 300, 100), 1)
    gameWindow.blit(Narwhal, (155, 20))
    graphics1 = font.render("Fight - Space", 1, WHITE)
    graphics2 = font.render("Mercy - Right Shift", 1, WHITE)
    gameWindow.blit(graphics1, (100, 625))
    gameWindow.blit(graphics2, (451, 625))
    pygame.display.update()

##def drawOppHP():
##
##def drawPlayHP():

# Load Music
pyame.mixer.music.load("field_of_hopes.ogg")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(loops = -1)

# Main Program

inPlay = True

while inPlay:
    startingPage()



pygame.quit()
