import math

input = '192,69,168,160,78,1,166,28,0,83,198,2,254,255,41,12'
#input = '3,4,1,5'
#input = 'AoC 2017'

ending = [17, 31, 73, 47, 23]

llist = []
for x in range(256):
    llist.append(x)


def swap(llist, pos1, pos2):
    tmp = llist[pos1]
    llist[pos1] = llist[pos2]
    llist[pos2] = tmp


def reverse(llist, pos, length):
    start = pos % len(llist)
    end = (pos + length - 1) % len(llist)
    for x in range(math.ceil(length / 2)):
        swap(llist, start, end)
        start = (start + 1) % len(llist)
        end = (end - 1) % len(llist)


input_values = []
for i in input:
    input_values.append(ord(i))
input_values += ending
print(input_values)

current_pos = 0
skip_size = 0
for x in range(64):
    for i in input_values:
        reverse(llist, current_pos, i)
        current_pos = (current_pos + i + skip_size) % len(llist)
        skip_size += 1

output = ''
pos = 0
for x in range(16):
    char = 0
    for y in range(16):
        char = char ^ llist[pos]
        pos += 1
    output += '%02x' % char
    
print(output)
