def solve():
    n = int(input())
    for i in range(1, n+1):
        ways = (i**4-i**2)//2 - 4*(i-1)*(i-2)  # nC2 - 4(n-1)(n-2)
        print(ways)


solve()