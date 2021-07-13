n = int(input())
a = list(map(int, input().split()))
max_el = a[0]
for i in range(1, n):
    if (a[i] > max_el):
        max_el = a[i]

was_max_el = False
best_score = 0
for i in range(n - 1):
    if (a[i] == max_el and was_max_el == False):
        was_max_el = True
    elif (was_max_el and a[i] % 10 == 5 and a[i] > best_score and a[i + 1] < a[i]):
        best_score = a[i]

#print(best_score)
if (best_score == 0):
    print(0)
else:
    ans = 0
    for i in range(n):
        if (a[i]> best_score):
            ans += 1

    print(ans + 1)
