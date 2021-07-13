n, m = list(map(int, input().split()))
a = []
for _ in range(n):
    c = sorted(list(map(int, input().split())))
    a.append([c[0], -2])
    a.append([c[1], max(n, m) + 1])
p = list(map(int, input().split()))
p = [[p[i], i] for i in range(m)]
a += p
a.sort()

ans = [0 for _ in range(m)]
cnt = 0
for el in a:
    if el[1] == -2:
        cnt +=1
    elif el[1] == max(n, m) + 1:
        cnt -= 1
    else:
        ans[el[1]] = cnt

print(*ans)
