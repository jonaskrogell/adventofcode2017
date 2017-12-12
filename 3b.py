def getSum(matrix, x, y):
    s = 0
    cords = [(x + 1, y), (x + 1, y + 1), (x + 1, y - 1), (x - 1, y), (x - 1, y + 1), (x - 1, y - 1), (x, y + 1), (x, y - 1)]
    for cord in cords:
        if cord in matrix:
            s += matrix[cord]
    return s


def find(target):
    matrix = {}
    matrix[0, 0] = 1
    if target == 1:
        return 0, 0, 1
    x = 0
    y = 0
    counter = 1
    step_x = 1
    dir_x = 1
    step_y = 1
    dir_y = 1

    while True:
        for a in range(step_x):
            x += dir_x
            counter = getSum(matrix, x, y)
            matrix[x, y] = counter
            if counter > target:
                return x, y, counter
        for a in range(step_y):
            y += dir_y
            counter = getSum(matrix, x, y)
            matrix[x, y] = counter
            if counter > target:
                return x, y, counter
        step_x += 1
        step_y += 1
        dir_x = dir_x * -1
        dir_y = dir_y * -1


for target in [1, 12, 23, 1024, 312051]:
    x, y, counter = find(target)
    print('Target, x, y, distance, counter:', target, x, y, abs(x) + abs(y), counter)
