import pygame, sys
from random import randint
from pygame.sprite import Sprite

#Game parameters
screen_width = 800
screen_height = 800
black = (0,0,0)
white = (255, 255, 255)
red = (255,0,0)
score = 0
button_down = False


# Functions
def redrawGameWindow():
    screen.fill(black)
    for balloon in balloons:
        #Update then draw balloon
        balloon.update(time_passed)
        balloon.blitme()
    crosshair_x = mouse_x - (crosshair_w/2)
    crosshair_y = mouse_y - (crosshair_h/2)
    screen.blit(crosshair_image, (crosshair_x, crosshair_y))
    pygame.display.flip()

#Initializing game
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Minigame1")
clock = pygame.time.Clock()
gameWindow=pygame.display.set_mode((screen_width,screen_height))
font = pygame.font.SysFont("Comic Sans MS",30)

#Create Crosshair
crosshair_image = pygame.image.load("crosshair.png").convert_alpha()
crosshair_w, crosshair_h = crosshair_image.get_size()

#Create balloons class
class Balloon(Sprite):
 
    def __init__(self, screen):
 
        Sprite.__init__(self)
        self.screen = screen
        self.image = pygame.image.load("new-green-balloon-light-lft-th.png").convert_alpha()
        self.image_w, self.image_h = self.image.get_size()
        self.speed = randint(25,75) * 0.01
        
        self.x_position = randint(self.image_w/2, self.screen.get_width()-self.image_w/2)
        self.y_position = self.screen.get_height() + self.image_h/2
    
    def update(self, time_passed):
        self.y_position -= self.speed * time_passed
    
    def blitme(self):
        self.draw_pos = self.image.get_rect().move(self.x_position-self.image_w/2, self.y_position-self.image_h/2)
        self.screen.blit(self.image, self.draw_pos)
    
#List of balloons
balloons = [Balloon(screen)]
for x in range(0, randint(3, 5)):
    balloons.append(Balloon(screen))
    
#Game Loop
gameLoop=True
while gameLoop:
    #Time passed and FPS
    time_passed = clock.tick(150)
    
    #Mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()
    
    #Draw scoreboard
    balloonScore = font.render("Balloons Popped: " + str(score), 1, white)
    gameWindow.blit(balloonScore,(50,30))
    pygame.display.update()

    #Killing the loop if quit game
    for event in pygame.event.get():
        if (event.type==pygame.QUIT):
            gameLoop=False
            
    #Drawing and updating balloons
    redrawGameWindow()
##    screen.fill(black)
##    for balloon in balloons:
##        #Update then draw balloon
##        balloon.update(time_passed)
##        balloon.blitme()
        
        #If balloon shot
    if pygame.mouse.get_pressed()[0] == 1 and button_down == False:
        if balloon.draw_pos.collidepoint(pygame.mouse.get_pos()):
            balloons.remove(balloon)
            score += 1
            button_down = True

    elif pygame.mouse.get_pressed()[0] == 0 and button_down == True:
        button_down = False
        
        #If no more balloons, make more
    if len(balloons) == 0:
        for x in range(0, randint(3, 5)):
            balloons.append(Balloon(screen))
        
        #Draw multiple balloons after a balloon dies
    if balloon.y_position < -balloon.image_h/2:
        balloons.remove(balloon)
        if len(balloons) < 7:
            for x in range(0, randint(2, 4)):
                balloons.append(Balloon(screen))
            
    if pygame.time.get_ticks() >= 10000:
        print (score)
        pygame.quit()
        
    #Draw crosshair
##    crosshair_x = mouse_x - (crosshair_w/2)
##    crosshair_y = mouse_y - (crosshair_h/2)
##    screen.blit(crosshair_image, (crosshair_x, crosshair_y))
##    pygame.display.flip()
    
pygame.quit()
