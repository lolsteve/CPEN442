import sys, time, datetime
from Crypto.Hash import SHA

def main(input):
    salt = input[:2]
    hash = input[2:]
    print 'Salt:', salt
    print 'Hash', hash
    ts = time.time()
    for i in range(0,10000):
        pin = str(i).zfill(4)
        h = SHA.new()
        h.update(salt+pin)
        if h.hexdigest().upper() == hash:
            te = time.time()
            print 'Hash matched'
            print 'PIN:', pin
            print 'Time Elapsed:', te-ts
            return

if __name__ == '__main__':
    main(sys.argv[1])
