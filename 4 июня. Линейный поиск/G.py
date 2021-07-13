a = list(map(int, input().split()))
was_zero = False
max_el = [0, 0]
min_el = [0, 0]
for i in range(len(a)):
    if (a[i] == 0):
        was_zero = True
    elif (a[i] > 0):
        max_el_new = max_el.copy()
        max_el_new.append(a[i])
        if (sorted(max_el_new)[1:3] != max_el):
            max_el = sorted(max_el_new)[1:3]
    else:
        min_el_new = min_el.copy()
        min_el_new.append(a[i])
        if (sorted(min_el_new)[:2] != min_el):
            min_el = sorted(min_el_new)[:2]
            
#print(max_el, min_el)
ans = []
if (max_el[0] != 0):
    ans.append([max_el[0], max_el[1]])
if (min_el[1] != 0):
    ans.append([min_el[0], min_el[1]])
if (was_zero):
    el = max_el[1]
    if (el == 0):
        el = min_el[0]
    ans.append([0, el])
ans.append([min_el[0], max_el[1]])
ans.sort(key = lambda x: x[0] * x[1])
print(*ans[-1])
