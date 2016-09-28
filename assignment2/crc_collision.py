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
        print s

    return ''.join(s)

def find_collision(start, crc):
    print 'starting at:', start
    found = 0
    y = start
    while found == 0:
        y_crc = CRC32().calculate(y)
        if y_crc == crc:
            print 'y:', y, 'CRC(y)', format(y_crc, '#04X')
            found = 1
            ts = time.time()
            st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            print st
        y = get_next(y)

ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
print st

x = 'plumless'
x_crc = CRC32().calculate(x)

print 'x:', x, 'CRC(x)', format(x_crc, '#04X')

find_collision('0', x_crc)
