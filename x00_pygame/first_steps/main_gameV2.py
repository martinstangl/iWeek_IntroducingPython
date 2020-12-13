import random
import pygame   # https://www.pygame.org/

pygame.init()

win = pygame.display.set_mode((500, 500))   # setup window
pygame.display.set_caption("My First Game")

x = 250          # x-coordiante
y = 480          # y-coordinate
width = 40      # player-width
height = 10     # player-height

run = True
speed = 5

c_pos_x = 250
c_pos_y = 0
score = 0
high_score = 0

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


def check_collision():
    global x, y, c_pos_x, c_pos_y, score, c_speed_y, high_score
    if x <= c_pos_x <= x+width:
        if y <= c_pos_y <= y+height:
            score += 1
            if high_score < score:
                high_score = score
            c_pos_y = 0
            c_pos_x = random.randint(0, 500)
            c_speed_y = random.randint(1, score)
            print(score)


def game_over():
    global score, run
    if score < 0:
        run = False

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
        score -= 1
        c_pos_y = 0
        c_speed_y = random.randint(1, high_score+1)
    check_collision()
    game_over()
    pygame.display.update()
pygame.quit()
