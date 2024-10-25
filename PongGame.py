import pygame
import random
from math import sin, cos, radians

pygame.init()  #initiates pygame module

#define screen size
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

#score
PLAYER1_SCORE = 0
PLAYER2_SCORE = 0

#movement boolean (used to stop add a delay to ball)

DELAY_COUNTER = 0








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

        
    
        
#creation of squares
square1 = Square("white", 950, 300, 10, 75, pygame.K_UP, pygame.K_DOWN)
square2 = Square("white", 50, 300, 10, 75, pygame.K_w, pygame.K_s)
border_Top = Square("white", 500, 0, 1000, 10, None, None)
border_Bottom = Square("white", 500, 600, 1000, 10, None, None)
border_Right = Square("black", 1000, 300, 10, 600, None, None)
border_Left = Square("black", 0, 300, 10, 600, None, None)
ball = Ball("white", 500, 300, 25, 25)

#create sprite group for squares
squares = pygame.sprite.Group()
borders = pygame.sprite.Group()
balls = pygame.sprite.Group()

#create square and add to group
squares.add(square1)
squares.add(square2)
borders.add(border_Top)
borders.add(border_Bottom)
borders.add(border_Right)
borders.add(border_Left)
balls.add(ball)


#game loop
run = True
while run:
    
    clock.tick(FPS)
    
    #update background
    screen.fill("black")
    
    #update sprite group
    
    #squares.update()
    balls.update(500, 300)
    
    #collisions testing
    
    #get mouse coordinates and use them to position the rectangle
    pos = pygame.mouse.get_pos()
    square1.center = pos
    
    #draw sprite group
    squares.draw(screen)
    borders.draw(screen)
    balls.draw(screen)
   # squares.render(screen)
    
    
    #print(squares)
    #print(borders)
    

    
    
    
    #event handler
    for event in pygame.event.get():
        
        #This bit of code is not used in the pong game and was used for experimental stuff
        ''' 
        if event.type == pygame.MOUSEBUTTONDOWN:
            #get mouse coordinates
            pos = pygame.mouse.get_pos()
            #create square
            square = Square(random.choice(colors), pos[0], pos[1])
            squares.add(square)
            '''
        
            #checks for key press
        if event.type == pygame.KEYDOWN:
            squares.update(event.key)
        if event.type == pygame.KEYUP:
            squares.update(event.key)
                
            
        #quit program
        if event.type == pygame.QUIT:
            run = False
            
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