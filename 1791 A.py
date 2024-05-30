def solve():
    n = int(input())
    a = [int(x) for x in input().split()]
    arr = sorted(a, key=lambda x: abs(x))

    for i in range(n-1, 0, -1):
        if arr[i] + arr[i-1] < -1 * arr[i] + -1 * arr[i-1]:
            arr[i] = -1 * arr[i]
            arr[i-1] = -1 * arr[i-1]
            i -= 1

    print(sum(arr))


for t in range(int(input())):
    solve()
