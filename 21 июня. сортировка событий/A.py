n, m = list(map(int, input().split()))
a = []
for _ in range(m):
    a.append(list(map(int, input().split())))
a.sort()

ans = a[0][0]
cur = a[0][1]
for i in range(1, m):
    if (a[i][0] <= cur):
        ans += 0
    else:
        ans += a[i][0] - cur - 1
    cur = max(cur, a[i][1])

ans += n - 1 - cur
print(ans)
