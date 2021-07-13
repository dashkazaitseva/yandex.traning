n, x, y = list(map(int, input().split()))

t0 = min(x, y)
n -= 1
l = -1
r = 10**10
while (r - l > 1):
    m = (l + r) // 2
    if (n <= (m // x) + (m // y)):
        r = m
    else:
        l = m

print(r + t0)
