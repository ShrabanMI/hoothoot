def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def lcm(a, b, g):
    return int((a*b)/g)


def solve():
    a, b = [int(x) for x in input().split()]
    g = gcd(a, b)
    l = lcm(a, b, g)
    print(g, l)


for i in range(int(input())):
    solve()