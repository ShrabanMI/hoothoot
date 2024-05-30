def magic(arr, l, r, elem):
    if l == r:
        if r == len(arr)-1:
            return r+1
        return r
    mid = (l + r) // 2
    if arr[mid] == elem:
        return mid
    elif arr[mid] > elem:
        return magic(arr, l, mid, elem)
    else:
        return magic(arr, mid + 1, r, elem)


def solve():
    n, q = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    l, r = 0, n - 1
    for i in range(q):
        ak, bk = [int(x) for x in input().split()]
        a, b = magic(arr, l, r, ak), magic(arr, l, r, bk)
        print(b-a)


for i in range(int(input())):
    print(f"Case {i + 1}:")
    solve()