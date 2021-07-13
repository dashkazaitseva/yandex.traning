n = int(input())
a0 = float(input())
ans = [30, 4000]
for _ in range(n - 1):
    s = input().split()
    a1, s = float(s[0]), s[1]
    if (a0 >= a1):
        if s == 'closer':
            ans[1] = min(ans[1], (a0 + a1) / 2)
        else:
            ans[0] = max(ans[0], (a0 + a1) / 2)
    else: #a0 <= a1
        if s == 'closer':
            ans[0] = max(ans[0], (a0 + a1) / 2)
        else:
            ans[1] = min(ans[1], (a0 + a1) / 2)
    a0 = a1
print(*ans)
