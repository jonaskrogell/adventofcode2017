import sys
import re

particles = {}

id = 0
for row in sys.stdin.read().split('\n'):
    if len(row.strip()) == 0:
        continue
    result = re.match(r'p=<(-?\d+),(-?\d+),(-?\d+)>,v=<(-?\d+),(-?\d+),(-?\d+)>,a=<(-?\d+),(-?\d+),(-?\d+)>', row.replace(' ', ''))
    p = [int(result.group(1)), int(result.group(2)), int(result.group(3))]
    v = [int(result.group(4)), int(result.group(5)), int(result.group(6))]
    a = [int(result.group(7)), int(result.group(8)), int(result.group(9))]
#    print(p, v, a)
    particles[id] = {'p': p, 'v': v, 'a': a}
    id += 1

#print(particles)


def updateParticle(particle):
    for p in particles:
        particles[p]['v'][0] += particles[p]['a'][0]
        particles[p]['v'][1] += particles[p]['a'][1]
        particles[p]['v'][2] += particles[p]['a'][2]
        particles[p]['p'][0] += particles[p]['v'][0]
        particles[p]['p'][1] += particles[p]['v'][1]
        particles[p]['p'][2] += particles[p]['v'][2]


def getDistances(particles):
    distances = []
    for p in particles:
        distances.append(abs(particles[p]['p'][0]) + abs(particles[p]['p'][1]) + abs(particles[p]['p'][2]))
    return distances


def checkCollisions(particles):
    positions = {}
    for p in particles:
        pos = ','.join(str(particles[p]['p']))
        if pos not in positions:
            positions[pos] = []
        positions[pos].append(p)

    for pos in positions:
        if len(positions[pos]) > 1:
            for del_pos in positions[pos]:
                print('Removing', del_pos)
                del particles[del_pos]
    return


for x in range(1000):
    updateParticle(particles)
    checkCollisions(particles)
    distances = getDistances(particles)

print('(0,0,0) closest id:', distances.index(min(distances)), 'total particles:', len(particles))
