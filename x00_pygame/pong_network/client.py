import pygame
from pong_network.network import Network
from pong_network.player import Player
from pong_network.settings import Settings

screen_width = Settings.config["screen_width"]
screen_height = Settings.config["screen_height"]
background = (128, 128, 128)
display = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong Game")
clientNumber = 0
pygame.init()


def redraw_window(display, player, player2, ball):
    display.fill(background)
    draw_board(display)
    player.draw(display)
    player2.draw(display)
    ball.draw(display)
    pygame.display.update()
    pygame.display.flip() #check


def draw_board(display):

    pygame.draw.circle(display, (0, 0, 0), (int(screen_width / 2), int(screen_height / 2)), 30, 1)
    pygame.draw.aaline(display, (0, 0, 0), (int(screen_width / 2), 0),
                       (int(screen_width / 2), int(screen_height / 2) - 30))
    pygame.draw.aaline(display,
                       (0, 0, 0),
                       (int(screen_width / 2), int(screen_height / 2) + 30),
                       (int(screen_width / 2), screen_height))


def main():
    run = True
    n = Network()
    do = n.getP()
    p = do.player
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        if do is not None:
            do.player = p
            do = n.send(do)
            if do is not None:
                p2 = do.player
                ball = do.ball
                p.move()
                redraw_window(display, p, p2, ball)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()


main()
