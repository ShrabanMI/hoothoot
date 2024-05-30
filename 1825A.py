def solve():
    s = input()
    frq = {x: s.count(x) for x in s}
    if len(frq) == 1:
        print(-1)
    else:
        print(len(s)-1)


for _ in range(int(input())):
    solve()