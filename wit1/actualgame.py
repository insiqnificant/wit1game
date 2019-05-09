import pygame
import sys
import os
import random
pygame.init()
pygame.font.init()
obstacleRNG = random.randrange(5)
'''
shortcvuts
'''
dis = pygame.display
draw = pygame.draw
'''
display
'''
dis.set_caption("sumn")
_height = 500
_width = 500
half_height = int(_height)/2
half_width = int(_width)/2
display = (_height, _width)
win = pygame.display.set_mode(display)
minimize = False
maximize = False
rad = 500
'''
colors
'''
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
orange = (242, 130, 26)
yellow = (255, 217, 28)
purple = (163, 24, 249)
magenta = (255, 0, 255)
playColor = white
optionsColor = white
exitColor = white
circleColor = white
'''
timer
'''
fps = 50
clock = pygame.time.Clock()
clockTimer = 500
countdown = False
'''
text
'''
font = pygame.font.SysFont('Comic Sans MS', 70)
font2 = pygame.font.SysFont('Comic Sans MS', 50)
introText = font.render("THE GAME", True, (white))

play_selected = False
options_selected = False
exit_selected = False
'''
obstacle stuff
'''

'''
functions
'''


def discrete_selections():
    global playColor
    global optionsColor
    global exitColor
    global red
    global Intro
    global rad
    global circleColor
    global maximize
    if event.key == pygame.K_s and playColor == red:
        optionsColor = red
        playColor = white
    if event.key == pygame.K_RETURN and playColor == red:  # WORKS
        maximize = True
    if event.key == pygame.K_w and optionsColor == red:
        playColor = red
        optionsColor = white
    if event.key == pygame.K_s and optionsColor == red:
        exitColor = red
        optionsColor = white
    if event.key == pygame.K_w and exitColor == red:
        optionsColor = red
        exitColor = white
    if event.key == pygame.K_RETURN and exitColor == red:
        pygame.quit()


'''
  intro sequence
'''

Intro = True
caption1 = 0
while Intro:
    clock.tick(fps)
    if caption1 == 0:
        dis.set_caption("Press RETURN")
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.quit()
        if event.type == pygame.KEYDOWN:
            discrete_selections()
    win.fill(black)
    i_play = font2.render("PLAY", True, (playColor))
    i_options = font2.render("OPTIONS", True, (optionsColor))
    i_exit = font2.render("EXIT", True, (exitColor))
    draw.circle(win, circleColor, (int(half_width), int(half_height)), (rad))
    if keys[pygame.K_RETURN] and rad == 500:
        minimize = True
        caption1 = 1
    if minimize == True:
        rad -= 10
    if rad == 0:
        circleColor = black
        minimize = False
        win.blit(introText, (240 - introText.get_width() //
                             2, 170 - introText.get_height() // 2))
        countdown = True
        if caption1 == 1:
            dis.set_caption("THE GAME")
    if countdown == True:
        clockTimer -= 10
    if clockTimer <= -50:
        win.blit(i_play, (240 - i_play.get_width() //
                          2, 240 - i_play.get_height() // 2))
    if clockTimer <= -100:
        win.blit(i_options, (240 - i_options.get_width() //
                             2, 280 - i_options.get_height() // 2))
    if clockTimer <= -150:
        win.blit(i_exit, (240 - i_exit.get_width() //
                          2, 320 - i_exit.get_height() // 2))
    if clockTimer == -170:
        playColor = red
    if clockTimer == -171:
        countdown = False

    if maximize == True:
        playColor = white
        circleColor = white
        rad += 9
    if rad == 495:
        Intro = False
    #selections()
    dis.flip()

'''
actual game
'''
'''
reset variables
'''
clockTimer = 500
countdown = False

'''
player variables
'''
posX = half_width
posY = half_width
p_height = 20
p_width = 10
vel = 5
jumpHeight = .19
jumping = False
reversejumping = False
j_count = 10
playerColor = black
onGround = True
score = 0
'''
game stuff
'''

'''
object stuff
'''
o_posX1 = 720
o_posX2 = 750
o_posX3 = 810
o_posY1 = half_width - 20
o_posY2 = half_width - 20
o_posY3 = half_width - 20
o_width1 = 20
o_width2 = 20
o_width3 = 20
o_height1 = 40
o_height2 = 40
o_height3 = 40
scroll_vel = 2
scrolling = False
objectScrolling = False


'''
class
'''

'''
actual game
'''
Running = True
while Running:

    countdown = True
    if countdown:
        clockTimer -= 10
    clock.tick(fps)
    win.fill(white)
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.quit()
    draw.rect(win, playerColor, ((posX, posY), (p_width, p_height)))
    if clockTimer == 0:
        countdown = False
        scrolling = True
        objectScrolling = True
    draw.rect(win, red, ((o_posX1, o_posY1), (o_width1, o_height1)))
    draw.rect(win, red, ((o_posX2, o_posY2), (o_width2, o_height2)))
    draw.rect(win, red, ((o_posX3, o_posY3), (o_width3, o_height3)))
    if objectScrolling == True:
        o_posX1 -= scroll_vel * 2.5
        o_posX2 -= scroll_vel * 2.5
        o_posX3 -= scroll_vel * 2.5
    if o_posX1 <= 2:
        o_posX1 = 700
    if o_posX2 <= 2:
        o_posX2 = 730
    if o_posX3 <= 2:
        o_posX3 = 760

    if scrolling and onGround:
        posX -= scroll_vel
    if not (jumping):
        if keys[pygame.K_w]:
            jumping = True
            onGround = False
    else:
        if j_count >= -10:
            posY -= (j_count * abs(j_count)) * jumpHeight
            j_count -= 1
        else:
            onGround = True
            jumping = False
            j_count = 10
    if posX <= 2:
        playerColor = white
        Running = False
    if keys[pygame.K_a]:
        posX -= vel
    if keys[pygame.K_d]:
        posX += vel
    print(posX)
    dis.update()

gameOver = True
'''
losing stuff
'''
gameSet = font.render("GAME OVER", True, (white))
yourScore = font.render("Your score is:", True, (white))

while gameOver:
    clock.tick(fps)
    dis.set_caption("Press RETURN")
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.quit()
        if event.type == pygame.KEYDOWN:
            discrete_selections()
    if gameOver and keys[pygame.K_RETURN]:
        gaeOver = False
    win.fill(black)
    win.blit(gameSet, (240 - gameSet.get_width() //
                       2, 170 - gameSet.get_height() // 2))
    dis.update()
