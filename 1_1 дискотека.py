import random
from all_colors import *
import pygame
pygame.init()

# pygame.mixer.init()
# pygame.mixer.music.load('resurs/La La Land.mp3')
# pygame.mixer.music.play(-1)

size = (0,0)
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
pygame.display.set_caption("My Game")
BACKGROUND = (255, 255, 255)
screen.fill(BACKGROUND)

COLORS = [RED,GREEN, BLUE, YELLOW, CYAN, MAGENTA, GRAY, ORANGE, PINK, BROWN , PURPLE, LIME, NAVY, OLIVE, MAROON, TEAL, SILVER, GOLD]



running = True
timer = 0
while running:
    #Обработка событий игры
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Основная логика игры
    BACKGROUND = random.choice(COLORS)
    # Отрисовка объектов
    screen.fill(BACKGROUND)#очистка экрана
    pygame.display.flip()
    pygame.time.delay(random.randint(200,800))

pygame.quit()