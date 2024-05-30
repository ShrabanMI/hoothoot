def solve():
    n = int(input())
    a = [int(x) for x in input().split()]

    mx = 0
    x = 0
    for i in range(n-1):
        x = a[i] * a[i+1]
        if x > mx:
            mx = x
    print(mx)


for _ in range(int(input())):
    solve()