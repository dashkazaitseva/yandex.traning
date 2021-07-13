n, r, c = list(map(int, input().split()))
a = [int(input()) for _ in range(n)]
a.sort()

l = 0
r = a[-1] + 1
while (r - l > 1):
    m = (l + r) // 2
    if (check(m)):
        l = m
    else:
        r = m

print(l)
