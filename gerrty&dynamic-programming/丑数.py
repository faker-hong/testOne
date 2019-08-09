"""
丑数就是只包含质因数 2, 3, 5 的正整数。
1是丑数
"""
import numpy as np


def nthUglyNumber(n):
    """
    超出时间限制
    dp = [1]*n
    for i in range(1,n):
        compare = set()
        for j in range(0,i):
            if dp[j]*2 > dp[i-1]:
                compare.add(dp[j]*2)
            elif dp[j]*3 > dp[i-1]:
                compare.add(dp[j]*3)
            elif dp[j]*5 > dp[i-1]:
                compare.add(dp[j]*5)
        dp[i] = min(compare)
    return dp[-1]
    """
    res = [1]
    num2 = 0
    num3 = 0
    num5 = 0
    for i in range(n-1):
        res.append(min(res[num2]*2, res[num3]*3, res[num5]*5))
        if res[-1] == res[num2]*2:
            num2 += 1
        if res[-1] == res[num3]*3:
            num3 += 1
        if res[-1] == res[num5]*5:
            num5 += 1
    return res[-1]


if __name__ == '__main__':
    print(nthUglyNumber(11))