#
from all_colors import *
import pygame
pygame.init()
size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")
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

    # Отрисовка объектов
    screen.fill(BACKGROUND)#очистка экрана

    pygame.draw.line(screen, line_color, start_pos, end_pos, line_width)

    pygame.draw.rect(screen, ORANGE, (50,50,100,100))
    pygame.draw.rect(screen, ORANGE, (250,50,100,100),1)
    pygame.draw.rect(screen, ORANGE, (450,50,100,100),
                     border_radius=10)

    pygame.draw.ellipse(screen, ORANGE, (50,450,100,100))
    pygame.draw.ellipse(screen, ORANGE,(250,450,100,100),1)

    pygame.draw.polygon(screen, ORANGE, ((750, 250),
                                          (800, 450),
                                          (850, 250)))
    pygame.draw.polygon(screen, ORANGE, ((650, 350),
                                         (700, 350),
                                         (750, 350)),3)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()