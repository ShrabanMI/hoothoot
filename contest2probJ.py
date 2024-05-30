def solve():
    n, x = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]

    l = -1
    sum = r = 0

    for i in range(n):
        if a[i] % x != 0:
            if l == -1:
                l = i
            r = i
        sum += a[i]

    if sum % x != 0:
        return n
    elif l == -1:
        return l
    else:
        return n - min(l+1, n-r)


for t in range(int(input())):
    print(solve())
