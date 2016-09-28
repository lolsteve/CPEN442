from PyCRC.CRC32 import CRC32
import sys, time, datetime

alpha_numeric = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def get_next(input):
    s = list(input)
    i = len(s)-1
    carry = True
    while i>=0 and carry:
        index = alpha_numeric.index(s[i])
        index += 1
        if index >= 62:
            index = 0
        else:
            carry = False

        s[i] = alpha_numeric[index]
        i -= 1

    if carry:
        s.append('0')

    return ''.join(s)

def find_collision(start):
    print 'starting at:', start
    found = 0
    attempts = 0
    y = start
    while found == 0:
        y_crc = CRC32().calculate(y)
        #print y, format(y_crc, '#04X')
        if hashes.has_key(y_crc):
            print 'found collision', hashes.get(y_crc), y, format(y_crc, '#04X')
            found = 1
            ts = time.time()
            st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            print st
        else:
            hashes[y_crc] = y
        y = get_next(y)
        attempts += 1
        if attempts % 10000000 == 0:
            print 'attempts:', attempts

ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
print st

hashes = {}

find_collision('0')
