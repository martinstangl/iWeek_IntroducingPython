import random
import pygame   # https://www.pygame.org/

pygame.init()

win = pygame.display.set_mode((500, 500))   # setup window
pygame.display.set_caption("My First Game")

x = 50          # x-coordiante
y = 50          # y-coordinate
width = 40      # player-width
height = 60     # player-height

run = True
speed = 5

c_pos_x = 250
c_pos_y = 0


def check_events():
    global x, y, run, speed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()     # https://www.pygame.org/docs/ref/key.html#pygame.key.get_pressed

    if keys[pygame.K_LEFT]:
        x -= speed

    if keys[pygame.K_RIGHT]:
        x += speed

    if keys[pygame.K_UP]:
        y -= speed

    if keys[pygame.K_DOWN]:
        y += speed


rand_pos = [random.randint(0, 500), random.randint(0, 500)]
c_speed_y = random.randint(2, 5)

while run:
    pygame.time.delay(10)   # delay of 10ms

    check_events()
    win.fill((0, 0, 0))  # Fills the screen with black
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))   # https://www.pygame.org/docs/ref/draw.html
    c_pos_y += c_speed_y
    pygame.draw.circle(win, (0, 255, 0), [c_pos_x, c_pos_y], 10)
    if c_pos_y >= 500:
        c_pos_y = 0
        c_speed_y = random.randint(1, 3)
    pygame.display.update()

pygame.quit()
