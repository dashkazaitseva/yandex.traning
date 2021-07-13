import itertools

def get_needed(v):
    if (len(v) <= 6):
        return v
    sign = 1
    if (v[0] < 0):
        sign = -1
        for i in range(len(v)):
            v[i] *= -1

    min_el = [10000000000000, 100000000000, 100000000000]
    max_el = [0, 0, 0]
    for i in range(len(v)):
        min_el.append(v[i])
        min_el.sort()
        min_el = min_el[:3]
        max_el.append(v[i])
        max_el.sort()
        max_el = max_el[1:]
    min_el += max_el
    for i in range(6):
        min_el[i] *= sign
    return (min_el)

    
a = list(map(int, input().split()))
was_zero = 0
less_zero = []
greater_zero = []

for i in range(len(a)):
    if (a[i] == 0):
        was_zero += 1
    elif (a[i] > 0):
        greater_zero.append(a[i])
    else:
        less_zero.append(a[i])
            
ans = []
for i in range(min(3, was_zero)):
    ans.append(0)
ans += get_needed(less_zero)
ans += get_needed(greater_zero)


ans.sort()
ansishe = []
for el in itertools.permutations(ans, 3):
    ansishe.append(el)

ansishe.sort(key = lambda x: x[0] * x[1] * x[2])
print(*ansishe[-1])
