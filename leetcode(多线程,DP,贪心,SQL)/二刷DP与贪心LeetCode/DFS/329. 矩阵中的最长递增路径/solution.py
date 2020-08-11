from functools import lru_cache


class Solution:
    def longestIncreasingPath(self, matrix):
        if not matrix:
            return 0

        @lru_cache(maxsize=None)
        def dfs(i, j):
            best = 1
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_i = i + di
                new_j = j + dj
                if 0 <= new_i < len(matrix) and 0 <= new_j < len(matrix[0]) and matrix[new_i][new_j] > matrix[i][j]:
                    best = max(best, dfs(new_i, new_j) + 1)
            return best

        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
               res = max(res, dfs(i, j))

        return res

    def longestIncreasingPath_(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix:
            return 0
        n, m = len(matrix), len(matrix[0])
        visit = {}

        def dfs(i, j):
            if (i, j) in visit:
                return visit[(i, j)]
            res = 1
            for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_x, new_y = i + x, j + y
                if 0 <= new_x < n and 0 <= new_y < m and matrix[i][j] < matrix[new_x][new_y]:
                    res = max(res, dfs(new_x, new_y) + 1)
            visit[(i, j)] = res
            return res

        res = 1
        for i in range(n):
            for j in range(m):
                res = max(res, dfs(i, j))

        return res