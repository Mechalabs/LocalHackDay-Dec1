import pygame, sys
import time
pygame.init()
pygame.font.init()
pygame.mixer.init()
WIDTH = 800
HEIGHT = 800
gameWindow = pygame.display.set_mode((WIDTH, HEIGHT))

# variables

WHITE = (255,255,255)
BLACK = (  0,  0,  0)
RED = (255, 0, 0)
outline = 0
font = pygame.font.SysFont("Comic Sans MS", 32)
font2 = pygame.font.SysFont("Comic Sans MS", 36)

oppHP = 100
playHP = 100

Narwhal = pygame.image.load("Evil Narwhal.png")
fightNarwhal = pygame.image.load("Evil Narwhal - FIGHT.png")

## SHOULD ADD GLITCHES ON PURPOSE

inPlay = True

# functions
def startPage():
    gameWindow.fill(BLACK)
    pygame.draw.rect(gameWindow, WHITE, (50, 600, 300, 100), 1)
    pygame.draw.rect(gameWindow, WHITE, (450, 600, 300, 100), 1)
    gameWindow.blit(Narwhal, (155, 20))
    fight = font.render("Fight - Space", 1, WHITE)
    mercy = font.render("Mercy - Right Shift", 1, WHITE)
    gameWindow.blit(fight, (100, 625))
    gameWindow.blit(mercy, (451, 625))
##    pygame.display.update()

def drawOppHP(oppHP):
    Jeff = font.render("Jeff", 1, WHITE)
    opphealth = font.render("HP - ", 1, WHITE)
    opponentHP = font.render(str(oppHP), 1, WHITE)
    gameWindow.blit(Jeff, (10, 0))
    gameWindow.blit(opphealth, (100, 0))
    gameWindow.blit(opponentHP, (180, 0))

def drawPlayHP(playHP):
    Player = font.render("Player", 1, WHITE)
    playhealth = font.render("HP - ", 1, WHITE)
    playerHP = font.render(str(playHP), 1, WHITE)
    gameWindow.blit(Player, (10, 750))
    gameWindow.blit(playhealth, (130, 750))
    gameWindow.blit(playerHP, (210, 750))
    pygame.display.update()

pygame.mixer.music.load("field_of_hopes.ogg")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(loops = -1)

while inPlay:
    startPage()
    drawOppHP(oppHP)
    drawPlayHP(playHP)
    pygame.time.delay(50)

    pygame.event.clear()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        inPlay = False

    if keys[pygame.K_SPACE]:
        def startPage():
            gameWindow.fill(BLACK)
            pygame.draw.rect(gameWindow, WHITE, (50, 600, 300, 100), 1)
            pygame.draw.rect(gameWindow, WHITE, (450, 600, 300, 100), 1)
            gameWindow.blit(fightNarwhal, (155, 20))
            fight = font.render("Fight - Space", 1, WHITE)
            mercy = font.render("Mercy - Right Shift", 1, WHITE)
            gameWindow.blit(fight, (100, 625))
            gameWindow.blit(mercy, (451, 625))

        def drawPlayHP(playHP):
            Player = font.render("Player", 1, RED)
            playhealth = font.render("HP - ", 1, RED)
            playerHP = font.render(str(playHP), 1, RED)
            gameWindow.blit(Player, (10, 750))
            gameWindow.blit(playhealth, (130, 750))
            gameWindow.blit(playerHP, (210, 750))
            pygame.display.update()
        
##
##    if keys[pygame.K_RSHIFT]:
        

pygame.quit()
