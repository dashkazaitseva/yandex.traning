a = [0, 0, 0]
a[0] = int(input())
a[1] = int(input())
a[2] = int(input())
a.sort()

if (a[2] < a[0] + a[1]):
    print("YES")
else:
    print("NO")
