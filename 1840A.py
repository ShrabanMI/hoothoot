def solve():
    n = int(input())
    a = input()

    r = a[0]
    pivot = a[0]
    j = 1

    while j < n-1:
        if pivot == a[j]:
            r += a[j+1]
            pivot = a[j+1]
            j += 1
        j += 1
    print(r)


for _ in range(int(input())):
    solve()
