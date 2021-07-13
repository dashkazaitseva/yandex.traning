def get_min(a, t):
    return ((a + 1) * (t - 1) + 1)
def get_max(a, t):
    return ((a + 1) * (t) + a)

f1 = open('INPUT.TXT', 'r')
f2 = open('OUTPUT.TXT', 'w')

a = int(f1.readline())
b = int(f1.readline())
n = int(f1.readline())
m = int(f1.readline())

t1 = [get_min(a, n), get_max(a, n)]
t2 = [get_min(b, m), get_max(b, m)]

ans = []

ans = [max(t1[0], t2[0]), min(t1[1], t2[1])]

if (ans[0] > ans[1]):
    ans = [-1]
ans = " ".join(list(map(str, ans)))

    

f2.write(ans)
f1.close()
f2.close()
