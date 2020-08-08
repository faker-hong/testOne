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