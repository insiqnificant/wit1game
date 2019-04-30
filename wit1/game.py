import pygame, sys, time
from pygame import *
pygame.init()
##COLORS##
blue = (0, 0, 255)
red = (255, 0, 0)
purple = (190, 10, 255)
green = (0, 255, 0)
yellow = (255, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)
screenColor = red
###########
##SCREEN##
screenWidth = (500,500)
screen = pygame.display.set_mode(screenWidth)
##########
##TIME##
clock = pygame.time.Clock()
fps = 60
########
##PLAYER##
posX = 300
posY = 300
boxvel = 5
radius = 15
moving = False
##########
##BULLET STUFF##
bposX = 300
bposY = 300
bheight = 2
bwidth = 4
bulletVel = 10
################
def rainbowscreen():
    global screenColor
    global red
    global blue
    global green
    global yellow
    global black
    global white
    if screenColor == red:
        screenColor = blue
    elif screenColor == blue:
        screenColor = green
    elif screenColor == green:
        screenColor = yellow
    elif screenColor == yellow:
        screenColor = red
def drawCharacters():
    global screen
    global screenColor
    global posX
    global posY
    global radius
    pygame.draw.circle(screen, (white), (posX, posY), (radius))
def drawBullet():
    global screen
    global yellow
    global bposX
    global bposY
    global bwidth
    global bheight
    if moving == True:
        bposX 
    if keys[pygame.K_LEFT]:
       pygame.draw.ellipse(screen, (yellow), ((bposX, bposY), (bwidth, bheight)))
       bposX -= bulletVel
    if keys[pygame.K_RIGHT]:
        pygame.draw.ellipse(screen, (yellow), ((bposX, bposY), (bwidth, bheight)))
        bposX -= bulletVel
def playercontrols():
    global keys
    global posX
    global posY
    global boxvel

    if keys[pygame.K_a] and posX >= 16:
        posX -= boxvel
        moving = True
    if keys[pygame.K_d] and posX <= 484:
        posX += boxvel
        moving = True
    if keys[pygame.K_w] and posY >= 16:
        posY -= boxvel
        moving = True
    if keys[pygame.K_s] and posY <= 484:
        posY += boxvel
        moving = True
while True:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            pygame.quit()
            sys.quit()
    keys = pygame.key.get_pressed()
    screen.fill(black)
    clock.tick(fps)
    rainbowscreen()
    drawCharacters()
    drawBullet()
    playercontrols()
    moving = False
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
    print("POS:",posX,",",posY,"FPS:",fps)
    pygame.display.update()
