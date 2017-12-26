h = 0
b_s = 93 * 100 + 100000
c = b_s + 17000

def isPrime(number):
    for x in range(2, int(number/2)+1):
        if number % x == 0:
            return False
    return True

for b in range(b_s, c + 1, 17):
    print(b)
    if not isPrime(b):
        print(b, 'prime')
        h = h + 1

print('finished, h:', h)
