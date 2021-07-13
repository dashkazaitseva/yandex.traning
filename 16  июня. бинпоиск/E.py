a = int(input())
b = int(input())
c = int(input())
l = -1
r = a + b + c + 1

while (r - l > 1):
    m = (l + r) // 2

    if (2*a + 3*b + 4*c + 5*m < 3.5 *(a+b+c+m)):
        l = m
    else:
        r = m

print(r)
