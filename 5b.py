import sys


stack = []
for instruction in sys.stdin.read().strip().split('\n'):
    stack.append(int(instruction))

pos = 0
counter = 0
while True:
#    print(stack, counter, pos)
    if pos < 0 or pos >= len(stack):
        break
    value = stack[pos]
    if stack[pos] >= 3:
        stack[pos] -= 1
    else:
        stack[pos] += 1
    counter += 1
    pos += value

print('Jumps:', counter)
