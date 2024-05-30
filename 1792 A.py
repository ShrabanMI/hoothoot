from math import ceil


def solve(n):
    h = [int(x) for x in input().split()]
    x = sorted(h).count(1)
    count = ceil(x/2)
    count += (n-x)
    return count


for i in range(int(input())):
    print(solve(n=int(input())))