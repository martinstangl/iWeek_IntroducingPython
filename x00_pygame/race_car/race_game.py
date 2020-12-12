import sys
from math import cos, sin, pi
# scroll background
# https://www.techwithtim.net/tutorials/game-development-with-python/side-scroller-pygame/background/
import pygame

from x00_pygame.race_car.classes.car import Car

clock, screen_size, bg_image, display = None, None, None, None


def setup():
    global clock, screen_size, display, bg_image
    pygame.init()
    clock = pygame.time.Clock()
    clock.tick(30)
    # background = (255, 255, 255)
    # info_object = pygame.display.Info()
    screen_size = (1200, 700)
    display = pygame.display.set_mode(screen_size)
    image = pygame.image.load("./images/marina.png")
    bg_image = pygame.transform.scale(image.convert(), (3*screen_size[0], 3*screen_size[1]))

    pygame.display.set_caption("Race Game")


setup()
car = Car([screen_size[0]/2, screen_size[1]/2])

center = [0, 0]
while True:
    if car.pos[0]+250 >= screen_size[0]:
        center[0] -= cos((car.angle * pi / 180) % (2 * pi)) * car.speed
        center[1] -= sin((car.angle * pi / 180) % (2 * pi)) * car.speed
        car.pos[0] -= cos((car.angle * pi / 180) % (2 * pi)) * car.speed
        car.pos[1] -= sin((car.angle * pi / 180) % (2 * pi)) * car.speed
    elif car.pos[0] <= 250:
        center[0] += car.speed
        car.pos[0] += car.speed
    if car.pos[1]+250 >= screen_size[1]:
        center[1] -= sin((car.angle * pi / 180) % (2 * pi)) * car.speed
        car.pos[1] -= sin((car.angle * pi / 180) % (2 * pi)) * car.speed

    display.blit(bg_image, center)
    car.move()
    car.draw(display)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
