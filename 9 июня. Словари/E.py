n = int(input())
d = dict()
for _ in range(n):
    a = list(map(int, input().split()))
    if (a[0] in d):
        d[a[0]] = max(d[a[0]], a[1])
    else:
        d[a[0]] = a[1]

print(sum([d[el] for el in d]))
