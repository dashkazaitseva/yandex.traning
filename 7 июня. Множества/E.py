there_is = set(map(int, input().split()))
n = int(input())
number = set()
while n > 0:
    number.update([n % 10])
    n //= 10

print(len(number.difference(there_is)))
