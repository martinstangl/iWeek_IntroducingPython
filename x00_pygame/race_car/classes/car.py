from math import cos, sin, pi
import pygame


class Car:
    def __init__(self, pos):
        self.pos = pos
        self.image = pygame.transform.scale(
            pygame.image.load("./images/car_red.png"), (40, 40))
        self.angle = 0
        self.speed = 0
        self.image_rot = self.image
        self.slow_down = False

    def draw(self, display):
        display.blit(self.image_rot, self.pos)
        # self.check_slow_down(display)     # uncomment to activate slow speed outside track

    def move(self):
        pygame.time.delay(30)
        if pygame.key.get_pressed()[pygame.K_UP]:
            self.speed += 1
        elif pygame.key.get_pressed()[pygame.K_DOWN]:
            self.speed -= 1
        elif pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.angle += 5
            self.image_rot = Car.rot_center(self.image, -self.angle)
        elif pygame.key.get_pressed()[pygame.K_LEFT]:
            self.angle -= 5
            self.image_rot = Car.rot_center(self.image, -self.angle)
        if self.slow_down:
            self.speed = 2
        self.__move()

    def __move(self):
        self.pos[0] += cos((self.angle*pi / 180) % (2*pi)) * self.speed
        self.pos[1] += sin((self.angle*pi / 180) % (2*pi)) * self.speed

    def check_slow_down(self, display):
        rgba = display.get_at([int(i) for i in self.pos])
        if rgba[1] == 100:
            self.slow_down = True  # should be True
        else:
            self.slow_down = False

        #print(display.get_at([int(i) for i in self.pos]))

    @staticmethod
    def rot_center(image, angle):
        """rotate an image while keeping its center and size"""
        orig_rect = image.get_rect()
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()
        return rot_image


