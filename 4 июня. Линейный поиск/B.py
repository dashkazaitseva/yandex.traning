eq = False
asc = False
des = False
a0 = int(input())
a1 = int(input())
while (a1 != -2 * 1000000000):
    if (a0 == a1):
        eq = True
    elif (a0 < a1):
        asc = True
    else:
        des = True
    a0 = a1
    a1 = int(input())

if (eq and asc and des):
    print('RANDOM')
elif (eq and asc):
    print('WEAKLY ASCENDING')
elif (asc):
    print('ASCENDING')
elif (eq and des):
    print('WEAKLY DESCENDING')
elif (eq):
    print('CONSTANT')
else:
    print('DESCENDING')
