import sys
#https://www.youtube.com/watch?v=Qf3-aDXG8q4

import pygame

from sample02.fighter import Fighter

pygame.init()
clock = pygame.time.Clock()

screen_width = 500
screen_height = 500
background = (255, 255, 255)

display = pygame.display.set_mode((screen_width, screen_height))
bg_image = pygame.transform.scale(pygame.image.load("./img/background.jpg").convert(),((500, 500)))

pygame.display.set_caption("SpriteSheet")

player_pos = [screen_width // 4, screen_height // 2]
player_pos2 = [screen_width * 3 // 4, screen_height // 2]
player = Fighter(player_pos, screen_width, screen_height)
player2 = Fighter(player_pos2, screen_width, screen_height, True)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #display.fill(background)
    display.blit(bg_image, [0, 0])
    player.move()
    player.draw(display)
    player2.move()
    player2.draw(display)
    pygame.display.update()
    #pygame.display.flip()
    clock.tick(30)
