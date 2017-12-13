import sys

nodes = {}
for row in sys.stdin.read().strip().split('\n'):
    name = row.split(' ')[0]
    weight = int(row.split(' ')[1].strip('(').strip(')'))
    childs = []
    if ' -> ' in row:
        childs = [child.strip() for child in row.split('>')[1].split(',')]
#    print(name, weight, childs)
    nodes[name] = {'weight': weight, 'childs': childs}

#print(nodes)


def isChild(name, nodes):
    for node in nodes:
        if name in nodes[node]['childs']:
            return True
    return False


for node in nodes:
#    print(node)
    if not isChild(node, nodes):
        print('Root:', node)
        break

