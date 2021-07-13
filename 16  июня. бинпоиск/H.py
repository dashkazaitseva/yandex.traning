n, k = list(map(int, input().split()))
a = []
for i in range(n):
    a.append(int(input()))


l = 0
r = max(a) + 1
while (r - l > 1):
    m = (r + l) // 2
    s = sum([el // m for el in a])
    if (s >= k):
        l = m
    else:
        r = m

print(l)
