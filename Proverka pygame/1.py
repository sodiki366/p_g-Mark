import pygame as pg
import random

w = 800  # ширина экрана
h = 600  # высота
sc = pg.display.set_mode((w, h))  #
keep_going = True  #

x = w // 2  # расположение по ширине
y = h // 2  # расположение по высоте
r = 50  # радиус
YELLOW = (255, 255, 0)  # желтый
BLUE = (0, 0, 255)  # синий
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)  # белый
timer = pg.time.Clock()
colors = [0] * 100
locations = [0] * 100
sizes = [0] * 100
for n in range(100):
    colors[n] = (random.randint(0, 255), random.randint(0, 255), random.randint
    (0, 255))
    locations[n] = (random.randint(0, 800), random.randint(0, 600))
    sizes[n] = (random.randint(10, 100))

while keep_going:  #
    for event in pg.event.get():  # в цикле слушаем события
        if event.type == pg.QUIT:  # если событие-закрытие окна:сменить флаг
            keep_going = False  #
    for n in range(100):
        pg.draw.circle(sc, colors[n], locations[n], sizes[n])
        x = locations[n][0] + 1
        y = locations[n][1] + 1
        if x > 800:
            x -= 800
        if y > 600:
            y -= 600
        locations[n] = (x, y)
    timer.tick(40)

    pg.display.update()  # обновление экрана
    sc.fill(BLACK)

pg.quit()  # выход