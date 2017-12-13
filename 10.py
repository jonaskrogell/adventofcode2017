import math

input = '192,69,168,160,78,1,166,28,0,83,198,2,254,255,41,12'
#input = '3,4,1,5'

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


current_pos = 0
skip_size = 0
for i in input.split(','):
    i = int(i)
    print('current_pos', current_pos, 'skip_size', skip_size, 'length', i)
    print('Start:', llist)
    reverse(llist, current_pos, i)
    print('After:', llist)
    current_pos = (current_pos + i + skip_size) % len(llist)
    skip_size += 1

print('Result:', llist[0] * llist[1])
