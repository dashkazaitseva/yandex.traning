n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
for i in range(k):
    l = 0
    r = n
    while (r - l > 1):
        m = (l + r) // 2
        if a[m] <= b[i]:
            l = m
        else:
            r = m

    if (a[l] == b[i]):
        print('YES')
    else:
        print('NO')
