import random

import pygame


class Auto:
    def __init__(self, pos, speed, tank, bot=True):
        self.color = (random.randint(0, 255),
                      random.randint(0, 255),
                      random.randint(0, 255))
        self.speed = speed
        self.tank = tank
        self.pos = pos
        if bot:
            self.img = pygame.transform.scale(
                pygame.image.load("./images/car_red.png"), (40, 40))
        else:
            self.img = pygame.transform.scale(
                pygame.image.load("./images/mario.png"), (40, 40))
        self.rect = self.img.get_rect()   # get rect with position and size of image

    def acc(self, a):
        self.speed += a

    def move(self):
        if self.fahrbereit:
            pass

    def output(self):
        print("Farbe:",self.color,"Speed:",self.speed,"Tank:",self.tank)

    def draw(self, win):
        #pygame.draw.rect(win, self.color, (self.pos[0], self.pos[1], 50, 20))
        win.blit(self.img, (self.pos[0], self.pos[1]))

    def auto_pilot(self):
        self.pos[0] += self.speed
        if self.pos[0] >= 700:
            self.pos[0] = 0
            self.pos[1] = random.randint(1, 500)

    def check_col(self, cars):
        for car in cars:
            if self.img.get_rect().colliderect(car.img.get_rect()):
                car.crashed()
                self.crashed()

    def crashed(self):
        self.speed = 0

    def get_img_size(self):
        print(self.img.get_rect().size)
