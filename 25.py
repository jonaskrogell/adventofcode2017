#!env python3
import sys
import re

program = {}

diag_counter = None
begin_state = None
current_state = None
current_value = None
write_value = None
move_value = None
next_state = None

for row in sys.stdin.read().split('\n'):
    if len(row.strip()) == 0:
        continue
    diag_match = re.match(r'Perform a diagnostic checksum after (\d+) steps', row)
    if diag_match:
        diag_counter = int(diag_match.group(1))
    begin_match = re.match(r'Begin in state (.+).', row)
    if begin_match:
        begin_state = begin_match.group(1)
    state_match = re.match(r'In state (.+):', row)
    if state_match:
        current_state = state_match.group(1)
        program[current_state] = {}
    current_value_match = re.match(r'.*If the current value is (\d):', row)
    if current_value_match:
        current_value = int(current_value_match.group(1))
    op_match = re.match(r'.*- Write the value (\d).', row)
    if op_match:
        write_value = int(op_match.group(1))
    op_match = re.match(r'.*- Move one slot to the (.+).', row)
    if op_match:
        move_value = op_match.group(1)
    op_match = re.match(r'.*- Continue with state (.+).', row)
    if op_match:
        next_state = op_match.group(1)
        program[current_state][current_value] = {}
        program[current_state][current_value]['write'] = write_value
        program[current_state][current_value]['move'] = move_value
        program[current_state][current_value]['next'] = next_state


def renderTape(tape, pos):
    for x in range(min(tape) - 3, max(tape) + 3 + 1):
        if x in tape:
            if pos == x:
                print(x, tape[x], '<--')
            else:
                print(x, tape[x])
        else:
            print(x, '0 -')


print('Do diagnostics after steps:', diag_counter)
print('Begin state:', begin_state)
print(program)

tape = {}
pos = 0
state = begin_state
while diag_counter > 0:
    if pos not in tape:
        tape[pos] = 0
#    print('State:', state, 'Pos:', pos)
#    renderTape(tape, pos)
    if tape[pos] == 0:
        actions = program[state][0]
    else:
        actions = program[state][1]

    tape[pos] = actions['write']
    if actions['move'] == 'left':
        pos -= 1
    else:
        pos += 1
    state = actions['next']

    diag_counter -= 1
    if diag_counter % 100000:
        print('Steps left:', diag_counter)

print('Done')
renderTape(tape, pos)
count = 0
for value in tape.values():
    if value == 1:
        count += 1
print('Ones:', count)
