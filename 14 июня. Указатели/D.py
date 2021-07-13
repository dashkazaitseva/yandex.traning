n, r = list(map(int, input().split()))
d = list(map(int, input().split()))
d.sort()

i = 0
j = 1
ans = 0

while (j < n and i < n - 1):
    if d[j] - d[i] <= r:
        j += 1
    else:
        ans += n - j
        i += 1

print(ans)
