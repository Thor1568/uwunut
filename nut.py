import pygame
import math
from os import path

pygame.init()
pygame.font.init()

displayWidth = 800
displayHeight = 600


SCREEN_SIZE = (displayWidth, displayHeight)
gameWin = pygame.display.set_mode(SCREEN_SIZE)


gameDisplay = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()


black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 0, 255)
blue = (0, 255, 0)

##image hell
pinballImage = pygame.image.load('C:/Users/Celeste/Pictures/gamePhotos/pinball.png')







##Game Loop

def distBetween(pos1, pos2):
    "Takes in tuple pos1 = (x, y) and tuple pos2 = (x,y) and returns absolute val of float distance between them."
    xdiff = pos2[0] - pos1[0]
    ydiff = pos2[1] - pos1[1]
    dist = math.sqrt(math.pow(xdiff, 2) + math.pow(ydiff, 2))
    return math.abs(dist)
        
def vecToSlope(myvector):
    "Takes in a vector(x,y) and returns the slope and y intercept of it UwU"
    #Implement UwU
    x = myvector[0]; y = myvector[1];
    m = math.sqrt(math.pow(x, 2) + math.pow(y, 2))
    b = (-1 * m) * x + y
    return m, b














    
def pinball(x,y):
    gameDisplay.blit(pinballImage, (x,y))

def ask(screen, question):
    "ask(screen, question) -> answer"
    current_string = []
    display_box(screen, question + ": " + string.join(current_string,""))
    while 1:
      inkey = get_key()
      if inkey == K_BACKSPACE:
        current_string = current_string[0:-1]
      elif inkey == K_RETURN:
        break
      elif inkey == K_MINUS:
        current_string.append("_")
      elif inkey <= 127:
        current_string.append(chr(inkey))
      display_box(screen, question + ": " + string.join(current_string,""))
    return string.join(current_string,"")



#Reed stuff uwu
    for all bumpers
        if equation mx+b = +/- (sqrt(x-h)^2) - k
        record in array
        calc distance from last point
        lesser of values return

        take bumperIntersec coords
        take center of circle (hk) and cordInt and calcule the slope and solve for b
        when less than 2 way, tp to cord.
        reflect vector <uv> across normal line slope via reflect formula.

        
        
        
        when mx+b = +/- (sqrt(x-h)^2) - k, reflect off of normal line. 




##Math Variables
bigR = 0
litR = 0
bigX = 0
BigY = 0
oneLitX = 0
oneLitY = 0
twoLitX = 0
twoLitY = 0
threeLitX = 0
threeLitY = 0 
ballVel = 0
ballVec = ( 0, 0)
ballX = 320
ballY = 240
touchPt = 0
radVec = 0
bumpCount = 0
offSCreen = 0
intsecX = 0
intsecY = 0
lastPt = 0




##Prompt   
#startCenter = input('Start at origin?')
#defaultBumpers = input('Bumpers in an equilateral?')
    
      



crashed = False
while not crashed:

    for event in pygame.event.get():
        #Within tick events loop
        if event.type == pygame.QUIT:
            crashed = True


    #Outside of tick events loop
    if ballVec not == (0,0)    
        move pinball along vector.

    if ballVec
            
        



    gameDisplay.fill(white)
    pinball(ballX, ballY)
    pygame.display.update()
    clock.tick(60)




pygame.quit()
quit()
