n, d = list(map(int, input().split()))
a = list(map(int, input().split()))
a = sorted([[a[i], i] for i in range(n)])


ans = [0 for _ in range(n)]
an = -1
ans_max = 0
i = 0
j = 0
while (j < n):
    
    if (a[j][0] - a[i][0] > d):
      an = i
      i += 1


    if (j - i + 1 > ans_max):
        ans_max = j - i + 1
        ans[a[j][1]] = ans_max
    else:
        ans[a[j][1]] = ans[a[an][1]]
    
    j += 1

print(str(max(ans)))
print(" ".join(list(map(str, ans))))

