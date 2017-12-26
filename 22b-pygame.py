#!env python3
import sys
import pygame
import time

pygame.init()
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

infected = (245, 30, 30)
warning = (245, 137, 30)
marked = (245, 30, 137)

infected = (255, 255, 255)
warning = (150, 150, 150)
marked = (100, 100, 100)


size = [1920, 1080]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("AoC 22")
clock = pygame.time.Clock()


def renderMap(cur_x, cur_y):
    min_x = None
    min_y = None
    max_x = None
    max_y = None
    for key in virusmap:
        if min_x is None or key[0] < min_x:
            min_x = key[0]
        if max_x is None or key[0] > max_x:
            max_x = key[0]
        if min_y is None or key[1] < min_y:
            min_y = key[1]
        if max_y is None or key[1] > max_y:
            max_y = key[1]

    print('Map size (x,y):', min_x, '-', max_x, ',', min_y, '-', max_y)
    margin = 3
    for y in range(min_y - margin, max_y + 1 + margin):
        for x in range(min_x - margin, max_x + 1 + margin):
            item = '.'
            if (x, y) in virusmap:
                item = virusmap[x, y]
            print(item, end='')
            if y == cur_y and x == cur_x - 1:
                print('[', end='')
            elif y == cur_y and x == cur_x:
                print(']', end='')
            else:
                print(' ', end='')
        print()


virusmap = {}
y = 0
for row in sys.stdin.read().split('\n'):
    if len(row.strip()) == 0:
        continue
    x = 0
    for dot in row:
        virusmap[x, y] = dot
        x += 1
    y += 1

x = int((x - 1) / 2)
y = int((y - 1) / 2)
print('Starting position (x,y):', x, y)
# renderMap(x, y)
directions = ['up', 'right', 'down', 'left']
direction = 0
infections = 0

screen.fill(BLACK)


def draw(x, y, color):
    zoom = 6
    x = x - 25
    y = y - 10
    x = x * zoom + int(size[0] / 2)
    y = y * zoom + int(size[1] / 2)
#    pygame.draw.circle(screen, color, [x , y], 2)
    pygame.draw.rect(screen, color, [x, y, zoom - 1, zoom - 1])

c = 0
for step in range(1000000):
#    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break

    if step % 100000 == 0:
        print('Step:', step, 'Direction:', directions[direction], 'Pos (x,y):', x, y)
    if (x, y) in virusmap and virusmap[x, y] != '.':
        if virusmap[x, y] == '#':
            # turn right
            direction = (direction + 1) % len(directions)
            virusmap[x, y] = 'F'
            draw(x, y, marked)
        elif virusmap[x, y] == 'W':
            virusmap[x, y] = '#'
            infections += 1
            draw(x, y, infected)
        elif virusmap[x, y] == 'F':
            # turn in reverse
            direction = (direction + 2) % len(directions)
            virusmap[x, y] = '.'
            draw(x, y, BLACK)
    else:
        # turn left
        direction = (direction - 1) % len(directions)
        # infect
        virusmap[x, y] = 'W'
        draw(x, y, warning)

    if directions[direction] == 'up':
        y -= 1
    if directions[direction] == 'down':
        y += 1
    if directions[direction] == 'right':
        x += 1
    if directions[direction] == 'left':
        x -= 1

    draw(x, y, RED)

    
    if step % 278 == 0:
        pygame.display.flip()
        pygame.image.save(screen, '22-images/{num:06d}.png'.format(num=c))
        c += 1
#        renderMapGame(x, y)

# renderMapGame(x, y)
print('Total infections:', infections)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
    pygame.display.flip()
    time.sleep(1)
pygame.quit()
