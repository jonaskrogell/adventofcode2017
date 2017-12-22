#!env python3
import sys


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
renderMap(x, y)
directions = ['up', 'right', 'down', 'left']
direction = 0
infections = 0
for step in range(10000):
    print('Step:', step, 'Direction:', directions[direction], 'Pos (x,y):', x, y)
    if (x, y) in virusmap and virusmap[x, y] == '#':
        # turn right
        direction = (direction + 1) % len(directions)
        # clean
        virusmap[x, y] = '.'
    else:
        # turn left
        direction = (direction - 1) % len(directions)
        # infect
        virusmap[x, y] = 'W'
        infections += 1

    if directions[direction] == 'up':
        y -= 1
    if directions[direction] == 'down':
        y += 1
    if directions[direction] == 'right':
        x += 1
    if directions[direction] == 'left':
        x -= 1

    if step % 1000 == 0:
        renderMap(x, y)

renderMap(x, y)
print('Total infections:', infections)
