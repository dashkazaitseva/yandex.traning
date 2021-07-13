n = int(input())
a = sorted(list(map(int, input().split())))
d = dict()
m = int(input())
for i in range(m):
    p, c = list(map(int, input().split()))
    if p in d:
        d[p] = min(d[p], c)
    else:
        d[p] = c

d = [[el, d[el]] for el in d]
d = sorted(d)
for i in range(len(d) - 2, -1, -1):
    d[i][1] = min(d[i][1], d[i + 1][1])

ans = 0
i = 0
j = 0
while (i < n):
    if (a[i] > d[j][0]):
        j += 1
    if (a[i] <= d[j][0]):
        ans += d[j][1]
        i += 1

print(ans)
