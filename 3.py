def find(target):
    if target == 1:
        return 0, 0
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
            counter += 1
            if counter == target:
                return x, y
        for a in range(step_y):
            y += dir_y
            counter += 1
            if counter == target:
                return x, y
        step_x += 1
        step_y += 1
        dir_x = dir_x * -1
        dir_y = dir_y * -1


for target in [1, 12, 23, 1024, 312051]:
    x, y = find(target)
    print('Target, x, y, distance:', target, x, y, abs(x) + abs(y))
