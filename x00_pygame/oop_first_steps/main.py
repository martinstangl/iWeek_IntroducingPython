from x00_pygame.oop_first_steps.auto import Auto

import pygame   # https://www.pygame.org/

pygame.init()

width = 700
height = 500

win = pygame.display.set_mode((width, height))   # setup window
pygame.display.set_caption("Car Sample")

run = True

auto1 = Auto([250, 250],10, 70, False)
auto2 = Auto([50, 50], 5, 80, False)
auto3 = Auto([50, 100], 2, 80, False)

auto1.speed = 10


x = 30
y = 50

def check_keys():
    global x, y
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and width > 0:
        auto1.pos[0] -= 1

    if keys[pygame.K_RIGHT] and x < width-50:
        auto1.pos[0] += 1

    if keys[pygame.K_UP]:
        pass

    if keys[pygame.K_DOWN]:
        pass


while run:
    pygame.time.delay(10)
    auto2.auto_pilot()
    auto3.auto_pilot()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    check_keys()
    win.fill((0, 0, 0))  # Fills the screen with black
    auto1.draw(win)
    auto2.draw(win)
    auto3.draw(win)

    #pygame.draw.rect(win, (255, 0, 0), (x, y, 50, 20))   # https://www.pygame.org/docs/ref/draw.html
    pygame.display.update()

pygame.quit()












