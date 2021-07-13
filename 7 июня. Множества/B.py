f1 = open('input.txt', 'r')
f2 = open('output.txt', 'w')

a = set(map(int, f1.readline().split()))
b = set(map(int, f1.readline().split()))
f2.write(" ".join(list(map(str, sorted(list(a.intersection(b)))))))

f1.close()
f2.close()
