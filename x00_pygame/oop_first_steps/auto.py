import random

import pygame


class Auto:
    def __init__(self, pos, speed, tank, fahrbereit=True):
        self.color = (random.randint(0, 255),
                      random.randint(0, 255),
                      random.randint(0, 255))
        self.speed = speed
        self.tank = tank
        self.fahrbereit = fahrbereit
        self.pos = pos

    def acc(self, a):
        self.speed += a

    def move(self):
        if self.fahrbereit:
            pass

    def output(self):
        print("Farbe:",self.color,"Speed:",self.speed,"Tank:",self.tank)

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.pos[0], self.pos[1], 50, 20))

    def auto_pilot(self):
        self.pos[0] += self.speed
        if self.pos[0] >= 700:
            self.pos[0] = 0


    # def set_color(self,rw,gw,bw):
    #     if 0 <= rw <= 255:
    #         pass

