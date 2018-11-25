import pygame, sys
import time as t
from random import randint
from pygame.sprite import Sprite
pygame.init()

#Setup
WIDTH = 800
HEIGHT = 800
BLACK = (0,0,0)
WHITE = (255, 255, 255)
score = 0
buttonDown = False
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minigame")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Comic Sans MS",30)

#Create Heart
heartImage = pygame.image.load("AttackHeart.png").convert_alpha()
heartW, heartH = heartImage.get_size()

#Classes
class Balloon(Sprite):

    def __init__(self, screen):
 
        Sprite.__init__(self)
        self.screen = screen
        self.image = pygame.image.load("new-green-balloon-light-lft-th.png").convert_alpha()
        self.imageW, self.imageH = self.image.get_size()
        self.speed = randint(25,50) * 0.01

        self.xPosition = self.screen.get_width() + self.imageW/2
        self.yPosition = randint(self.imageH/2, self.screen.get_height()-self.imageH/2-200)
    
    def update(self, timePassed):
        self.xPosition -= self.speed * timePassed
    
    def blitme(self):
        self.drawPos = self.image.get_rect().move(self.xPosition-self.imageW/2, self.yPosition-self.imageH/2)
        self.screen.blit(self.image, self.drawPos)
        
class Bullet(Sprite):

    def __init__(self, screen):
 
        Sprite.__init__(self)
        self.screen = screen
        self.image = pygame.image.load("HeartBullet.png").convert_alpha()
        self.imageW, self.imageH = self.image.get_size()
        self.speed = 0.3
        
        mouseX, mouseY = pygame.mouse.get_pos()
        self.xPosition = mouseX
        self.yPosition = 750
    
    def update(self, timePassed):
        self.yPosition -= self.speed * timePassed
    
    def blitme(self):
        self.drawPos = self.image.get_rect().move(self.xPosition-10, self.yPosition-10)
        self.screen.blit(pygame.transform.scale(self.image, (20, 20)), (self.drawPos)) 
    
#Lists
bullets = [Bullet(screen)]
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
    
    #Shoot bullet
    if pygame.mouse.get_pressed()[0] == 1 and buttonDown == False:
        bullets.append(Bullet(screen))
        buttonDown = True
    
    elif pygame.mouse.get_pressed()[0] == 0 and buttonDown == True:
        buttonDown = False
                    
    #Drawing and updating balloons
    screen.fill(BLACK)
    for balloon in balloons:      
        #Update then draw balloon
        balloon.update(timePassed)
        balloon.blitme() 
     
        for bullet in bullets:
            #Update then draw bullet
            bullet.update(timePassed)
            bullet.blitme()   
            
            if balloon.drawPos.collidepoint(bullet.xPosition-10, bullet.yPosition-10):
                balloons.remove(balloon)
                bullets.remove(bullet)
                score += 1
        
        #If no more balloons, make more
        if len(balloons) == 0:
            for x in range(0, randint(2, 4)):
                balloons.append(Balloon(screen))
        
        #Draw multiple balloons after a balloon dies
        if balloon.xPosition < -balloon.imageW/2:
            balloons.remove(balloon)
            if len(balloons) < 6:
                for x in range(0, randint(1, 3)):
                    balloons.append(Balloon(screen))
            
        if pygame.time.get_ticks() >= 10000:
            gameLoop = False
        
    #Draw heart
    screen.blit(pygame.transform.scale(heartImage, (40, 40)), (mouseX - 20, 720))
    
    scoreboard(score)
    pygame.display.flip()

#End Game
gameOverScreen()
t.sleep(5)
pygame.quit()
