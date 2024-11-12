import pygame
import random
import sys
from math import sin, cos, radians
from time import sleep

pygame.init()  #initiates pygame module

#define screen size
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

#score
PLAYER1_SCORE = 0
PLAYER2_SCORE = 0

#movement boolean (used to stop add a delay to ball)

DELAY_COUNTER = 0


#to check whether in menu or not
paused = True
started = True



#key pressed


#create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


#frame rate
clock = pygame.time.Clock()
FPS = 60

#colors (not part of pong game and was used for experimental things)
colors = ["crimson", "chartreuse", "coral", "darkorange", "forestgreen", "lime", "navy"]


#creates class for squares(while inheriting the Sprite class)
class Square(pygame.sprite.Sprite):
    
    
    #constructor
    def __init__(self, col, x, y, width, height, upKey, downKey):
        pygame.sprite.Sprite.__init__(self) #sprite constructor
        self.image = pygame.Surface((width,height))
        self.image.fill(col)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.up_Key = upKey
        self.down_Key = downKey
        self.up_Pressed = False
        self.down_Pressed = False
        
        

        
    #overwrites the update method of the sprite class
    def update(self, pressKey):
        #self.rect.move_ip(0, 5)


        #checks if a key is pressed
        if pressKey == self.up_Key:
                self.up_Pressed = True if not self.up_Pressed else False
        if pressKey == self.down_Key:
                self.down_Pressed = True if not self.down_Pressed else False
            
            
        
        
        '''
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()
        '''



class Ball(pygame.sprite.Sprite):
    
    def __init__(self, col, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width,height))
        self.image.fill(col)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
        self.velocityY = 3
        self.velocityX = 3
        self.SCORED = False
    
    def update(self, x, y):

        
        #moves ball
        if not self.SCORED:
            self.rect.y += self.velocityY
            self.rect.x += self.velocityX
        
        #checks if collide with border and switches y direction
        if self.rect.colliderect(border_Top) or self.rect.colliderect(border_Bottom):
            self.velocityY = -self.velocityY
            
        #checks if collide with paddle and switches x direction
        if self.rect.x > square1.rect.right and self.rect.x < square1.rect.left and self.rect.y < square1.rect.top and self.rect.y > square1.rect.bottom:
            self.rect.x += 5
        if self.rect.colliderect(square1) or self.rect.colliderect(square2):
            self.velocityX = -self.velocityX
        

        

        
        #scoring
        '''
        if self.rect.right > SCREEN_WIDTH+2:
            #self.rect.center = (x, y)
            self.rect.x -= 10
            self.SCORED = True
            self.image.fill("black")
        elif self.rect.left < -2:
            self.rect.x += 10
            self.SCORED = True
            self.image.fill("black")
        '''

class Button(pygame.sprite.Sprite):
    
    def __init__(self, col, x, y, word, width, height, textCol):
        pygame.sprite.Sprite.__init__(self)
        self.textColor = textCol
        self.image = pygame.Surface((width, height))
        self.image.fill(col)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.font = pygame.font.Font(None, 50)
        self.text = self.font.render(word, 1, (self.textColor))
        
    def update(self, x, y):
        screen.blit(self.text, (x, y))
        
    def countdown(self):
        font = pygame.font.Font(None, 36)
        text = font.render("3", 1, (255,255,255))
        screen.blit(text, (500, 300))
        pygame.display.update()
        sleep(1)
        screen.fill("black")
        text = font.render("2", 1, (255,255,255))
        screen.blit(text, (500, 300))
        pygame.display.update()
        sleep(1)
        screen.fill("black")
        text = font.render("1", 1, (255,255,255))
        screen.blit(text, (500, 300))
        pygame.display.update()
        sleep(1)

        
        
    
        
#creation of squares
square1 = Square("white", 950, 300, 10, 75, pygame.K_UP, pygame.K_DOWN)
square2 = Square("white", 50, 300, 10, 75, pygame.K_w, pygame.K_s)
border_Top = Square("white", 500, 0, 1000, 10, None, None)
border_Bottom = Square("white", 500, 600, 1000, 10, None, None)
border_Right = Square("black", 1000, 300, 10, 600, None, None)
border_Left = Square("black", 0, 300, 10, 600, None, None)
ball = Ball("white", 500, 300, 25, 25)
start = Button("black", 500, 250,"Start Match", 200, 50, "white")
exit = Button("black", 500, 300, "Exit Match", 200, 50, "white")
resume = Button("black", 500, 250, "Resume", 200, 50, "white")
leave = Button("black", 500, 300, "Exit Game", 200, 50, "white")

