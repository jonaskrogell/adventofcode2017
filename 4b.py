import sys


def isValid(checkword, words):
    check = list(checkword)
    check.sort()
    for word in words:
        word = list(word)
        word.sort()
        if check == word:
            return False
    return True


valid = 0
for passphrase in sys.stdin.read().strip().split('\n'):
    words = set()
    for password in passphrase.split(' '):
        if isValid(password, words):
            words.add(password)
        else:
            break
    else:
        valid += 1
print(valid)
