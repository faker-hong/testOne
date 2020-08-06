class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        n = len(prices)

        dp = [[-prices[0], 0, 0]] + [[0, 0, 0] for _ in range(n - 1)]

        # dp[i][0] 第i天买入股票的累积收益
        # dp[i][1] 第i天卖出股票，进入冷冻期的累积收益
        # dp[i][2] 第i天手上无股票，不在冷冻期的累积收益
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][2] - prices[i])
            dp[i][1] = dp[i-1][0] + prices[i]
            dp[i][2] = max(dp[i-1][1], dp[i-1][2])

        return max(dp[n-1][1], dp[n-1][2])