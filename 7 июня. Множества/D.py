import sys

s = set()

for line in sys.stdin:
    s.update(line.split())

print(len(s))
