
from all_colors import *
import random
from pygame.constants import *
import pygame
pygame.init()
size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")
BACKGROUND = (255, 255, 255)
screen.fill(BACKGROUND)

rect = pygame.Rect(0,100,200,150)
speed = 100


COLORS = [RED,GREEN, BLUE, YELLOW, CYAN, MAGENTA, GRAY, ORANGE, PINK, BROWN , PURPLE, LIME, NAVY, OLIVE, MAROON, TEAL, SILVER, GOLD]
FPS = 60
clock = pygame.time.Clock()
running = True
while running:
    #Обработка событий игры
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    rect.x += speed
    if rect.x > screen.get_width():
        rect.x = -rect.width




                # Отрисовка объектов
    screen.fill(BACKGROUND)  # очистка экрана
    screen.fill(BACKGROUND)
    pygame.draw.rect(screen, YELLOW , rect)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()