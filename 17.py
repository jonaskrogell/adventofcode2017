
jump = 394

lock = [0]

step = 1
pos = 0
while step <= 2017:
    print(step, pos, lock)
    pos = ((pos + jump) % len(lock)) + 1
    lock.insert(pos, step)
    step += 1

print(lock)
print(lock[pos+1])
