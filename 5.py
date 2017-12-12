import sys


stack = []
for instruction in sys.stdin.read().strip().split('\n'):
    stack.append(int(instruction))

pos = 0
counter = 0
while True:
    if pos < 0 or pos >= len(stack):
        break
    value = stack[pos]
    stack[pos] += 1
    counter += 1
    pos += value

print('Jumps:', counter)
