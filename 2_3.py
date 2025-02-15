
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

width, height =100,100
x,y = 50,50
color = RED
speed = 5

COLORS = [RED,GREEN, BLUE, YELLOW, CYAN, MAGENTA, GRAY, ORANGE, PINK, BROWN , PURPLE, LIME, NAVY, OLIVE, MAROON, TEAL, SILVER, GOLD]
FPS = 60
clock = pygame.time.Clock()
running = True
while running:
    #Обработка событий игры
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed
    # Основная логика игры

    if x < 0:
        x = 0
        color = random.choice(COLORS)
        continue
    if x > 1280 - width:
        x = 1280 - width
        color = random.choice(COLORS)
        continue
    if y < 0:
        y = 0
        color = random.choice(COLORS)
        continue
    if y > 720 - height:
        y = 720 - height
        color = random.choice(COLORS)
        continue


                # Отрисовка объектов
    screen.fill(BACKGROUND)  # очистка экрана
    screen.fill(BACKGROUND)
    pygame.draw.rect(screen, color, (x, y, width, height))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

