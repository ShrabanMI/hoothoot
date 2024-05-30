def printArr(arr):
    for x in arr:
        print(x, end=' ')
    print()


def createPerm(n):
    arr = []
    for i in range(n):
        arr.append([int(x) for x in input().split()])
    return arr


def solve():
    n = int(input())
    perm = createPerm(n)


for _ in range(int(input())):
    solve()