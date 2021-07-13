n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    cur_a = a.copy()
    cur_a += cur_a[:i][::-1]
    if (cur_a == cur_a[::-1]):
        print(i)
        print(*cur_a[:i][::-1])
        break
