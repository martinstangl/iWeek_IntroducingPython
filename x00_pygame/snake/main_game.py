import pygame   # https://www.pygame.org/

from x00_pygame.snake.player import Player

pygame.init()
width = 500
height = 500
win = pygame.display.set_mode((width, height))   # setup window
pygame.display.set_caption("Snake")

x = 50          # x-coordiante
y = 50          # y-coordinate


run = True

p2 = Player()
p1 = Player((0, 0, 255), [250, 250])
p3 = Player((0, 255, 0), [120, 250])

def check_events():
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        p1.direction = 2
    if keys[pygame.K_RIGHT]:
        p1.direction = 0
    if keys[pygame.K_UP]:
        p1.direction = 3
    if keys[pygame.K_DOWN]:
        p1.direction = 1

    if keys[pygame.K_a]:
        p2.direction = 2
    if keys[pygame.K_d]:
        p2.direction = 0
    if keys[pygame.K_w]:
        p2.direction = 3
    if keys[pygame.K_s]:
        p2.direction = 1

    if keys[pygame.K_f]:
        p3.direction = 2
    if keys[pygame.K_h]:
        p3.direction = 0
    if keys[pygame.K_t]:
        p3.direction = 3
    if keys[pygame.K_g]:
        p3.direction = 1

while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    check_events()
    win.fill((255, 255, 255))  # Fills the screen with black
    p1.draw(win)
    p2.draw(win)
    p3.draw(win)
    #pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))   # https://www.pygame.org/docs/ref/draw.html
    pygame.display.update()

pygame.quit()
