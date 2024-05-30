from math import ceil

def solve():
    n, k = [int(x) for x in input().split()]
    div = set()
    for i in range(1, ceil(n**.5), 1):
        if n % i == 0:
            div.add(i)
    for i in range(ceil(n**.5), 0, -1):
        if n % i == 0:
            div.add(n//i)
    div = list(div)

    try:
        print(div[k-1])
    except IndexError:
        print(-1)


solve()