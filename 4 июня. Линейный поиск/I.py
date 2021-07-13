n, m, k = list(map(int, input().split()))
a = []
for i in range(n + 2):
    temp = []
    for j in range(m + 2):
        temp.append(0)
    a.append(temp)

for i in range(k):
    x, y = list(map(int, input().split()))
    a[x][y] = 9

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if (a[i][j] == 9):
            if (a[i - 1][j - 1] != 9):
                a[i - 1][j - 1] += 1
            if (a[i - 1][j] != 9):
                a[i - 1][j] += 1
            if (a[i - 1][j + 1] != 9):
                a[i - 1][j + 1] += 1
            if (a[i][j - 1] != 9):
                a[i][j - 1] += 1
            if (a[i][j + 1] != 9):
                a[i][j + 1] += 1
            if (a[i + 1][j - 1] != 9):
                a[i + 1][j - 1] += 1
            if (a[i + 1][j] != 9):
                a[i + 1][j] += 1
            if (a[i + 1][j + 1] != 9):
                a[i + 1][j + 1] += 1


for i in range(1, n + 1):
    for j in range(1, m + 1):
        if (a[i][j] == 9):
            print('*', end = ' ')
        else:
            print(a[i][j], end = ' ')
    print()
