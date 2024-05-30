def printArr(arr):
    for x in arr:
        print(x, end=' ')
    print()


def solve():
    n, s, r = [int(i) for i in input().split()]
    mx = s-r
    a = [0]*(n-1)

    i = 0
    while True:
        if sum(a) == r:
            break
        if a[i % n-1] < mx:
            a[i % n-1] += 1
        i += 1
    a.append(mx)
    printArr(a)


for i in range(int(input())):
    solve()