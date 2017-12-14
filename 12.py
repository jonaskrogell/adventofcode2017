import sys

visited = set()
pipes = {}

for row in sys.stdin.read().strip().split('\n'):
    parts = row.split(' ', 2)
    pipe_start = int(parts[0])
    for pipe_dest in parts[2].split(','):
        pipe_dest = int(pipe_dest)
        if pipe_start not in pipes:
            pipes[pipe_start] = []
        if pipe_dest not in pipes[pipe_start]:
            pipes[pipe_start].append(pipe_dest)
        if pipe_dest not in pipes:
            pipes[pipe_dest] = []
        if pipe_start not in pipes[pipe_dest]:
            pipes[pipe_dest].append(pipe_start)


def tracePipes(start):
    visited.add(start)
    sum = 1
    for pipe in pipes[start]:
        if pipe not in visited:
            sum += tracePipes(pipe)
    return sum


groups = 0
for start_place in pipes:
    if start_place not in visited:
        sum = tracePipes(start_place)
        print('Group start:', start_place, 'Sum:', sum)
        groups += 1
print('Total groups:', groups)
