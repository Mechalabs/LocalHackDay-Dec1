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

Narwhal = pygame.image.load("Evil Narwhal.png")

## SHOULD ADD GLITCHES ON PURPOSE

inPlay = True

# functions
def battlepage():
    gameWindow.fill(BLACK)
    pygame.draw.rect(gameWindow, WHITE, (50, 600, 300, 100), 1)
    pygame.draw.rect(gameWindow, WHITE, (450, 600, 300, 100), 1)
    gameWindow.blit(Narwhal, (155, 20))
    graphics1 = font.render("Fight", 1, WHITE)
    graphics2 = font.render("Mercy", 1, WHITE)
    gameWindow.blit(graphics1, (150, 620))
    gameWindow.blit(graphics2, (550, 620))
    pygame.display.update()


pygame.mixer.music.load("Gasters_Theme.mid")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(loops = -1)

while inPlay:
    battlepage()
    pygame.time.delay(50)

    pygame.event.clear()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        inPlay = False

pygame.quit()
