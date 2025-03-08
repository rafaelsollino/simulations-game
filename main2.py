import pygame
import numpy as np
from menu import *
from config import *

t = table(100)


pygame.init()

screen = pygame.display.set_mode((800,800))


clock = pygame.time.Clock()
running = True

main_menu()
while running:

    screen.fill((0,0,0))

    rows, cols = np.shape(t)

    # Draw inds
    for i in range(1, rows):
        v = t[i][3]
        pos = (t[i][0], t[i][1])
        pygame.draw.circle(screen, get_color(v), pos, 5)

    # Walk
    for i in range(1, rows):
        pos = (t[i][0], t[i][1])
        theta = t[i][2]
        v = t[i][3]

        if pos[0] >= 800-5 or pos[1] >= 800-5:
            theta += pi
        else: 
            theta += uniform(-0.5, 0.5)

        pos = walk(pos, theta, v)
        t[i][0] = pos[0]
        t[i][1] = pos[1]
        t[i][2] = theta



    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False

    pygame.display.flip()

    clock.tick(60)

pygame.quit()