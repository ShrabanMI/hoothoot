from collections import deque

xy = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def flood_fill(n, m, grid, r, c):
    room = 0
    if r < 0 or r >= n or c < 0 or c >= m:
        return 0
    if grid[r][c] == 0 or grid[r][c] == 'V':
        return 0

    queue = deque([(r, c)])
    while queue:
        r, c = queue.popleft()
        if grid[r][c] == 0 or grid[r][c] == 'V':
            continue

        room += grid[r][c]
        grid[r][c] = 'V'

        for x, y in xy:
            n_r, n_c = r + x, c + y
            if 0 <= n_r < n and 0 <= n_c < m:
                queue.append((n_r, n_c))

    return room


def largestLake(n, m, grid):
    largest_lake = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] != 0:
                lake = flood_fill(n, m, grid, i, j)
                if largest_lake < lake:
                    largest_lake = lake
    return largest_lake


def solve():
    n, m = [int(x) for x in input().split()]
    grid = []
    for i in range(n):
        row = [int(x) for x in input().split()]
        grid.append(row)

    ans = largestLake(n, m, grid)
    print(ans)


for _ in range(int(input())):
    solve()