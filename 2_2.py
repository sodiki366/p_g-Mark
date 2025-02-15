
from all_colors import *
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

FPS = 60
clock = pygame.time.Clock()
running = True
while running:
    #Обработка событий игры
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y -= speed
                if y < 0:
                    y = 0
            elif event.key == pygame.K_DOWN:
                y += speed
                if y > 720:
                    y = 720
            elif event.key == pygame.K_LEFT:
                x -= speed
                if x < 0:
                    x = 0  # Защита от выхода за границы экрана
            elif event.key == pygame.K_RIGHT:
                x += speed
                if x > 1280:
                    x = 1280  # Защита от выхода за границы экрана





    # Основная логика игры
    # Отрисовка объектов
    screen.fill(BACKGROUND)  # очистка экрана
    screen.fill(BACKGROUND)
    pygame.draw.rect(screen, color , (x,y,width,height))


    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()