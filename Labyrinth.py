from collections import deque

xy = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def floodFill(n, m, grid, r, c):
    path = ""
    if r < 0 or r >= n or c < 0 or c >= m:
        return 0
    if grid[r][c] == '#' or grid[r][c] == 'V':
        return 0

    queue = deque([(r, c, path)])
    while queue:
        r, c, path = queue.popleft()
        if grid[r][c] == '#' or grid[r][c] == 'V':
            continue
        if grid[r][c] == 'B':
            grid[r][c] = 'V'
            return f"YES\n{len(path)}\n{path}"

        grid[r][c] = 'V'

        for x, y in xy:
            n_r, n_c = r + y, c + x
            if 0 <= n_r < n and 0 <= n_c < m:
                queue.append((n_r, n_c, path + getDir(x, y)))

    return 'NO'


def getDir(x, y):
    if x == 1 and y == 0:
        return 'R'
    elif x == -1 and y == 0:
        return 'L'
    elif x == 0 and y == 1:
        return 'D'
    elif x == 0 and y == -1:
        return 'U'


def solve():
    n, m = [int(x) for x in input().split()]
    grid = []
    for i in range(n):
        grid.append([x for x in input()])
    ans = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'A':
                ans = floodFill(n, m, grid, i, j)
                break
    print(ans)


solve()