def solve():
    w, d, h = [int(i) for i in input().split()]
    a, b, x, y = [int(i) for i in input().split()]
    ans = h + min(abs(a-x), abs(b-y))
    ans += min((d-y),y)



for i in range(int(input())):
    solve()