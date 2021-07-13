
n = int(input())
a = []
for _ in range(n):
    b = list(map(int, input().split()))
    sta = b[0] * 60 + b[1]
    sto = b[2] * 60 + b[3]
    sto -= 1
    sto %= 1440
    if (sta < sto):
        a.append([sta % 1440, -1])
        a.append([(sto) % 1440, 1])
    elif (sta > sto):
        a.append([0, -1])
        a.append([(sto ) % 1440, 1])
        a.append([sta % 1440, -1])
        a.append([24*60 - 1, 1])
    else:
        n -= 1

a.sort()


cur = 1
ans = 0

for i in range(1, len(a)):
    if (a[i][1] == -1):
        cur += 1
    if (a[i][1] == 1):
        if (cur == n):
            ans += a[i][0] - a[i - 1][0] + 1
        cur -= 1
if (n == 0):
    print(str(24 * 60))
else:
    print(str(ans))
