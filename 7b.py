import sys

nodes = {}
for row in sys.stdin.read().strip().split('\n'):
    name = row.split(' ')[0]
    weight = int(row.split(' ')[1].strip('(').strip(')'))
    childs = []
    if ' -> ' in row:
        childs = [child.strip() for child in row.split('>')[1].split(',')]
    nodes[name] = {'weight': weight, 'childs': childs}


def isChild(name, nodes):
    for node in nodes:
        if name in nodes[node]['childs']:
            return True
    return False


def getWeight(name, nodes):
    sum = nodes[name]['weight']
    for child in nodes[name]['childs']:
        sum += getWeight(child, nodes)
    return sum


for node in nodes:
    if not isChild(node, nodes):
        root = node
        break


def findBadChild(name, nodes):
    print('Diving into', name)
    child_weights = []
    weights = {}
    if len(nodes[name]['childs']) < 2:
        print('Bad child:', name, nodes[name])
        return True
    for child in nodes[name]['childs']:
        w = getWeight(child, nodes)
        child_weights.append((w, child))
        if w in weights:
            weights[w] += 1
        else:
            weights[w] = 1
    print(child_weights)
    print(weights)

    if len(weights) == 1:
        print('This level is balanced')
        return False
    for child in child_weights:
        if weights[child[0]] == 1:
            if not findBadChild(child[1], nodes):
                print('Bad child is:', child[1], 'with current weight', nodes[child[1]]['weight'])
                print(child_weights)
                for c2 in child_weights:
                    if c2[1] != child[1]:
                        print('Weight diffrence is', c2[0] - child[0])
                        print(child[1], 'should be', nodes[child[1]]['weight'] + (c2[0] - child[0]))
                        return True
                return True
    return True


print('Starting with root:', root)
findBadChild(root, nodes)
