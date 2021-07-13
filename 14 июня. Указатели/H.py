n, k = list(map(int, input().split()))
s = input()
a = []
for i in range(26):
    a.append(0)

i = 0
j = 0
able = 1
ans = [0, 0]

while (j < n):
    if (able == 1):
        if (j - i > ans[1] - ans[0]):
            ans = [i, j]
        cur = ord(s[j]) - ord('a')

        a[cur] += 1
        if (a[cur] > k):
            able = 0
        j += 1
    if (able == 0):
        while (able == 0):
  
            cur = ord(s[i]) - ord('a')
            a[cur] -= 1
            if (a[ord(s[j - 1]) - ord('a')] <= k):
                able = 1
            i += 1

if (able == 1):
    if (j - i > ans[1] - ans[0]):
        ans = [i, j]

print( ans[1] - ans[0], ans[0] + 1)
