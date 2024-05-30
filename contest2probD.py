def solve():
    x1, y1, x2, y2 = [int(x) for x in input().split()]
    steps = abs(x1-x2)+abs(y1-y2)

    print(steps)


for i in range(int(input())):
    solve()