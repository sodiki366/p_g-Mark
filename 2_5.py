
import random
from all_colors import *
import pygame
pygame.init()
size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Моя игра")
BACKGROUND = WHITE
screen.fill(BACKGROUND)
x = 0
y = 0
rect_size = 200
colors =  [RED,GREEN, BLUE, YELLOW, CYAN, MAGENTA, GRAY, ORANGE, PINK, BROWN , PURPLE, LIME, NAVY, OLIVE, MAROON, TEAL, SILVER, GOLD]



for i in range(1,18):
    rect = pygame.Rect(x, y ,rect_size/i, rect_size/i)
    rect.center = (screen.get_width() // 2 , screen.get_height() //2)
    color = random.choice(colors)
    pygame.draw.rect(screen,color, rect)

FPS = 60
clock = pygame.time.Clock()
running = True
while running:
    # Обработка событий игры
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #
    #
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()



