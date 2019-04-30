import pygame, sys
pygame.init()
fps = 50 
white = (255,255,255)
clock = pygame.time.Clock()
screenWidth = (500,500)
black = (0,0,0)
pX = 250
pY = 250
width = 50
height = 50
vel = 10
screen = pygame.display.set_mode(screenWidth)
def playerControls():
    global pY
    global pX
    global vel
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        pY-=vel
    if keys[pygame.K_d]:
        pY+=vel
    if keys[pygame.K_a]:
        pX-=vel
    if keys[pygame.K_d]:
        pX+=vel
while True:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            pygame.quit()
            sys.quit()

    screen.fill(black)
    pygame.draw.rect(screen, (white),((pX,pY), (width,height)))
    clock.tick(fps)
    playerControls()

    playerControls()
    pygame.display.update()
