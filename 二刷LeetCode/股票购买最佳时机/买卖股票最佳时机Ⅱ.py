'''
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

'''


def maxProfit(prices):

    res = 0
    min_price = prices[0]

    if len(prices) <= 1:
        return res

    for i in range(1, len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        elif prices[i] > min_price:
            res += prices[i] - min_price
            min_price = prices[i]
    return res