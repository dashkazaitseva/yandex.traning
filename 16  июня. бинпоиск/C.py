
w, h, n = list(map(int, input().split()))

l = 0
r = 10**27 + 1

while (r - l > 1):
    m = (l + r) // 2
    cur_number = (m // w) * (m // h)
    if (cur_number < n):
        l = m
    else:
        r = m

print(r)
 
