n = int(input())
d = dict()
l = list(map(int, input().split()))
for i in range(len(l)):
    d[i + 1] = l[i]

m = int(input())
l = list(map(int, input().split()))

for el in l:
    d[el] -= 1


for el in d:
    if d[el] < 0:
        print('YES')
    else:
        print('NO')
