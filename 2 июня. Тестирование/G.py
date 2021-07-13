n, k, m = list(map(int, (input().split())))
ans = 0
number_of_m = k // m
if (k < m):
    print(0)
else:    
    while (n >= k):
        cur_z = n // k
        n -= cur_z * m * number_of_m
        ans += cur_z * number_of_m
    print(ans)
