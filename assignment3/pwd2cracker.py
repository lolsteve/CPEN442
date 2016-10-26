# Use Hashcat instead
# hashcat -m 100 -a 3 <HASH> "<SALT>?a?a?a?a?a?a"

import sys, time, datetime
from Crypto.Hash import SHA

SYMBOLS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-='

def get_next(input):
    s = list(input)
    i = len(s)-1
    carry = True
    while i>=0 and carry:
        index = SYMBOLS.index(s[i])
        index += 1
        if index >= len(SYMBOLS):
            index = 0
        else:
            carry = False

        s[i] = SYMBOLS[index]
        i -= 1

    if carry:
        print 'Looping passwords'

    return ''.join(s)

def main(input):
    salt = input[:2]
    hash = input[2:]
    print 'Salt:', salt
    print 'Hash', hash
    ts = time.time()
    password = 'aaaaaa'
    attempt = 0
    while True:
        if attempt % 1000000 == 0:
            print attempt, password
        h = SHA.new()
        h.update(salt+password)
        if h.hexdigest().upper() == hash:
            te = time.time()
            print 'Hash matched'
            print 'Password:', password
            print 'Time Elapsed:', te-ts
            return
        password = get_next(password)
        attempt += 1

if __name__ == '__main__':
    main(sys.argv[1])
