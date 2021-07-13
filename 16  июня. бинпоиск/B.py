n, k = list(map(int, input().split()))
a = list(set(list(map(int, input().split()))))
b = list(map(int, input().split()))
a.sort()
a += [10000000000000000]
ans = [0 for i in range(k)]

b = [[b[i], i] for i in range(k)]
b.sort()


i, j = 0, 0
while (j < k):
    
    while (abs(b[j][0] - a[i]) > abs(b[j][0] - a[i + 1])):
        i += 1
    if (abs(b[j][0] - a[i]) <= abs(b[j][0] - a[i + 1])):
        ans[b[j][1]] = a[i]
    else:
        i += 1
        ans[b[j][1]] = a[i]
    j += 1

for el in ans:
    print(el)
