import sys


valid = 0
for passphrase in sys.stdin.read().strip().split('\n'):
    words = set()
    for password in passphrase.split(' '):
        if password not in words:
            words.add(password)
        else:
            break
    else:
        valid += 1
print(valid)
