a = list(map(int, input().split()))
t = True
for i in range(1, len(a)):
    if (a[i - 1] >= a[i]):
        t = False

if (t):
    print("YES")
else:
    print("NO")
