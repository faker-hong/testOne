'''
给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。
输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。

假设  2 <= n <= 58
'''


class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 看能否被3整除，能被3整除，那就全用3，不能被3整除，如果余数为1，那就少用一个3，余数为4，用2*2，余数为2，那就直接用2

        # 用多少个3
        sum_three = n // 3

        if n % 3 == 0:
            return 3**sum_three
        elif n % 3 == 1:
            return 3**(sum_three - 1) * 4
        else:
            return 3**sum_three * 2

    # 动态规划
    def intergerBreak_(self, n):
        dp = [0] * (n + 1)

        # base case
        # 0和1都不可拆分，所以为0

        # 动态规划方程
        # i拆分为j和i-j就不可拆分，那么结果为j*(i - j), 如果还能拆分，结果为j * dp[i - j]

        for i in range(2, n + 1):
            for j in range(i):
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])

        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    res = s.integerBreak(2)
    print(res)