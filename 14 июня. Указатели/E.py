n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

used = []
for i in range(k + 1):
    used.append(0)


i = 0
j = 0
su = 0
best_ans = [1, n]

while (j < n):
    if (su < k):
        used[a[j]] += 1
        if used[a[j]] == 1:
            su += 1
        j += 1
    while (su == k):
        if (j - i - 1 < best_ans[1] - best_ans[0]):
            best_ans = [i + 1, j]
        used[a[i]] -= 1
        if used[a[i]] == 0:
            su -= 1
        i += 1

while (i < n ):

    if (n - i - 1 < best_ans[1] - best_ans[0] and su == k):
        best_ans = [i + 1, n]
    used[a[i]] -= 1
    if used[a[i]] == 0:
       su -= 1
    i += 1
    
print(*best_ans)
    
