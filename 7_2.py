#
import math
import pygame
pygame.init()

pacman_images = {
    "up": pygame.image.load('resours/pacman_up.png'),
    'down': pygame.image.load('resours/pacman_down.png'),
    "left": pygame.image.load('resours/pacman_left.png'),
    'right': pygame.image.load('resours/pacman_right.png'),
    "up_left": pygame.image.load('resours/pacman_up_left.png'),
    'down_left': pygame.image.load('resours/pacman_dow_left.png'),
    "up_right": pygame.image.load('resours/pacman_up_right.png'),
    'down_right': pygame.image.load('resours/pacman_down_right.png'),
}
def get_direction(pos1,pos2):
    dx = pos2[0] - pos1[0]
    dy = pos2[1] - pos1[1]

    direction = 'right'
    if dy < 0:
        if dx < 0:
            direction = 'up_left'
        elif dx > 0:
            direction = 'up_right'
        else:
            direction = 'up'
    elif dy > 0:
        if dx < 0:
            direction = 'down_left'
        elif dx > 0:
            direction = 'down_right'
        else:
            direction = 'down'
    else:
        if dx < 0:
            direction = 'left'
        elif dx > 0:
            direction = 'right'

    return direction


def distance(pos1,pos2):
    return math.sqrt((pos2[0] - pos1[0]) ** 2 + (pos2[1] - pos1[1]) ** 2 )
def move_towards(pos1,pos2,min_speed=1, max_speed = 10):
    x1,y1 = pos1
    x2,y2 = pos2
    dx = x2 - x1
    dy = y2 - y1

    dist = distance(pos1,pos2)

    if dist < min_speed:
        return pos2
    if dist == 0:
        return pos1

    speed = max(min_speed, min(dist / 5, max_speed))

    dx /= dist
    dy /= dist
    print(dx,dy)

    x1 += dx * speed
    y1 += dy * speed

    return (x1,y1)

size = (640, 480)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")
BACKGROUND = (0,0,0)
CIRCLE_COLOR = (255,255,255)
CIRCLE_RADIUS = 20

circle_pos = (320, 240)
speed = 3

screen.fill(BACKGROUND)
FPS = 60
clock = pygame.time.Clock()
running = True
while running:
    #Обработка событий игры
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse_pos = pygame.mouse.get_pos()
    direction = get_direction(pacman_pos, mouse_pos)
    pacman_pos = move_towards(pacman_pos, mouse_pos)
    # Основная логика игры
    # Отрисовка объектов
    screen.fill(BACKGROUND)#очистка экрана
    pacman_image = pacman_images[direction]
    screen.blit(pacman_image, pacman_pos)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()