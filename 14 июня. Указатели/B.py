n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

i = 0
j = 0
cur_s = 0
ans = 0
while (j < n):
    if (cur_s < k):
        cur_s += a[j]
        j += 1
    if (cur_s > k):
        cur_s -= a[i]
        i += 1
    if (cur_s == k):
        ans += 1
        if (j < n):
            cur_s += a[j]
            j += 1

while (i < n):
    cur_s -= a[i]
    if (cur_s == k):
        ans += 1
        cur_s -= a[i]
    i += 1

print(ans)
