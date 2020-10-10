from numpy import *


class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        n = len(matrix)
        m = len(matrix[0])

        dp = [[0] * m for _ in range(n)]

        for i in range(n):
            if matrix[i][0] == 1:
                dp[i][0] = 1

        for i in range(m):
            if matrix[0][i] == 1:
                dp[0][i] = 1

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 1:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
        return sum(sum(dp))


if __name__ == '__main__':
    s = Solution()
    s.countSquares([[0,1,1,1],[1,1,1,1],[0,1,1,1]])