import pygame


class Bullet:
    def __init__(self, pos, speed, color, screen_width):
        self.speed = speed
        self.visual = pygame.Rect(pos[0],
                                  pos[1],
                                  5,
                                  5)
        self.color = color
        self.screen_width = screen_width

    def move(self):
        self.visual.x += self.speed[0]
        self.visual.y += self.speed[1]

    def draw(self, display):
        pygame.draw.ellipse(display, self.color, self.visual)
