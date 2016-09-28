length = int(raw_input('length of string: '))
cipher = raw_input('input cipher text: ')

counts = {}

for i in range(length,len(cipher)):
    triple = cipher[i-length:i]
    if triple not in counts:
        counts[triple] = 0
    counts[triple] += 1

for key, value in counts.iteritems():
    if value != 1:
        print key, ':', value
