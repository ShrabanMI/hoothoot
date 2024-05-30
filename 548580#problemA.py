def solve():
    n, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    ans = 0

    for i in range(n):
        lucky = 0
        while True:
            if a[i] == 0:
                break
            if a[i] % 10 == 4 or a[i] % 10 == 7:
                lucky += 1
            a[i] //= 10

        if lucky <= k:
            ans += 1

    print(ans)


solve()
