class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 参考网上的动态规划
        if not prices:
            return 0
        dp = [[0]*len(prices) for i in range(3)]
        for j in range(1, 3):
            pre_max = -prices[0]
            for i in range(1, len(prices)):
                pre_max = max(pre_max, dp[j-1][i-1] - prices[i])
                dp[j][i] = max(dp[j-1][i-1], prices[i] + pre_max)
        return dp[-1][-1]


        # 最多只能两次交易，实现利润最大
        # 正向一次，反向一次，取两次利润最大
        # import sys
        # min_price, total_max_price = sys.maxsize, 0
        # list_profit = [0]*len(prices)   # 在区间内的最大利润
        # for i in range(len(prices)):
        #     min_price = min(min_price, prices[i])
        #     total_max_price = max(total_max_price, prices[i] - min_price)
        #     list_profit[i] = total_max_price
        #
        # # 反向遍历
        # max_price, max_profit = -sys.maxsize, 0
        # for j in range(len(prices)-1, 0, -1):
        #     max_price = max(prices[j], max_price)
        #     max_profit = max(max_profit, max_price - prices[j])
        #     # 比较整个区间一次的利润和两个区间内的利润和的大小
        #     total_max_price = max(total_max_price, max_profit + list_profit[j-1])
        #
        # return total_max_price


if __name__ == '__main__':
    s = Solution()
    prices = [3,3,5,0,0,3,1,4]
    re = s.maxProfit(prices)
    print(re)