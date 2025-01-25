def shiftGrid(grid, k):
    m = len(grid)
    n = len(grid[0])
    ck = k % (m * n) % n
    rk = k % (m * n) // n
    if rk != 0:
        temp = grid[m - rk:]
        grid[rk:] = grid[:m - rk]
        grid[:rk] = temp
    tmp0 = grid[m - 1][n - ck:]
    for i in range(m):
        tmp1 = grid[i][n - ck:]
        grid[i][ck:] = grid[i][:n - ck]
        grid[i][:ck] = tmp0
        tmp0 = tmp1
    return grid


if __name__ == '__main__':
    grid = [[1],[2],[3],[4],[7],[6],[5]]
    k = 23
    new_grid = shiftGrid(grid, k)
    print(new_grid)