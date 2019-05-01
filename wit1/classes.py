import pygame, sys

class screen:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.hwidth = int(self.width/2)
        self.hheight = int(self.height/2)

    def initScreen(self):
        self.myscreen = pygame.display.set_mode((self.width,self.height))

    def fill(self, color):
        self.myscreen.fill(color)

class playerObject:
    def __init__(self,posX,posY,height,width,color)
    
white = (255,255,255)
black = (0,0,0)
class gamePlay:
    def basics(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
pygame.init()
mygame = gamePlay()
screen = screen(500, 500)
screen.initScreen()

while True:

    mygame.basics()
    screen.fill(black)
    pygame.display.update()










if any(posY < y < (posY + p_height) for y in range:

if 10 < x 20 and any(posY < y < (posY + p_height + p_width) for y in range:

if any(posY < y < (posY + p_width) for y in range:
if any(posY < y < (posY + p_width + p_height) for y in range:
