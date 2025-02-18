import pygame
import random
import sys
import os
from math import sin, cos, radians
from time import sleep

pygame.init()  #initiates pygame module

'''
def resizeScreen(paddle1, paddle2, borderTop, borderBottom, borderRight, borderLeft, ball1, start1, exit1, resume1, leave1, restart1):
    
    NEW_SCREEN_WIDTH = pygame.display.get_surface().get_width()
    NEW_SCREEN_HEIGHT = pygame.display.get_surface().get_height()
    CURRENT_SCREEN_HEIGHT = NEW_SCREEN_HEIGHT
    CURRENT_SCREEN_WIDTH = NEW_SCREEN_WIDTH
    SCREEN_SIZER = 200
    paddle1.set_Location(NEW_SCREEN_WIDTH-SCREEN_SIZER, NEW_SCREEN_HEIGHT/2)
    paddle1.set_Size(10 + NEW_SCREEN_WIDTH, 75 + NEW_SCREEN_HEIGHT)
    paddle2.set_Location(0+SCREEN_SIZER, NEW_SCREEN_HEIGHT/2)
    paddle2.set_Size(10 + NEW_SCREEN_WIDTH, 75 + NEW_SCREEN_HEIGHT)
'''
def get_path(file_path: str) -> str:
    """
    Returns the absolute path of a desired file

    Args:
        file_path (str): Relative path to the desired file

    Returns:
        str: Absolute path to the desired file
    """
    return os.path.join(os.path.dirname(__file__), file_path)


#define screen size
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 729
CURRENT_SCREEN_HEIGHT = SCREEN_HEIGHT
CURRENT_SCREEN_WIDTH = SCREEN_WIDTH
SCREEN_SIZER = 50
NEW_SCREEN_HEIGHT = 0
NEW_SCREEN_WIDTH = 0



#score
PLAYER1_SCORE = 0
PLAYER2_SCORE = 0

#movement boolean (used to stop add a delay to ball)

DELAY_COUNTER = 0


#to check whether in menu or not
paused = False
started = True
win = False
resized = False

#font sizes
START_FONT_SIZE = 150
BUTTON_FONT_SIZE = 50
COUNTDOWN_FONT_SIZE = 36
WIN_FONT_SIZE = 125
PAUSE_FONT_SIZE = 100
#key pressed


