import sys

d = dict()
for line in sys.stdin:
    line = line.split()
    if line[0] in d:
        if line[1] in d[line[0]]:
            d[line[0]][line[1]] += int(line[2])
        else:
            d[line[0]][line[1]] = int(line[2])
    else:
        d[line[0]] = {line[1] : int(line[2])}


d = dict(sorted(d.items(), key = lambda x: x[0]))
for el in d:
    print(el, ':', sep = '')
    d_cur = d[el]
    d_cur = dict(sorted(d_cur.items(), key = lambda x: x[0]))
    for el1 in d_cur:
        print(el1, d_cur[el1])
