import random
from all_colors import *  # Предположим, что этот модуль содержит определения цветов
import pygame

# Инициализация pygame
pygame.init()

# Установка размеров окна
size = (1280, 720)
screen = pygame.display.set_mode(size)

# Заголовок окна
pygame.display.set_caption("Моя игра")

# Цвет фона
BACKGROUND = WHITE
screen.fill(BACKGROUND)

# Координаты начала рисования
x = 0
y = 0

# Размер самого большого прямоугольника
rect_size = 200

# Список доступных цветов
colors = [
    RED, GREEN, BLUE, YELLOW, CYAN, MAGENTA,
    GRAY, ORANGE, PINK, BROWN, PURPLE, LIME,
    NAVY, OLIVE, MAROON, TEAL, SILVER, GOLD
]

# Создаем список всех прямоугольников
rects = []

# Создаем список начальных цветов для каждого прямоугольника
color_list = []

# Рисуем начальные квадраты и сохраняем их параметры
for i in range(1, 18):
    rect = pygame.Rect(
        x, y,  # Левый верхний угол
        rect_size / i, rect_size / i  # Ширина и высота
    )
    rect.center = (
        screen.get_width() // 2,  # Центрирование по горизонтали
        screen.get_height() // 2  # Центрирование по вертикали
    )

    # Выбираем случайный цвет для каждого прямоугольника
    color = random.choice(colors)
    color_list.append(color)

    # Рисуем начальный прямоугольник
    pygame.draw.rect(screen, color, rect)

    # Сохраняем прямоугольники в списке
    rects.append(rect)

# Устанавливаем таймер для смены цвета каждый 100 мс (или другой интервал)
TIMER_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(TIMER_EVENT, 100)  # Меняет цвет каждые 100 мс

# Настройка частоты кадров
FPS = 60
clock = pygame.time.Clock()

# Основной игровой цикл
running = True
while running:
    # Обработка событий игры
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == TIMER_EVENT:
            # Если сработал таймер, меняем цвет каждого прямоугольника
            for idx, rect in enumerate(rects):
                new_color = random.choice(colors)
                while new_color == color_list[idx]:  # Чтобы избежать повторения текущего цвета
                    new_color = random.choice(colors)
                color_list[idx] = new_color
                pygame.draw.rect(screen, new_color, rect)

            # После перерисовки всех прямоугольников обновляем экран
            pygame.display.flip()

    # Ограничение FPS
    clock.tick(FPS)

# Завершение работы pygame
pygame.quit()