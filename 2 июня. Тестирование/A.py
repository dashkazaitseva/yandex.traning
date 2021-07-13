a, b = list(map(int, input().split()))
s = input()
if (s == "auto"):
    print(b)
elif (s == "fan"):
    print(a)
else:
    if (a < b and s == "heat" or a > b and s == "freeze"):
        print(b)
    else:
        print(a)
