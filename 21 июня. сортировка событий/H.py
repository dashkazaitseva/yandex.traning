def solve():
    helper = list(map(int, input().split()))
    n = helper[0]
    helper = [[helper[i], helper[i + 1]] for i in range(1, len(helper), 2)]
    helper.sort()
    print(helper)
    
t = int(input())
while (t):
    solve()
    t -= 1
