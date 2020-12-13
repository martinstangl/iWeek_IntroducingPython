import pygame   # https://www.pygame.org/

pygame.init()

win = pygame.display.set_mode((500, 500))   # setup window
pygame.display.set_caption("My First Game")

x = 50          # x-coordiante
y = 50          # y-coordinate
width = 40      # screen-width
height = 60     # screen-height

run = True

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= 1

    if keys[pygame.K_RIGHT]:
        x += 1

    if keys[pygame.K_UP]:
        y -= 1

    if keys[pygame.K_DOWN]:
        y += 1

    win.fill((0, 0, 0))  # Fills the screen with black
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))   # https://www.pygame.org/docs/ref/draw.html
    pygame.display.update()

pygame.quit()
