import sys

highest_value = 0
registry = {}
for instruction in sys.stdin.read().strip().split('\n'):
    instruction = instruction.split(' ')
    reg = instruction[0]
    op = instruction[1]
    value = int(instruction[2])
    statement = instruction[3]
    comp_reg = instruction[4]
    comp_operator = instruction[5]
    comp_value = int(instruction[6])

    print('Before:', registry)
    print('Executing:', reg, op, value, statement, comp_reg, comp_operator, comp_value)
    if reg not in registry:
        registry[reg] = 0
    if comp_reg not in registry:
        registry[comp_reg] = 0

    if op == 'inc':
        diff = value
    elif op == 'dec':
        diff = -1 * value
    else:
        raise Exception('Unknown operator "%s"' % op)
    if statement != 'if':
        raise Exception('Unknown statement "%s"' % statement)

    execute = False
    if comp_operator == '==' and registry[comp_reg] == comp_value:execute = True
    elif comp_operator == '>'  and registry[comp_reg] >  comp_value: execute = True
    elif comp_operator == '>=' and registry[comp_reg] >= comp_value: execute = True
    elif comp_operator == '<'  and registry[comp_reg] <  comp_value: execute = True
    elif comp_operator == '<=' and registry[comp_reg] <=  comp_value: execute = True
    elif comp_operator == '!=' and registry[comp_reg] != comp_value: execute = True

    if execute:
        print('Updating reg...')
        registry[reg] += diff
        if registry[reg] > highest_value:
            highest_value = registry[reg]

    print('After:', registry)

print('Registry:', registry)
print('Largest value in registry currently:', max(registry.values()))
print('Largest value ever seen in registry :', highest_value)
