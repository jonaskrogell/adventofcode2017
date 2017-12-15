import sys

firewall = {}


def tickFirewall():
    for layer in firewall:
        firewall[layer]['state'] += firewall[layer]['direction']
        if firewall[layer]['state'] == 0:
            firewall[layer]['direction'] = 1
        elif firewall[layer]['state'] == firewall[layer]['length'] - 1:
            firewall[layer]['direction'] = -1


for row in sys.stdin.read().strip().split('\n'):
    parts = row.split(':')
    pos = int(parts[0])
    length = int(parts[1].strip())
    firewall[pos] = {}
    firewall[pos]['length'] = length
    firewall[pos]['state'] = 0
    firewall[pos]['direction'] = 1

for x in range(max(firewall) + 1):
    print(x, firewall)
    tickFirewall()
    print(x, firewall)
