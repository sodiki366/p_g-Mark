#
from all_colors import *
import pygame
pygame.init()
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")
BACKGROUND = (255, 255, 255)
screen.fill(YELLOW)

r = pygame.Rect(0,0,400, 200)
r.center = screen.get_rect().center
pygame.draw.rect(screen, GREEN, r)

my_surface = pygame.Surface((200,100))
my_surface.fill(WHITE)
pygame.draw.circle(my_surface, RED, (100,50), 40)

my_surface.set_colorkey((WHITE))#белый цвет невидимый
my_surface.set_alpha(128)#все цвета полупрозрачные


my_rect = my_surface.get_rect()
my_rect.center = (400,300)
screen.blit(my_surface, my_rect)
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
   # screen.fill(BACKGROUND)#очистка экрана
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()