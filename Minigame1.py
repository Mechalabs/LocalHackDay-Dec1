import pygame, sys
import time as t
from random import randint
from pygame.sprite import Sprite
pygame.init()
pygame.mixer.init()

#Setup
WIDTH = 800
HEIGHT = 800
BLACK = (0,0,0)
WHITE = (255, 255, 255)
score = 0
buttonDown = False
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minigame1")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Comic Sans MS",30)

pygame.mixer.music.load("Bonetrousle.MP3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(loops = -1)

#Create Crosshair
crosshairImage = pygame.image.load("crosshair.png").convert_alpha()
crosshairW, crosshairH = crosshairImage.get_size()
heartImage = pygame.image.load("AttackHeart.png").convert_alpha()

#Create balloons class
class Balloon(Sprite):
 
    def __init__(self, screen):
 
        Sprite.__init__(self)
        self.screen = screen
        self.image = pygame.image.load("new-green-balloon-light-lft-th.png").convert_alpha()
        self.imageW, self.imageH = self.image.get_size()
        self.speed = randint(25,75) * 0.01
        
        self.xPosition = randint(self.imageW/2, self.screen.get_width()-self.imageW/2)
        self.yPosition = self.screen.get_height() + self.imageH/2
    
    def update(self, timePassed):
        self.yPosition -= self.speed * timePassed
    
    def blitme(self):
        self.drawPos = self.image.get_rect().move(self.xPosition-self.imageW/2, self.yPosition-self.imageH/2)
        self.screen.blit(self.image, self.drawPos)
    
#List of balloons
balloons = [Balloon(screen)]
for x in range(0, randint(3, 5)):
    balloons.append(Balloon(screen))
    
#Functions
def scoreboard(poppedCount):
    poppedScore = font.render("Balloons Popped " + str(score), 1, WHITE)
    screen.blit(poppedScore,(50,30))
    pygame.display.update()
    
def gameOverScreen():
    screen.fill(BLACK)
    graphics = font.render("Your Total Score: " + str(score),1,WHITE)
    screen.blit(graphics,(270,250))
    pygame.display.update()
    
def main():
    #Game Loop
    gameLoop=True
    while gameLoop:
        #Time passed and FPS
        timePassed = clock.tick(150)
        
        #Mouse position
        mouseX, mouseY = pygame.mouse.get_pos()
        
        #Killing the loop if quit game
        for event in pygame.event.get():
            if (event.type==pygame.QUIT):
                gameLoop=False
                
        #Drawing and updating balloons
        screen.fill(BLACK)
        for balloon in balloons:
            #Update then draw balloon
            balloon.update(timePassed)
            balloon.blitme()
            
            #If balloon shot
            if pygame.mouse.get_pressed()[0] == 1 and buttonDown == False:
                if balloon.drawPos.collidepoint(pygame.mouse.get_pos()):
                    balloons.remove(balloon)
                    score += 1
                    buttonDown = True

            elif pygame.mouse.get_pressed()[0] == 0 and buttonDown == True:
                buttonDown = False
            
            #If no more balloons, make more
            if len(balloons) == 0:
                for x in range(0, randint(3, 5)):
                    balloons.append(Balloon(screen))
            
            #Draw multiple balloons after a balloon dies
            if balloon.yPosition < -balloon.imageH/2:
                balloons.remove(balloon)
                if len(balloons) < 7:
                    for x in range(0, randint(2, 4)):
                        balloons.append(Balloon(screen))
                
            if pygame.time.get_ticks() >= 10000:
                gameLoop = False
            
        #Draw crosshair
        screen.blit(crosshairImage, (mouseX - (crosshairW/2), mouseY - (crosshairH/2)))
        screen.blit(pygame.transform.scale(heartImage, (40, 40)), (mouseX - 20, mouseY - 20))
        
        scoreboard(score)
        pygame.display.flip()

main()