#create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)



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
    def set_Location(self):
        self.rect.x = self.rect.x * (CURRENT_SCREEN_WIDTH/SCREEN_WIDTH)
        self.rect.y = self.rect.y * (CURRENT_SCREEN_HEIGHT/SCREEN_HEIGHT)
    def set_Size(self, width, height):
        self.image = pygame.Surface((width, height))
    
    def resize(self):
        self.image = pygame.transform.scale_by(self.image, ((CURRENT_SCREEN_WIDTH/SCREEN_WIDTH),(CURRENT_SCREEN_HEIGHT/SCREEN_HEIGHT)))
        self.rect = self.image.get_rect()
        
        



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
        print(self.rect.x)
        
        if paused:
            self.rect.y = y
            self.rect.x = x
        
        
        
        #checks if collide with border and switches y direction
        if self.rect.colliderect(border_Top):
            self.rect.y = 9
            self.velocityY = -self.velocityY
        elif self.rect.colliderect(border_Bottom):
            self.rect.y = 670
            self.velocityY = -self.velocityY
            
        #checks if collide with paddle and switches x direction
        '''
        if self.rect.x > square1.rect.right and self.rect.x < square1.rect.left and self.rect.y < square1.rect.top and self.rect.y > square1.rect.bottom:
            self.rect.x += 5
        '''
        if self.rect.colliderect(square1):
            self.rect.x = 1170
            self.velocityX = -self.velocityX
            if self.velocityX <= 11.5 and self.velocityX >= -11.5:
                self.velocityX = self.velocityX * 1.15   
            if self.velocityY < 1.5 and self.velocityY > -1.5:
                side2 = random.randint(0,1)
                if side2 == 0:
                    side2 = -1
                angle = random.randint(-45, 45)
                self.velocityY = 3*(2**0.5)*sin(radians(angle)) * side2
        elif self.rect.colliderect(square2):
            self.rect.x = 60
            self.velocityX = -self.velocityX
            if self.velocityX <= 11.5 and self.velocityX >= -11.5:
                self.velocityX = self.velocityX * 1.15   
            if self.velocityY < 1.5 and self.velocityY > -1.5:
                side2 = random.randint(0,1)
                if side2 == 0:
                    side2 = -1
                angle = random.randint(-45, 45)
                self.velocityY = 3*(2**0.5)*sin(radians(angle)) * side2
                
        #moves ball
        if not self.SCORED:
            self.rect.y += self.velocityY
            self.rect.x += self.velocityX
                
        
    def randomMovement(self):
        side = random.randint(0,1)
        side2 = random.randint(0,1)
        if side == 0:
            side = -1
        if side2 == 0:
            side2 = -1
        angle = random.randint(-45, 45)
        self.rect.x = 640
        self.rect.y = SCREEN_HEIGHT/2
        self.image.fill("white")
        self.velocityX = 3*(2**0.5)*cos(radians(angle)) * side
        self.velocityY = 3*(2**0.5)*sin(radians(angle)) * side2
        if self.velocityY < 1.5 and self.velocityY > -1.5:
                side2 = random.randint(0,1)
                if side2 == 0:
                    side2 = -1
                angle = random.randint(-45, 45)
                self.velocityY = 3*(2**0.5)*sin(radians(angle)) * side2
        
    

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
        self.font = pygame.font.Font(None, BUTTON_FONT_SIZE)
        self.text = self.font.render(word, 1, (self.textColor))
        
    def update(self, x, y):
        screen.blit(self.text, (x, y))
        
    #A countdown for when starting or resuming a match
    def countdown(self):
        font = pygame.font.Font(None, COUNTDOWN_FONT_SIZE)
        text = font.render("3", 1, (255,255,255))
        screen.blit(text, (CURRENT_SCREEN_WIDTH/2, CURRENT_SCREEN_HEIGHT/2))
        pygame.display.update()
        sleep(1)
        screen.fill("black")
        text = font.render("2", 1, (255,255,255))
        screen.blit(text, (CURRENT_SCREEN_WIDTH/2, CURRENT_SCREEN_HEIGHT/2))
        pygame.display.update()
        sleep(1)
        screen.fill("black")
        text = font.render("1", 1, (255,255,255))
        screen.blit(text, (CURRENT_SCREEN_WIDTH/2, CURRENT_SCREEN_HEIGHT/2))
        pygame.display.update()
        sleep(1)

    
        
        
    
        
#creation of squares
square1 = Square("white", CURRENT_SCREEN_WIDTH-SCREEN_SIZER, CURRENT_SCREEN_HEIGHT/2, 10, 125, pygame.K_UP, pygame.K_DOWN)
square2 = Square("white", 0+SCREEN_SIZER, CURRENT_SCREEN_HEIGHT/2, 10, 125, pygame.K_w, pygame.K_s)
border_Top = Square("white", CURRENT_SCREEN_WIDTH/2, 0, SCREEN_WIDTH, 10, None, None)
border_Bottom = Square("white", CURRENT_SCREEN_WIDTH/2, CURRENT_SCREEN_HEIGHT, SCREEN_WIDTH, 10, None, None)
border_Right = Square("black", CURRENT_SCREEN_WIDTH, CURRENT_SCREEN_HEIGHT/2, 90, SCREEN_HEIGHT, None, None)
border_Left = Square("black", 0, CURRENT_SCREEN_HEIGHT/2, 90, SCREEN_HEIGHT, None, None)
ball = Ball("white", SCREEN_WIDTH/2, SCREEN_HEIGHT/2, 50, 50)
start = Button("black", SCREEN_WIDTH/2, 320,"Start Match", 200, 50, "white")
exit = Button("black", SCREEN_WIDTH/2, 420, "Exit Match", 200, 50, "white")
resume = Button("black", SCREEN_WIDTH/2, 320, "Resume", 200, 50, "white")
leave = Button("black", SCREEN_WIDTH/2, 370, "Exit Game", 200, 50, "white")
restart = Button("black", SCREEN_WIDTH/2, 370, "Restart Match", 200, 50, "white")

