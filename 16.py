import sys
import math

programs = []
for x in range(16):
    programs.append(chr(64 + 32 + 1 + x))


def swap(programs, p1, p2):
    tmp = programs[p1]
    programs[p1] = programs[p2]
    programs[p2] = tmp


moves = []
for move in sys.stdin.read().strip().split(','):
    moves.append(move)

start = ''.join(programs)
states = {}

counter = 0
loop = 1000000000
while counter < loop:
    counter += 1
    for move in moves:
        if move[0] == 's':
            size = -1 * int(move[1:])
            programs = programs[size:] + programs[0:size]
        elif move[0] == 'x':
            x1, x2 = move[1:].split('/')
            swap(programs, int(x1), int(x2))
        elif move[0] == 'p':
            x1, x2 = move[1:].split('/')
            swap(programs, programs.index(x1), programs.index(x2))

    state = ''.join(programs)
    states[counter] = state
    if counter == 1:
        print('After first dance state:', state)
    if state == start:
        # cycle found
        print('Cycle found at', counter)
        counter += math.floor((loop - counter) / counter) * counter
        print(loop, 'State is', states[(loop - counter)])
        break
