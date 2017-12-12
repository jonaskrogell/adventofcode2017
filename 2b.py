import sys


def doDivision(values):
    c = 1
    for value1 in values:
        for value2 in values[c:]:
            if value1 % value2 == 0:
                return (value1 / value2)
            if value2 % value1 == 0:
                return (value2 / value1)
        c += 1


data = sys.stdin.read().strip()
sum = 0
for row in data.split('\n'):
    values = []
    for value in row.split():
        values.append(int(value))
    sum += doDivision(values)
print('Sum:', sum)
