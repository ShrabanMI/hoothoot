def solve():
    n, k, q = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]

    dc = 0

    for i in range(n):
        if a[i] < q:
            dc += 1

    


for t in range(int(input())):
    solve()