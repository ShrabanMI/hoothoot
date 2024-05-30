def tictactoe(grid):
    ans = ""
    for i in range(3):
        if grid[i][0] == grid[i][1] == grid[i][2]:
            if grid[i][0] == '.':
                continue
            return grid[i][0]

    for i in range(3):
        if grid[0][i] == grid[1][i] == grid[2][i]:
            if grid[0][i] == '.':
                continue
            return grid[2][i]

    if grid[0][0] == grid[1][1] == grid[2][2]:
        return grid[2][2]
    if grid[0][2] == grid[1][1] == grid[2][0]:
        return grid[2][0]


def solve():
    grid = []
    for i in range(3):
        grid.append([x for x in input()])

    ans = tictactoe(grid)
    if ans == '.' or ans is None:
        ans = 'DRAW'
    print(ans)


for t in range(int(input())):
    solve()