#create sprite group for squares
squares = pygame.sprite.Group()
borders = pygame.sprite.Group()
balls = pygame.sprite.Group()
startMenu = pygame.sprite.Group()
pauseMenu = pygame.sprite.Group()
winMenu = pygame.sprite.Group()


#create square and add to group
squares.add(square1)
squares.add(square2)
borders.add(border_Right)
borders.add(border_Left)
borders.add(border_Top)
borders.add(border_Bottom)
balls.add(ball)
startMenu.add(start)
startMenu.add(leave)
pauseMenu.add(exit)
pauseMenu.add(resume)


#game loop
run = True
while run:

    
    
    #update background
    screen.fill("black")
    
    #update sprite group
    
    #squares.update()
    if not paused and not started and not win:
        balls.update(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)  
    
    #collisions testing
    
    #get mouse coordinates and use them to position the rectangle
    pos = pygame.mouse.get_pos()
    square1.center = pos
    
    
    #draw sprite group
    if not paused and not started and not win:
        borders.draw(screen)
        squares.draw(screen)
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
            if exit.rect.collidepoint(pos) and (paused or win) and not started:
                PLAYER1_SCORE = 0
                PLAYER2_SCORE = 0
                started = True
                paused = False
                win = False
            elif resume.rect.collidepoint(pos) and paused and not started and not win:
                resume.countdown()
                paused = False
            elif start.rect.collidepoint(pos) and started and not paused and not win:
                start.countdown()
                #1170 for paddle bounce and 1150 for slow marker
                ball.rect.x = SCREEN_WIDTH / 2
                ball.rect.y = SCREEN_HEIGHT / 2
                #ball.velocityX = 0
                #ball.velocityY = 0
                started = False
                paused = False
            elif restart.rect.collidepoint(pos) and (paused or win) and not started:
                restart.countdown()
                PLAYER1_SCORE = 0
                PLAYER2_SCORE = 0
                ball.rect.x = SCREEN_WIDTH / 2
                ball.rect.y = SCREEN_WIDTH / 2
                paused = False
                win = False 
            elif leave.rect.collidepoint(pos) and started and not paused and not win:
                pygame.quit()
                sys.exit(0)
            '''
            #create square
            square = Square(random.choice(colors), pos[0], pos[1])
            squares.add(square)
            '''
        if not paused and not started and not win:  
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
                    font = pygame.font.Font(None, COUNTDOWN_FONT_SIZE)
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
                    ball.update(640,SCREEN_HEIGHT/2)
                    font = pygame.font.Font(None, COUNTDOWN_FONT_SIZE)
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
        '''
        if event.type == pygame.VIDEORESIZE: 
            NEW_SCREEN_WIDTH = pygame.display.get_surface().get_width()
            NEW_SCREEN_HEIGHT = pygame.display.get_surface().get_height()
            CURRENT_SCREEN_HEIGHT = NEW_SCREEN_HEIGHT
            CURRENT_SCREEN_WIDTH = NEW_SCREEN_WIDTH
            print(NEW_SCREEN_WIDTH)
            print(NEW_SCREEN_HEIGHT)
            resized = True
            #print(pygame.display.get_surface)
            #resizeScreen(square1, square2, border_Top, border_Bottom, border_Right, border_Left, ball, start, exit, resume, leave, restart)
            ball.resize()
            square1.resize()
            square1.rect.x = CURRENT_SCREEN_WIDTH - 100
            square1.rect.y = CURRENT_SCREEN_HEIGHT/2
            square2.resize()
            square2.rect.x = 100
            square2.rect.y = CURRENT_SCREEN_HEIGHT/2
            border_Right.image = pygame.Surface((180,CURRENT_SCREEN_HEIGHT))
            border_Right.rect = border_Right.image.get_rect()  
            

            
            border_Top.resize()
            border_Bottom.resize()
            border_Left.resize()
            border_Right.resize()
            '''
            

            
            
    #Pause Menu print
    if paused and not started and not win and not resized:
        font = pygame.font.Font(None, PAUSE_FONT_SIZE)
        text = font.render("PAUSED", 1, (255,255,255))
        screen.blit(text, (500, 225))
        pauseMenu.draw(screen)
        exit.update(541, 415)
        restart.update(541,365)
        resume.update(541,315)
        pos = pygame.mouse.get_pos()
        if exit.rect.collidepoint(pos):
            font = pygame.font.Font(None, BUTTON_FONT_SIZE)
            exit.text = font.render("Exit Match", 1, ("grey"))
        else:
            font = pygame.font.Font(None, BUTTON_FONT_SIZE)
            exit.text = font.render("Exit Match", 1, ("white"))
        if resume.rect.collidepoint(pos):
            font = pygame.font.Font(None, BUTTON_FONT_SIZE)
            resume.text = font.render("Resume", 1, ("grey"))
        else:
            font = pygame.font.Font(None, BUTTON_FONT_SIZE)
            resume.text = font.render("Resume", 1, ("white"))
        if restart.rect.collidepoint(pos):
            font = pygame.font.Font(None, BUTTON_FONT_SIZE)
            restart.text = font.render("Restart Match", 1, ("grey"))
        else:
            font = pygame.font.Font(None, BUTTON_FONT_SIZE)
            restart.text = font.render("Restart Match", 1, ("white"))
        '''
        font = pygame.font.Font(None, 36)
        text = font.render("Exit Game", 1, (255,255,255))
        screen.blit(text, (445, 300))
        '''
    #resized paused menu
    if paused and not started and not win and resized:
        font = pygame.font.Font(None, round(PAUSE_FONT_SIZE * ((((NEW_SCREEN_HEIGHT**2)+(NEW_SCREEN_WIDTH**2))**0.5)/(((SCREEN_HEIGHT**2)+(SCREEN_WIDTH**2))**0.5))))
        text = font.render("PAUSED", 1, (255,255,255))
        screen.blit(text, (375, 150))
        pauseMenu.draw(screen)
        exit.update(410, 330)
        restart.update(410,280)
        resume.update(410,230)
        pos = pygame.mouse.get_pos()
        if exit.rect.collidepoint(pos):
            font = pygame.font.Font(None, round(BUTTON_FONT_SIZE * ((((NEW_SCREEN_HEIGHT**2)+(NEW_SCREEN_WIDTH**2))**0.5)/(((SCREEN_HEIGHT**2)+(SCREEN_WIDTH**2))**0.5))))
            exit.text = font.render("Exit Match", 1, ("grey"))
        else:
            font = pygame.font.Font(None, round(BUTTON_FONT_SIZE * ((((NEW_SCREEN_HEIGHT**2)+(NEW_SCREEN_WIDTH**2))**0.5)/(((SCREEN_HEIGHT**2)+(SCREEN_WIDTH**2))**0.5))))
            exit.text = font.render("Exit Match", 1, ("white"))
        if resume.rect.collidepoint(pos):
            font = pygame.font.Font(None, round(BUTTON_FONT_SIZE * ((((NEW_SCREEN_HEIGHT**2)+(NEW_SCREEN_WIDTH**2))**0.5)/(((SCREEN_HEIGHT**2)+(SCREEN_WIDTH**2))**0.5))))
            resume.text = font.render("Resume", 1, ("grey"))
        else:
            font = pygame.font.Font(None, round(BUTTON_FONT_SIZE * ((((NEW_SCREEN_HEIGHT**2)+(NEW_SCREEN_WIDTH**2))**0.5)/(((SCREEN_HEIGHT**2)+(SCREEN_WIDTH**2))**0.5))))
            resume.text = font.render("Resume", 1, ("white"))
        if restart.rect.collidepoint(pos):
            font = pygame.font.Font(None, round(BUTTON_FONT_SIZE * ((((NEW_SCREEN_HEIGHT**2)+(NEW_SCREEN_WIDTH**2))**0.5)/(((SCREEN_HEIGHT**2)+(SCREEN_WIDTH**2))**0.5))))
            restart.text = font.render("Restart Match", 1, ("grey"))
        else:
            font = pygame.font.Font(None, round(BUTTON_FONT_SIZE * ((((NEW_SCREEN_HEIGHT**2)+(NEW_SCREEN_WIDTH**2))**0.5)/(((SCREEN_HEIGHT**2)+(SCREEN_WIDTH**2))**0.5))))
            restart.text = font.render("Restart Match", 1, ("white"))
            
    #Start Menu Print
    if not paused and started and not win and not resized:
        font = pygame.font.Font(None, START_FONT_SIZE)
        text = font.render("PONG", 1, (255,255,255))
        screen.blit(text, (500, 200))
        startMenu.draw(screen)
        start.update(541, 315)
        leave.update(541, 365)
        pos = pygame.mouse.get_pos()
        if start.rect.collidepoint(pos):
            font = pygame.font.Font(None, BUTTON_FONT_SIZE)
            start.text = font.render("Start Match", 1, ("grey"))
        else:
            font = pygame.font.Font(None, BUTTON_FONT_SIZE)
            start.text = font.render("Start Match", 1, ("white"))
        if leave.rect.collidepoint(pos):
            font = pygame.font.Font(None, BUTTON_FONT_SIZE)
            leave.text = font.render("Exit Game", 1, ("grey"))
        else:
            font = pygame.font.Font(None, BUTTON_FONT_SIZE)
            leave.text = font.render("Exit Game", 1, ("white"))
        '''
        font = pygame.font.Font(None, 50)
        text = font.render("Start Game", 1, (255,255,255))
        screen.blit(text, (415, 100))  
        '''
    #Resized start menu
    if not paused and started and not win and resized:
        font = pygame.font.Font(None, round(START_FONT_SIZE * ((((NEW_SCREEN_HEIGHT**2)+(NEW_SCREEN_WIDTH**2))**0.5)/(((SCREEN_HEIGHT**2)+(SCREEN_WIDTH**2))**0.5))))
        text = font.render("PONG", 1, (255,255,255))
        screen.blit(text, (350, 100))
        startMenu.draw(screen)
        start.update(400, 230)
        leave.update(400, 280)
        pos = pygame.mouse.get_pos()
        if start.rect.collidepoint(pos):
            font = pygame.font.Font(None, round(BUTTON_FONT_SIZE * ((((NEW_SCREEN_HEIGHT**2)+(NEW_SCREEN_WIDTH**2))**0.5)/(((SCREEN_HEIGHT**2)+(SCREEN_WIDTH**2))**0.5))))
            start.text = font.render("Start Match", 1, ("grey"))
        else:
            font = pygame.font.Font(None, round(BUTTON_FONT_SIZE * ((((NEW_SCREEN_HEIGHT**2)+(NEW_SCREEN_WIDTH**2))**0.5)/(((SCREEN_HEIGHT**2)+(SCREEN_WIDTH**2))**0.5))))
            start.text = font.render("Start Match", 1, ("white"))
        if leave.rect.collidepoint(pos):
            font = pygame.font.Font(None, round(BUTTON_FONT_SIZE * ((((NEW_SCREEN_HEIGHT**2)+(NEW_SCREEN_WIDTH**2))**0.5)/(((SCREEN_HEIGHT**2)+(SCREEN_WIDTH**2))**0.5))))
            leave.text = font.render("Exit Game", 1, ("grey"))
        else:
            font = pygame.font.Font(None, round(BUTTON_FONT_SIZE * ((((NEW_SCREEN_HEIGHT**2)+(NEW_SCREEN_WIDTH**2))**0.5)/(((SCREEN_HEIGHT**2)+(SCREEN_WIDTH**2))**0.5))))
            leave.text = font.render("Exit Game", 1, ("white"))
        
    #Win menu print
    if not paused and not started and win and not resized:
        font = pygame.font.Font(None, WIN_FONT_SIZE)
        if PLAYER1_SCORE == 5:
            text = font.render("Player 1 Wins!!", 1, ("white"))
        elif PLAYER2_SCORE == 5:
            text = font.render("Player 2 Wins!!", 1, ("white"))
        screen.blit(text, (350,250))
        restart.update(525, 365)
        exit.update(525, 415)
        if restart.rect.collidepoint(pos):
            font = pygame.font.Font(None, BUTTON_FONT_SIZE)
            restart.text = font.render("Restart Match", 1, ("grey"))
        else:
            font = pygame.font.Font(None, BUTTON_FONT_SIZE)
            restart.text = font.render("Restart Match", 1, ("white"))
        if exit.rect.collidepoint(pos):
            font = pygame.font.Font(None, BUTTON_FONT_SIZE)
            exit.text = font.render("Exit Match", 1, ("grey"))
        else:
            font = pygame.font.Font(None, BUTTON_FONT_SIZE)
            exit.text = font.render("Exit Match", 1, ("white"))
    
    #Resized win menu
    if not paused and not started and win and resized:
        font = pygame.font.Font(None, WIN_FONT_SIZE)
        if PLAYER1_SCORE == 5:
            text = font.render("Player 1 Wins!!", 1, ("white"))
        elif PLAYER2_SCORE == 5:
            text = font.render("Player 2 Wins!!", 1, ("white"))
        screen.blit(text, (200,150))
        restart.update(400, 280)
        exit.update(400, 330)
        if restart.rect.collidepoint(pos):
            font = pygame.font.Font(None, BUTTON_FONT_SIZE)
            restart.text = font.render("Restart Match", 1, ("grey"))
        else:
            font = pygame.font.Font(None, BUTTON_FONT_SIZE)
            restart.text = font.render("Restart Match", 1, ("white"))
        if exit.rect.collidepoint(pos):
            font = pygame.font.Font(None, BUTTON_FONT_SIZE)
            exit.text = font.render("Exit Match", 1, ("grey"))
        else:
            font = pygame.font.Font(None, BUTTON_FONT_SIZE)
            exit.text = font.render("Exit Match", 1, ("white"))
            
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
        font = pygame.font.Font(None, COUNTDOWN_FONT_SIZE)
        text = font.render(str(PLAYER1_SCORE), 1, (255,255,255))
        screen.blit(text, (590, 10))
        text = font.render(str(PLAYER2_SCORE), 1, (255,255,255))
        screen.blit(text, (690, 10))
    
    #hides ball if it hits either right or left side of screen
    if ball.rect.colliderect(border_Right):
        #self.rect.center = (x, y)
        ball.SCORED = True
        ball.rect.x = SCREEN_WIDTH/2
        ball.rect.y = SCREEN_HEIGHT/2
        ball.image.fill("black")
    elif ball.rect.colliderect(border_Left):
        ball.SCORED = True
        ball.rect.x = SCREEN_WIDTH/2
        ball.rect.y = SCREEN_HEIGHT/2
        ball.image.fill("black")
    
    #starts a counter if the ball is scored and respawns the ball in a random direction after a certain amount of time
    if ball.SCORED == True and not DELAY_COUNTER == 50:
        DELAY_COUNTER += 1
    elif DELAY_COUNTER == 50: #controls how long it take for the ball to respawn
        DELAY_COUNTER = 0
        #respawns the ball and moves it in a random direction
        ball.randomMovement()
        ball.SCORED = False
        '''
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
        '''

        
        #ball.velocityX += random.randint()
    
    #win condition
    if PLAYER1_SCORE == 5 or PLAYER2_SCORE == 5:
        win = True


    
    clock.tick(FPS)        
    #update display
    pygame.display.flip()
    
pygame.quit()
    