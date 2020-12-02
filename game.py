"""PyGame Interface"""
# Further Reference:
# http://inventwithpython.com/pygame/
# http://www.pygame.org/docs/

import pygame
from drone import *

# define 32-bit RGB colours

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# initialise pygame

pygame.init()

# define parameters

screen_height = 500
screen_width = 500

voyager = Drone("voyager", 250, 250)
enemy = Drone("enemy", 400, 400, 100, 30, red, 5)


# initialise pygame screen

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Voyager")
fps = pygame.time.Clock()
pygame.key.set_repeat(100, 5)

done = False
while not done:
    fps.tick(940)

    # draw drone
    screen.fill(black)
    pygame.draw.circle(screen, voyager.c, [voyager.x, voyager.y], voyager.r, voyager.t)
    pygame.draw.circle(screen, enemy.c, [enemy.x, enemy.y], enemy.r, enemy.t)

    # update screen
    pygame.display.flip()

    # check quit/keyboard events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        # https://www.pygame.org/docs/ref/key.html
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                voyager.move("up")
            if keys[pygame.K_DOWN]:
                voyager.move("down")
            if keys[pygame.K_LEFT]:
                voyager.move("left")
            if keys[pygame.K_RIGHT]:
                voyager.move("right")

    # Keep Voyager in screen
    if voyager.x > screen_width - voyager.r:
        voyager.x = screen_width - voyager.r
    if voyager.x < voyager.r:
        voyager.x = voyager.r
    if voyager.y > screen_height - voyager.r:
        voyager.y = screen_height - voyager.r
    if voyager.y < voyager.r:
        voyager.y = voyager.r

# uninitialise pygame

pygame.quit()
