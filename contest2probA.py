def solve():
    a, b = [int(x) for x in input().split()]
    if abs(a-b) >= 2 or a % 2 == 1 and b % 2 == 1:
        return 'Yes'
    return 'No'


print(solve())