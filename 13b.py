import sys

firewall = {}


def tickLayer(layer, time):
    return time % max((2 * firewall[layer]['length'] - 2), 1)
#    firewall[layer]['state'] += firewall[layer]['direction']
#    if firewall[layer]['state'] == 0:
#        firewall[layer]['direction'] = 1
#    elif firewall[layer]['state'] == firewall[layer]['length'] - 1:
#        firewall[layer]['direction'] = -1


def tickFirewall(layer, time):
    if layer in firewall:
        tickLayer(layer, time)
#    for layer in firewall:
#        tickLayer(layer)


def resetFirewall():
    for layer in firewall:
        firewall[layer]['state'] = 0
        firewall[layer]['direction'] = 1


for row in sys.stdin.read().strip().split('\n'):
    parts = row.split(':')
    pos = int(parts[0])
    length = int(parts[1].strip())
    firewall[pos] = {}
    firewall[pos]['length'] = length
    firewall[pos]['state'] = 0
    firewall[pos]['direction'] = 1

delay = 0
max_caught_pos = 0
while True:
    time = delay
    pos = -1
    caught = False
    while pos < max(firewall):
        pos += 1
        if pos in firewall and tickLayer(pos, time) == 0:
            #print(pos, 'caught at length', firewall[pos]['length'])
            caught = True
            break
        time += 1
    if not caught:
        print('Not caught using delay: ', delay)
        break
    if pos >= max_caught_pos:
        max_caught_pos = pos
    #print('Delay:', delay, 'Caught at:', pos, 'Max caught:', max_caught_pos)
    delay += 1

