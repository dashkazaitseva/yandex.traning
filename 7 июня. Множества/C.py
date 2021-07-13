n, m = list(map(int, input().split()))
a = []
b = []
for _ in range(n):
    a.append(int(input()))

for _ in range(m):
    b.append(int(input()))
a.sort()
b.sort()
a = set(a)
b = set(b)
    
print (len(a.intersection(b)))
print(" ".join(list(map(str, sorted(list(a.intersection(b)))))))
print(len(a.difference(b)))
print(" ".join(list(map(str, sorted(list(a.difference(b)))))))
print(len(b.difference(a)))
print(" ".join(list(map(str, sorted(list(b.difference(a)))))))

