import sys


def process(stream, level):
    groups = 0
    score = 0

    pos = 0
    while pos < len(stream):
        if stream[pos] == '{':
            found_groups, steps, found_score = process(stream[pos + 1:], level + 1)
            score += level + found_score
            groups += 1 + found_groups
            pos += steps
        elif stream[pos] == '}':
            return groups, pos + 1, score
        elif stream[pos] == '<':
            garbage = True
            while garbage:
                pos += 1
                if stream[pos] == '!':
                    pos += 1
                elif stream[pos] == '>':
                    garbage = False
        pos += 1
    return groups, pos, score


for row in sys.stdin.read().strip().split('\n'):
    print(row)
    data = process(row, 1)
    print('Groups:', data[0], 'Score:', data[2])
