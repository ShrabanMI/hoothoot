def oddCount(arr):
    c = 0
    for x in arr:
        if x % 2 == 1:
            c += 1
    return c


def evenCount(arr):
    c = 0
    for x in arr:
        if x % 2 == 0:
            c += 1
    return c


def solve():
    n, x = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]

    o, e = oddCount(a), evenCount(a)

    evenTaken = min(e, x-1)
    oddNeeded = x - evenTaken

    if oddNeeded % 2 == 0:
        oddNeeded += 1
    if o >= oddNeeded and oddNeeded <= x:
        print('Yes')
    else:
        print('No')


for i in range(int(input())):
    solve()