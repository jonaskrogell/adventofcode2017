import sys

network = []
for row in sys.stdin.read().split('\n'):
    line = []
    for item in row:
        line.append(item)
    network.append(line)

for line in network:
    print(line)

y = 0
x = network[0].index('|')
direction = 'down'
directions = ['down', 'left', 'up', 'right']
visisted = {}


def getNextPos():
    if direction == 'down':
        next_y = y + 1
        next_x = x
    elif direction == 'up':
        next_y = y - 1
        next_x = x
    elif direction == 'right':
        next_y = y
        next_x = x + 1
    elif direction == 'left':
        next_y = y
        next_x = x - 1

    valid = True
    if next_y < 0 or next_y > len(network):
        print('Edge reached in Y')
        valid = False
    elif next_x < 0 or next_x > len(network[next_y]):
        print('Edge reached in X')
        valid = False
    elif network[next_y][next_x] == ' ':
        valid = False

    return next_x, next_y, valid


letters = ''
while True:
    print('Pos (x, y, direction):', x, y, direction)
    visisted[x, y] = True

    if network[y][x] not in (' ', '|', '-', '+'):
        print('Found letter:', network[y][x])
        letters += network[y][x]

    next_x, next_y, valid = getNextPos()

    if not valid:
        stuck = 4
        while stuck > 0:
            direction = directions[(directions.index(direction) + 1) % len(directions)]
            print('Try change direction to', direction, next_x, next_y)
            next_x, next_y, valid = getNextPos()
            if valid and (next_x, next_y) not in visisted:
                break
            stuck -= 1
        if stuck == 0:
            print('Stuck!')
            print('Found letters:', letters)
            sys.exit(0)
        continue

    if network[next_y][next_x] != ' ':
        x = next_x
        y = next_y
        continue


print('Letters:', letters)
