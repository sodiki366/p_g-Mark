#
from all_colors import *
import random
import pygame
pygame.init()
# pygame.mixer.init()
# pygame.mixer.music.load('resurs/La La Land.mp3')
# pygame.mixer.music.play(-1)

size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")
COLORS = [RED,GREEN, BLUE, YELLOW, CYAN, MAGENTA, GRAY, ORANGE, PINK, BROWN , PURPLE, LIME, NAVY, OLIVE, MAROON, TEAL, SILVER, GOLD]
BACKGROUND = (255, 255, 255)
screen.fill(BACKGROUND)
line_color = RED
line_width = 5
start_pos = (0, size[1]//2)
end_pos = (size[0], size[1]//2)

FPS = 60
clock = pygame.time.Clock()
for _ in range(10):
    x = random.randint(0,1280)
    y = random.randint(0, 720)
    radius = random.randint(10,100)
    color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    pygame.draw.circle(screen, color, (x, y), radius)
    after(2000 // FPS)

running = True

while running:
    #Обработка событий игры
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Основная логика игры

    # Отрисовка объектов

    screen.fill(BACKGROUND)#очистка экрана







    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()