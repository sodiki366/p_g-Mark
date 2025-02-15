
from all_colors import *
import random
from pygame.constants import *
import pygame
pygame.init()
size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")
BACKGROUND = WHITE
screen.fill(BACKGROUND)
x = 0
y = 0
rect_size = 200
colors = [RED,BLACK]

# rect1 = pygame.Rect(x,y,rect_size, rect_size)
# rect1.center = (screen.get_width() // 2 , screen.get_height() // 2)
# pygame.draw.rect(screen, BLACK, rect1)
# rect2 = pygame.Rect(x,y,rect_size/2, rect_size/2)
# rect2.center = (screen.get_width() // 2 , screen.get_height() // 2)
# pygame.draw.rect(screen, BLACK, rect2)

for _ in range(2):
    color = random.choice(colors)
    x = random.randint(0, size[0] - rect_size)
    y = random.randint(0, size[1] - rect_size)
    rect = pygame.Rect(x, y, rect_size, rect_size)
    pygame.draw.rect(screen, color, rect)

COLORS = [RED,GREEN, BLUE, YELLOW, CYAN, MAGENTA, GRAY, ORANGE, PINK, BROWN , PURPLE, LIME, NAVY, OLIVE, MAROON, TEAL, SILVER, GOLD]
FPS = 60
clock = pygame.time.Clock()
running = True
while running:
    #Обработка событий игры
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #Основная логика игры



        # Отрисовка объектов


pygame.quit()
