def solve():
    a = [int(x) for x in input().split()]
    gcd = 1
    mx = max(a)
    for i in range(len(a)):
        if mx % a[i] == 0 and gcd < a[i] and mx != a[i]:
            gcd = a[i]
    print(gcd)


for _ in range(int(input())):
    solve()