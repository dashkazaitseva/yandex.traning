import itertools

a, b, c, d = list(map(int, input().split()))
a = [a, b]
c = [c, d]
a.sort()
c.sort()
tes = []
for el1 in itertools.permutations(a):
    for el2 in itertools.permutations(c):
        tes.append([max(el1[0], el2[0]), el1[1] + el2[1]])
        tes.append([el1[0] + el2[0], max(el1[1], el2[1])])

tes.sort(key = lambda el : el[0] * el[1])
print(*tes[0])
    
