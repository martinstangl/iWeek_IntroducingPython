import random
import pygame   # https://www.pygame.org/

pygame.init()

win = pygame.display.set_mode((500, 500))   # setup window
pygame.display.set_caption("My First Game")
sounds = {'hit': './sounds/hit.mp3', 'fail': './sounds/fail.mp3'}

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
c_speed_y = random.randint(2, 5)


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
    global x, y, c_pos_x, c_pos_y, score, c_speed_y, high_score, sounds
    if x <= c_pos_x <= x+width:
        if y <= c_pos_y <= y+height:
            score += 1
            if high_score < score:
                high_score = score
            c_pos_y = 0
            c_pos_x = random.randint(0, 500)
            c_speed_y = random.randint(1, score)
            pygame.mixer.music.load(sounds['hit'])
            pygame.mixer.music.play(0)


def display_score():        # https://www.techwithtim.net/tutorials/game-development-with-python/tetris-pygame/tutorial-4/
    global score, win, high_score
    print(high_score)
    pygame.font.init()
    font = pygame.font.SysFont('comicsans', 30)
    label = font.render('Score: ' + str(score) + " / " + str(high_score), 1, (255, 255, 255))
    win.blit(label, [250, 10])


def game_over():
    global score, run
    if score < 0:
        run = False


def move_circle():
    global c_pos_y, score, c_pos_y, c_speed_y, high_score, sounds
    c_pos_y += c_speed_y
    if c_pos_y >= 500:
        score -= 1
        c_pos_y = 0
        c_speed_y = random.randint(1, high_score+1)
        pygame.mixer.music.load(sounds['fail'])
        pygame.mixer.music.play(0)


while run:
    pygame.time.delay(10)   # delay of 10ms
    win.fill((0, 0, 0))  # Fills the screen with black
    check_events()
    move_circle()
    check_collision()
    game_over()
    display_score()
    pygame.draw.circle(win, (0, 255, 0), [c_pos_x, c_pos_y], 10)
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))  # https://www.pygame.org/docs/ref/draw.html
    pygame.display.update()


pygame.quit()
