n = int(input())
a = list(map(int, input().split()))
b = int(input())
ans = a[0]
for i in range(1, len(a)):
    if (abs(ans - b) > abs(a[i] - b)):
        ans = a[i]

print(ans)
