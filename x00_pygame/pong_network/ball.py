import random as random
import pygame


class Ball:
    def __init__(self, size, screen_width, screen_height, speed=[-2, 7], color=(0, 255, 0)):
        pygame.init()
        self.__start = False
        self.size = size
        self.speed = speed
        self.momentum = 0
        self.color = color
        self.visual = pygame.Rect(int(screen_width/2-size/2),
                                  int(screen_height/2-size/2),
                                  size, size)
        self.sounds = {'hit': './sounds/hit.mp3', 'fail': './sounds/fail.mp3'}
        self.screen_width = screen_width
        self.screen_height = screen_height


    def move(self):
        self.visual.x += self.speed[0]
        self.visual.y += self.speed[1]
        if self.visual.right >= self.screen_width or self.visual.left <= 0:
            self.point_over()
        if self.visual.bottom >= self.screen_height or self.visual.top <= 0:
            self.speed[1] *= -1

    def check_collision(self, p1, p2):
        if self.visual.colliderect(p2.visual) and self.speed[0] > 0:
            pygame.mixer.music.load(self.sounds['hit'])
            pygame.mixer.music.play(0)
            self.speed[0] *= -1
            self.speed[1] = self.__calc_momentum(p2)

        if self.visual.colliderect(p1.visual) and self.speed[0] < 0:
            pygame.mixer.music.load(self.sounds['hit'])
            pygame.mixer.music.play(0)
            self.speed[0] *= -1
            self.speed[1] = self.__calc_momentum(p1)

    def __calc_momentum(self, player):
        d_y = int(3 / (player.size['height'] / 2) * (player.visual.y - self.visual.y))
        if (player.visual.y - self.visual.y) < player.size['height']/2:
            d_y *= -1
        print(d_y)
        return d_y

    def restart(self):
        pygame.mixer.music.load(self.sounds['fail'])
        pygame.mixer.music.play(0)
        self.visual.x = int(self.screen_width / 2 - self.size)
        self.visual.y = int(self.screen_height / 2 - self.size)
        self.speed = [random.choice([i for i in range(-3, 3) if i != 0]),
                      random.randint(1, 3)]
        self.speed = [-3, 0]

    def point_over(self):
        self.restart()

    def draw(self, display):
        pygame.draw.ellipse(display, self.color, self.visual)

    def is_start(self):
        return self.__start

    def start(self):
        self.__start = True
