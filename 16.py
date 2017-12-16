import sys

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

states = {}

counter = 1
loop = 1000000000
while counter < loop:
    state = ''.join(programs)
    if counter < (loop - 1000) and state in states:
        counter += states[state]
        continue
    elif counter > 100 and state not in states:
        states[state] = counter

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
    counter += 1

print('State table:', len(states))
print(counter, ''.join(programs))
