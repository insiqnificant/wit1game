jumpCount = 10
isJump = False
jumpHeight = .5


   if not (isJump):
        if keys[pygame.K_UP]:
               isJump = True
    else:
        if jumpCount >= -10:
            playeroneY -= (jumpCount * abs(jumpCount)) * jumpHeight
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
