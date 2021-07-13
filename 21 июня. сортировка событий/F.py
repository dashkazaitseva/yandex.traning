n = int(input())
a = []
s = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
for i in range(1, n + 1):
    l = list(map(int, input().split()))
    l[2] += 18
    sta = l[2] * 270 + s[l[1]] + l[0]
    sto = l[5] * 270 + s[l[4]] + l[3] - 1
    if (sta <= sto):
        a.append()
