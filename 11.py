import sys


for row in sys.stdin.read().strip().split('\n'):
    pos = {'x': 0, 'y': 0, 'z': 0}
#    print(row)
    for op in row.split(','):
        if op == 'n':
            pos['x'] -= 1
            pos['y'] += 1
        elif op == 'nw':
            pos['x'] -= 1
            pos['z'] += 1
        elif op == 'ne':
            pos['y'] += 1
            pos['z'] -= 1
        elif op == 's':
            pos['x'] += 1
            pos['y'] -= 1
        elif op == 'sw':
            pos['y'] -= 1
            pos['z'] += 1
        elif op == 'se':
            pos['x'] += 1
            pos['z'] -= 1

    m = 0
    for key in pos:
        if abs(pos[key]) > m:
            m = abs(pos[key])
    print('Length:', m)
