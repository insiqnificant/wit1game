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
    if keys[pygame.K_LEFT]:
       pygame.draw.ellipse(
           screen, (yellow), ((bposX, bposY), (bwidth, bheight)))
       bposX -= bulletVel
    if keys[pygame.K_RIGHT]:
        pygame.draw.ellipse(
            screen, (yellow), ((bposX, bposY), (bwidth, bheight)))
        bposX -= bulletVel


def playercontrols():
    global keys
    global posX
    global posY
    global boxvel

    if keys[pygame.K_a] and posX >= 16:
        posX -= boxvel
    if keys[pygame.K_d] and posX <= 484:
        posX += boxvel
    if keys[pygame.K_w] and posY >= 16:
        posY -= boxvel
    if keys[pygame.K_s] and posY <= 484:
        posY += boxvel
def event_get():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
