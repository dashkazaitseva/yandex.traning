a = int(input())
b = int(input())
c = int(input())

if (c < 0):
    print ('NO SOLUTION')
else:
    c *= c
    c -= b
    if (a == 0 and c == 0):
        print('MANY SOLUTIONS')
    elif (a == 0 and c != 0):
        print ('NO SOLUTION')
    elif (c % a == 0):
        print(c // a)
    else:
        print('NO SOLUTION')
