import sys

def dep():
    if line[1] in d:
        d[line[1]] += int(line[2])
    else:
        d[line[1]] = int(line[2])

def wit():
    if line[1] in d:
        d[line[1]] -= int(line[2])
    else:
        d[line[1]] = -1* int(line[2])

d = dict()
for line in sys.stdin:
    line = line.split()
    if (line[0] == 'BALANCE'):
        if line[1] in d:
            print(d[line[1]])
        else:
            print('ERROR')
    elif (line[0] == 'DEPOSIT'):
        dep()
        
    elif (line[0] == 'WITHDRAW'):
        wit()
    elif (line[0] == 'INCOME'):
        for el in d:
            if d[el] > 0:
                d[el] += int(line[1]) * d[el]//100 
    elif (line[0] == 'TRANSFER'):
        l_save = line.copy()
        line[2] = line[3]
        wit()
        line[1] = l_save[2]
        dep()
