import math


def reverse(llist, pos, length):
    start = pos % len(llist)
    end = (pos + length - 1) % len(llist)
    for x in range(math.ceil(length / 2)):
        tmp = llist[start]
        llist[start] = llist[end]
        llist[end] = tmp
        start = (start + 1) % len(llist)
        end = (end - 1) % len(llist)


def knotHash(input):
    input_values = []
    for i in input:
        input_values.append(ord(i))
    input_values += [17, 31, 73, 47, 23]

    llist = []
    for x in range(256):
        llist.append(x)

    current_pos = 0
    skip_size = 0
    for x in range(64):
        for i in input_values:
            reverse(llist, current_pos, i)
            current_pos = (current_pos + i + skip_size) % len(llist)
            skip_size += 1

    hex_output = ''
    bits_output = ''
    pos = 0
    for x in range(16):
        char = 0
        for y in range(16):
            char = char ^ llist[pos]
            pos += 1
        hex_output += format(char, 'x').zfill(2)
        bits_output += format(char, 'b').zfill(8)

    return hex_output, bits_output


my_input = 'vbqugkhl'
#my_input = 'flqrgnkx'

matrix = []

total_bits = 0
for x in range(128):
    input = my_input + '-' + str(x)
    knothashoutput, bits = knotHash(input)
    total_bits += bits.count('1')
    row = []
    for bit in bits:
        row.append(bit)
    matrix.append(row)
    print(input, knothashoutput)
print('Total bits:', total_bits)


def destroyTheMatrix(matrix, x, y):
    if x > 127 or y > 127 or x < 0 or y < 0:
        return 0
    if matrix[x][y] == '0':
        return 0
    matrix[x][y] = '0'
    destroyTheMatrix(matrix, x + 1, y)
    destroyTheMatrix(matrix, x - 1, y)
    destroyTheMatrix(matrix, x, y + 1)
    destroyTheMatrix(matrix, x, y - 1)
    return 1


groups = 0
for y in range(128):
    for x in range(128):
        groups += destroyTheMatrix(matrix, x, y)
print('Total groups:', groups)
