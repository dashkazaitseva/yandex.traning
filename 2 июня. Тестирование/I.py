a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
a = [a, b, c]
d = [d, e]
d.sort()
a.sort()
if (a[0] <= d[0] and a[1] <= d[1]):
    print("YES")
else:
    print("NO")