#create sprite group for squares
squares = pygame.sprite.Group()
borders = pygame.sprite.Group()
balls = pygame.sprite.Group()
startMenu = pygame.sprite.Group()
pauseMenu = pygame.sprite.Group()


#create square and add to group
squares.add(square1)
squares.add(square2)
borders.add(border_Top)
borders.add(border_Bottom)
borders.add(border_Right)
borders.add(border_Left)
balls.add(ball)
startMenu.add(start)
startMenu.add(leave)
pauseMenu.add(exit)
pauseMenu.add(resume)


#game loop
run = True
while run:
    
    clock.tick(FPS)
    
    #update background
    screen.fill("black")
    
    #update sprite group
    
    #squares.update()
    if not paused and not started:
        balls.update(500, 300)  
    
    #collisions testing
    
    #get mouse coordinates and use them to position the rectangle
    pos = pygame.mouse.get_pos()
    square1.center = pos
    
    #draw sprite group
    if not paused and not started:
        squares.draw(screen)
        borders.draw(screen)
        balls.draw(screen)
        
        
   # squares.render(screen)
    
    
    #print(squares)
    #print(borders)
    

    
    
    
    #event handler
    for event in pygame.event.get():
        
        #This bit of code is not used in the pong game and was used for experimental stuff
         
        if event.type == pygame.MOUSEBUTTONDOWN:
            #get mouse coordinates
            pos = pygame.mouse.get_pos()
            if exit.rect.collidepoint(pos) and paused and not started:
                started = True
            if resume.rect.collidepoint(pos) and paused and not started:
                resume.countdown()
                paused = False
            if start.rect.collidepoint(pos) and started and paused:
                start.countdown()
                started = False
                paused = False
            if leave.rect.collidepoint(pos) and started and paused:
                pygame.quit()
                sys.exit(0)
            '''
            #create square
            square = Square(random.choice(colors), pos[0], pos[1])
            squares.add(square)
            '''
        if not paused and not started:  
            if event.type == pygame.KEYDOWN:
                squares.update(event.key)
                if event.key == pygame.K_ESCAPE:
                    paused = True
            if event.type == pygame.KEYUP:
                squares.update(event.key)
            
        #will be used to navigate through menu
        #if event.type == pygame.MOUSEBUTTONDOWN: 
            
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    font = pygame.font.Font(None, 36)
                    text = font.render("3", 1, (255,255,255))
                    screen.blit(text, (500, 300))
                    pygame.display.update()
                    sleep(1)
                    screen.fill("black")
                    text = font.render("2", 1, (255,255,255))
                    screen.blit(text, (500, 300))
                    pygame.display.update()
                    sleep(1)
                    screen.fill("black")
                    text = font.render("1", 1, (255,255,255))
                    screen.blit(text, (500, 300))
                    pygame.display.update()
                    sleep(1)
                    paused = False
                if event.key == pygame.K_r:
                    PLAYER1_SCORE = 0
                    PLAYER2_SCORE = 0
                    ball.update(500,300)
                    font = pygame.font.Font(None, 36)
                    text = font.render("3", 1, (255,255,255))
                    screen.blit(text, (500, 300))
                    pygame.display.update()
                    sleep(1)
                    screen.fill("black")
                    text = font.render("2", 1, (255,255,255))
                    screen.blit(text, (500, 300))
                    pygame.display.update()
                    sleep(1)
                    screen.fill("black")
                    text = font.render("1", 1, (255,255,255))
                    screen.blit(text, (500, 300))
                    pygame.display.update()
                    sleep(1)
                    paused = False
            
                
            
        #quit program
        if event.type == pygame.QUIT:
            run = False
            
    
    #Pause Menu print
    if paused and not started:
        font = pygame.font.Font(None, 100)
        text = font.render("PAUSED", 1, (255,255,255))
        screen.blit(text, (375, 150))
        pauseMenu.draw(screen)
        exit.update(410, 280)
        resume.update(410,230)
        pos = pygame.mouse.get_pos()
        if exit.rect.collidepoint(pos):
            font = pygame.font.Font(None, 50)
            exit.text = font.render("Exit Match", 1, ("grey"))
        else:
            font = pygame.font.Font(None, 50)
            exit.text = font.render("Exit Match", 1, ("white"))
        if resume.rect.collidepoint(pos):
            font = pygame.font.Font(None, 50)
            resume.text = font.render("Resume", 1, ("grey"))
        else:
            font = pygame.font.Font(None, 50)
            resume.text = font.render("Resume", 1, ("white"))
        '''
        font = pygame.font.Font(None, 36)
        text = font.render("Exit Game", 1, (255,255,255))
        screen.blit(text, (445, 300))
        '''
        
    
    #Start Menu Print
    if paused and started:
        font = pygame.font.Font(None, 150)
        text = font.render("PONG", 1, (255,255,255))
        screen.blit(text, (350, 100))
        startMenu.draw(screen)
        start.update(410, 230)
        leave.update(410, 280)
        pos = pygame.mouse.get_pos()
        if start.rect.collidepoint(pos):
            font = pygame.font.Font(None, 50)
            start.text = font.render("Start Match", 1, ("grey"))
        else:
            font = pygame.font.Font(None, 50)
            start.text = font.render("Start Match", 1, ("white"))
        if leave.rect.collidepoint(pos):
            font = pygame.font.Font(None, 50)
            leave.text = font.render("Exit Game", 1, ("grey"))
        else:
            font = pygame.font.Font(None, 50)
            leave.text = font.render("Exit Game", 1, ("white"))
        '''
        font = pygame.font.Font(None, 50)
        text = font.render("Start Game", 1, (255,255,255))
        screen.blit(text, (415, 100))  
        '''
        
            
            
    #paddle movement (squares group)
    if square1.up_Pressed:
        square1.rect.y -= 6
    if square2.up_Pressed:
        square2.rect.y -= 6
    if square1.down_Pressed:
        square1.rect.y += 6
    if square2.down_Pressed:
        square2.rect.y += 6
    
        #preventing paddle from moving past border
    if square1.rect.colliderect(border_Bottom):
        square1.rect.y -= 6
    if square1.rect.colliderect(border_Top):
        square1.rect.y += 6
    if square2.rect.colliderect(border_Bottom):
        square2.rect.y -= 6
    if square2.rect.colliderect(border_Top):
        square2.rect.y += 6
    
    #old and not working way of scoring
    '''
    if ball.rect.right > SCREEN_WIDTH:
        PLAYER1_SCORE += 1
    if ball.rect.left < 0:
        PLAYER2_SCORE += 1
    '''  
    
    #if ball touches either right or left side it'll add score to respective player (player 1 paddle is on the left side and player 2 is on the right side)
    if ball.rect.colliderect(border_Right):
        PLAYER1_SCORE += 1
    if ball.rect.colliderect(border_Left):
        PLAYER2_SCORE += 1
    
    #display scores
    if not paused and not started:
        font = pygame.font.Font(None, 36)
        text = font.render(str(PLAYER1_SCORE), 1, (255,255,255))
        screen.blit(text, (450, 10))
        text = font.render(str(PLAYER2_SCORE), 1, (255,255,255))
        screen.blit(text, (550, 10))
    
    #hides ball if it hits either right or left side of screen
    if ball.rect.colliderect(border_Right):
        #self.rect.center = (x, y)
        ball.rect.x -= 10
        ball.SCORED = True
        ball.image.fill("black")
    elif ball.rect.colliderect(border_Left):
        ball.rect.x += 10
        ball.SCORED = True
        ball.image.fill("black")
    
    #starts a counter if the ball is scored and respawns the ball in a random direction after a certain amount of time
    if ball.SCORED == True and not DELAY_COUNTER == 50:
        DELAY_COUNTER += 1
    elif DELAY_COUNTER == 50: #controls how long it take for the ball to respawn
        DELAY_COUNTER = 0
        #respawns the ball and moves it in a random direction
        side = random.randint(0,1)
        side2 = random.randint(0,1)
        if side == 0:
            side = -1
        if side2 == 0:
            side2 = -1
        angle = random.randint(-45, 45)
        ball.rect.x = 500
        ball.rect.y = 300
        ball.image.fill("white")
        ball.velocityX = 3*(2**0.5)*cos(radians(angle)) * side
        ball.velocityY = 3*(2**0.5)*sin(radians(angle)) * side2
        ball.SCORED = False

        
        #ball.velocityX += random.randint()
    
    


    
            
    #update display
    pygame.display.flip()
    
pygame.quit()

