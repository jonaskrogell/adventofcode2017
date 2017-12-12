import sys

data = sys.stdin.read().strip()

sum = 0
for row in data.split('\n'):
    min = None
    max = None
    for value in row.split():
        value = int(value)
        if min is None or value < min:
            min = value
        if max is None or value > max:
            max = value
    sum += max - min
print('Sum:', sum)
