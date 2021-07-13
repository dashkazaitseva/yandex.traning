n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

a.sort()
a = [el[1] for el in a]


ans_straight = [0]
for i in range(1, n):
    cur = 0
    if (a[i] > a[i - 1]):
        cur = a[i] - a[i - 1]
    ans_straight.append(ans_straight[-1] + cur)

ans_back = [0]
a = a[::-1]
for i in range(1, n):
    cur = 0
    if (a[i] > a[i - 1]):
        cur = a[i] - a[i - 1]
    ans_back.append(ans_back[-1] + cur)
ans_back = ans_back[::-1]
m = int(input())

for i in range(m):
    a1, a2 = list(map(int, input().split()))
    if (a1 <= a2):
        print(ans_straight[a2 - 1] - ans_straight[a1 - 1])
    else:
        print(ans_back[a2 - 1] - ans_back[a1 - 1])
    
