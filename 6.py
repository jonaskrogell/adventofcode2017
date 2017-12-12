#input = '0 2 7 0'
input = '2 8 8 5 4 2 3 1 5 5 1 2 15 13 5 14'

banks = []
for i in input.split(' '):
    banks.append(int(i))


def redistribute(banks):
    banks = list(banks)
    pos = 0
    for index, value in enumerate(banks):
        if value > banks[pos]:
            pos = index

    data = banks[pos]
    banks[pos] = 0
    while data > 0:
        pos = (pos + 1) % len(banks)
        banks[pos] += 1
        data -= 1
    return banks


counter = 0
history = []
while True:
    print(banks)
    history.append(banks)
    banks = redistribute(banks)
    counter += 1
    if banks in history:
        break
print('Counter:', counter)

print('Loop cycle:', counter - history.index(banks))
