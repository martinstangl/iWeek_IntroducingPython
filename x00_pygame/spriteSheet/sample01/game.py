import pygame
pygame.init()

win = pygame.display.set_mode((500, 480))
pygame.display.set_caption("Sprites")

walkRight = [pygame.image.load('./img/Game/R1.png'), pygame.image.load('./img/Game/R2.png'),
             pygame.image.load('./img/Game/R3.png'), pygame.image.load('./img/Game/R4.png'),
             pygame.image.load('./img/Game/R5.png'), pygame.image.load('./img/Game/R6.png'),
             pygame.image.load('./img/Game/R7.png'), pygame.image.load('./img/Game/R8.png'),
             pygame.image.load('./img/Game/R9.png')]
walkLeft = [pygame.image.load('./img/Game/L1.png'), pygame.image.load('./img/Game/L2.png'),
            pygame.image.load('./img/Game/L3.png'), pygame.image.load('./img/Game/L4.png'),
            pygame.image.load('./img/Game/L5.png'), pygame.image.load('./img/Game/L6.png'),
            pygame.image.load('./img/Game/L7.png'), pygame.image.load('./img/Game/L8.png'),
            pygame.image.load('./img/Game/L9.png')]
bg = pygame.image.load('./img/Game/bg.jpg')
char = pygame.image.load('./img/Game/standing.png')

x = 50
y = 400
width = 40
height = 60
vel = 5

clock = pygame.time.Clock()

isJump = False
jumpCount = 10

left = False
right = False
walkCount = 0


def redrawGameWindow():
    global walkCount

    win.blit(bg, (0, 0))
    if walkCount + 1 >= 27:
        walkCount = 0

    if left:
        win.blit(walkLeft[walkCount // 3], (x, y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount // 3], (x, y))
        walkCount += 1
    else:
        win.blit(char, (x, y))
        walkCount = 0

    pygame.display.update()


run = True

while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False

    elif keys[pygame.K_RIGHT] and x < 500 - vel - width:
        x += vel
        left = False
        right = True

    else:
        left = False
        right = False
        walkCount = 0

    if not (isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            left = False
            right = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else:
            jumpCount = 10
            isJump = False

    redrawGameWindow()

pygame.quit()