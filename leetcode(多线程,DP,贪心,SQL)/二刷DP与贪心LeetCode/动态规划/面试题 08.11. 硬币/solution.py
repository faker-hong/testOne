'''
硬币。给定数量不限的硬币，币值为25分、10分、5分和1分，编写代码计算n分有几种表示法。
(结果可能会很大，你需要将结果模上1000000007)
'''


class Solution(object):
    def waysToChange(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1] + [0] * n

        coins = [1, 5, 10, 25]

        for coin in coins:
            for i in range(coin, n+1):
                dp[i] += dp[i-coin]

        return dp[-1] % 1000000007