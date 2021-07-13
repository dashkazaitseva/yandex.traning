def manh(el, x, y):
    return abs(el[0] - x) + abs(el[1] - y)

t, d, n = list(map(int, (input().split())))
x1, x2, y1, y2 = 0, 0, 0, 0

for _ in range(n):
    x, y = list(map(int, input().split()))
    x2 = min(x2 + t, x + y + d)
    x1 = max(x1 - t, x + y - d)
    y2 = min(y2 + t, x - y + d)
    y1 = max(y1 - t, x - y - d)

ans = 0
s = set()
for i in range(x1, x2 + 1):
    for j in range(y1, y2 + 1):
        if (i + j) % 2 == 0:
            ans += 1
            s.add(((i + j)//2, (i - j)//2))

print(ans)
for el in s:
    print (*el)
