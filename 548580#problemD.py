def solve():
    n = int(input())
    a = [int(x) for x in input().split()]

    print(int((n*(n+1))/2) - sum(a))


solve()