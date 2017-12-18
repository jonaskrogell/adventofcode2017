import sys

instructions = []
for row in sys.stdin.read().strip().split('\n'):
    instructions.append(row)


registry = {}
last_player = None
pos = 0
while pos >= 0 and pos < len(instructions):
    instruction = instructions[pos].split(' ')
    op = instruction[0]
    reg = instruction[1]
    if len(instruction) > 2:
        try:
            value = int(instruction[2])
        except ValueError:
            value = registry[instruction[2]]
    else:
        value = None

    print('Executing:', pos, op, reg)

    if reg not in registry:
        registry[reg] = 0

    if op == 'snd':
        print('Play:', registry[reg])
        last_player = registry[reg]
    elif op == 'set':
        registry[reg] = value
    elif op == 'add':
        registry[reg] += value
    elif op == 'mul':
        registry[reg] *= value
    elif op == 'mod':
        registry[reg] = registry[reg] % value
    elif op == 'rcv':
        if registry[reg] > 0:
            print('Recover:', last_player)
            break
    elif op == 'jgz':
        if registry[reg] > 0:
            pos += value - 1
    else:
        raise Exception('Unknown operator "%s"' % op)

    print('After:', registry)
    pos += 1


print('Finished with pos and reg:', pos, registry)
print('Last played:', last_player)
