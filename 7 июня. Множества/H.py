n = int(input())
s1 = set()
s2 = set()
m = int(input())
s_cur = set()
for i in range(m):
    s_cur.add(input())
s1 = s_cur.copy()
s2 = s_cur.copy()
for _ in range(n - 1):
    m = int(input())
    s_cur = set()
    for i in range(m):
        s_cur.add(input())
    s1.update(s_cur)
    s2.intersection_update(s_cur)



print(len(s2))
for el in s2:
    print(el)
print(len(s1))
for el in s1:
    print(el)
