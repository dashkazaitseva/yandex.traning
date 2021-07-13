n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

i = 0
j = 0
best_ans = [a[0], b[0]]

while (i < n and j < m):
    if (abs(best_ans[0] - best_ans[1]) > abs(a[i] - b[j])):
        best_ans = [a[i], b[j]]
    if (a[i] < b[j]):
        i += 1
    else:
        j += 1

while (i < n):
    if (abs(best_ans[0] - best_ans[1]) > abs(a[i] - b[-1])):
        best_ans = [a[i], b[-1]]
    i += 1

while (j < m):
    if (abs(best_ans[0] - best_ans[1]) > abs(a[-1] - b[j])):
        best_ans = [a[-1], b[j]]
    j += 1

print(*best_ans)
