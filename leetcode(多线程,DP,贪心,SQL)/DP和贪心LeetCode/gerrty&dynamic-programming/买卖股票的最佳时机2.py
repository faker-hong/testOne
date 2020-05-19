def maxProfit(prices, fee):
    """
    :type prices: List[int]
    :type fee: int
    :rtype: int
    """
    res = 0
    minprice = prices[0]
    for i in range(1, len(prices)):
        if prices[i] < minprice:
            minprice = prices[i]
        elif prices[i] > minprice + fee:
            res += prices[i] - minprice - fee
            minprice = prices[i] - fee
    return res


if __name__ == '__main__':
    print(maxProfit([1,4,7,10], 2))