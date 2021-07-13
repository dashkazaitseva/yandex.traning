n = int(input())
k = int(input())
num = int(input())
l = 0
r = min(n, k) // 2 + 1
while (r - l > 1):
    m = (r + l) // 2
    if (((2*(n - 1) - 2 * (m - 1)) * m) + ((2 * (k - 1) - 2 * (m - 1)) * m)) <= num:
        l = m
    else:
        r = m

print(l)
