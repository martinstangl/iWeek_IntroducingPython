import random

from x00_pygame.oop_first_steps.auto import Auto

import pygame   # https://www.pygame.org/

pygame.init()

life = 3
heart_img = pygame.transform.scale(
        pygame.image.load("./images/heart.png"), (40, 40))

width = 700
height = 500

win = pygame.display.set_mode((width, height))   # setup window
pygame.display.set_caption("Car Sample")

run = True

cars = []
player = Auto([int(width/2), int(height/2)], 5, 100, False)

for i in range(10):     # autos erzeugen und in liste speichern
    cars.append(Auto([random.randint(0, width),
                     random.randint(0, height)],
                     random.randint(1, 5), 70))



def show_life():
    for l in range(1, life+1):
        win.blit(heart_img, (width-l*50, 10))


def check_keys():
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player.pos[0] > 0:
        player.pos[0] -= 1

    if keys[pygame.K_RIGHT] and player.pos[0] < width:
        player.pos[0] += 1

    if keys[pygame.K_UP]:
        player.pos[1] -= 1

    if keys[pygame.K_DOWN]:
        player.pos[1] += 1


while run:
    pygame.time.delay(10)
    win.fill((0, 0, 0))  # Fills the screen with black
    for a in cars:
        a.auto_pilot()
        a.draw(win)
        # a.check_col(cars)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    show_life()
    check_keys()
    player.draw(win)
   # player.get_img_size()
    pygame.display.update()

pygame.quit()












