class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        def max_profit(prices):
            profit = 0
            for i in range(len(prices)-1):
                if prices[i+1] > prices[i]:
                    profit += prices[i+1]-prices[i]
            return profit
        if k == 0 or not prices or len(prices) == 1:
            return 0
        if k >= len(prices)/2:
            return max_profit(prices)

        import sys
        m = -sys.maxsize
        sell = [0]*(k+1)
        buy = [m]*(k+1)
        # 四种状态：买入，不买，卖出，不卖
        for i in range(len(prices)):
            for j in range(k):
                buy[j+1] = max(buy[j+1], sell[j] - prices[i])   # 购买状态
                sell[j+1] = max(sell[j+1], buy[j+1] + prices[i])    # 卖出状态
        return sell[k]


if __name__ == '__main__':
    s = Solution()
    prices = [3, 2, 6, 5, 0, 3]
    k = 2
    re = s.maxProfit(k, prices)
    print(re)