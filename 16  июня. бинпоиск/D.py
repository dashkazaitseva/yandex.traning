def get_ans(n, a, b, w, h):
    l = 0
    r = 10**30

    while (r - l > 1):
        m = (l + r) // 2
        cur_num = (w // (a + 2*m)) * (h // (b + 2*m))
        if (cur_num >= n):
            l = m
        else:
            r = m


    return(l)
n, a, b, w, h = list(map(int, input().split()))
ans = [get_ans(n, a, b, w, h), get_ans(n, b, a, w, h)]
ans.sort()
print(ans[-1])
