from collections import Counter

n = int(input())
fs = set()
a = []
for _ in range(n):
    x, y = list(map(int, input().split()))
    if (x < 0 or y < 0):
        continue
    fs.add((x, y))
fs = Counter([el[0] + el[1] for el in list(fs)])

print(fs[n - 1])

