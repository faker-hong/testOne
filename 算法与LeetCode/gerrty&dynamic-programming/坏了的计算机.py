def brokenCalc(X, Y):
    """
    :type X: int
    :type Y: int
    :rtype: int
    """
    # 只能*2或者-1
    res = 0
    while X < Y:
        res += 1
        if Y % 2 == 1:
            Y += 1
        else:
            Y /= 2
    return res + X - Y