'''
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。

注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

输入: [2,4,329. 矩阵中的最长递增路径], k = 2
输出: 2
解释: 在第 329. 矩阵中的最长递增路径 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。

'''

class Solution:
    def maxProfit(self, k, prices):
        '''
            如果k大于股票数组长度的一半，则和买卖股票2的做法相同，贪心求最大收益，
            如果k小于股票数组长度的一半，则和买卖股票3的做法类似，动态规划求最优收益
        '''
        if k < 1:
            return 0

        if k >= len(prices)/2:
            return self.greedy(prices)

        import sys
        buy = [-sys.maxsize]*len(prices)
        sell = [0]*len(prices)

        for i in range(len(prices)):
            for j in range(k):
                buy[j+1] = max(buy[j+1], sell[j] - prices[i])
                sell[j+1] = max(sell[j+1], buy[j+1] + prices[i])

        return sell[k]

    def greedy(self, prices):
        profit = 0
        minprices = prices[0]

        for i in range(len(prices)):
            if prices[i] < minprices:
                minprices = prices[i]
            else:
                profit = profit + prices[i] - minprices
                minprices = prices[i]

        return profit