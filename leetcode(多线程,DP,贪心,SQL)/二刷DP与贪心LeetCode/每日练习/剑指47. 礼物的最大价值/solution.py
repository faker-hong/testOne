'''
在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。
你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。
给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 12
解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物
'''


class Solution(object):
    def maxValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
        dp = [[0] * m for _ in range(n)]
        dp[0][0] = grid[0][0]

        # base case
        for i in range(1, n):
            dp[i][0] = dp[i - 1][0] + grid[i][0]

        for j in range(1, m):
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = grid[i][j] + max(dp[i - 1][j], dp[i][j - 1])

        return dp[n-1][m-1]


if __name__ == '__main__':
    grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    s = Solution()
    res = s.maxValue(grid)
    print(res)