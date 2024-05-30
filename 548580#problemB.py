def solve():
    n = int(input())
    a = []
    while n != 1:
        a.append(n)
        if n % 2 == 1:
            n = 3 * n + 1
        elif n % 2 == 0:
            n = n // 2
    a.append(1)

    print(*a)


solve()
