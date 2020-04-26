'''
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。

注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

输入: [3,3,5,0,0,3,1,4]
输出: 6
解释: 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
     随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。

找出获利最大的两笔，两笔买卖时间之间无交集
'''

def maxProfit(prices):
    n = len(prices)
    if n == 0:
        return 0

    # 取正向与逆向的两个最大利益，两次交易的区间在[0:i],[i: len(prices)-1]
    minprice, maxpro1 = prices[0], 0
    maxprice, maxpro2 = prices[-1], 0
    pro1, pro2 = [0]*n, [0]*n

    for i in range(n):
        if prices[i] <= minprice:
            minprice = prices[i]
        else:
            maxpro1 = max(prices[i] - minprice, maxpro1)
            pro1[i] = maxpro1

        if prices[n-i-1] >= maxprice:
            maxprice = prices[n-i-1]
        else:
            maxpro2 = max(maxprice - prices[n-i-1], maxpro2)
            pro2[n-i-1] = maxpro2

    # 因为两次交易，所以第二次的交易时间要i+1
    maxpro = pro1[-1]

    for i in range(n-1):
        maxpro = max(maxpro, pro1[i] + pro2[i+1])

    return maxpro


if __name__ == '__main__':
    res = maxProfit([3,3,5,0,0,3,1,4])
    print(res)
