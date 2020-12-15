from x00_pygame.oop_first_steps.auto import Auto

import pygame   # https://www.pygame.org/

pygame.init()

width = 700
height = 500
win = pygame.display.set_mode((width, height))   # setup window
pygame.display.set_caption("Car Sample")

run = True

auto1 = Auto(10, 100, False)
auto2 = Auto(5, 80, False)
auto1.speed = 10
auto1.output()
auto2.output()


def check_keys():
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        pass

    if keys[pygame.K_RIGHT]:
        pass

    if keys[pygame.K_UP]:
        pass

    if keys[pygame.K_DOWN]:
        pass


while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    check_keys()

    win.fill((0, 0, 0))  # Fills the screen with black
    pygame.draw.rect(win, (255, 0, 0), (30, 30, 50, 20))   # https://www.pygame.org/docs/ref/draw.html
    pygame.display.update()

pygame.quit()












