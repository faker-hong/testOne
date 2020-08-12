class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        # 不成立购买条件的
        if k == 0 or not prices or n == 0:
            return 0
        # 无限次购买
        if k >= n / 2:
            return self.greedy(prices)
        # k值有效的
        # dp[i][k][0]   i天内k次交易手上无股票的最大收益
        # dp[i][k][1]   i天内k次交易手上有股票的最大收益
        dp = [[[0, 0] for _ in range(k+1)] for _ in range(n)]
        dp[0][0][0] = 0
        dp[0][0][1] = -prices[0]

        # base case
        for i in range(1, n):
            dp[i][0][0] = 0
            dp[i][0][1] = max(dp[i-1][0][1], -prices[i])

        for j in range(k+1):
            dp[0][j][0] = 0
            dp[0][j][1] = -prices[0]

        for i in range(1, n):
            for j in range(1, k+1):
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j-1][1] + prices[i])
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j][0] - prices[i])
        profit = 0
        for i in range(k+1):
            profit = max(profit, dp[n-1][i][0])
        return profit

    def greedy(self, prices):
        n = len(prices)
        profit = 0
        for i in range(n-1):
            if prices[i+1] > prices[i]:
                profit += prices[i+1] - prices[i]
        return profit
