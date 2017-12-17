
jump = 394

lock_length = 1

last_nr1 = None

step = 1
pos = 0
while step <= 50000000:
    if step % 10000000 == 0:
        print(step, pos)
    pos = ((pos + jump) % lock_length) + 1
    if pos == 1:
        last_nr1 = step
    lock_length += 1
    step += 1

print('Nr 1:', last_nr1)
