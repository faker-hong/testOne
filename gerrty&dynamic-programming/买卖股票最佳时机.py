def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    profits = 0
    for i in range(1, len(prices)):
        profit = prices[i] - prices[i - 1]
        if profit > 0:
            profits += profit
    return profits

if __name__ == '__main__':
    print(maxProfit([7, 1, 5, 3, 6, 4]))