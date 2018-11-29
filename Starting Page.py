import pygame
import time
pygame.init()
WIDTH = 800
HEIGHT = 800
gameWindow = pygame.display.set_mode((WIDTH, HEIGHT))

# variables

WHITE = (255,255,255)
BLACK = (  0,  0,  0)
outline = 0
pygame.font.init()
pygame.mixer.init()
font = pygame.font.SysFont("Comic Sans MS", 36)

Narwhal = pygame.image.load("C:\Users\user\Desktop\Meccha Labs\Undertale Game Thing\Evil Narwhal.png")
##Gaster = pygame.image.load("C:\Users\user\Desktop\Meccha Labs\Undertale Game Thing\Gaster_Sprite2.png")

## SHOULD ADD GLITCHES ON PURPOSE

inPlay = True

# functions
def battlepage():
    gameWindow.fill(BLACK)
    pygame.draw.rect(gameWindow, WHITE, (50, 600, 300, 100), 1)
    pygame.draw.rect(gameWindow, WHITE, (450, 600, 300, 100), 1)
    gameWindow.blit(Narwhal, (155, 20))
    graphics1 = font.render("Fight-space", 1, WHITE)
    graphics2 = font.render("Mercy-enter", 1, WHITE)
    gameWindow.blit(graphics1, (150, 620))
    gameWindow.blit(graphics2, (550, 620))
    pygame.display.update()
    pygame.mixer.music.load("C:\Users\user\Desktop\Meccha Labs\Undertale Game Thing\Gasters_Theme.mid")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(loops = -1)
    time.sleep(5)

##def health-point ()  - see Eric's code as referene
##
##def int ball_game_sim(health)
##    print "this is bgame sim, health passed in is ", health
##    return 10


while inPlay:
    battlepage()
##    score-board(new health point)
##    
##    if key== "space"
##        point = call ballon-game_sim()
##        recalculate health
##
##        if still have health points
##           call game2
##           recalculate health
##        
##    if key == "enter"
##        point = call game2
