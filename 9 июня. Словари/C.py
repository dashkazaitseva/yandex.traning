from collections import Counter
import sys

line = []

for l in sys.stdin:
    line += l.split()

line.sort()

c = Counter(line)
print(c.most_common(1)[0][0])
