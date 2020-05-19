def minPathSum(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    rows = len(grid)        # 行
    cols = len(grid[0])     # 列
    # dp = [[0 for i in range(cols)] for i in range(rows)]
    for i in range(1,rows):
        grid[0][i] += grid[0][i-1]
    for i in range(1, cols):
        grid[i][0] += grid[i-1][0]

    for i in range(1,rows):
        for j in range(1,cols):
            grid[i][j] += min(grid[i-1][j], grid[i][j-1])

    return grid


if __name__ == '__main__':
    print(minPathSum([[1, 2], [1, 1]]))