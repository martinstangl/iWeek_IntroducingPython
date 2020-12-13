import pygame
from pygame.constants import KEYDOWN
from pong_network.bullet import Bullet


class Player:
    def __init__(self, pos, screen_width, screen_height,size={'width': 10, 'height': 50}, color=(128, 128, 128)):  #={'x': 10, 'y': screen_height/2}
        self.size = size
        self.color = color
        self.visual = pygame.Rect(pos['x'],
                                  int(pos['y']-self.size['width']/2),
                                  self.size['width'],
                                  self.size['height'])
        self.bullet_list = []
        self.bullet_dir = -5 if pos['x'] > 30 else 5
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.bullet_counter = 0

    def move(self):
        if pygame.key.get_pressed()[pygame.K_UP]:
            self.move_up()
        elif pygame.key.get_pressed()[pygame.K_DOWN]:
            self.move_down()
        elif pygame.key.get_pressed()[pygame.K_SPACE]:
            if self.bullet_counter == 0:
                self.bullet_list.append(Bullet([self.visual.x, self.visual.y],
                                               [self.bullet_dir, 0],
                                               (255, 0, 0),
                                               self.screen_width
                                               ))
                self.bullet_counter += 1
            if self.bullet_counter > 0:
                self.bullet_counter += 1
            self.bullet_counter %= 10

        for b in self.bullet_list:
            if 0 <= b.visual.x >= self.screen_width:
                self.bullet_list.remove(b)
            b.move()

    def move_up(self):
        self.visual.y -= 3
        #self.__momentum -= 1

    def move_down(self):
        self.visual.y += 3
        #self.__momentum += 1

    def move_right(self):
        self.visual.x += 10
       # self.__momentum -= 1

    def move_left(self):
        self.visual.x -= 10
      #  self.__momentum += 1

    def clear_momentum(self):
        self.__momentum = 0

    def get_momentum(self):
        return self.__momentum

    def check_bullet_collision(self,bullet_list):
        for b in bullet_list:
            if self.visual.colliderect(b.visual):
                self.make_gap(b.visual.y)


    def draw(self, display):
        pygame.draw.rect(display, self.color, self.visual)
        for b in self.bullet_list:
            b.draw(display)

    def make_gap(self, y):
        pass

