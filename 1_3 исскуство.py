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


running = True

while running:
    #Обработка событий игры
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Основная логика игры
    BACKGROUND = random.choice(COLORS)

    # Отрисовка объектов
    x = random.randint(0,1280)
    y = random.randint(0,720)
    COLOR = random.choice(COLORS)
    radius = random.randint(0,100)

    pygame.draw.ellipse(screen, COLOR, (x,y,radius))

    screen.fill(BACKGROUND)#очистка экрана







    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()