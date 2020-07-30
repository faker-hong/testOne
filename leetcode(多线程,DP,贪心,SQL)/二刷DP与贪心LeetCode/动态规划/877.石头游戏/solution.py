'''
    A和B轮流拿piles中的石头堆，最后A拿的石头多返回True，否则返回False。
    A先手，石头总数为奇数，所以不存在平局

'''
from math import ceil
import numpy as np


class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        n = len(piles)

        # dp[i][j] 代表i-j的闭区间，先手与后手的差值
        dp = [[0] * n for _ in range(n)]

        # base case
        for i in range(n):
            dp[i][i] = piles[i]

        # 从base case 和最终需要的结果，可以得出是从底往上的遍历顺序
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                # 后手的选，要取最大值
                dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])

        return dp[0][-1] > 0


if __name__ == '__main__':
    piles = [5, 3, 4, 5]
    s = Solution()
    res = s.stoneGame(piles)
    print(res)