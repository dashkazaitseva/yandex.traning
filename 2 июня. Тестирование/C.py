def pred(s):
    s_cur = "".join([el for el in s if el >= '0' and el <= '9'])
    if (len(s_cur) != 11):
        s_cur = '8495' + s_cur
    return s_cur[1:]
s0 = pred(input())
for _ in range(3):
    if s0 == pred(input()):
        print("YES")
    else:
        print("NO")
