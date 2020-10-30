class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0

        row = len(grid)
        col = len(grid[0])
        res = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    for x, y in [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]:
                        if x >= row or y >= col or x < 0 or y < 0 or grid[x][y] == 0:
                            res += 1
                        else:
                            continue

        return res