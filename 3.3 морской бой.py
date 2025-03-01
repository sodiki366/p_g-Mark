#
from all_colors import *
import pygame
pygame.init()

import pygame.mixer
pygame.mixer.init()

shot_sound = pygame.mixer.Sound('')
size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")
BACKGROUND = (255, 255, 255)
screen.fill(BACKGROUND)

screen_rect = screen.get_rect()

ship = pygame.Rect(300,200,50,100)
ship.right = screen_rect.right
ship.centery = screen_rect.centery

missile = pygame.Rect(50,50,10,10)
missile.left = screen_rect.left
missile.centery = screen_rect.centery

missile_speed_x = 0
missile_speed_y = 0

ship_speed_y = 1

ship_alive = True
missile_alive = True

missile_launched = False
hp_ship = 10
screen_rect = screen.get_rect()

FPS = 120
clock = pygame.time.Clock()
running = True
while running:
    #Обработка событий игры
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not missile_launched:
                missile_launched = True
                missile_speed_x = 3
                missile_speed_y = 0

            elif event.key == pygame.K_w and not missile_launched:
                missile_speed_y = -2
            elif event.key == pygame.K_s and not missile_launched:
                missile_speed_y = 2


    # Основная логика игры
    if missile_alive:
        missile.move_ip(missile_speed_x, missile_speed_y)
        if not missile.colliderect(screen_rect):
            missile_alive = False
        if ship_alive and missile_colliderect(ship):
           missile_alive = False
           ship_alive = False
    if ship_alive:
        ship.move_ip(0, ship_speed_y)
    if ship.bottom > screen_rect.bottom or ship.top < screen_rect.top:
        ship_speed_y = -ship_speed_y
    # Отрисовка объектов

    screen.fill(BACKGROUND)#очистка экрана
    if ship_alive:
        pygame.draw.rect(screen, BLUE, ship)
    if missile_alive:
        pygame.draw.rect(screen, RED, missile)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()