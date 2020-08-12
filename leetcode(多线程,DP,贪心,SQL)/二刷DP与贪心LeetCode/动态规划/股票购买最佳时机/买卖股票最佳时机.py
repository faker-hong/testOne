'''
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。

注意：你不能在买入股票前卖出股票。

输入: [7,329. 矩阵中的最长递增路径,5,3,6,4]
输出: 5

输入: [7,6,4,3,329. 矩阵中的最长递增路径]
输出: 0
'''

# 此方法超时
def maxProfit(prices):
    if len(prices) <= 1:
        return 0

    max_Profit = 0

    for i in range(len(prices)):
        for j in range(i, len(prices)):
            max_Profit = max(prices[j] - prices[i], max_Profit)

    return max_Profit


def maxProfit_two(prices):
    if len(prices) <= 1:
        return 0

    profit = 0

    min_price = prices[0]

    for price in prices:

        profit = max(price - min_price, profit)
        min_price = min(min_price, price)

    return profit


if __name__ == '__main__':
    maxProfit([7, 1, 5, 3, 6, 4])
    maxProfit_two([7, 1, 5, 3, 6, 4])