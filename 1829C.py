def solve():
    n = int(input())
    l_s1 = l_s2 = 10**9
    ans = 10**9
    for i in range(n):
        m, s = [x for x in input().split()]
        m = int(m)
        if s == '11' and m < ans:
            ans = m
        elif s == '01' and m < l_s2:
            l_s2 = m
        elif s == '10' and m < l_s1:
            l_s1 = m

    if l_s1 + l_s2 < ans:
        print(l_s1 + l_s2)
    elif ans >= 10**9:
        print(-1)
    else:
        print(ans)


for _ in range(int(input())):
    solve()