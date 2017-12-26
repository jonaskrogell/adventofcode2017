#!env python3
import sys


def buildBridges(pin, components, path=[]):
    # print('buildBridges', pin, path, 'remain components:', components)
    longer_bridge = False
    paths = []
    for c in components:
        if pin in c:
            if pin == c[0]:
                next_pin = c[1]
            else:
                next_pin = c[0]
            new_components = components[:]
            new_components.remove((c[0], c[1]))
            paths += buildBridges(next_pin, new_components, path + [c])
            longer_bridge = True
    if not longer_bridge:
        paths += [path]
    return paths


def scorePath(path):
    score = 0
    for c in path:
        score += c[0] + c[1]
    return score


components = []

for row in sys.stdin.read().split('\n'):
    if len(row.strip()) == 0:
        continue
    s1, s2 = row.split('/')
    components.append((int(s1), int(s2)))

# print(components)

max_score = 0
paths = buildBridges(0, components)
for path in paths:
    score = scorePath(path)
    if score > max_score:
        max_score = score
#    print(path, score)
print('Paths found:', len(paths))
print('Max score:', max_score)
