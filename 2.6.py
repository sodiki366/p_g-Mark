
from all_colors import *
import random
import pygame
from pygame.examples.go_over_there import screen

pygame.init()
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width,  screen_height))
screen.fill((255,255,255))
BLACK = (0,0,0)
width = 100
height = 75
color = [RED,GREEN, BLUE, YELLOW, CYAN, MAGENTA, GRAY, ORANGE, PINK, BROWN , PURPLE, LIME, NAVY, OLIVE, MAROON, TEAL, SILVER, GOLD]
rects = []

rects.append(pygame.Rect(0, 0, width, height))
colors = random.choice(color)

rects.append(pygame.Rect(0, 0, width, height))
rects[-1].topright = (screen_width, 0)
colors = random.choice(color)

rects.append(pygame.Rect(0, 0, width, height))
rects[-1].bottomleft = (0, screen_height)
colors = random.choice(color)

rects.append(pygame.Rect(0, 0, width, height))
rects[-1].bottomright = (screen_width, screen_height)
colors = random.choice(color)



rects.append(pygame.Rect(0,0, width, height))
rects[-1].center = (screen_width // 2, screen_height // 2)

for rect in rects:
    pygame.draw.rect(screen, BLACK, rect, colors)

pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()