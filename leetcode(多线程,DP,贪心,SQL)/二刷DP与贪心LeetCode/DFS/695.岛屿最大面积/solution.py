class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0

        m = len(grid)
        n = len(grid[0])

        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n:
                return 0
            if grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            u = dfs(i - 1, j)
            d = dfs(i + 1, j)
            l = dfs(i, j - 1)
            r = dfs(i, j + 1)
            return 1 + sum([u, d, l, r])

        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i, j))

        return res