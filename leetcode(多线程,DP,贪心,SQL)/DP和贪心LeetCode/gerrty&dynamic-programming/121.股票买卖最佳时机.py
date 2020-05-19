class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 暴力求解超出时间限制
        # profit = 0
        # for i in range(len(prices)-1):
        #     if prices[i] > prices[i+1]:
        #         continue
        #     for j in range(i+1, len(prices)):
        #         profit = max(profit, prices[j] - prices[i])
        # return profit
        profit = 0
        import sys
        minprice = sys.maxsize
        for i in range(len(prices)):
            if prices[i] < minprice:
                minprice = prices[i]
            elif prices[i] - minprice > profit:
                profit = prices[i] - minprice
        return profit


if __name__ == '__main__':
    s = Solution()
    re = s.maxProfit([7,1,5,3,6,4])
    print(re)