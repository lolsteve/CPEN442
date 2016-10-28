import sys, time, datetime
from Crypto.Hash import SHA

OFFSET = 0x0001e018
#OFFSET = 0x9

def main(filename):
    fh = open(filename, 'r+b')
    fh.seek(OFFSET)

    password = raw_input('Enter new password: ')
    h = SHA.new()
    h.update(password)

    print 'Password hashed:', h.hexdigest()

    fh.write(h.digest())
    fh.close()

    print 'Done'


if __name__ == '__main__':
    main(sys.argv[1])
