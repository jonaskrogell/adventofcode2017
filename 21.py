import sys
import math

rules = {}
for row in sys.stdin.read().split('\n'):
    if len(row.strip()) == 0:
        continue
    row = row.split(' ')
    key = row[0]
    data = row[2].split('/')
    rules[key] = []
    for r in data:
        items = []
        for value in r:
            items.append(value)
        rules[key].append(items)
print(rules)


def printMatrix(matrix):
    print('Matrix:')
    for row in matrix:
        print(''.join(row))


def applyRules(data, rotations = 3):
    key_items = []
    for row in data:
        key_items.append(''.join(row))
    key = '/'.join(key_items)
#    print(key)
    if key in rules:
#        print('Found in rules', rules[key])
        return rules[key]
    elif rotations >= 0:
#        print('Rotate', data)
        new_data = []
        for x in zip(*data[::-1]):
            new_data.append(list(x))
#        print('Rotated data', new_data)
        return applyRules(new_data, rotations - 1)
    else:
#        print('Flip', data)
        for row in data:
            row.reverse()
#        print('Flipped data', data)
        return applyRules(data)


matrix = ['.#.', '..#', '###']
# matrix = [['.', '#', '.'], ['.', '.', '#'], ['#', '#', '#']]

for x in range(18):
#    print(matrix)
    if (len(matrix) % 2) == 0:
#        print('Devide into 2x2')
        cut_size = 2
    elif (len(matrix) % 3) == 0:
#        print('Devide into 3x3')
        cut_size = 3
    else:
        raise Exception('Unknown size on matrix', len(matrix))

    new_blocks = []

    steps = int(len(matrix) / cut_size)
    for part_y in range(steps):
        for part_x in range(steps):
            data = []
            for cut_step in range(cut_size):
                data.append(matrix[part_y * cut_size + cut_step][part_x * cut_size:part_x * cut_size + cut_size])
            new_blocks.append(applyRules(data))

#    print('New blocks', len(new_blocks), new_blocks)

    block_size = len(new_blocks[0])
    new_size = int(math.sqrt(len(new_blocks))) * block_size
    new_matrix = [[None] * new_size for x in range(new_size)]
    x = 0
    y = 0
    for block in new_blocks:
        y_local = 0
        for row in block:
            x_local = 0
            for item in row:
                new_matrix[y + y_local][x + x_local] = item
                x_local += 1
            y_local += 1
        x = (x + block_size) % new_size
        if x == 0:
            y += block_size

    matrix = new_matrix

#    printMatrix(matrix)


printMatrix(matrix)

count = 0
for row in matrix:
    for item in row:
        if item == '#':
            count += 1
print('Pixels on:', count)
