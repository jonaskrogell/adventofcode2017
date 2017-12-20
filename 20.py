import sys
import re

particles = []

for row in sys.stdin.read().split('\n'):
    print(row)
    if len(row.strip()) == 0:
        continue
    result = re.match(r'p=<(-?\d+),(-?\d+),(-?\d+)>,v=<(-?\d+),(-?\d+),(-?\d+)>,a=<(-?\d+),(-?\d+),(-?\d+)>', row.replace(' ', ''))
    p = [int(result.group(1)), int(result.group(2)), int(result.group(3))]
    v = [int(result.group(4)), int(result.group(5)), int(result.group(6))]
    a = [int(result.group(7)), int(result.group(8)), int(result.group(9))]
    print(p, v, a)
    particles.append({'p': p, 'v': v, 'a': a})

print(particles)


def updateParticle(particle):
    particle['v'][0] += particle['a'][0]
    particle['v'][1] += particle['a'][1]
    particle['v'][2] += particle['a'][2]
    particle['p'][0] += particle['v'][0]
    particle['p'][1] += particle['v'][1]
    particle['p'][2] += particle['v'][2]


def getDistances(particles):
    distances = []
    for particle in particles:
        distances.append(abs(particle['p'][0]) + abs(particle['p'][1]) + abs(particle['p'][2]))
    return distances


for x in range(1000):
    for particle in particles:
        updateParticle(particle)

distances = getDistances(particles)
print(distances.index(min(distances)))
