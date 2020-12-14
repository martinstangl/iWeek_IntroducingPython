import pygame


class Player:
    def __init__(self, color=(255, 0, 0), start=[0, 0]):
        self.size = 100
        self.color = color
        self.points = [start]
        self.head = self.points[-1]
        self.direction = 0                      # 0: rechts 1: runter...
        self.speed = 3

    def draw(self, win):
        self.move()
        pygame.draw.lines(win, self.color, False, self.points, 3)

    def move(self):
        #print(self.points)
        new_point = [self.points[-1][0], self.points[-1][1]]
        if self.direction == 0:
            new_point[0] += self.speed
            pass
        elif self.direction == 1:
            new_point[1] += self.speed
            pass
        elif self.direction == 2:
            new_point[0] -= self.speed
            pass
        else:
            new_point[1] -= self.speed
            pass
        if not self.check_crash(new_point):
            self.points.append(new_point)
        else:
            self.speed = 0

    def check_crash(self, point):
        if point in self.points:
            return True
        else:
            return False

    def check_crash_list(self, points):
        for p in points:
            if p in self.points:
                self.speed = 0
