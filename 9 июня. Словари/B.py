import sys

d = dict()
for line in sys.stdin:
    w = line.split()
    for word in w:
        if word in d:
            print(d[word], end = ' ')
            d[word] += 1
        else:
            print(0, end = ' ')
            d[word] = 1
